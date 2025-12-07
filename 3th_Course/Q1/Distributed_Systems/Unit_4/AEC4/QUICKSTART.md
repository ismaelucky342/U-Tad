#  GUÍA DE CONFIGURACIÓN Y PRESENTACIÓN
## AEC4 - Sistemas Distribuidos - Despliegue con Kubernetes

---

##  TABLA DE CONTENIDOS

1. [Descripción del Proyecto](#descripcion)
2. [Arquitectura del Sistema](#arquitectura)
3. [Guía de Configuración Paso a Paso](#configuracion)
4. [Guión para la Presentación](#presentacion)
5. [Scripts de Ayuda](#scripts)
6. [Solución de Problemas](#troubleshooting)

---

##  DESCRIPCIÓN DEL PROYECTO <a name="descripcion"></a>

### Objetivo
Desplegar una aplicación distribuida de gestión de archivos en un cluster de Kubernetes con instancias EC2, implementando:
- **Contenedores Docker** para broker y servidores
- **Orquestación con Kubernetes** (deployments, services, réplicas)
- **Balanceo de carga** entre múltiples instancias
- **Almacenamiento compartido** (opcional: hostPath o NFS)

### Componentes del Sistema
1. **brokerFileManager** (Puerto 32002)
   - Coordina conexiones entre clientes y servidores
   - Proporciona información de conexión a los clientes
   - Debe iniciarse primero

2. **serverFileManager** (Puerto 32001)
   - Gestiona archivos en carpeta `FileManagerDir`
   - Se registra con el broker al iniciar
   - Recibe IP del broker como parámetro

3. **clienteFileManager**
   - Interfaz de usuario para gestionar archivos
   - Comandos: `ls`, `lls`, `upload`, `download`, `exit`

### Configuraciones Disponibles

####  Configuración Básica (5 puntos)
- 1 nodo master (control-plane)
- 1 nodo worker con broker
- 1 nodo worker con servidor
- 1 réplica de cada servicio

####  Configuración Avanzada 1 (+2 puntos)
- Múltiples réplicas del servidor en UN SOLO nodo
- Carpeta compartida usando **hostPath**
- Todos los pods ven los mismos archivos

####  Configuración Avanzada 2 (+5 puntos)
- Múltiples réplicas en VARIOS nodos
- Carpeta compartida usando **NFS** (Network File System)
- Persistencia de datos entre nodos

---

##  ARQUITECTURA DEL SISTEMA <a name="arquitectura"></a>

```

                      NODO MASTER                             
                   (Control Plane)                            
    
    • Kubernetes API Server                               
    • etcd                                                 
    • Scheduler                                            
    • Controller Manager                                  
    

                            
        
                                               
                    
  NODO WORKER 1                       NODO WORKER 2  
                                                     
                            
    BROKER                            SERVER 1   
    POD                               POD        
   :32002                             :32001     
                            
                                        
  NodePort                              SERVER 2   
  Service                               POD        
                                        :32001     
                        
                                                       
                                        NodePort       
                                        Service +      
                                        LoadBalancer   
                                      
                                               
                                      
                                         Volumen NFS   
                                        (Opcional)     
                                       FileManagerDir  
                                      
```

---

##  GUÍA DE CONFIGURACIÓN PASO A PASO <a name="configuracion"></a>

### FASE 1: PREPARACIÓN INICIAL

#### 1.1. Obtener Ejecutables
```bash
# Descargar P3FileManager.zip del Blackboard
cd /home/nirmata/Documentos/University/U-Tad/3th_Course/Q1/Distributed_Systems/Unit_4/AEC4

# Copiar ejecutables a sus ubicaciones
cp /ruta/descarga/brokerFileManager docker/broker/
cp /ruta/descarga/serverFileManager docker/server/
cp /ruta/descarga/clienteFileManager client/
```

#### 1.2. Verificar Estructura del Proyecto
```bash
tree -L 2
# Deberías ver:
#  docker/
#     broker/
#        Dockerfile
#        brokerFileManager
#     server/
#         Dockerfile
#         serverFileManager
#  kubernetes/
#     broker/
#     server/
#     nfs/
#  client/
#      clienteFileManager
```

---

### FASE 2: CREACIÓN DE IMÁGENES DOCKER

#### 2.1. Construir Imagen del Broker
```bash
cd docker/broker/

# Revisar Dockerfile
cat Dockerfile

# Construir imagen (reemplaza <tu-usuario> con tu Docker Hub username)
docker build -t <tu-usuario>/broker-filemanager:latest .

# Verificar
docker images | grep broker
```

#### 2.2. Construir Imagen del Servidor
```bash
cd ../server/

# Revisar Dockerfile
cat Dockerfile

# Construir imagen
docker build -t <tu-usuario>/server-filemanager:latest .

# Verificar
docker images | grep server
```

#### 2.3. Subir Imágenes a Docker Hub
```bash
# Iniciar sesión en Docker Hub
docker login
# Ingresar usuario y contraseña

# Subir imágenes
docker push <tu-usuario>/broker-filemanager:latest
docker push <tu-usuario>/server-filemanager:latest

# Verificar en https://hub.docker.com/
```

** Script Automático:**
```bash
./build-images.sh <tu-usuario>
```

---

### FASE 3: CONFIGURACIÓN DE AWS EC2

#### 3.1. Crear Instancias EC2

**Especificaciones mínimas:**
- **AMI:** Ubuntu Server 20.04 LTS
- **Tipo:** t2.medium (2 vCPUs, 4 GB RAM)
- **Cantidad:** Mínimo 2 instancias (1 master + 1 worker)

**Configuración de Security Group:**
```
PUERTO      PROTOCOLO    ORIGEN          DESCRIPCIÓN
22          TCP          0.0.0.0/0       SSH
6443        TCP          VPC             Kubernetes API
2379-2380   TCP          VPC             etcd
10250       TCP          VPC             Kubelet API
10251       TCP          VPC             kube-scheduler
10252       TCP          VPC             kube-controller
32001-32002 TCP          0.0.0.0/0       Aplicación
2049        TCP          VPC             NFS (opcional)
```

#### 3.2. Conectar a las Instancias
```bash
# Dar permisos a la clave
chmod 400 tu-clave.pem

# Conectar al master
ssh -i "tu-clave.pem" ubuntu@<MASTER_IP>

# Conectar a cada worker (en otra terminal)
ssh -i "tu-clave.pem" ubuntu@<WORKER_IP>
```

---

### FASE 4: INSTALACIÓN DE DEPENDENCIAS

#### 4.1. Instalar Docker (EN TODAS LAS INSTANCIAS)
```bash
# Actualizar sistema
sudo apt-get update && sudo apt-get upgrade -y

# Instalar dependencias
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release

# Añadir repositorio de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Añadir usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker

# Verificar
docker --version
```

#### 4.2. Instalar Kubernetes (EN TODAS LAS INSTANCIAS)
```bash
# Deshabilitar swap
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

# Cargar módulos del kernel
sudo modprobe overlay
sudo modprobe br_netfilter

# Configurar parámetros del sistema
cat <<EOF | sudo tee /etc/sysctl.d/kubernetes.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

sudo sysctl --system

# Añadir repositorio de Kubernetes
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

# Instalar componentes
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl

# Verificar
kubeadm version
```

#### 4.3. Configurar Containerd (EN TODAS LAS INSTANCIAS)
```bash
# Crear configuración
sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml

# Habilitar systemd cgroup
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# Reiniciar servicio
sudo systemctl restart containerd
sudo systemctl enable containerd
```

---

### FASE 5: INICIALIZACIÓN DEL CLUSTER

#### 5.1. Inicializar Master (SOLO EN NODO MASTER)
```bash
# Inicializar cluster
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# Configurar kubectl
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Instalar red de pods (Flannel)
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# Verificar
kubectl get nodes
kubectl get pods -A
```

** IMPORTANTE:** Guardar el comando de join que aparece, similar a:
```bash
kubeadm join <master-ip>:6443 --token <token> \
  --discovery-token-ca-cert-hash sha256:<hash>
```

#### 5.2. Unir Workers al Cluster (EN CADA NODO WORKER)
```bash
# Ejecutar el comando de join guardado
sudo kubeadm join <master-ip>:6443 --token <token> \
  --discovery-token-ca-cert-hash sha256:<hash>
```

#### 5.3. Verificar Cluster (EN NODO MASTER)
```bash
kubectl get nodes
# Todos los nodos deben aparecer como "Ready"

kubectl get pods -A
# Todos los pods del sistema deben estar "Running"
```

---

### FASE 6: DESPLIEGUE DE APLICACIONES

#### 6.1. Actualizar Archivos YAML
```bash
# En tu máquina local o master
./update-yamls.sh <tu-usuario>

# O manualmente:
# Editar kubernetes/broker/deployment.yaml
# Editar kubernetes/server/deployment-basic.yaml
# Reemplazar <tu-usuario> con tu Docker Hub username
```

#### 6.2. Copiar Archivos al Master
```bash
# Desde tu máquina local
scp -i "tu-clave.pem" -r kubernetes/ ubuntu@<MASTER_IP>:~/
```

#### 6.3. Desplegar Broker
```bash
# En el nodo master
kubectl apply -f kubernetes/broker/deployment.yaml

# Verificar
kubectl get deployments
kubectl get pods -l app=broker
kubectl get services
```

#### 6.4. Desplegar Servidor

**Opción A: Configuración Básica (5 puntos)**
```bash
kubectl apply -f kubernetes/server/deployment-basic.yaml

# Verificar
kubectl get deployments
kubectl get pods -l app=filemanager-server
kubectl get services
```

**Opción B: Configuración Avanzada 1 (+2 puntos - hostPath)**
```bash
kubectl apply -f kubernetes/server/deployment-advanced1.yaml

# Verificar réplicas
kubectl get pods -o wide -l app=filemanager-server
# Deben estar en el mismo nodo

# Verificar volumen
kubectl describe pod <server-pod-name>
```

**Opción C: Configuración Avanzada 2 (+5 puntos - NFS)**
```bash
# Primero configurar NFS (ver sección siguiente)
# Luego desplegar
kubectl apply -f kubernetes/nfs/nfs-pv-pvc.yaml
kubectl apply -f kubernetes/server/deployment-advanced2.yaml

# Verificar
kubectl get pv
kubectl get pvc
kubectl get pods -o wide -l app=filemanager-server
# Deben estar en diferentes nodos
```

---

### FASE 7: PRUEBAS Y VALIDACIÓN

#### 7.1. Verificar Estado del Cluster
```bash
# Ver todos los recursos
kubectl get all

# Ver pods en detalle
kubectl get pods -o wide

# Ver logs del broker
kubectl logs <broker-pod-name>

# Ver logs de un servidor
kubectl logs <server-pod-name>
```

#### 7.2. Probar con el Cliente

**Preparar archivos de prueba:**
```bash
cd client/
echo "Archivo de prueba 1" > test1.txt
echo "Archivo de prueba 2" > test2.txt
echo "Contenido demo" > demo.txt
```

**Ejecutar cliente:**
```bash
# Obtener IP del nodo master o worker
kubectl get nodes -o wide

# Ejecutar cliente
./clienteFileManager <IP_DEL_NODO>
```

**Comandos de prueba:**
```
ls              # Listar archivos locales
lls             # Listar archivos remotos (vacío inicialmente)
upload test1.txt # Subir archivo
lls             # Verificar que aparece test1.txt
upload test2.txt
upload demo.txt
lls             # Ver todos los archivos
download test1.txt  # Descargar archivo
exit            # Salir
```

---

##  GUIÓN PARA LA PRESENTACIÓN <a name="presentacion"></a>

### ESTRUCTURA DEL VIDEO (15-20 minutos)

---

####  PARTE 1: INTRODUCCIÓN (2 minutos)

**Qué mostrar:**
```
- Diapositiva con tu nombre y asignatura
- Título: "AEC4 - Despliegue de Aplicación Distribuida con Kubernetes"
- Diagrama de arquitectura del sistema
```

**Qué decir:**
```
"Buenos días/tardes. En este video voy a presentar la práctica AEC4 de Sistemas 
Distribuidos, donde he implementado el despliegue de una aplicación de gestión 
de archivos distribuida utilizando Kubernetes en AWS EC2.

La aplicación consta de tres componentes principales:
1. Un broker que coordina las conexiones
2. Servidores que gestionan archivos
3. Clientes que interactúan con los servidores

He implementado la [CONFIGURACIÓN BÁSICA / AVANZADA 1 / AVANZADA 2], que incluye
[describir características específicas]."
```

---

####  PARTE 2: ARQUITECTURA DEL CLUSTER (3 minutos)

**Qué mostrar:

##  Niveles de Configuración

### Básico (5 puntos) 
- [x] 1 nodo master
- [x] 1 pod broker
- [x] 1 pod servidor
- [x] Servicios funcionando

**Archivo a usar:** `kubernetes/server/deployment-basic.yaml`

### Avanzado 1 (+2 puntos) 
- [x] Todo lo básico
- [x] Múltiples réplicas del servidor en UN nodo
- [x] Volumen compartido con `hostPath`
- [x] Datos persistentes

**Archivo a usar:** `kubernetes/server/deployment-advanced1.yaml`

**Preparación adicional:**
```bash
# En el nodo worker, crear carpeta compartida
ssh ubuntu@WORKER_IP
sudo mkdir -p /mnt/filemanager-shared
sudo chmod 777 /mnt/filemanager-shared
```

### Avanzado 2 (+5 puntos) 
- [x] Todo lo básico
- [x] Múltiples réplicas en MÚLTIPLES nodos
- [x] Volumen NFS compartido entre nodos
- [x] Datos persistentes y sincronizados

**Archivos a usar:**
- `kubernetes/nfs/nfs-pv-pvc.yaml`
- `kubernetes/server/deployment-advanced2.yaml`

**Preparación adicional:**
```bash
# Configurar servidor NFS (ver docs/setup.md sección 11)
# O usar el servidor NFS interno del cluster
kubectl apply -f kubernetes/nfs/nfs-server-setup.yaml
```

---

##  Para el Video Demostrativo


### Configuración Avanzada 1: HostPath (Múltiples réplicas, un nodo)

**Requisito:**
- Varios pods/réplicas en UN MISMO nodo
- Carpeta compartida usando `hostPath`

**Deployment:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: server-deployment
spec:
  replicas: 3  # Múltiples réplicas
  selector:
    matchLabels:
      app: filemanager-server
  template:
    metadata:
      labels:
        app: filemanager-server
    spec:
      # Forzar que todos los pods estén en el mismo nodo
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - filemanager-server
            topologyKey: kubernetes.io/hostname
      containers:
      - name: server
        image: <tu-usuario>/server-filemanager:latest
        args: ["broker-service"]
        ports:
        - containerPort: 32001
        volumeMounts:
        - name: file-storage
          mountPath: /app/FileManagerDir
      volumes:
      - name: file-storage
        hostPath:
          path: /data/FileManagerDir  # Carpeta en el nodo host
          type: DirectoryOrCreate
```

**Preparación del nodo:**
```bash
# En el nodo worker donde correrán los pods
sudo mkdir -p /data/FileManagerDir
sudo chmod 777 /data/FileManagerDir
```

---

### Configuración Avanzada 2: NFS (Múltiples réplicas, múltiples nodos)

**Requisito:**
- Varios nodos esclavos
- Múltiples réplicas distribuidas
- Almacenamiento compartido en red (NFS)

#### Paso 1: Configurar Servidor NFS

**En un nodo o instancia separada:**
```bash
# Instalar servidor NFS
sudo apt-get update
sudo apt-get install -y nfs-kernel-server

# Crear directorio compartido
sudo mkdir -p /mnt/nfs-share/FileManagerDir
sudo chmod 777 /mnt/nfs-share

# Configurar exports
echo "/mnt/nfs-share *(rw,sync,no_subtree_check,no_root_squash)" | sudo tee -a /etc/exports

# Reiniciar NFS
sudo exportfs -a
sudo systemctl restart nfs-kernel-server

# Verificar
showmount -e localhost
```

#### Paso 2: Instalar Cliente NFS en Workers

**En TODOS los nodos worker:**
```bash
sudo apt-get install -y nfs-common
```

#### Paso 3: Crear PersistentVolume y PersistentVolumeClaim

**Archivo: kubernetes/nfs/nfs-pv-pvc.yaml**
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteMany
  nfs:
    server: <IP_SERVIDOR_NFS>  # IP del servidor NFS
    path: "/mnt/nfs-share"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nfs-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
```

#### Paso 4: Deployment con NFS

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: server-deployment
spec:
  replicas: 3  # Distribuidas en múltiples nodos
  selector:
    matchLabels:
      app: filemanager-server
  template:
    metadata:
      labels:
        app: filemanager-server
    spec:
      containers:
      - name: server
        image: <tu-usuario>/server-filemanager:latest
        args: ["broker-service"]
        ports:
        - containerPort: 32001
        volumeMounts:
        - name: nfs-storage
          mountPath: /app/FileManagerDir
      volumes:
      - name: nfs-storage
        persistentVolumeClaim:
          claimName: nfs-pvc
```

---

##  SCRIPTS DE AYUDA <a name="scripts"></a>

### Script: build-images.sh

```bash
#!/bin/bash

# Script para construir y subir imágenes Docker

if [ -z "$1" ]; then
    echo " Error: Debes proporcionar tu usuario de Docker Hub"
    echo "Uso: ./build-images.sh <tu-usuario>"
    exit 1
fi

DOCKER_USER=$1

echo " Construyendo imágenes para usuario: $DOCKER_USER"

# Construir broker
echo " Construyendo broker-filemanager..."
cd docker/broker/
docker build -t $DOCKER_USER/broker-filemanager:latest .

# Construir servidor
echo " Construyendo server-filemanager..."
cd ../server/
docker build -t $DOCKER_USER/server-filemanager:latest .

cd ../../

echo " Imágenes construidas exitosamente"
echo ""
echo " Subiendo imágenes a Docker Hub..."

docker push $DOCKER_USER/broker-filemanager:latest
docker push $DOCKER_USER/server-filemanager:latest

echo " Proceso completado"
echo ""
echo " Verifica tus imágenes en: https://hub.docker.com/u/$DOCKER_USER"
```

### Script: update-yamls.sh

```bash
#!/bin/bash

# Script para actualizar archivos YAML con usuario de Docker Hub

if [ -z "$1" ]; then
    echo " Error: Debes proporcionar tu usuario de Docker Hub"
    echo "Uso: ./update-yamls.sh <tu-usuario>"
    exit 1
fi

DOCKER_USER=$1

echo " Actualizando archivos YAML con usuario: $DOCKER_USER"

# Actualizar deployment del broker
sed -i "s/<tu-usuario>/$DOCKER_USER/g" kubernetes/broker/deployment.yaml
echo " kubernetes/broker/deployment.yaml"

# Actualizar deployments del servidor
sed -i "s/<tu-usuario>/$DOCKER_USER/g" kubernetes/server/deployment-basic.yaml
echo " kubernetes/server/deployment-basic.yaml"

sed -i "s/<tu-usuario>/$DOCKER_USER/g" kubernetes/server/deployment-advanced1.yaml
echo " kubernetes/server/deployment-advanced1.yaml"

sed -i "s/<tu-usuario>/$DOCKER_USER/g" kubernetes/server/deployment-advanced2.yaml
echo " kubernetes/server/deployment-advanced2.yaml"

echo ""
echo " Todos los archivos YAML han sido actualizados"
echo " Ya puedes desplegarlos con: kubectl apply -f <archivo.yaml>"
```

### Script: cleanup.sh

```bash
#!/bin/bash

# Script para limpiar recursos de Kubernetes

echo " Limpiando recursos de Kubernetes..."

# Eliminar deployments
kubectl delete deployment broker-deployment 2>/dev/null
kubectl delete deployment server-deployment 2>/dev/null

# Eliminar services
kubectl delete service broker-service 2>/dev/null
kubectl delete service server-service 2>/dev/null

# Eliminar PVC y PV (si existen)
kubectl delete pvc nfs-pvc 2>/dev/null
kubectl delete pv nfs-pv 2>/dev/null

echo ""
echo " Limpieza completada"
echo " Estado actual:"
kubectl get all
```

### Script: status.sh

```bash
#!/bin/bash

# Script para ver estado del cluster

echo ""
echo " ESTADO DEL CLUSTER KUBERNETES"
echo ""
echo ""

echo "  NODOS:"
kubectl get nodes -o wide
echo ""

echo " PODS:"
kubectl get pods -o wide
echo ""

echo " SERVICES:"
kubectl get services
echo ""

echo " DEPLOYMENTS:"
kubectl get deployments
echo ""

echo " PERSISTENT VOLUMES:"
kubectl get pv
kubectl get pvc
echo ""

echo " LOGS RECIENTES DEL BROKER:"
BROKER_POD=$(kubectl get pods -l app=broker -o jsonpath='{.items[0].metadata.name}')
if [ ! -z "$BROKER_POD" ]; then
    kubectl logs $BROKER_POD --tail=10
else
    echo "No se encontró pod del broker"
fi
echo ""

echo ""
```

---

##  SOLUCIÓN DE PROBLEMAS <a name="troubleshooting"></a>

### Problema 1: Pod en estado Pending

**Síntoma:**
```bash
kubectl get pods
# NAME                               READY   STATUS    RESTARTS   AGE
# server-deployment-xxx              0/1     Pending   0          5m
```

**Soluciones:**
```bash
# Ver detalles del problema
kubectl describe pod <pod-name>

# Causas comunes:
# 1. Recursos insuficientes
kubectl top nodes

# 2. Volumen no disponible
kubectl get pv
kubectl get pvc

# 3. Imagen no encontrada
kubectl describe pod <pod-name> | grep -i image
```

### Problema 2: Service no accesible desde fuera

**Síntoma:**
```bash
# No puedo conectar el cliente a la IP del nodo
./clienteFileManager <IP_NODO>
# Connection refused
```

**Soluciones:**
```bash
# 1. Verificar que el service está creado
kubectl get services

# 2. Verificar que el puerto está expuesto
kubectl describe service broker-service

# 3. Verificar security group en AWS
# Debe permitir tráfico en puertos 32001-32002

# 4. Verificar que el pod está corriendo
kubectl get pods

# 5. Probar desde dentro del cluster
kubectl run -it --rm debug --image=busybox --restart=Never -- sh
# Dentro del pod:
# wget -O- http://broker-service:32002
```

### Problema 3: Pods no pueden ver archivos compartidos

**Síntoma (Avanzada 1):**
```bash
# Los pods no ven los mismos archivos
```

**Soluciones:**
```bash
# 1. Verificar que los pods están en el mismo nodo
kubectl get pods -o wide

# 2. Verificar montaje del volumen
kubectl describe pod <pod-name> | grep -A 10 Mounts

# 3. Verificar que el directorio hostPath existe
ssh al-nodo
ls -la /data/FileManagerDir

# 4. Verificar permisos
sudo chmod 777 /data/FileManagerDir
```

**Síntoma (Avanzada 2):**
```bash
# Error montando volumen NFS
```

**Soluciones:**
```bash
# 1. Verificar que el servidor NFS está corriendo
systemctl status nfs-server

# 2. Verificar exports
cat /etc/exports
showmount -e localhost

# 3. Probar montaje manual desde un nodo
sudo mount -t nfs <NFS_SERVER_IP>:/mnt/nfs-share /mnt/test
ls -la /mnt/test

# 4. Verificar firewall/security groups
# Puerto 2049 debe estar abierto
```

### Problema 4: Cliente no encuentra broker

**Síntoma:**
```bash
./clienteFileManager <IP>
# No se puede conectar al broker
```

**Soluciones:**
```bash
# 1. Obtener la IP correcta
kubectl get nodes -o wide
# Usar IP EXTERNAL

# 2. Verificar que el broker está corriendo
kubectl get pods -l app=broker

# 3. Ver logs del broker
kubectl logs <broker-pod-name>

# 4. Verificar puerto NodePort
kubectl get service broker-service
# Debe mostrar 32002:32002/TCP

# 5. Probar conexión con netcat
nc -zv <IP_NODO> 32002
```

### Problema 5: Imágenes no se descargan

**Síntoma:**
```bash
kubectl describe pod <pod-name>
# Failed to pull image...  ErrImagePull
```

**Soluciones:**
```bash
# 1. Verificar que la imagen existe en Docker Hub
docker pull <tu-usuario>/broker-filemanager:latest

# 2. Crear secret para Docker Hub (si es privado)
kubectl create secret docker-registry dockerhub-secret \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=<tu-usuario> \
  --docker-password=<tu-password> \
  --docker-email=<tu-email>

# 3. Añadir secret al deployment
# En el YAML, bajo spec.template.spec:
# imagePullSecrets:
# - name: dockerhub-secret

# 4. Verificar nombre de la imagen en el YAML
grep image kubernetes/*/deployment*.yaml
```

### Problema 6: Nodo no se une al cluster

**Síntoma:**
```bash
# En el worker:
sudo kubeadm join...
# Error de token o certificado
```

**Soluciones:**
```bash
# 1. Generar nuevo token en el master
kubeadm token create --print-join-command

# 2. Verificar conectividad
ping <MASTER_IP>
telnet <MASTER_IP> 6443

# 3. Verificar que containerd está corriendo
systemctl status containerd

# 4. Resetear kubeadm en el worker y reintentar
sudo kubeadm reset
# Luego volver a ejecutar el join
```

### Comandos Útiles de Diagnóstico

```bash
# Ver todos los eventos del cluster
kubectl get events --sort-by='.lastTimestamp'

# Ver estado detallado de un recurso
kubectl describe <tipo> <nombre>

# Ver logs en tiempo real
kubectl logs -f <pod-name>

# Ejecutar shell dentro de un pod
kubectl exec -it <pod-name> -- /bin/bash

# Ver uso de recursos
kubectl top nodes
kubectl top pods

# Ver configuración de un recurso
kubectl get <tipo> <nombre> -o yaml

# Ver todos los recursos en todos los namespaces
kubectl get all -A

# Forzar eliminación de un pod
kubectl delete pod <pod-name> --force --grace-period=0
```

---

##  RECURSOS ADICIONALES

### Documentación Oficial
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

### Archivos del Proyecto
- `docs/setup.md` - Guía detallada de instalación
- `docs/demo-script.md` - Script completo para demostración
- `docs/cheatsheet.md` - Comandos rápidos de referencia

### Configuraciones del Proyecto
```
kubernetes/
 broker/
    deployment.yaml          # Deployment del broker
 server/
    deployment-basic.yaml    # Configuración básica (5 pts)
    deployment-advanced1.yaml # hostPath (7 pts)
    deployment-advanced2.yaml # NFS (10 pts)
 nfs/
     nfs-server.yaml          # Servidor NFS
     nfs-pv-pvc.yaml          # Volúmenes persistentes
```

---

##  CHECKLIST DE ENTREGA

### Archivos a Entregar (archivo ZIP)

- [ ] **Dockerfiles**
  - [ ] `docker/broker/Dockerfile`
  - [ ] `docker/server/Dockerfile`

- [ ] **Archivos YAML de Kubernetes**
  - [ ] `kubernetes/broker/deployment.yaml`
  - [ ] `kubernetes/server/deployment-[basic|advanced1|advanced2].yaml`
  - [ ] `kubernetes/nfs/*.yaml` (si aplica)

- [ ] **Video de Demostración** (15-20 min)
  - [ ] Introducción y descripción de la configuración
  - [ ] Mostrar nodos del cluster
  - [ ] Explicar Dockerfiles
  - [ ] Explicar archivos YAML
  - [ ] Mostrar pods, services y deployments activos
  - [ ] Demostración con cliente 1:
    - [ ] Comando `ls`
    - [ ] Comando `lls`
    - [ ] Comando `upload`
    - [ ] Verificar con `lls`
  - [ ] Cerrar cliente 1
  - [ ] Demostración con cliente 2:
    - [ ] Comando `lls` (ver archivos del cliente 1)
    - [ ] Comando `download`
    - [ ] Verificar descarga
  - [ ] Conclusiones

- [ ] **Documentación adicional** (opcional)
  - [ ] README con instrucciones
  - [ ] Capturas de pantalla
  - [ ] Diagrama de arquitectura

---

##  CRITERIOS DE EVALUACIÓN

### Configuración Básica (5 puntos)
-  Cluster con al menos 2 nodos (master + worker)
-  Dockerfile funcional para broker
-  Dockerfile funcional para servidor  
-  Deployment del broker con service NodePort
-  Deployment del servidor con service NodePort
-  Cliente puede conectarse y realizar operaciones

### Configuración Avanzada 1 (+2 puntos)
-  Múltiples réplicas del servidor en un nodo
-  Volumen compartido con hostPath
-  Todos los pods acceden a los mismos archivos
-  Persistencia entre conexiones de clientes

### Configuración Avanzada 2 (+5 puntos)
-  Múltiples nodos worker
-  Réplicas distribuidas en diferentes nodos
-  Servidor NFS configurado
-  PersistentVolume y PersistentVolumeClaim
-  Almacenamiento compartido en red funcional
-  Persistencia entre reinicios de pods

---

##  CONSEJOS FINALES

### Para la Configuración
1. **Empieza Simple:** Consigue que funcione la configuración básica primero
2. **Prueba Local:** Verifica los ejecutables en EC2 antes de containerizar
3. **Security Groups:** No olvides abrir los puertos necesarios en AWS
4. **Documenta:** Anota cada paso y problema que encuentres
5. **Backup:** Guarda copia de tus archivos YAML y configuraciones

### Para el Video
1. **Planificación:** Escribe un guión detallado antes de grabar
2. **Práctica:** Prueba la demo completa 2-3 veces antes de grabar
3. **Calidad:** Usa resolución mínima 1080p, audio claro
4. **Edición:** Corta partes largas de espera o errores
5. **Duración:** Mantén el video entre 15-20 minutos
6. **Claridad:** Explica cada paso, no asumas conocimiento previo

### Para la Presentación
1. **Introducción Clara:** Explica qué configuración implementaste
2. **Arquitectura Visual:** Muestra diagrama del cluster
3. **Código Comentado:** Explica partes importantes de Dockerfiles y YAMLs
4. **Demo Fluida:** Practica hasta que salga natural
5. **Persistencia:** Demuestra que los datos persisten
6. **Balanceo:** Si aplica, muestra cómo se distribuyen las peticiones
7. **Conclusión:** Resume logros y aprendizajes

---

##  CONTACTO Y SOPORTE

Si tienes dudas adicionales:
1. Revisa la documentación en `docs/`
2. Consulta los ejemplos en el repositorio
3. Contacta al profesor durante las horas de tutoría
4. Revisa el foro de la asignatura en Blackboard

---

**Última actualización:** Diciembre 2025  
**Versión:** 2.0  
**Asignatura:** Sistemas Distribuidos - U-TAD  
**Práctica:** AEC4 - Despliegue con Kubernetes

---

**¡Éxito con tu presentación!** 
