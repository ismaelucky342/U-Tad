# Guía de Configuración del Cluster Kubernetes

## 1. Preparación de Instancias EC2

### 1.1 Crear Instancias
- Crear al menos 2 instancias EC2 (Ubuntu 20.04 LTS)
  - t2.medium o superior recomendado
  - Mínimo 2 CPUs y 2GB RAM por instancia
- Asignar IPs elásticas (opcional pero recomendado)
- Configurar security groups:
  - Puerto 22 (SSH)
  - Puerto 6443 (Kubernetes API)
  - Puertos 32001-32002 (aplicaciones)
  - Puertos 10250-10252 (Kubelet)
  - Puerto 2049 (NFS, si aplica)

### 1.2 Conectar a las Instancias
```bash
ssh -i "tu-clave.pem" ubuntu@<EC2_IP>
```

## 2. Instalación de Docker

En **todas las instancias**:

```bash
# Actualizar paquetes
sudo apt-get update
sudo apt-get upgrade -y

# Instalar dependencias
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Añadir clave GPG de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Añadir repositorio
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Añadir usuario al grupo docker
sudo usermod -aG docker $USER

# Verificar instalación
docker --version
```

## 3. Instalación de Kubernetes

En **todas las instancias**:

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

# Verificar instalación
kubeadm version
```

## 4. Configurar Containerd

```bash
# Crear directorio de configuración
sudo mkdir -p /etc/containerd

# Generar configuración por defecto
sudo containerd config default | sudo tee /etc/containerd/config.toml

# Editar configuración para usar systemd cgroup
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# Reiniciar containerd
sudo systemctl restart containerd
sudo systemctl enable containerd
```

## 5. Inicializar Cluster (Solo en Nodo Master)

```bash
# Inicializar cluster
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# Configurar kubectl para el usuario
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Instalar red de pods (Flannel)
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# Verificar nodos
kubectl get nodes
```

**Guardar el comando de join** que aparece al final, similar a:
```bash
kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

## 6. Unir Nodos Esclavos al Cluster

En cada **nodo esclavo**:

```bash
# Ejecutar el comando de join obtenido del master
sudo kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

Verificar desde el **nodo master**:
```bash
kubectl get nodes
# Todos los nodos deberían aparecer como Ready
```

## 7. Construir y Subir Imágenes Docker

En tu **máquina local o en una instancia EC2**:

```bash
# Navegar al directorio del broker
cd docker/broker/
# Copiar el ejecutable brokerFileManager aquí
cp /ruta/al/brokerFileManager .

# Construir imagen
docker build -t <tu-usuario>/broker-filemanager:latest .

# Subir a Docker Hub
docker login
docker push <tu-usuario>/broker-filemanager:latest

# Repetir para el servidor
cd ../server/
cp /ruta/al/serverFileManager .
docker build -t <tu-usuario>/server-filemanager:latest .
docker push <tu-usuario>/server-filemanager:latest
```

## 8. Desplegar Aplicaciones en Kubernetes

Desde el **nodo master**:

```bash
# Actualizar las imágenes en los archivos YAML con tu usuario de Docker Hub

# Desplegar broker
kubectl apply -f kubernetes/broker/deployment.yaml

# Verificar que el broker esté corriendo
kubectl get pods
kubectl get services

# Desplegar servidor (configuración básica)
kubectl apply -f kubernetes/server/deployment-basic.yaml

# Verificar deployments
kubectl get deployments
kubectl get pods
kubectl get services
```

## 9. Probar la Aplicación

Desde tu **máquina local o cliente**:

```bash
# Copiar el ejecutable del cliente
# Ejecutar el cliente apuntando a la IP del master y puerto del broker
./clienteFileManager <MASTER_IP>

# Una vez conectado, probar comandos:
ls       # Listar archivos locales
lls      # Listar archivos remotos
upload archivo.txt
download archivo.txt
exit
```

## 10. Configuración Avanzada 1 (Opcional +2 puntos)

```bash
# En el nodo esclavo, crear carpeta compartida
sudo mkdir -p /mnt/filemanager-shared
sudo chmod 777 /mnt/filemanager-shared

# Aplicar deployment avanzado 1
kubectl apply -f kubernetes/server/deployment-advanced1.yaml

# Verificar réplicas
kubectl get pods -o wide
```

## 11. Configuración Avanzada 2 (Opcional +5 puntos)

### Opción A: Servidor NFS Externo

En una **instancia dedicada como servidor NFS**:

```bash
# Instalar servidor NFS
sudo apt-get install -y nfs-kernel-server

# Crear directorio para exportar
sudo mkdir -p /exports/filemanager
sudo chmod 777 /exports/filemanager

# Configurar exportación
echo "/exports/filemanager *(rw,sync,no_subtree_check,no_root_squash)" | sudo tee -a /etc/exports

# Reiniciar servicio
sudo exportfs -ra
sudo systemctl restart nfs-kernel-server
```

En **todos los nodos del cluster**:

```bash
# Instalar cliente NFS
sudo apt-get install -y nfs-common
```

Desde el **nodo master**:

```bash
# Editar kubernetes/nfs/nfs-pv-pvc.yaml con la IP del servidor NFS
# Aplicar PV y PVC
kubectl apply -f kubernetes/nfs/nfs-pv-pvc.yaml

# Verificar
kubectl get pv
kubectl get pvc

# Desplegar con almacenamiento NFS
kubectl apply -f kubernetes/server/deployment-advanced2.yaml
```

### Opción B: Servidor NFS dentro del Cluster

```bash
kubectl apply -f kubernetes/nfs/nfs-server-setup.yaml
kubectl apply -f kubernetes/nfs/nfs-pv-pvc.yaml
kubectl apply -f kubernetes/server/deployment-advanced2.yaml
```

## 12. Comandos Útiles de Depuración

```bash
# Ver logs de un pod
kubectl logs <pod-name>

# Entrar en un pod
kubectl exec -it <pod-name> -- /bin/bash

# Ver detalles de un pod
kubectl describe pod <pod-name>

# Ver detalles de un servicio
kubectl describe service <service-name>

# Ver eventos del cluster
kubectl get events

# Eliminar un deployment
kubectl delete deployment <deployment-name>

# Escalar un deployment
kubectl scale deployment <deployment-name> --replicas=5

# Ver recursos del cluster
kubectl top nodes
kubectl top pods
```

## 13. Limpieza

Para limpiar todos los recursos:

```bash
kubectl delete -f kubernetes/server/
kubectl delete -f kubernetes/broker/
kubectl delete -f kubernetes/nfs/
```

## Troubleshooting

### Problema: Los pods no se inician
- Verificar logs: `kubectl logs <pod-name>`
- Verificar eventos: `kubectl describe pod <pod-name>`
- Verificar que las imágenes existan en Docker Hub

### Problema: No se puede conectar al servicio
- Verificar que los security groups permitan los puertos
- Verificar que los servicios estén corriendo: `kubectl get services`
- Usar la IP externa del nodo para conectar

### Problema: Los archivos no persisten
- Para configuración básica, esto es normal (emptyDir)
- Para configuración avanzada, verificar que el volumen esté montado correctamente
- Verificar permisos de la carpeta compartida

### Problema: NFS no funciona
- Verificar que el servidor NFS esté corriendo
- Verificar que el cliente NFS esté instalado en todos los nodos
- Verificar reglas de firewall para puerto 2049
- Probar montar manualmente: `sudo mount -t nfs <nfs-server-ip>:/exports/filemanager /mnt/test`
