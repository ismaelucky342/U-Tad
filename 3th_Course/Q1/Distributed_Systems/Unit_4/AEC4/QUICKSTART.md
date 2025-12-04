# 🚀 Quick Start Guide

## Pasos Rápidos para Empezar

### 1️⃣ Obtener los Ejecutables

Descarga el archivo `P3FileManager.zip` del Blackboard y extrae los ejecutables:

```bash
# Copiar ejecutables a sus ubicaciones
cp ruta/al/brokerFileManager docker/broker/
cp ruta/al/serverFileManager docker/server/
cp ruta/al/clienteFileManager client/
```

### 2️⃣ Construir Imágenes Docker

```bash
# Usar el script de ayuda
./build-images.sh TU_USUARIO_DOCKERHUB

# O manualmente:
cd docker/broker/
docker build -t tu-usuario/broker-filemanager:latest .
cd ../server/
docker build -t tu-usuario/server-filemanager:latest .
```

### 3️⃣ Subir Imágenes a Docker Hub

```bash
docker login
docker push tu-usuario/broker-filemanager:latest
docker push tu-usuario/server-filemanager:latest
```

### 4️⃣ Actualizar Archivos YAML

```bash
# Usar el script de ayuda
./update-yamls.sh TU_USUARIO_DOCKERHUB

# O editar manualmente los archivos en kubernetes/
# Reemplazar <tu-usuario> por tu usuario de Docker Hub
```

### 5️⃣ Crear Cluster en AWS EC2

```bash
# Crear al menos 2 instancias EC2 (Ubuntu 20.04)
# Configurar security groups (ver docs/setup.md)
# Conectar a cada instancia e instalar Docker + Kubernetes

# En el MASTER:
ssh -i "clave.pem" ubuntu@MASTER_IP
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# En cada WORKER:
ssh -i "clave.pem" ubuntu@WORKER_IP
sudo kubeadm join MASTER_IP:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

### 6️⃣ Desplegar Aplicaciones

Desde el nodo **MASTER**:

```bash
# Copiar archivos YAML al master
scp -i "clave.pem" -r kubernetes/ ubuntu@MASTER_IP:~/

# En el master:
kubectl apply -f kubernetes/broker/deployment.yaml
kubectl apply -f kubernetes/server/deployment-basic.yaml

# Verificar
kubectl get pods
kubectl get services
```

### 7️⃣ Probar la Aplicación

Desde tu **máquina local** o desde una instancia EC2:

```bash
# Crear archivos de prueba
echo "Contenido de prueba" > test.txt

# Ejecutar cliente (usar IP externa del nodo master)
./client/clienteFileManager MASTER_IP

# Dentro del cliente:
ls              # Ver archivos locales
lls             # Ver archivos remotos
upload test.txt # Subir archivo
lls             # Verificar que se subió
download test.txt  # Descargar archivo
exit            # Salir
```

---

## 📊 Niveles de Configuración

### Básico (5 puntos) ✅
- [x] 1 nodo master
- [x] 1 pod broker
- [x] 1 pod servidor
- [x] Servicios funcionando

**Archivo a usar:** `kubernetes/server/deployment-basic.yaml`

### Avanzado 1 (+2 puntos) 🎯
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

### Avanzado 2 (+5 puntos) 🏆
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

## 🎬 Para el Video Demostrativo

Sigue el script detallado en: **`docs/demo-script.md`**

### Checklist Mínimo a Mostrar:
- [ ] Arquitectura del cluster (diagrama o explicación)
- [ ] Código de Dockerfiles con explicaciones
- [ ] Código de archivos YAML con explicaciones
- [ ] Cluster funcionando (`kubectl get all`)
- [ ] Pods corriendo en diferentes nodos (si aplica)
- [ ] Conexión del cliente al broker
- [ ] Comando `ls` (archivos locales)
- [ ] Comando `lls` (archivos remotos)
- [ ] Comando `upload` con un archivo
- [ ] Verificar archivo subido con `lls`
- [ ] Comando `download` de un archivo
- [ ] Verificar persistencia (reiniciar pod y verificar archivos)
- [ ] Balanceo de carga (si aplica)

---

## 📚 Documentación Completa

### Guías Detalladas:
- **`docs/setup.md`** - Configuración completa paso a paso
- **`docs/demo-script.md`** - Script para el video demostrativo
- **`docs/cheatsheet.md`** - Comandos rápidos de referencia

### Archivos de Configuración:
- **`docker/`** - Dockerfiles para broker y servidor
- **`kubernetes/broker/`** - Deployment y service del broker
- **`kubernetes/server/`** - Deployments del servidor (básico y avanzados)
- **`kubernetes/nfs/`** - Configuración de almacenamiento NFS

---

## 🆘 Ayuda Rápida

### Ver logs de un pod:
```bash
kubectl logs <nombre-del-pod>
```

### Entrar a un pod:
```bash
kubectl exec -it <nombre-del-pod> -- /bin/bash
```

### Ver por qué un pod no inicia:
```bash
kubectl describe pod <nombre-del-pod>
```

### Reiniciar un deployment:
```bash
kubectl rollout restart deployment <nombre-deployment>
```

### Escalar réplicas:
```bash
kubectl scale deployment server-deployment --replicas=3
```

---

## ✅ Checklist de Entrega

### Archivos a Entregar:
- [ ] `docker/broker/Dockerfile`
- [ ] `docker/server/Dockerfile`
- [ ] `kubernetes/broker/deployment.yaml`
- [ ] `kubernetes/server/deployment-*.yaml` (el que uses)
- [ ] `kubernetes/nfs/*.yaml` (si usas configuración avanzada 2)
- [ ] README.md con instrucciones
- [ ] Video demostrativo (MP4 recomendado)

### En el Video:
- [ ] Presentación y arquitectura
- [ ] Explicación de Dockerfiles
- [ ] Explicación de archivos YAML
- [ ] Cluster funcionando
- [ ] Demo completa del cliente
- [ ] Persistencia de datos (si aplica)
- [ ] Balanceo de carga (si aplica)
- [ ] Conclusiones

---

## 🎯 Consejos Finales

1. **Empieza Simple:** Consigue que funcione la configuración básica primero
2. **Prueba Local:** Verifica los ejecutables en EC2 antes de containerizar
3. **Security Groups:** No olvides abrir los puertos necesarios
4. **Documenta:** Anota cada paso y problema que encuentres
5. **Video:** Practica la demo varias veces antes de grabar
6. **Backup:** Guarda copia de tus archivos YAML y configuraciones
7. **Tiempo:** Empieza con anticipación, esta práctica requiere tiempo

---

## 📞 Recursos

- **Kubernetes Docs:** https://kubernetes.io/docs/
- **Docker Docs:** https://docs.docker.com/
- **AWS EC2:** https://docs.aws.amazon.com/ec2/
- **NFS Guide:** https://www.jorgedelacruz.es/2017/12/26/kubernetes-volumenes-nfs/

**¡Buena suerte con la práctica!** 🚀
