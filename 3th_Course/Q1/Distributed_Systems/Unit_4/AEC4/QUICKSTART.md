# COMANDOS COPY-PASTE - CONFIGURACIÓN DESDE CERO
## Setup Completo AWS EC2 → Kubernetes → Aplicación Desplegada

---

## 📋 ÍNDICE

### PARTE A: CONFIGURACIÓN INICIAL (Hacer antes de la grabación)
1. [Preparación de Instancias AWS](#paso1)
2. [Instalación de Docker](#paso2)
3. [Instalación de Kubernetes](#paso3)
4. [Inicialización del Cluster](#paso4)
5. [Construcción y Despliegue de Aplicaciones](#paso5)
6. [Configuración NFS (Avanzada 2)](#paso6)

### PARTE B: COMANDOS PARA LA DEMOSTRACIÓN (Durante el video)
7. [Comandos para Mostrar Nodos y Servicios](#demo1)
8. [Comandos para Mostrar Dockerfiles y YAMLs](#demo2)
9. [Comandos para la Demostración Práctica](#demo3)
10. [Comandos Extra (Opcional)](#demo4)

---

# PARTE A: CONFIGURACIÓN INICIAL
## (Ejecutar TODO esto ANTES de grabar el video)

---

## PASO 1: PREPARACIÓN DE INSTANCIAS AWS <a name="paso1"></a>

### 1.1. Crear Security Group

**Ir a AWS Console → EC2 → Security Groups → Create Security Group**

1. **Nombre:** kubernetes-cluster-sg
2. **Descripción:** Security group para cluster Kubernetes
3. **VPC:** Dejar el default (no necesitas crear uno nuevo)

**Agregar Inbound Rules (click en "Add Rule" para cada puerto):**

| Tipo | Protocolo | Puerto | Origen | Descripción |
|------|-----------|---------|---------|-------------|
| SSH | TCP | 22 | 0.0.0.0/0 | SSH desde cualquier lugar |
| Custom TCP | TCP | 6443 | `sg-XXXXX` (mismo SG) | Kubernetes API |
| Custom TCP | TCP | 2379-2380 | `sg-XXXXX` (mismo SG) | etcd |
| Custom TCP | TCP | 10250-10252 | `sg-XXXXX` (mismo SG) | Kubelet |
| Custom TCP | TCP | 32001 | 0.0.0.0/0 | Aplicación Server |
| Custom TCP | TCP | 32002 | 0.0.0.0/0 | Aplicación Broker |
| NFS | TCP | 2049 | `sg-XXXXX` (mismo SG) | NFS (Avanzada 2) |
| Custom TCP | TCP | 8472 | `sg-XXXXX` (mismo SG) | Flannel VXLAN |

**IMPORTANTE:** 
- Para las reglas que dicen `sg-XXXXX (mismo SG)`, en "Source" selecciona el **mismo Security Group** que estás creando (aparecerá en el dropdown)
- Esto permite que las instancias del cluster se comuniquen entre sí
- Solo SSH y los puertos 32001-32002 necesitan estar abiertos al mundo (0.0.0.0/0)

### 1.2. Crear Instancias EC2

**Ir a AWS Console → EC2 → Launch Instance**

**Configuración de cada instancia:**

1. **Name:** 
   - Primera: `kubernetes-master`
   - Siguientes: `kubernetes-worker1`, `kubernetes-worker2`, `kubernetes-worker3`

2. **AMI:** Ubuntu Server 20.04 LTS

3. **Instance type:** 
   - **RECOMENDADO:** t2.medium (2 vCPUs, 4 GB RAM)
   - **MÍNIMO:** t2.small (1 vCPU, 2 GB RAM) - Funcionará pero con limitaciones
   - **NO USAR:** t2.micro (1 GB RAM) - Kubernetes requiere mínimo 2GB

4. **Key pair:** 
   - Crear o seleccionar una existente
   - Descargar el archivo .pem si es nueva

5. **Network settings:**
   - VPC: Default
   - **Security Group:** Seleccionar `kubernetes-cluster-sg` (el que creaste)

6. **Storage:** 20 GB gp2

7. **Number of instances:** 4 (o créalas una por una)

8. **Launch Instance**

**IPs públicas de las instancias:**
```
MASTER:   44.210.109.96
WORKER1:  44.211.31.66
WORKER2:  98.92.124.197
WORKER3:  3.238.235.150
```

### 1.3. Conectar a las Instancias

```bash
# Dar permisos a la clave
chmod 400 /home/nirmata/Descargas/Kubernetes.pem

# Conectar al MASTER
ssh -i "/home/nirmata/Descargas/Kubernetes.pem" ubuntu@44.210.109.96

# Conectar a cada WORKER (abrir 3 terminales adicionales)
ssh -i "/home/nirmata/Descargas/Kubernetes.pem" ubuntu@44.211.31.66
ssh -i "/home/nirmata/Descargas/Kubernetes.pem" ubuntu@98.92.124.197
ssh -i "/home/nirmata/Descargas/Kubernetes.pem" ubuntu@3.238.235.150
```

---

## PASO 2: INSTALACIÓN DE DOCKER <a name="paso2"></a>

### ⚠️ EJECUTAR EN TODAS LAS INSTANCIAS (Master + 3 Workers)

```bash
# Actualizar sistema
sudo apt-get update && sudo apt-get upgrade -y

# Instalar dependencias
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release

# Añadir clave GPG de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Añadir repositorio de Docker
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Añadir usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker

# Verificar instalación
docker --version
```

**Salida esperada:** `Docker version 24.0.x, build ...`

---

## PASO 3: INSTALACIÓN DE KUBERNETES <a name="paso3"></a>

### ⚠️ EJECUTAR EN TODAS LAS INSTANCIAS (Master + 3 Workers)

```bash
# Deshabilitar swap (requisito de Kubernetes)
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

# Cargar módulos del kernel necesarios
sudo modprobe overlay
sudo modprobe br_netfilter

# Configurar parámetros del sistema para Kubernetes
cat <<EOF | sudo tee /etc/sysctl.d/kubernetes.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

sudo sysctl --system

# Añadir clave GPG de Kubernetes (nuevo repositorio)
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# Añadir repositorio de Kubernetes (nuevo)
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

# Instalar componentes de Kubernetes
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl

# Evitar actualizaciones automáticas
sudo apt-mark hold kubelet kubeadm kubectl

# Verificar instalación
kubeadm version
kubectl version --client
```

**Salida esperada:** Versiones de kubeadm y kubectl

### Configurar Containerd

```bash
# Crear directorio de configuración
sudo mkdir -p /etc/containerd

# Generar configuración por defecto
sudo containerd config default | sudo tee /etc/containerd/config.toml

# Habilitar systemd cgroup (necesario para Kubernetes)
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# Reiniciar containerd
sudo systemctl restart containerd
sudo systemctl enable containerd

# Verificar que está corriendo
sudo systemctl status containerd
```

---

## PASO 4: INICIALIZACIÓN DEL CLUSTER <a name="paso4"></a>

### 4.1. Inicializar Master (SOLO EN EL NODO MASTER)

```bash
# Inicializar cluster de Kubernetes (ignorando check de RAM para instancias pequeñas)
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=Mem

# Configurar kubectl para el usuario actual
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Instalar red de pods (Flannel)
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# Verificar nodos (debe aparecer el master como Ready)
kubectl get nodes

# Verificar pods del sistema (todos deben estar Running)
kubectl get pods -A
```

**⚠️ IMPORTANTE:** Al final de `kubeadm init` aparecerá un comando como este:

```bash
kubeadm join 172.31.76.253:6443 --token fn83zx.t6b3zlpk0ov0dyv4 \
  --discovery-token-ca-cert-hash sha256:3f8735efb9667c93cd4c0c2334c9ed42a2efc27c1faad40de8354f5771a97302
```

**COPIA Y GUARDA este comando**, lo necesitarás para unir los workers. La IP privada del master será diferente a la pública.

⚠️ **NOTA:** Si el token expira (válido por 24 horas), genera uno nuevo con:
```bash
# En el master
kubeadm token create --print-join-command
```

### 4.2. Unir Workers al Cluster (EN CADA WORKER)

```bash
# Ejecutar el comando de join que guardaste del master
# IMPORTANTE: Añadir --ignore-preflight-errors=Mem también en los workers
sudo kubeadm join 172.31.76.253:6443 --token fn83zx.t6b3zlpk0ov0dyv4 \
  --discovery-token-ca-cert-hash sha256:3f8735efb9667c93cd4c0c2334c9ed42a2efc27c1faad40de8354f5771a97302 \
  --ignore-preflight-errors=Mem
```

### 4.3. Verificar Cluster (EN EL MASTER)

```bash
# Ver todos los nodos (deben aparecer 4 nodos en Ready)
kubectl get nodes

# Ver con más detalle
kubectl get nodes -o wide

# Esperar hasta que todos los nodos estén "Ready"
# Puede tardar 1-2 minutos
```

**Salida esperada:**
```
NAME        STATUS   ROLES           AGE   VERSION
master      Ready    control-plane   5m    v1.28.x
worker1     Ready    <none>          2m    v1.28.x
worker2     Ready    <none>          2m    v1.28.x
worker3     Ready    <none>          2m    v1.28.x
```

---

## PASO 5: CONSTRUCCIÓN Y DESPLIEGUE DE APLICACIONES <a name="paso5"></a>

### 5.1. Preparar Imágenes Docker (EN TU MÁQUINA LOCAL)

```bash
# Ir al directorio del proyecto
cd /home/nirmata/Documentos/University/U-Tad/3th_Course/Q1/Distributed_Systems/Unit_4/AEC4

# Copiar ejecutables (ya descargados de Blackboard)
cp ~/Descargas/P3FileManager/brokerFileManager docker/broker/
cp ~/Descargas/P3FileManager/serverFileManager docker/server/
cp ~/Descargas/P3FileManager/clientFileManager client/

# Dar permisos de ejecución
chmod +x docker/broker/brokerFileManager
chmod +x docker/server/serverFileManager
chmod +x client/clientFileManager

# REEMPLAZA <tu-usuario> con tu username de Docker Hub
export DOCKER_USER="<tu-usuario>"

# Construir imagen del broker
cd docker/broker/
docker build -t $DOCKER_USER/broker-filemanager:latest .

# Construir imagen del servidor
cd ../server/
docker build -t $DOCKER_USER/server-filemanager:latest .

cd ../../

# Iniciar sesión en Docker Hub
docker login

# Subir imágenes
docker push $DOCKER_USER/broker-filemanager:latest
docker push $DOCKER_USER/server-filemanager:latest

# Verificar que se subieron
echo "Verifica en: https://hub.docker.com/u/$DOCKER_USER"
```

### 5.2. Actualizar Archivos YAML

```bash
# Actualizar YAMLs con tu usuario de Docker Hub
./update-yamls.sh $DOCKER_USER

# Verificar que se actualizaron
grep "image:" kubernetes/broker/deployment.yaml
grep "image:" kubernetes/server/deployment-advanced2.yaml
```

### 5.3. Copiar Archivos al Master

```bash
# Desde tu máquina local
scp -i "/home/nirmata/Descargas/Kubernetes.pem" -r kubernetes/ ubuntu@44.210.109.96:~/
```

### 5.4. Desplegar Broker (EN EL MASTER)

```bash
# Aplicar deployment del broker
kubectl apply -f kubernetes/broker/deployment.yaml

# Verificar que se creó
kubectl get deployments
kubectl get pods -l app=broker
kubectl get services

# Esperar a que el pod esté Running
kubectl get pods -w
# Ctrl+C para salir cuando esté Running
```

---

## PASO 6: CONFIGURACIÓN NFS (SOLO AVANZADA 2) <a name="paso6"></a>

### 6.1. Configurar Servidor NFS (EN UNA INSTANCIA SEPARADA O EN EL MASTER)

**Opción A: Usar el Master como servidor NFS**

```bash
# En el MASTER - Instalar NFS Server (puede tardar un poco)
sudo apt-get update
sudo apt-get install -y nfs-kernel-server nfs-common

# Crear directorio compartido
sudo mkdir -p /mnt/nfs-share/FileManagerDir
sudo chmod 777 /mnt/nfs-share
sudo chmod 777 /mnt/nfs-share/FileManagerDir

# Configurar exports (permitir acceso desde cualquier IP del cluster)
echo "/mnt/nfs-share *(rw,sync,no_subtree_check,no_root_squash)" | sudo tee /etc/exports

# Aplicar cambios en exports
sudo exportfs -a

# Reiniciar servicio NFS
sudo systemctl restart nfs-kernel-server
sudo systemctl enable nfs-kernel-server

# Verificar que el servicio está corriendo
sudo systemctl status nfs-kernel-server

# Verificar exports
sudo exportfs -v
showmount -e localhost
```

**Salida esperada:**
```
Export list for localhost:
/mnt/nfs-share *
```

**Si se congela en la instalación:**
```bash
# Cancelar con Ctrl+C y probar instalación alternativa
sudo apt-get install -y --no-install-recommends nfs-kernel-server
# O si sigue fallando:
sudo dpkg --configure -a
sudo apt-get install -f
```

### 6.2. Instalar Cliente NFS (EN TODOS LOS WORKERS)

```bash
# En cada WORKER
sudo apt-get update
sudo apt-get install -y nfs-common

# Probar montaje manual (opcional)
sudo mkdir -p /mnt/test
sudo mount -t nfs 172.31.76.253:/mnt/nfs-share /mnt/test
ls -la /mnt/test
sudo umount /mnt/test
```

### 6.3. Actualizar YAML de NFS

```bash
# EN TU MÁQUINA LOCAL
# Editar kubernetes/nfs/nfs-pv-pvc.yaml
# Reemplazar <IP_SERVIDOR_NFS> con la IP del master

# O con sed:
sed -i "s/<IP_SERVIDOR_NFS>/172.31.76.253/g" kubernetes/nfs/nfs-pv-pvc.yaml

# Copiar al master
scp -i "/home/nirmata/Descargas/Kubernetes.pem" kubernetes/nfs/nfs-pv-pvc.yaml ubuntu@44.210.109.96:~/kubernetes/nfs/
```

### 6.4. Desplegar NFS y Servidor (EN EL MASTER)

```bash
# Aplicar PersistentVolume y PersistentVolumeClaim
kubectl apply -f kubernetes/nfs/nfs-pv-pvc.yaml

# Verificar que se crearon y están Bound
kubectl get pv
kubectl get pvc

# Aplicar deployment del servidor (Avanzada 2)
kubectl apply -f kubernetes/server/deployment-advanced2.yaml

# Verificar deployments
kubectl get deployments
kubectl get pods -o wide

# Esperar a que los 3 pods estén Running
kubectl get pods -w
# Ctrl+C para salir
```

**Verificar que los pods están en nodos diferentes:**

```bash
kubectl get pods -l app=filemanager-server -o wide
```

**Salida esperada:**
```
NAME                          READY   STATUS    NODE
server-deployment-xxx-yyy     1/1     Running   worker1
server-deployment-xxx-zzz     1/1     Running   worker2
server-deployment-xxx-www     1/1     Running   worker3
```

### 6.5. Preparar Archivos de Prueba para el Cliente

```bash
# EN TU MÁQUINA LOCAL
cd client/

# Crear archivos de prueba
echo "Este es el archivo de prueba 1" > test1.txt
echo "Este es el archivo de prueba 2" > test2.txt
echo "Contenido de demostración para el video" > demo.txt

# Verificar
ls -la *.txt
```

---

# ✅ CHECKPOINT: TODO LISTO PARA GRABAR

Antes de continuar, verifica que:

- [ ] Cluster tiene 4 nodos (1 master + 3 workers) todos en Ready
- [ ] Broker está desplegado y Running
- [ ] 3 réplicas del servidor están Running en nodos diferentes
- [ ] PV y PVC están en estado Bound
- [ ] Servicios broker-service y server-service están creados
- [ ] Archivos de prueba (test1.txt, test2.txt, demo.txt) están creados
- [ ] Cliente funciona: `./client/clientFileManager 44.210.109.96 32002` conecta correctamente

**Si todo está ✅, estás listo para grabar el video**

---
---

# PARTE B: COMANDOS PARA LA DEMOSTRACIÓN
## ═══════════════════════════════════════════════════════
## 🎬 INICIA LA GRABACIÓN AQUÍ
## ═══════════════════════════════════════════════════════

---

## DEMO 1: MOSTRAR NODOS Y SERVICIOS <a name="demo1"></a>

### Comando 1: Conectar al Master

```bash
ssh -i "/home/nirmata/Descargas/Kubernetes.pem" ubuntu@44.210.109.96
```

### Comando 2: Mostrar Nodos del Cluster

```bash
kubectl get nodes -o wide
```

**Qué decir:** "Aquí podéis ver mi cluster completo. Tengo 4 nodos: 1 master que ejecuta el control-plane de Kubernetes y 3 workers donde corren las aplicaciones. Todos están en estado Ready."

### Comando 3: Mostrar Deployments

```bash
kubectl get deployments
```

**Qué decir:** "Aquí vemos los deployments. El broker-deployment tiene 1/1 ready, y el server-deployment tiene 3/3 ready, las tres réplicas funcionando correctamente."

### Comando 4: Mostrar Pods en Detalle

```bash
kubectl get pods -o wide
```

**Qué decir:** "En los pods con detalle, vemos que el broker está corriendo en uno de los workers, y lo más importante: las 3 réplicas del servidor están repartidas en los 3 workers diferentes. Cada réplica está en un nodo distinto, lo cual maximiza la disponibilidad."

### Comando 5: Mostrar Servicios

```bash
kubectl get services
```

**Qué decir:** "Los servicios expuestos son el broker-service en el puerto 32002 y el server-service en el puerto 32001. El server-service automáticamente balancea las peticiones entre las 3 réplicas."

### Comando 6: Mostrar Volúmenes NFS

```bash
kubectl get pv,pvc
```

**Qué decir:** "El PersistentVolume nfs-pv está en estado Bound, vinculado al PVC. Tiene 5Gi disponibles y el modo ReadWriteMany activo, lo que permite que múltiples pods lean y escriban simultáneamente."

---

## DEMO 2: MOSTRAR DOCKERFILES Y YAMLS <a name="demo2"></a>

### Comando 7: Mostrar Dockerfile del Broker

```bash
cat docker/broker/Dockerfile
```

**Qué decir:** "El Dockerfile del broker es sencillo. He usado Ubuntu 20.04 como imagen base por compatibilidad con los binarios. Instalo libstdc++6 como dependencia necesaria, copio el binario del broker, expongo el puerto 32002 y ejecuto el broker."

### Comando 8: Mostrar Dockerfile del Servidor

```bash
cat docker/server/Dockerfile
```

**Qué decir:** "El Dockerfile del servidor es similar, pero aquí creo el directorio /app/FileManagerDir para almacenar archivos. El puerto es el 32001. Uso ENTRYPOINT porque el servidor necesita recibir la IP del broker como parámetro al arrancar."

### Comando 9: Mostrar Deployment del Broker

```bash
cat kubernetes/broker/deployment.yaml
```

**Qué decir:** "El deployment del broker es simple. Solo necesito 1 réplica. Uso mi imagen de Docker Hub, expongo el puerto 32002, y le pongo límites de recursos para el scheduler de Kubernetes. El service es de tipo NodePort, accesible desde fuera del cluster."

### Comando 10: Mostrar Configuración NFS

```bash
cat kubernetes/nfs/nfs-pv-pvc.yaml
```

**Qué decir:** "Aquí está toda la configuración del almacenamiento distribuido. El PersistentVolume nfs-pv conecta con el servidor NFS usando su IP. Tiene 5Gi de capacidad y ReadWriteMany, que permite que múltiples pods lean y escriban simultáneamente."

### Comando 11: Mostrar Deployment Avanzado 2

```bash
cat kubernetes/server/deployment-advanced2.yaml
```

**Qué decir:** "Este es el deployment avanzado 2. Tengo 3 réplicas del servidor, y Kubernetes las distribuye automáticamente en diferentes nodos. Cada réplica monta el PVC nfs-pvc en /app/FileManagerDir, entonces las 3 réplicas acceden al mismo almacenamiento NFS."

---

## DEMO 3: DEMOSTRACIÓN PRÁCTICA CON CLIENTES <a name="demo3"></a>

### Comando 12: Mostrar Nodos Completo

```bash
kubectl get nodes -o wide
```

**Qué decir:** "Aquí vemos los 4 nodos del cluster. El nodo con rol control-plane es el master y los otros 3 son workers. La IP pública del master para conectar desde el cliente es 44.210.109.96."

### Comando 13: Preparar Archivos de Prueba (EN TU MÁQUINA LOCAL)

```bash
cd /home/nirmata/Documentos/University/U-Tad/3th_Course/Q1/Distributed_Systems/Unit_4/AEC4/client

# Verificar archivos
ls -la *.txt
```

### Comando 14: Ejecutar Primer Cliente

```bash
./clientFileManager 44.210.109.96 32002
```

**Qué decir:** "Voy a ejecutar el primer cliente conectándolo al broker en la IP pública del master y puerto 32002. El cliente se ha conectado correctamente."

### Comando 15: Listar Archivos Locales

```bash
ls
```

**Qué decir:** "Aquí tengo los archivos de prueba locales: test1.txt, test2.txt y demo.txt."

### Comando 16: Listar Archivos Remotos

```bash
lls
```

**Qué decir:** "El directorio remoto está vacío porque es la primera ejecución."

### Comando 17: Subir Primer Archivo

```bash
upload test1.txt
```

**Qué decir:** "Archivo subido correctamente. Voy a verificar."

e .### Comando 18: Verificar con lls

```bash
lls
```

**Qué decir:** "Perfecto, ahora aparece test1.txt en el listado remoto."

### Comando 19: Subir Más Archivos

```bash
upload test2.txt
upload demo.txt
lls
```

**Qué decir:** "Ahora tengo 3 archivos en el servidor. Lo importante es que estos archivos están en el almacenamiento NFS compartido. Los 3 pods del servidor, en 3 nodos diferentes, pueden acceder a estos mismos archivos."

### Comando 20: Verificar en el Servidor NFS (Abrir otra terminal)

```bash
# En otra terminal, conectar al master (donde está el NFS)
ssh -i "/home/nirmata/Descargas/Kubernetes.pem" ubuntu@44.210.109.96

# Listar archivos en el NFS
ls -la /mnt/nfs-share/FileManagerDir/
```

**Qué decir:** "Voy a conectarme al servidor NFS para verificar que los archivos están ahí físicamente. Aquí están los archivos, almacenados en /mnt/nfs-share/FileManagerDir del servidor NFS. Esto es persistencia real en un sistema distribuido."

### Comando 21: Cerrar Primer Cliente

```bash
exit
```

**Qué decir:** "Cierro este cliente."

### Comando 22: Ejecutar Segundo Cliente

```bash
./clientFileManager 44.210.109.96 32002
```

**Qué decir:** "Ahora inicio un segundo cliente para demostrar la persistencia de datos. Conectado. Este segundo cliente puede haberse conectado a una réplica diferente gracias al balanceo de carga de Kubernetes."

### Comando 23: Listar Archivos Remotos (Cliente 2)

```bash
lls
```

**Qué decir:** "Perfecto! Este segundo cliente ve todos los archivos que subió el primer cliente: test1.txt, test2.txt y demo.txt. Esto demuestra que el almacenamiento NFS funciona correctamente, hay persistencia real entre diferentes conexiones, y el balanceo de carga distribuye clientes entre réplicas."

### Comando 24: Descargar Archivo

```bash
download test1.txt
```

**Qué decir:** "Voy a descargar uno de los archivos. Archivo descargado correctamente."

### Comando 25: Cerrar Segundo Cliente

```bash
exit
```

### Comando 26: Verificar Archivo Descargado

```bash
ls -la test1.txt
cat test1.txt
```

**Qué decir:** "Cierro el cliente y verifico que el archivo se descargó bien. Aquí está el archivo con su contenido correcto. Todo el ciclo funciona perfectamente."

---

## DEMO 4: COMANDOS EXTRA (OPCIONAL) <a name="demo4"></a>

### Comando 27: Ver Logs de las Réplicas

```bash
# Volver al master
ssh -i "/home/nirmata/Descargas/Kubernetes.pem" ubuntu@44.210.109.96

# Listar pods del servidor
kubectl get pods -l app=filemanager-server

# Ver logs de cada réplica
kubectl logs <server-pod-1> --tail=10
kubectl logs <server-pod-2> --tail=10
kubectl logs <server-pod-3> --tail=10
```

**Qué decir:** "Voy a ver los logs de las 3 réplicas para demostrar que las peticiones se distribuyen. Como podéis ver, las peticiones se han distribuido entre los diferentes pods. El balanceo de carga de Kubernetes funciona perfectamente."

### Comando 28: Demostrar Alta Disponibilidad

```bash
# Eliminar un pod
kubectl delete pod <server-pod-name>

# Ver cómo se recrea automáticamente
kubectl get pods -w
```

**Qué decir:** "Ahora voy a eliminar un pod para simular que un nodo falla. Kubernetes detecta inmediatamente que falta un pod y empieza a crear uno nuevo automáticamente para mantener las 3 réplicas. Mientras esto pasa, las otras 2 réplicas siguen funcionando con normalidad. Esto es alta disponibilidad real."

---

## 🎬 FIN DE LA DEMOSTRACIÓN

### Comando 29: Conclusión

```bash
# Mostrar estado final
kubectl get all
kubectl get pv,pvc
```

**Qué decir:** "Para terminar, he completado la Configuración Avanzada 2 con NFS, la más compleja de la práctica, que vale 10 puntos. He creado Dockerfiles optimizados, montado un cluster de Kubernetes con 4 nodos, configurado almacenamiento distribuido NFS, y demostrado alta disponibilidad, persistencia y balanceo de carga. Todo funciona como un sistema distribuido de producción real. Gracias por la atención."

---

## ═══════════════════════════════════════════════════════
## 🛑 FIN DE LA GRABACIÓN
## ═══════════════════════════════════════════════════════

---

## 📌 NOTAS FINALES

### Antes de Grabar:
- [ ] Ejecuta TODA la Parte A (Configuración Inicial)
- [ ] Verifica que todo funciona con el Checkpoint
- [ ] Practica la Parte B al menos 2-3 veces
- [ ] Ten las IPs anotadas para copiar/pegar rápido
- [ ] Configura tu terminal con letra grande (16pt mínimo)

### Durante la Grabación:
- Sigue el orden de comandos de la Parte B
- Lee el "Qué decir" mientras ejecutas los comandos
- No corras, habla despacio y claro
- Si un comando tarda, explica qué está pasando
- Muestra confianza, conoces lo que has montado

### Estructura del Video:
```
00:00-02:00  Introducción
02:00-05:00  DEMO 1 (Nodos y Servicios)
05:00-09:00  DEMO 2 (Dockerfiles y YAMLs)
09:00-16:00  DEMO 3 (Demostración Práctica)
16:00-18:00  DEMO 4 (Opcional - Alta Disponibilidad)
18:00-20:00  Conclusión
```

---

**¡Éxito con la práctica y el video!**
