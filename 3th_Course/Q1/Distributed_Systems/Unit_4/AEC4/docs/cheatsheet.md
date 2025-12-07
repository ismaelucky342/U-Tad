# Comandos Rápidos - Cheat Sheet

##  Setup Inicial

### Instalar Docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

### Instalar Kubernetes
```bash
# Deshabilitar swap
sudo swapoff -a

# Instalar kubeadm, kubelet, kubectl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

### Inicializar Master
```bash
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

##  Docker

### Construir y Subir Imágenes
```bash
# Broker
cd docker/broker/
docker build -t usuario/broker-filemanager:latest .
docker push usuario/broker-filemanager:latest

# Server
cd docker/server/
docker build -t usuario/server-filemanager:latest .
docker push usuario/server-filemanager:latest
```

### Comandos Útiles
```bash
docker images                    # Listar imágenes
docker ps                        # Listar contenedores corriendo
docker ps -a                     # Listar todos los contenedores
docker logs <container-id>       # Ver logs
docker exec -it <container-id> bash  # Entrar al contenedor
docker rm <container-id>         # Eliminar contenedor
docker rmi <image-id>           # Eliminar imagen
```

##  Kubernetes

### Desplegar Aplicaciones
```bash
# Broker
kubectl apply -f kubernetes/broker/deployment.yaml

# Server (elegir uno)
kubectl apply -f kubernetes/server/deployment-basic.yaml
kubectl apply -f kubernetes/server/deployment-advanced1.yaml
kubectl apply -f kubernetes/server/deployment-advanced2.yaml

# NFS (si usas advanced2)
kubectl apply -f kubernetes/nfs/nfs-pv-pvc.yaml
```

### Ver Recursos
```bash
kubectl get nodes               # Ver nodos
kubectl get pods                # Ver pods
kubectl get pods -o wide        # Ver pods con más detalle
kubectl get services            # Ver servicios
kubectl get deployments         # Ver deployments
kubectl get pv                  # Ver persistent volumes
kubectl get pvc                 # Ver persistent volume claims
kubectl get all                 # Ver todos los recursos
```

### Inspeccionar Recursos
```bash
kubectl describe node <node-name>
kubectl describe pod <pod-name>
kubectl describe service <service-name>
kubectl describe deployment <deployment-name>
kubectl logs <pod-name>
kubectl logs <pod-name> -f      # Seguir logs en tiempo real
kubectl exec -it <pod-name> -- /bin/bash  # Entrar al pod
```

### Gestionar Deployments
```bash
kubectl scale deployment <name> --replicas=3   # Escalar
kubectl delete deployment <name>               # Eliminar
kubectl edit deployment <name>                 # Editar
kubectl rollout status deployment <name>       # Ver estado
kubectl rollout restart deployment <name>      # Reiniciar
```

### Debugging
```bash
kubectl get events                              # Ver eventos
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl top nodes                               # Ver uso de recursos de nodos
kubectl top pods                                # Ver uso de recursos de pods
kubectl port-forward <pod-name> 8080:32001     # Forward de puertos
```

### Limpiar Recursos
```bash
kubectl delete -f <archivo.yaml>               # Eliminar recursos de un archivo
kubectl delete pod <pod-name>                  # Eliminar pod
kubectl delete service <service-name>          # Eliminar servicio
kubectl delete deployment <deployment-name>    # Eliminar deployment
kubectl delete all --all                       #  Eliminar TODO
```

##  NFS

### Instalar Servidor NFS
```bash
sudo apt-get install -y nfs-kernel-server
sudo mkdir -p /exports/filemanager
sudo chmod 777 /exports/filemanager
echo "/exports/filemanager *(rw,sync,no_subtree_check,no_root_squash)" | sudo tee -a /etc/exports
sudo exportfs -ra
sudo systemctl restart nfs-kernel-server
```

### Instalar Cliente NFS
```bash
sudo apt-get install -y nfs-common
```

### Probar NFS
```bash
# Desde un cliente
sudo mkdir -p /mnt/test
sudo mount -t nfs <nfs-server-ip>:/exports/filemanager /mnt/test
ls -la /mnt/test
sudo umount /mnt/test
```

##  Cliente FileManager

