# Kubernetes Básico - Estructura Mínima

Este directorio contiene los archivos YAML básicos de Kubernetes para entender la estructura mínima necesaria en sistemas distribuidos y orquestación.

## 📁 Archivos incluidos

1. **`namespace.yaml`** - Organización de recursos
2. **`configmap.yaml`** - Configuración no confidencial
3. **`secret.yaml`** - Información confidencial (contraseñas, tokens)
4. **`persistentvolume.yaml`** - Almacenamiento persistente (PV y PVC)
5. **`deployment.yaml`** - Gestión de réplicas de Pods
6. **`service.yaml`** - Exposición de Pods a la red
7. **`pod.yaml`** - Unidad básica de despliegue (referencia, normalmente se usan Deployments)

## 🚀 Comandos básicos

### Aplicar configuración
```bash
# Aplicar un archivo específico
kubectl apply -f deployment.yaml

# Aplicar todos los archivos del directorio
kubectl apply -f .

# Aplicar en un namespace específico
kubectl apply -f deployment.yaml -n dev
```

### Ver recursos
```bash
# Ver todos los pods
kubectl get pods

# Ver deployments
kubectl get deployments

# Ver services
kubectl get services

# Ver todos los recursos
kubectl get all

# Información detallada de un recurso
kubectl describe pod <nombre-pod>
```

### Logs y debugging
```bash
# Ver logs de un pod
kubectl logs <nombre-pod>

# Ver logs en tiempo real
kubectl logs -f <nombre-pod>

# Ejecutar comando dentro de un pod
kubectl exec -it <nombre-pod> -- /bin/sh
```

### Eliminar recursos
```bash
# Eliminar un recurso específico
kubectl delete -f deployment.yaml

# Eliminar todos los recursos del directorio
kubectl delete -f .

# Eliminar por nombre
kubectl delete pod <nombre-pod>
```

## 📊 Jerarquía de objetos Kubernetes

```
Cluster
  └── Namespace (organización lógica)
       ├── ConfigMap (configuración)
       ├── Secret (datos sensibles)
       ├── PersistentVolume (almacenamiento)
       ├── PersistentVolumeClaim (solicitud de almacenamiento)
       ├── Deployment (gestiona Pods)
       │    └── ReplicaSet (gestiona réplicas)
       │         └── Pod (contenedores)
       └── Service (expone Pods)
```

## 🔄 Flujo típico de despliegue

1. Crear el **Namespace** (opcional, si no se usa el default)
2. Crear **ConfigMap** y **Secret** para configuración
3. Crear **PersistentVolume** y **PersistentVolumeClaim** si se necesita almacenamiento
4. Crear el **Deployment** con la aplicación
5. Crear el **Service** para exponer la aplicación

## 🆚 Comparación con Docker Compose

| Docker Compose | Kubernetes |
|----------------|------------|
| `docker-compose.yaml` | Múltiples archivos YAML especializados |
| `services:` | `Deployment` + `Service` |
| `volumes:` | `PersistentVolume` + `PersistentVolumeClaim` |
| `environment:` | `ConfigMap` + `Secret` |
| `depends_on:` | Control a través de `readinessProbe` y orden de aplicación |

## 💡 Conceptos clave

- **Pod**: Unidad mínima, contiene uno o más contenedores
- **Deployment**: Gestiona la creación y actualización de Pods con réplicas
- **Service**: Proporciona una IP estable para acceder a los Pods
- **ConfigMap**: Almacena configuración no sensible
- **Secret**: Almacena información confidencial
- **Namespace**: Agrupa y aísla recursos
- **PersistentVolume**: Define almacenamiento disponible en el cluster
- **PersistentVolumeClaim**: Solicita almacenamiento para usar en Pods

## 📚 Recursos adicionales

- [Documentación oficial de Kubernetes](https://kubernetes.io/docs/)
- [Kubernetes Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Interactive Tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
