# AEC4 - Despliegue de Aplicación Distribuida con Kubernetes

## 📋 Información General

**Tipo de tarea:** Individual  
**Entregables:**
- Archivos YAML/Dockerfile
- Video con explicaciones

---

## 🎯 Objetivo

Realizar el despliegue de una aplicación remota a lo largo de un cluster de ordenadores usando:
- Docker (contenedores)
- Kubernetes (orquestación)
- AWS EC2 (infraestructura)

---

## 📦 Componentes Suministrados

### Programas Servidor
1. **`serverFileManager`** (Puerto: 32001)
   - Implementación del servidor de la práctica 2
   - Gestiona acceso a archivos en carpeta local
   - Directorio de trabajo: `FileManagerDir/`

2. **`brokerFileManager`** (Puerto: 32002)
   - Implementación del Broker de la práctica 2
   - Recibe conexiones de servidores y clientes
   - Gestiona registro de servidores disponibles

### Programa Cliente
- **`clienteFileManager`**
  - Se conecta al broker para obtener información de servidores
  - Se conecta a servidores para operaciones de archivos

---

## 🔄 Flujo de Funcionamiento

```
1. brokerFileManager (inicia primero)
   ↓
2. serverFileManager(s) (se registran en el broker)
   ↓
3. clienteFileManager (obtiene lista de servidores del broker)
   ↓
4. Conexión directa: cliente ↔ servidor
```

### Comandos Disponibles (Cliente)

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `ls` | Lista archivos locales al cliente | `ls` |
| `lls` | Lista archivos en el servidor | `lls` |
| `upload <archivo>` | Copia archivo local al servidor | `upload a.txt` |
| `download <archivo>` | Copia archivo del servidor al cliente | `download a.txt` |
| `exit` | Cierra la conexión y termina | `exit` |

---

## 🏗️ Arquitectura del Cluster

### Configuración Básica (5 puntos)

```
┌─────────────────────────────────────────────┐
│           Nodo Master (Control Plane)       │
└─────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
┌───────▼──────┐        ┌──────▼────────┐
│  Nodo Broker │        │ Nodo Esclavo  │
│              │        │               │
│  - Broker    │        │ - Server      │
│    Pod       │        │   Pod         │
└──────────────┘        └───────────────┘
```

**Componentes necesarios:**
- ✅ Nodo máster con control-plane
- ✅ Nodo broker con deployment de `brokerFileManager`
- ✅ Nodo esclavo con deployment de `serverFileManager`
- ✅ Servicios de Kubernetes para conectividad

---

## 🎓 Configuraciones Avanzadas

### Configuración Avanzada 1 (+2 puntos)
**Múltiples réplicas en un único nodo esclavo**

```
┌────────────────────────────────────────┐
│         Nodo Esclavo                   │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐│
│  │ Server  │  │ Server  │  │ Server  ││
│  │ Pod 1   │  │ Pod 2   │  │ Pod 3   ││
│  └────┬────┘  └────┬────┘  └────┬────┘│
│       └────────────┴────────────┘     │
│              hostPath                  │
│       (carpeta compartida local)       │
└────────────────────────────────────────┘
```

**Requisitos:**
- Varios pods/réplicas del servidor
- Carpeta compartida con `hostPath`
- Datos no volátiles

### Configuración Avanzada 2 (+5 puntos)
**Múltiples nodos esclavos con almacenamiento compartido NFS**

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Nodo Esclavo │  │ Nodo Esclavo │  │ Nodo Esclavo │
│   1          │  │   2          │  │   3          │
│ ┌──────────┐ │  │ ┌──────────┐ │  │ ┌──────────┐ │
│ │ Server   │ │  │ │ Server   │ │  │ │ Server   │ │
│ │ Pods     │ │  │ │ Pods     │ │  │ │ Pods     │ │
│ └─────┬────┘ │  │ └─────┬────┘ │  │ └─────┬────┘ │
└───────┼──────┘  └───────┼──────┘  └───────┼──────┘
        │                 │                  │
        └─────────────────┴──────────────────┘
                         NFS
              (almacenamiento en red)
```

**Requisitos:**
- Múltiples nodos físicos
- Volumen NFS compartido
- Sincronización entre todos los nodos

**Guía recomendada:** [Kubernetes Volúmenes NFS](https://www.jorgedelacruz.es/2017/12/26/kubernetes-volumenes-nfs/)

---

## 📁 Estructura de Archivos del Proyecto

```
AEC4/
├── README.md (este archivo)
├── docker/
│   ├── broker/
│   │   ├── Dockerfile
│   │   └── brokerFileManager (ejecutable)
│   └── server/
│       ├── Dockerfile
│       ├── serverFileManager (ejecutable)
│       └── FileManagerDir/
├── kubernetes/
│   ├── broker/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── server/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── volume.yaml (opcional)
│   └── nfs/ (para configuración avanzada 2)
│       ├── nfs-server.yaml
│       └── pv-pvc.yaml
├── client/
│   └── clienteFileManager (ejecutable)
├── tests/
│   └── archivos de prueba
└── docs/
    ├── setup.md
    └── demo-script.md
```

---

## 🔧 Pasos de Desarrollo

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

## 🚀 Comandos Útiles

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

## 📝 Checklist de Entrega

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

## 🎯 Criterios de Evaluación

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

## 🔍 Recomendaciones

1. **Probar localmente primero:** Antes de desplegar en Kubernetes, asegúrate de que los ejecutables funcionan en EC2.

2. **Incrementalidad:** Empieza con la configuración básica y ve añadiendo complejidad.

3. **Logs y debugging:** Usa `kubectl logs` y `kubectl describe` frecuentemente para detectar problemas.

4. **Security Groups:** Asegúrate de que los puertos 32001 y 32002 están abiertos en AWS.

5. **Persistencia:** Verifica que los datos sobreviven al reinicio de pods.

6. **Documentación:** Documenta cada paso y decisión tomada.

7. **Testing exhaustivo:** Prueba la demo varias veces antes de grabar el video.

---

## 📚 Referencias

- [Documentación oficial de Kubernetes](https://kubernetes.io/docs/)
- [Documentación oficial de Docker](https://docs.docker.com/)
- [Kubernetes Volúmenes NFS](https://www.jorgedelacruz.es/2017/12/26/kubernetes-volumenes-nfs/)
- AWS EC2 User Guide

---

## 📞 Contacto

Ante cualquier duda, contactar con el profesor para verificar que el trabajo se corresponde con lo pedido.

---

## 📅 Estado del Proyecto

**Fecha de inicio:** ___________  
**Fecha de entrega:** ___________  
**Estado actual:** No iniciado

### Progreso
- [ ] Configuración básica (5 puntos)
- [ ] Configuración avanzada 1 (+2 puntos)
- [ ] Configuración avanzada 2 (+5 puntos)
- [ ] Video demostrativo
- [ ] Documentación completa
