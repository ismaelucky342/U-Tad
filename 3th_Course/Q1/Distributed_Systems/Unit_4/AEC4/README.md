#  AEC4 - Despliegue de Aplicación Distribuida con Kubernetes

**Asignatura:** Sistemas Distribuidos - U-TAD  
**Curso:** 3º - Grado en Ingeniería Informática  
**Tipo:** Actividad Evaluable Continua  

---

##  ÍNDICE

1. [Descripción del Proyecto](#descripcion)
2. [Estructura del Repositorio](#estructura)
3. [Guías Disponibles](#guias)
4. [Inicio Rápido](#inicio)
5. [Configuraciones](#configuraciones)
6. [Requisitos](#requisitos)
7. [Entrega](#entrega)

---

##  DESCRIPCIÓN DEL PROYECTO <a name="descripcion"></a>

Despliegue de una aplicación distribuida de gestión de archivos en un cluster de Kubernetes sobre instancias AWS EC2.

### Objetivos de Aprendizaje
-  Containerización de aplicaciones con Docker
-  Orquestación con Kubernetes
-  Gestión de almacenamiento persistente
-  Balanceo de carga y alta disponibilidad
-  Despliegue en infraestructura cloud (AWS EC2)

### Componentes del Sistema

#### 1. **brokerFileManager** (Puerto 32002)
- Coordina conexiones entre clientes y servidores
- Mantiene registro de servidores disponibles
- Proporciona información de conexión a clientes

#### 2. **serverFileManager** (Puerto 32001)
- Gestiona archivos en carpeta `FileManagerDir`
- Se registra con el broker al iniciar
- Acepta operaciones de clientes (listar, subir, descargar)

#### 3. **clienteFileManager**
- Interfaz de usuario para gestionar archivos
- Comandos disponibles:
  - `ls` - Listar archivos locales
  - `lls` - Listar archivos remotos
  - `upload <archivo>` - Subir archivo al servidor
  - `download <archivo>` - Descargar archivo del servidor
  - `exit` - Salir

---

##  ESTRUCTURA DEL REPOSITORIO <a name="estructura"></a>

```
AEC4/
  QUICKSTART.md              #  Guía completa paso a paso
  PRESENTACION.md            #  Guión para el video
  RESUMEN_RAPIDO.md          #  Referencia rápida
  README.md                  # Este archivo

  docker/
    broker/
       Dockerfile            # Imagen del broker
    server/
        Dockerfile            # Imagen del servidor

   kubernetes/
    broker/
       deployment.yaml       # Deployment + Service del broker
    server/
       deployment-basic.yaml         # 5 puntos
       deployment-advanced1.yaml     # +2 puntos (hostPath)
       deployment-advanced2.yaml     # +5 puntos (NFS)
    nfs/
        nfs-server.yaml       # Servidor NFS
        nfs-pv-pvc.yaml       # Volúmenes persistentes

   client/
    clienteFileManager        # Ejecutable del cliente

  docs/
    setup.md                  # Instalación detallada del cluster
    demo-script.md            # Script de demostración
    cheatsheet.md             # Comandos de referencia

  scripts/
     build-images.sh           # Construir y subir imágenes
     update-yamls.sh           # Actualizar archivos YAML
     cleanup.sh                # Limpiar recursos
     status.sh                 # Ver estado del cluster
```

---

##  GUÍAS DISPONIBLES <a name="guias"></a>

### Para Configuración

| Documento | Propósito | ¿Cuándo usarlo? |
|-----------|-----------|-----------------|
| **QUICKSTART.md** | Guía completa con todos los pasos | Primera vez configurando |
| **RESUMEN_RAPIDO.md** | Referencia rápida de comandos | Ya sabes qué hacer |
| **docs/setup.md** | Instalación detallada paso a paso | Problemas con instalación |
| **docs/cheatsheet.md** | Comandos útiles de Kubernetes | Debugging |

### Para Presentación

| Documento | Propósito | ¿Cuándo usarlo? |
|-----------|-----------|-----------------|
| **PRESENTACION.md** | Guión completo para el video | Preparar presentación |
| **docs/demo-script.md** | Script de demostración | Practicar la demo |

---

##  INICIO RÁPIDO <a name="inicio"></a>

### Paso 1: Preparar Ejecutables
```bash
# Descargar P3FileManager.zip del Blackboard
# Copiar ejecutables a sus ubicaciones
cp /ruta/descarga/brokerFileManager docker/broker/
cp /ruta/descarga/serverFileManager docker/server/
cp /ruta/descarga/clienteFileManager client/
```

### Paso 2: Construir Imágenes Docker
```bash
# Usar script de ayuda
./build-images.sh TU_USUARIO_DOCKERHUB

# O manualmente:
cd docker/broker/
docker build -t tu-usuario/broker-filemanager:latest .
docker push tu-usuario/broker-filemanager:latest

cd ../server/
docker build -t tu-usuario/server-filemanager:latest .
docker push tu-usuario/server-filemanager:latest
```

### Paso 3: Crear Cluster en AWS EC2
```bash
# Ver guía completa en QUICKSTART.md o docs/setup.md
# Crear instancias EC2 (Ubuntu 20.04)
# Instalar Docker + Kubernetes
# Inicializar master y unir workers
```

### Paso 4: Actualizar YAMLs
```bash
./update-yamls.sh TU_USUARIO_DOCKERHUB
```

### Paso 5: Desplegar Aplicaciones
```bash
# Copiar archivos al master
scp -i "clave.pem" -r kubernetes/ ubuntu@<MASTER_IP>:~/

# En el master:
kubectl apply -f kubernetes/broker/deployment.yaml
kubectl apply -f kubernetes/server/deployment-basic.yaml  # O advanced1/advanced2
```

### Paso 6: Probar
```bash
./client/clienteFileManager <IP_DEL_NODO>
```

** Para más detalles, consulta [QUICKSTART.md](QUICKSTART.md)**

---

##  CONFIGURACIONES DISPONIBLES <a name="configuraciones"></a>

###  Configuración Básica (5 puntos)

**Requisitos:**
- 1 nodo master (control-plane)
- Al menos 1 nodo worker
- 1 pod broker
- 1 pod servidor

**Archivos:**
- `kubernetes/server/deployment-basic.yaml`

**Características:**
- Volumen `emptyDir` (temporal)
- Sin persistencia entre reinicios
- Sin balanceo de carga

---

###  Configuración Avanzada 1 (+2 puntos = 7 total)

**Requisitos:**
- Todo lo de la básica MÁS:
- Múltiples réplicas del servidor en UN MISMO nodo
- Carpeta compartida usando `hostPath`

**Archivos:**
- `kubernetes/server/deployment-advanced1.yaml`

**Características:**
- 3 réplicas del servidor
- Todas en el mismo nodo (usando affinity)
- Almacenamiento compartido: `/data/FileManagerDir`
- Persistencia entre reinicios de pods
- Balanceo de carga entre réplicas

**Preparación requerida:**
```bash
# En el nodo worker
sudo mkdir -p /data/FileManagerDir
sudo chmod 777 /data/FileManagerDir
```

---

###  Configuración Avanzada 2 (+5 puntos = 10 total)

**Requisitos:**
- Todo lo de la avanzada 1 MÁS:
- Réplicas distribuidas en MÚLTIPLES nodos
- Almacenamiento compartido en red (NFS)

**Archivos:**
- `kubernetes/nfs/nfs-server.yaml`
- `kubernetes/nfs/nfs-pv-pvc.yaml`
- `kubernetes/server/deployment-advanced2.yaml`

**Características:**
- 3 réplicas distribuidas en diferentes nodos
- Servidor NFS centralizado
- PersistentVolume con `ReadWriteMany`
- Persistencia real entre nodos
- Alta disponibilidad
- Tolerancia a fallos

**Preparación requerida:**
1. Configurar servidor NFS
2. Instalar `nfs-common` en workers
3. Crear PV y PVC
4. Desplegar servidor con volumen NFS

** Ver detalles completos en [QUICKSTART.md - Configuración Avanzada 2](QUICKSTART.md#configuracion)**

---

##  REQUISITOS <a name="requisitos"></a>

### Infraestructura

#### AWS EC2
- **Tipo de instancia:** t2.medium mínimo (2 vCPUs, 4 GB RAM)
- **AMI:** Ubuntu Server 20.04 LTS
- **Cantidad mínima:** 2 instancias (1 master + 1 worker)
- **Recomendado:** 3+ instancias (1 master + 2+ workers)

#### Security Groups
```
Puerto      Protocolo    Origen          Descripción
22          TCP          0.0.0.0/0       SSH
6443        TCP          VPC             Kubernetes API
2379-2380   TCP          VPC             etcd
10250       TCP          VPC             Kubelet API
10251       TCP          VPC             kube-scheduler
10252       TCP          VPC             kube-controller
32001-32002 TCP          0.0.0.0/0       Aplicaciones
2049        TCP          VPC             NFS (si avanzada 2)
```

### Software

#### En todas las instancias:
- Docker CE 20.10+
- Kubernetes 1.25+ (kubeadm, kubelet, kubectl)
- containerd

#### En tu máquina local:
- Cliente SSH
- Docker (para construir imágenes)
- Cuenta en Docker Hub

#### Para Avanzada 2:
- Servidor NFS
- `nfs-common` en todos los workers

---

##  ENTREGA <a name="entrega"></a>

### Archivos Requeridos

Crear un archivo **`AEC4_[TuNombre].zip`** conteniendo:

```
AEC4_[TuNombre]/
 docker/
    broker/
       Dockerfile
    server/
        Dockerfile

 kubernetes/
    broker/
       deployment.yaml
    server/
       deployment-[basic|advanced1|advanced2].yaml
    nfs/ (solo si usas avanzada 2)
        nfs-server.yaml (opcional)
        nfs-pv-pvc.yaml

 video/
    AEC4_Demo_[TuNombre].mp4

 README.md (opcional pero recomendado)
```

### Contenido del Video (15-20 minutos)

#### Parte 1: Introducción (2 min)
- [ ] Presentación personal
- [ ] Descripción de la configuración implementada
- [ ] Diagrama de arquitectura

#### Parte 2: Configuración (5 min)
- [ ] Mostrar nodos del cluster (`kubectl get nodes`)
- [ ] Explicar Dockerfiles (broker y servidor)
- [ ] Explicar archivos YAML (deployments y services)
- [ ] Mostrar pods y servicios activos

#### Parte 3: Demostración (8-10 min)
- [ ] **Cliente 1:**
  - Comando `ls` (listar archivos locales)
  - Comando `lls` (listar archivos remotos)
  - Comando `upload <archivo>`
  - Verificar con `lls`
- [ ] Cerrar Cliente 1
- [ ] **Cliente 2:**
  - Comando `lls` (debe ver archivos de Cliente 1)
  - Comando `download <archivo>`
  - Verificar archivo descargado
- [ ] **[Si avanzada 1/2]:** Demostrar almacenamiento compartido

#### Parte 4: Conclusiones (1 min)
- [ ] Resumen de lo implementado
- [ ] Aprendizajes clave

** Guión detallado en [PRESENTACION.md](PRESENTACION.md)**

---

##  CRITERIOS DE EVALUACIÓN

### Configuración Básica (5 puntos)
-  Cluster con al menos 2 nodos funcionando
-  Dockerfiles correctos para broker y servidor
-  Deployments de Kubernetes funcionales
-  Services con NodePort configurados
-  Cliente puede listar, subir y descargar archivos

### Configuración Avanzada 1 (+2 puntos)
-  Múltiples réplicas en un mismo nodo
-  Volumen hostPath compartido correctamente
-  Persistencia entre conexiones de clientes
-  Balanceo de carga funcionando

### Configuración Avanzada 2 (+5 puntos)
-  Múltiples nodos worker
-  Réplicas distribuidas en diferentes nodos
-  Servidor NFS configurado y funcional
-  PersistentVolume con ReadWriteMany
-  Almacenamiento compartido entre todos los nodos
-  Alta disponibilidad demostrada

### Video
-  Audio claro y comprensible
-  Pantalla legible (mínimo 1080p)
-  Explicaciones claras y completas
-  Demostración funcional de principio a fin
-  Duración adecuada (15-20 minutos)

---

##  SCRIPTS DE AYUDA

### build-images.sh
Construye y sube las imágenes Docker a Docker Hub.
```bash
./build-images.sh <tu-usuario-dockerhub>
```

### update-yamls.sh
Actualiza los archivos YAML con tu usuario de Docker Hub.
```bash
./update-yamls.sh <tu-usuario-dockerhub>
```

### cleanup.sh
Limpia todos los recursos de Kubernetes.
```bash
./cleanup.sh
```

### status.sh
Muestra el estado completo del cluster.
```bash
./status.sh
```

---

##  RECURSOS ADICIONALES

### Documentación Oficial
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)

### Tutoriales
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Kubernetes Volumes - NFS](https://www.jorgedelacruz.es/2017/12/26/kubernetes-volumenes-nfs/)

---

##  PREGUNTAS FRECUENTES

### ¿Puedo usar Minikube o Docker Desktop en lugar de AWS?
No, la práctica requiere específicamente AWS EC2 con múltiples nodos.

### ¿Puedo modificar los ejecutables suministrados?
No, debes usar los ejecutables tal como se proporcionan.

### ¿Qué configuración debo implementar?
- Mínimo: Configuración básica (5 puntos)
- Recomendado: Avanzada 1 o 2 para máxima puntuación

### ¿Cuánto tiempo lleva completar la práctica?
- Configuración básica: 4-6 horas
- Avanzada 1: 6-8 horas
- Avanzada 2: 8-12 horas

### ¿Puedo trabajar en grupo?
No, la práctica es individual.

---

##  SOLUCIÓN DE PROBLEMAS

### Pod en estado Pending
```bash
kubectl describe pod <pod-name>
# Ver causa: recursos insuficientes, volumen no disponible, etc.
```

### Imágenes no se descargan
```bash
# Verificar nombre de imagen
kubectl describe pod <pod-name> | grep Image

# Verificar que existe en Docker Hub
docker pull <tu-usuario>/broker-filemanager:latest
```

### Cliente no conecta
```bash
# Verificar servicios
kubectl get services

# Verificar logs del broker
kubectl logs <broker-pod-name>

# Verificar Security Groups en AWS
```

** Guía completa de troubleshooting en [QUICKSTART.md](QUICKSTART.md#troubleshooting)**

---

##  AUTOR

**[Tu Nombre]**  
Grado en Ingeniería Informática  
Universidad U-TAD  
Curso 2024-2025

---

##  LICENCIA

Este proyecto es material académico para la asignatura de Sistemas Distribuidos de U-TAD.

---

##  EMPEZAR AHORA

1. Lee **[QUICKSTART.md](QUICKSTART.md)** para configuración completa
2. Revisa **[PRESENTACION.md](PRESENTACION.md)** para preparar el video
3. Usa **[RESUMEN_RAPIDO.md](RESUMEN_RAPIDO.md)** como referencia

**¿Primera vez?** → Comienza con [QUICKSTART.md](QUICKSTART.md)

**¿Necesitas ayuda rápida?** → Consulta [RESUMEN_RAPIDO.md](RESUMEN_RAPIDO.md)

**¿Listo para grabar?** → Sigue [PRESENTACION.md](PRESENTACION.md)

---

**¡Buena suerte con tu práctica!** 

### Comandos Disponibles (Cliente)

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `ls` | Lista archivos locales al cliente | `ls` |
| `lls` | Lista archivos en el servidor | `lls` |
| `upload <archivo>` | Copia archivo local al servidor | `upload a.txt` |
| `download <archivo>` | Copia archivo del servidor al cliente | `download a.txt` |
| `exit` | Cierra la conexión y termina | `exit` |

---

##  Arquitectura del Cluster

### Configuración Básica (5 puntos)

```

           Nodo Master (Control Plane)       

                    
        
                               
        
  Nodo Broker          Nodo Esclavo  
                                     
  - Broker             - Server      
    Pod                  Pod         
        
```

**Componentes necesarios:**
-  Nodo máster con control-plane
-  Nodo broker con deployment de `brokerFileManager`
-  Nodo esclavo con deployment de `serverFileManager`
-  Servicios de Kubernetes para conectividad

---

##  Configuraciones Avanzadas

### Configuración Avanzada 1 (+2 puntos)
**Múltiples réplicas en un único nodo esclavo**

```

         Nodo Esclavo                   
      
   Server     Server     Server  
   Pod 1      Pod 2      Pod 3   
      
            
              hostPath                  
       (carpeta compartida local)       

```

**Requisitos:**
- Varios pods/réplicas del servidor
- Carpeta compartida con `hostPath`
- Datos no volátiles

### Configuración Avanzada 2 (+5 puntos)
**Múltiples nodos esclavos con almacenamiento compartido NFS**

```
    
 Nodo Esclavo    Nodo Esclavo    Nodo Esclavo 
   1               2               3          
          
  Server        Server        Server    
  Pods          Pods          Pods      
          
    
                                           
        
                         NFS
              (almacenamiento en red)
```

**Requisitos:**
- Múltiples nodos físicos
- Volumen NFS compartido
- Sincronización entre todos los nodos

**Guía recomendada:** [Kubernetes Volúmenes NFS](https://www.jorgedelacruz.es/2017/12/26/kubernetes-volumenes-nfs/)

---

##  Estructura de Archivos del Proyecto

```
AEC4/
 README.md (este archivo)
 docker/
    broker/
       Dockerfile
       brokerFileManager (ejecutable)
    server/
        Dockerfile
        serverFileManager (ejecutable)
        FileManagerDir/
 kubernetes/
    broker/
       deployment.yaml
       service.yaml
    server/
       deployment.yaml
       service.yaml
       volume.yaml (opcional)
    nfs/ (para configuración avanzada 2)
        nfs-server.yaml
        pv-pvc.yaml
 client/
    clienteFileManager (ejecutable)
 tests/
    archivos de prueba
 docs/
     setup.md
     demo-script.md
```

---

##  Pasos de Desarrollo

### 1. Preparación del Entorno
- [ ] Crear instancias EC2 en AWS
- [ ] Configurar security groups (puertos 32001, 32002)
- [ ] Instalar Docker en todas las instancias
- [ ] Instalar Kubernetes (kubeadm, kubelet, kubectl)

### 2. Creación de Imágenes Docker
- [ ] Dockerfile para `brokerFileManager`
- [ ] Dockerfile para `serverFileManager`
- [ ] Probar imágenes localmente
- [ ] Subir imágenes a un registry (Docker Hub o ECR)

### 3. Configuración de Kubernetes
- [ ] Inicializar cluster (master node)
- [ ] Unir nodos esclavos al cluster
- [ ] Crear namespaces si es necesario
- [ ] Configurar networking (CNI plugin)

### 4. Deployments y Services
- [ ] Deployment del broker
- [ ] Service para el broker (tipo LoadBalancer/NodePort)
- [ ] Deployment del servidor
- [ ] Service para el servidor (tipo LoadBalancer/NodePort)

### 5. Configuración de Volúmenes
- [ ] **Básico:** Volúmenes locales para cada pod
- [ ] **Avanzado 1:** hostPath para réplicas en un nodo
- [ ] **Avanzado 2:** NFS para múltiples nodos

### 6. Pruebas
- [ ] Levantar broker
- [ ] Levantar servidor(es)
- [ ] Conectar cliente y probar comandos:
  - [ ] `ls` - listar archivos locales
  - [ ] `lls` - listar archivos remotos
  - [ ] `upload` - subir archivo
  - [ ] `download` - descargar archivo
  - [ ] `exit` - cerrar conexión

### 7. Validación
- [ ] Verificar que los archivos se guardan correctamente
- [ ] Probar con múltiples clientes simultáneos
- [ ] Verificar balanceo de carga
- [ ] Probar reinicio de pods (datos no volátiles)

---

##  Comandos Útiles

### Docker
```bash
# Construir imagen
docker build -t nombre-imagen:tag .

# Listar imágenes
docker images

# Ejecutar contenedor
docker run -p 32001:32001 nombre-imagen

# Subir a Docker Hub
docker push usuario/nombre-imagen:tag
```

### Kubernetes
```bash
# Inicializar cluster
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# Unir nodo al cluster
sudo kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>

# Ver nodos
kubectl get nodes

# Aplicar configuración
kubectl apply -f archivo.yaml

# Ver pods
kubectl get pods

# Ver servicios
kubectl get services

# Logs de un pod
kubectl logs <pod-name>

# Describir pod
kubectl describe pod <pod-name>

# Escalar deployment
kubectl scale deployment <deployment-name> --replicas=3

# Eliminar recursos
kubectl delete -f archivo.yaml
```

### AWS EC2
```bash
# Conectar a instancia
ssh -i "clave.pem" ubuntu@<ec2-ip>

# Copiar archivos a EC2
scp -i "clave.pem" archivo ubuntu@<ec2-ip>:~/
```

---

##  Checklist de Entrega

### Archivos Requeridos
- [ ] Dockerfile(s) con comentarios explicativos
- [ ] Archivos YAML de Kubernetes
- [ ] README con instrucciones de despliegue
- [ ] Capturas de pantalla o logs de funcionamiento

### Video Demostrativo
- [ ] Mostrar arquitectura del cluster
- [ ] Explicar archivos Docker y YAML
- [ ] Demostrar funcionamiento:
  - [ ] Conexión cliente-broker-servidor
  - [ ] Comando `ls` y `lls`
  - [ ] Upload de archivo
  - [ ] Download de archivo
  - [ ] Verificar archivo en servidor
- [ ] Mostrar réplicas/balanceo (si aplica)
- [ ] Mostrar persistencia de datos

---

##  Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Imágenes Docker funcionales | 1 punto |
| Cluster Kubernetes configurado | 1 punto |
| Deployment de broker | 1 punto |
| Deployment de servidor | 1 punto |
| Servicios y conectividad funcionando | 1 punto |
| **Subtotal Configuración Básica** | **5 puntos** |
| Múltiples réplicas con hostPath | +2 puntos |
| Múltiples nodos con NFS | +5 puntos |
| **Total Máximo** | **10 puntos** |

---

##  Recomendaciones

1. **Probar localmente primero:** Antes de desplegar en Kubernetes, asegúrate de que los ejecutables funcionan en EC2.

2. **Incrementalidad:** Empieza con la configuración básica y ve añadiendo complejidad.

3. **Logs y debugging:** Usa `kubectl logs` y `kubectl describe` frecuentemente para detectar problemas.

4. **Security Groups:** Asegúrate de que los puertos 32001 y 32002 están abiertos en AWS.

5. **Persistencia:** Verifica que los datos sobreviven al reinicio de pods.

6. **Documentación:** Documenta cada paso y decisión tomada.

7. **Testing exhaustivo:** Prueba la demo varias veces antes de grabar el video.

---

##  Referencias

- [Documentación oficial de Kubernetes](https://kubernetes.io/docs/)
- [Documentación oficial de Docker](https://docs.docker.com/)
- [Kubernetes Volúmenes NFS](https://www.jorgedelacruz.es/2017/12/26/kubernetes-volumenes-nfs/)
- AWS EC2 User Guide

---

##  Contacto

Ante cualquier duda, contactar con el profesor para verificar que el trabajo se corresponde con lo pedido.

---

##  Estado del Proyecto

**Fecha de inicio:** ___________  
**Fecha de entrega:** ___________  
**Estado actual:** No iniciado

### Progreso
- [ ] Configuración básica (5 puntos)
- [ ] Configuración avanzada 1 (+2 puntos)
- [ ] Configuración avanzada 2 (+5 puntos)
- [ ] Video demostrativo
- [ ] Documentación completa