### Ejecutar Cliente
```bash
./clienteFileManager <IP_DEL_BROKER>
```

### Comandos Disponibles
```
ls                    # Listar archivos locales
lls                   # Listar archivos remotos
upload archivo.txt    # Subir archivo
download archivo.txt  # Descargar archivo
exit                  # Salir
```

##  AWS EC2

### Conectar a Instancia
```bash
ssh -i "clave.pem" ubuntu@<EC2_IP>
```

### Copiar Archivos
```bash
# A EC2
scp -i "clave.pem" archivo ubuntu@<EC2_IP>:~/

# Desde EC2
scp -i "clave.pem" ubuntu@<EC2_IP>:~/archivo .
```

### Security Groups (Puertos Necesarios)
```
22      - SSH
6443    - Kubernetes API
32001   - Server FileManager
32002   - Broker FileManager
10250-10252 - Kubelet
2049    - NFS (si aplica)
```

##  Troubleshooting

### Pod no inicia
```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl get events
```

### Servicio no accesible
```bash
kubectl get services
kubectl get endpoints
# Verificar security groups en AWS
# Verificar que el pod esté corriendo
```

### Imagen no se descarga
```bash
# Verificar que la imagen existe en Docker Hub
docker pull usuario/imagen:tag

# Verificar en el pod
kubectl describe pod <pod-name> | grep -i image
```

### Nodo Not Ready
```bash
kubectl describe node <node-name>
# Verificar que kubelet esté corriendo
sudo systemctl status kubelet
sudo systemctl restart kubelet
```

##  Monitoreo

### Ver Estado General
```bash
kubectl cluster-info
kubectl get componentstatuses
kubectl get nodes
kubectl get pods --all-namespaces
```

### Métricas de Recursos
```bash
kubectl top nodes
kubectl top pods
kubectl top pods --containers
```

##  Flujo de Trabajo Típico

### 1. Preparar Entorno
```bash
# Construir imágenes
docker build -t usuario/broker:latest docker/broker/
docker build -t usuario/server:latest docker/server/
docker push usuario/broker:latest
docker push usuario/server:latest
```

### 2. Desplegar
```bash
kubectl apply -f kubernetes/broker/deployment.yaml
kubectl apply -f kubernetes/server/deployment-basic.yaml
```

### 3. Verificar
```bash
kubectl get pods
kubectl get services
kubectl logs <broker-pod>
kubectl logs <server-pod>
```

### 4. Probar
```bash
./clienteFileManager <MASTER_IP>
```

### 5. Escalar (Opcional)
```bash
kubectl scale deployment server-deployment --replicas=3
kubectl get pods -w
```

### 6. Actualizar
```bash
# Construir nueva imagen
docker build -t usuario/server:v2 docker/server/
docker push usuario/server:v2

# Actualizar deployment
kubectl set image deployment/server-deployment server=usuario/server:v2
kubectl rollout status deployment/server-deployment
```

### 7. Limpiar
```bash
kubectl delete -f kubernetes/server/deployment-basic.yaml
kubectl delete -f kubernetes/broker/deployment.yaml
```

##  Para el Video

### Comandos Esenciales a Mostrar
```bash
# 1. Estado del cluster
kubectl get nodes -o wide
kubectl get all

# 2. Ver configuraciones
cat kubernetes/broker/deployment.yaml
cat kubernetes/server/deployment-basic.yaml

# 3. Ver pods corriendo
kubectl get pods -o wide
kubectl describe pod <pod-name>
kubectl logs <pod-name>

# 4. Probar cliente
./clienteFileManager <IP>
ls
lls
upload test.txt
download test.txt
exit

# 5. Verificar persistencia (si aplica)
kubectl delete pod <server-pod>
kubectl get pods -w
# Reconectar cliente y verificar archivos
```

##  Notas Importantes

-  Siempre ejecutar `kubectl apply` desde el nodo master
-  Los puertos 32001 y 32002 deben estar abiertos en security groups
-  Para NFS, todos los nodos necesitan nfs-common instalado
-  Las imágenes Docker deben estar en un registry accesible (Docker Hub)
-  Verificar que swap esté deshabilitado en todos los nodos
-  Guardar el token de kubeadm para unir nodos posteriormente
