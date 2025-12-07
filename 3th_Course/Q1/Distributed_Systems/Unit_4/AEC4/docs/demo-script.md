# Script para Video Demostrativo

## Estructura del Video (15-20 minutos recomendado)

### 1. Introducción (1-2 min)
- Presentación del proyecto
- Explicar arquitectura a implementar
- Mostrar diagrama del cluster

### 2. Mostrar Configuración del Cluster (3-4 min)

```bash
# Conectar al nodo master
ssh -i "clave.pem" ubuntu@<MASTER_IP>

# Mostrar nodos del cluster
kubectl get nodes -o wide

# Mostrar información de los nodos
kubectl describe nodes

# Mostrar namespaces
kubectl get namespaces
```

### 3. Explicar Archivos Docker (2-3 min)

**Broker Dockerfile:**
```bash
# Mostrar contenido del Dockerfile
cat docker/broker/Dockerfile

# Explicar:
# - Imagen base
# - Dependencias
# - Puerto expuesto (32002)
# - Comando de inicio
```

**Server Dockerfile:**
```bash
# Mostrar contenido del Dockerfile
cat docker/server/Dockerfile

# Explicar:
# - Imagen base
# - Directorio FileManagerDir
# - Puerto expuesto (32001)
# - Parámetros (IP del broker)
```

### 4. Explicar Archivos YAML de Kubernetes (3-4 min)

**Deployment del Broker:**
```bash
cat kubernetes/broker/deployment.yaml

# Explicar:
# - Configuración del deployment
# - Número de réplicas (1)
# - Imagen utilizada
# - Puerto y servicio
# - Tipo de servicio (NodePort)
```

**Deployment del Servidor:**
```bash
cat kubernetes/server/deployment-basic.yaml
# O el que hayas implementado (advanced1/advanced2)

# Explicar:
# - Configuración del deployment
# - Número de réplicas
# - Argumentos (IP del broker)
# - Volúmenes (emptyDir/hostPath/NFS)
# - Servicio y balanceo de carga
```

**Si usas configuración avanzada 2:**
```bash
cat kubernetes/nfs/nfs-pv-pvc.yaml

# Explicar:
# - PersistentVolume
# - PersistentVolumeClaim
# - Servidor NFS
# - AccessMode ReadWriteMany
```

### 5. Mostrar Deployments Activos (2-3 min)

```bash
# Listar todos los recursos
kubectl get all

# Ver pods en detalle
kubectl get pods -o wide

# Mostrar que los pods están en diferentes nodos (si aplica)
kubectl get pods -o wide | grep server

# Ver servicios
kubectl get services

# Ver información del servicio del broker
kubectl describe service broker-service

# Ver información del servicio del servidor
kubectl describe service server-service

# Si usas configuración avanzada, mostrar volúmenes
kubectl get pv
kubectl get pvc
```

### 6. Verificar Logs (1-2 min)

```bash
# Ver logs del broker
kubectl logs <broker-pod-name>

# Ver logs de un servidor
kubectl logs <server-pod-name>

# Mostrar que se están ejecutando correctamente
```

### 7. Demostración Práctica del Cliente (5-7 min)

**Preparar archivos de prueba:**
```bash
# Crear algunos archivos de prueba en el directorio local
cd /ruta/al/cliente
echo "Contenido de prueba 1" > test1.txt
echo "Contenido de prueba 2" > test2.txt
echo "Este es un archivo para demostración" > demo.txt
```

**Conectar el cliente:**
```bash
# Obtener la IP externa del nodo donde está el broker
# (o usar la IP del master si usas NodePort)
kubectl get nodes -o wide

# Ejecutar cliente
./clienteFileManager <IP_DEL_NODO>
```

**Demostrar comandos:**

1. **Listar archivos locales:**
```
ls
# Explicar: Muestra archivos en el directorio local del cliente
# Deberían aparecer: test1.txt, test2.txt, demo.txt
```

2. **Listar archivos remotos (servidor):**
```
lls
# Explicar: Muestra archivos en el servidor (carpeta FileManagerDir)
# Inicialmente podría estar vacío
```

3. **Subir un archivo:**
```
upload test1.txt
# Explicar: Copia test1.txt del cliente al servidor
# Mostrar confirmación de éxito
```

4. **Verificar que se subió:**
```
lls
# Explicar: Ahora debería aparecer test1.txt
```

5. **Subir más archivos:**
```
upload test2.txt
upload demo.txt
lls
# Explicar: Verificar que todos los archivos están en el servidor
```

6. **Descargar un archivo:**
```
# Primero borrar un archivo local para demostrar la descarga
# (fuera del cliente)
rm test1.txt

# Dentro del cliente
download test1.txt
ls
# Explicar: El archivo se descargó del servidor al cliente
```

7. **Salir:**
```
exit
# Explicar: Cierra la conexión
```

### 8. Verificar Persistencia (Si aplica) (2-3 min)

**Para configuración avanzada 1 o 2:**

```bash
# Verificar archivos en el volumen compartido

# Si usas hostPath (avanzado 1):
# Conectar al nodo esclavo
ssh ubuntu@<NODO_ESCLAVO_IP>
ls -la /mnt/filemanager-shared
# Deberían aparecer los archivos subidos

# Si usas NFS (avanzado 2):
# Conectar al servidor NFS o a cualquier nodo
ssh ubuntu@<NFS_SERVER_IP>
ls -la /exports/filemanager
# Deberían aparecer los archivos subidos
```

**Probar reinicio de pod:**
```bash
# Eliminar un pod
kubectl delete pod <server-pod-name>

# Esperar a que se recree automáticamente
kubectl get pods -w

# Volver a conectar el cliente y verificar que los archivos siguen ahí
./clienteFileManager <IP_DEL_NODO>
lls
# Los archivos deberían seguir estando
```

### 9. Demostrar Balanceo de Carga (Si aplica) (2-3 min)

**Si tienes múltiples réplicas:**

```bash
# Mostrar réplicas activas
kubectl get pods -l app=filemanager-server -o wide

# Conectar múltiples clientes simultáneamente
# (puedes abrir varias terminales)

# Terminal 1:
./clienteFileManager <IP_DEL_NODO>

# Terminal 2:
./clienteFileManager <IP_DEL_NODO>

# Terminal 3:
./clienteFileManager <IP_DEL_NODO>

# Verificar en los logs que diferentes pods están recibiendo conexiones
kubectl logs <server-pod-1>
kubectl logs <server-pod-2>
kubectl logs <server-pod-3>

# Explicar que Kubernetes está balanceando la carga entre los pods
```

**Escalar el deployment:**
```bash
# Aumentar réplicas en tiempo real
kubectl scale deployment server-deployment --replicas=5

# Mostrar cómo se crean nuevos pods
kubectl get pods -w

# Explicar que el servicio automáticamente incluye los nuevos pods
```

### 10. Conclusión (1-2 min)

- Resumir lo demostrado:
  -  Cluster de Kubernetes funcional
  -  Aplicaciones contenerizadas con Docker
  -  Broker y servidores desplegados
  -  Cliente puede subir/bajar archivos
  -  Persistencia de datos (si aplica)
  -  Balanceo de carga (si aplica)
  -  Múltiples nodos (si aplica)

- Mencionar dificultades encontradas y cómo se resolvieron
- Agradecimientos

---

## Checklist Pre-Grabación

- [ ] Cluster completamente configurado y funcionando
- [ ] Todas las imágenes Docker construidas y subidas
- [ ] Todos los deployments aplicados y pods corriendo
- [ ] Archivos de prueba preparados
- [ ] Cliente compilado y listo para usar
- [ ] Verificar conectividad (security groups, puertos)
- [ ] Tener múltiples terminales preparadas
- [ ] Script de comandos a mano para referencia
- [ ] Probar la demo completa al menos una vez antes de grabar

## Consejos para el Video

1. **Audio claro:** Usa un buen micrófono
2. **Pantalla legible:** Fuente grande en la terminal
3. **Ritmo pausado:** No corras, explica cada paso
4. **Edición:** Puedes cortar errores o tiempos muertos
5. **Subtítulos:** Considera añadir texto explicativo en pantalla
6. **Estructura:** Sigue el orden lógico del script
7. **Duración:** 15-20 minutos es ideal, no más de 25

## Errores Comunes a Evitar

-  No mostrar que los pods están corriendo
-  No explicar los archivos YAML
-  No demostrar todos los comandos del cliente
-  No verificar la persistencia de datos
-  Ir demasiado rápido sin explicar
-  No mostrar la arquitectura visual
-  No probar con múltiples archivos
