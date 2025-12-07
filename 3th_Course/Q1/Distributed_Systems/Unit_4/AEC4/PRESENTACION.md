#  GUIÓN DE PRESENTACIÓN - AEC4
## Sistemas Distribuidos - Kubernetes Deployment

---

##  INFORMACIÓN GENERAL

**Duración:** 15-20 minutos  
**Formato:** Video demostrativo  
**Configuración implementada:** [MARCA LA TUYA]
- [ ]  Básica (5 puntos)
- [ ]  Avanzada 1 - hostPath (7 puntos)
- [ ]  Avanzada 2 - NFS (10 puntos)

---

## ⏱ ESTRUCTURA TEMPORAL

| Parte | Contenido | Duración |
|-------|-----------|----------|
| 1 | Introducción y Arquitectura | 2 min |
| 2 | Mostrar Configuración del Cluster | 3 min |
| 3 | Explicar Dockerfiles | 2 min |
| 4 | Explicar YAMLs de Kubernetes | 3 min |
| 5 | Estado del Cluster | 2 min |
| 6 | Demostración Práctica | 6-8 min |
| 7 | Conclusiones | 1 min |

---

##  PARTE 1: INTRODUCCIÓN (2 minutos)

### Qué Mostrar en Pantalla
- Diapositiva con título del proyecto
- Tu nombre y asignatura
- Diagrama de arquitectura

### Qué Decir (Script)
```
"Buenos días/tardes. Mi nombre es [TU NOMBRE] y en este video voy a presentar 
la Actividad Evaluable Continua 4 de Sistemas Distribuidos.

En esta práctica he implementado el despliegue de una aplicación distribuida 
de gestión de archivos utilizando:
- Docker para containerización
- Kubernetes para orquestación
- AWS EC2 como infraestructura

La aplicación consta de tres componentes:
1. Un BROKER que coordina las conexiones (puerto 32002)
2. Uno o más SERVIDORES que gestionan archivos (puerto 32001)
3. CLIENTES que interactúan con los servidores

He implementado la configuración [BÁSICA / AVANZADA 1 / AVANZADA 2], 
que incluye:

[PARA BÁSICA]:
- 1 nodo master con control-plane
- 1 nodo worker con el broker
- 1 nodo worker con el servidor
- Servicios NodePort para acceso externo

[PARA AVANZADA 1]:
- Todo lo anterior MÁS:
- Múltiples réplicas del servidor en un mismo nodo
- Almacenamiento compartido con hostPath
- Balanceo de carga entre réplicas

[PARA AVANZADA 2]:
- Todo lo anterior MÁS:
- Réplicas distribuidas en múltiples nodos
- Servidor NFS para almacenamiento compartido en red
- PersistentVolume y PersistentVolumeClaim
- Alta disponibilidad y persistencia real

Vamos a ver cómo funciona todo el sistema."
```

---

##  PARTE 2: CONFIGURACIÓN DEL CLUSTER (3 minutos)

### Terminal - Conectar al Master
```bash
ssh -i "tu-clave.pem" ubuntu@<MASTER_IP>
```

### Comando 1: Mostrar Nodos
```bash
kubectl get nodes -o wide
```

#### Qué Decir
```
"Primero voy a mostrar la configuración del cluster. Como pueden ver, tengo 
[X] nodos en total:

- 1 nodo MASTER que actúa como control-plane, ejecutando:
  - El API Server de Kubernetes
  - El Scheduler
  - El Controller Manager
  - etcd para almacenar el estado del cluster

- [X-1] nodos WORKER donde corren las aplicaciones

[PARA AVANZADA 2]:
- Las réplicas del servidor están distribuidas entre estos workers
- Esto proporciona alta disponibilidad: si un nodo falla, los otros continúan

Todos los nodos están en estado 'Ready', lo que significa que están 
operativos y pueden ejecutar pods."
```

### Comando 2: Información Detallada
```bash
kubectl describe nodes | grep -E "Name:|Roles:|Internal IP:"
```

#### Qué Decir
```
"Aquí podemos ver más detalles de cada nodo, incluyendo sus IPs internas 
que Kubernetes usa para la comunicación entre pods."
```

---

##  PARTE 3: DOCKERFILES (2-3 minutos)

### Mostrar Dockerfile del Broker
```bash
cat docker/broker/Dockerfile
```

#### Qué Decir
```
"Ahora voy a mostrar cómo he containerizado las aplicaciones. Empezando por 
el Dockerfile del BROKER:

1. Uso Ubuntu 20.04 como imagen base por compatibilidad
2. Instalo libstdc++6, necesaria para ejecutar el binario
3. Copio el ejecutable brokerFileManager al contenedor
4. Expongo el puerto 32002, que es donde el broker escucha conexiones
5. El CMD ejecuta el broker sin parámetros adicionales

Este contenedor es muy ligero, solo con lo necesario para ejecutar el broker."
```

### Mostrar Dockerfile del Servidor
```bash
cat docker/server/Dockerfile
```

#### Qué Decir
```
"El Dockerfile del SERVIDOR es similar pero con algunas diferencias:

1. También usa Ubuntu 20.04 y libstdc++6
2. Crea el directorio /app/FileManagerDir donde se almacenarán los archivos
3. Copia el ejecutable serverFileManager
4. Expone el puerto 32001
5. Usa ENTRYPOINT en lugar de CMD porque el servidor necesita recibir la 
   IP del broker como parámetro de línea de comandos

Cuando Kubernetes ejecute este contenedor, pasará automáticamente el nombre 
del servicio del broker como argumento."
```

### Mostrar Imágenes en Docker Hub (Opcional)
```
"Estas imágenes las he construido localmente y subido a Docker Hub bajo 
el usuario [TU-USUARIO]:
- [tu-usuario]/broker-filemanager:latest
- [tu-usuario]/server-filemanager:latest

De esta forma, Kubernetes puede descargarlas desde cualquier nodo del cluster."
```

---

##  PARTE 4: DEPLOYMENTS DE KUBERNETES (3-5 minutos)

### Deployment del Broker
```bash
cat kubernetes/broker/deployment.yaml
```

#### Qué Decir - Deployment
```
"Ahora voy a explicar los archivos YAML de Kubernetes. Empezando por el 
deployment del BROKER:

DEPLOYMENT:
- Tipo: Deployment de Kubernetes
- Nombre: broker-deployment
- Réplicas: 1 (solo necesitamos un broker)
- Selector: identifica pods con label 'app=broker'

TEMPLATE:
- Define cómo serán los pods
- Usa la imagen de Docker Hub
- Expone el puerto 32002
- Limits y requests de recursos para el scheduler

Este deployment garantiza que siempre haya 1 instancia del broker corriendo. 
Si el pod falla, Kubernetes lo reinicia automáticamente."
```

#### Qué Decir - Service
```
"El SERVICE del broker:
- Tipo: NodePort - permite acceso desde fuera del cluster
- Puerto: 32002 tanto interno como externo
- Selector: dirige tráfico a pods con label 'app=broker'

Esto significa que puedo acceder al broker desde cualquier nodo del cluster 
usando <IP_NODO>:32002"
```

### Deployment del Servidor

#### PARA CONFIGURACIÓN BÁSICA:
```bash
cat kubernetes/server/deployment-basic.yaml
```

```
"El deployment del SERVIDOR básico:

DEPLOYMENT:
- 1 réplica del servidor
- Args: ['broker-service'] - usa el DNS interno de Kubernetes para encontrar 
  el broker
- Puerto 32001 expuesto

VOLUMEN:
- emptyDir: volumen temporal dentro del pod
- Se pierde cuando el pod se reinicia
- Suficiente para la funcionalidad básica

SERVICE:
- También NodePort en puerto 32001
- Permite que clientes externos se conecten
"
```

#### PARA CONFIGURACIÓN AVANZADA 1:
```bash
cat kubernetes/server/deployment-advanced1.yaml
```

```
"Para la configuración avanzada 1 he hecho modificaciones importantes:

RÉPLICAS:
- 3 réplicas del servidor en lugar de 1
- Todas deben estar en el MISMO nodo

AFFINITY:
- He configurado podAffinity para forzar que todos los pods del servidor 
  estén en el mismo nodo
- Esto es necesario para poder usar hostPath

VOLUMEN - hostPath:
- Monta /data/FileManagerDir del host en todos los pods
- Como están en el mismo nodo, todos acceden al mismo directorio físico
- Los archivos persisten incluso si los pods se reinician
- Preparé el nodo creando el directorio y dando permisos 777

SERVICE:
- Kubernetes balancea automáticamente las peticiones entre las 3 réplicas
- Proporciona distribución de carga
"
```

#### PARA CONFIGURACIÓN AVANZADA 2:
```bash
cat kubernetes/nfs/nfs-pv-pvc.yaml
cat kubernetes/server/deployment-advanced2.yaml
```

```
"Para la configuración avanzada 2 he implementado almacenamiento en red con NFS:

SERVIDOR NFS:
- He configurado un servidor NFS independiente
- Exporta el directorio /mnt/nfs-share
- Instalé nfs-common en todos los workers

PERSISTENTVOLUME:
- Define un volumen conectado al servidor NFS
- Capacidad: 5Gi
- AccessMode: ReadWriteMany - múltiples pods pueden leer/escribir 
  simultáneamente

PERSISTENTVOLUMECLAIM:
- Solicita acceso al PersistentVolume
- Los pods montan el PVC en lugar del volumen directamente

DEPLOYMENT:
- 3 réplicas distribuidas en DIFERENTES nodos
- Sin affinity, Kubernetes las distribuye automáticamente
- Todas montan el mismo PVC
- Todas acceden al mismo almacenamiento NFS

VENTAJAS:
- Alta disponibilidad: si un nodo falla, otros continúan
- Persistencia real: datos sobreviven a reinicios de pods y nodos
- Escalabilidad: puedo añadir más réplicas fácilmente
- Distribución de carga real entre múltiples máquinas físicas
"
```

---

##  PARTE 5: ESTADO DEL CLUSTER (2-3 minutos)

### Comando 1: Vista General
```bash
kubectl get all
```

#### Qué Decir
```
"Ahora voy a mostrar el estado actual del cluster con todos los recursos 
desplegados."
```

### Comando 2: Pods Detallados
```bash
kubectl get pods -o wide
```

#### Qué Decir
```
"Aquí vemos los pods en detalle:

BROKER:
- [nombre-del-pod] está corriendo en el nodo [nombre-nodo]
- Estado: Running
- Ready: 1/1

SERVIDORES:
- [Para básica]: 1 pod corriendo
- [Para avanzada 1]: 3 pods, todos en el mismo nodo [nombre]
- [Para avanzada 2]: 3 pods distribuidos en nodos [nombre1], [nombre2], [nombre3]

Todos están en estado Running y Ready, lo que significa que están aceptando 
conexiones."
```

### Comando 3: Servicios
```bash
kubectl get services
```

#### Qué Decir
```
"Los servicios expuestos:

- broker-service: NodePort 32002
- server-service: NodePort 32001
  [Para avanzada 1/2]: Con balanceo de carga entre las réplicas

Estos puertos están abiertos en todos los nodos del cluster."
```

### Comando 4: Volúmenes (Solo Avanzada 2)
```bash
kubectl get pv
kubectl get pvc
```

#### Qué Decir
```
"El almacenamiento persistente:

PERSISTENTVOLUME:
- Nombre: nfs-pv
- Capacidad: 5Gi
- Estado: Bound (vinculado)
- AccessMode: RWX (ReadWriteMany)

PERSISTENTVOLUMECLAIM:
- Nombre: nfs-pvc
- Estado: Bound al PV
- Montado por [X] pods

Esto confirma que el almacenamiento NFS está funcionando correctamente."
```

### Comando 5: Logs
```bash
# Obtener nombre del pod
BROKER_POD=$(kubectl get pods -l app=broker -o jsonpath='{.items[0].metadata.name}')
echo "Logs del broker:"
kubectl logs $BROKER_POD --tail=20
```

#### Qué Decir
```
"Voy a ver los logs del broker para verificar que está funcionando 
correctamente...

[Interpretar los logs]:
- El broker se ha iniciado correctamente
- Está escuchando en el puerto 32002
- [Si hay registros de servidores]: Los servidores se han registrado 
  correctamente
"
```

---

##  PARTE 6: DEMOSTRACIÓN PRÁCTICA (6-8 minutos)

### Preparación (NO grabar esta parte, hazla antes)
```bash
cd client/
echo "Este es el archivo de prueba 1" > test1.txt
echo "Este es el archivo de prueba 2" > test2.txt
echo "Contenido de demostración" > demo.txt
echo "Archivo adicional" > extra.txt
```

### Obtener IP para Conectar
```bash
kubectl get nodes -o wide
# O usa la IP pública de AWS
```

---

###  CLIENTE 1 - Primera Conexión

#### Conectar
```bash
./clienteFileManager <IP_DEL_NODO>
```

#### Qué Decir
```
"Ahora voy a demostrar el funcionamiento de la aplicación. Ejecuto el cliente 
pasándole la IP del nodo master...

[Esperar conexión]

Perfecto, el cliente se ha conectado correctamente. Primero obtuvo la 
información del broker y luego se conectó a uno de los servidores."
```

#### Comando: ls
```
> ls
```

#### Qué Decir
```
"El comando 'ls' lista los archivos locales en el directorio del cliente.
Como pueden ver, tengo varios archivos de prueba:
- test1.txt
- test2.txt
- demo.txt
- extra.txt
"
```

#### Comando: lls
```
> lls
```

#### Qué Decir
```
"Ahora con 'lls' listo los archivos en el servidor remoto...

[SI ESTÁ VACÍO]:
Como esta es la primera vez que ejecutamos la aplicación, el directorio 
remoto está vacío. No hay ningún archivo todavía.

[SI HAY ARCHIVOS]:
Podemos ver que ya hay algunos archivos de ejecuciones anteriores.
"
```

#### Comando: upload test1.txt
```
> upload test1.txt
```

#### Qué Decir
```
"Voy a subir el primer archivo al servidor con el comando 'upload test1.txt'...

[Esperar confirmación]

Excelente, el archivo se ha subido correctamente. El cliente lo ha enviado 
al servidor y este lo ha guardado en su directorio FileManagerDir."
```

#### Comando: lls (verificar)
```
> lls
```

#### Qué Decir
```
"Verifico con 'lls' nuevamente...

Perfecto, ahora aparece test1.txt en el listado del servidor. El archivo 
se ha transferido correctamente."
```

#### Comando: upload más archivos
```
> upload test2.txt
> upload demo.txt
```

#### Qué Decir
```
"Voy a subir algunos archivos más para tener varios en el servidor...

[Esperar confirmaciones]
"
```

#### Comando: lls (verificar todos)
```
> lls
```

#### Qué Decir
```
"Listando nuevamente los archivos remotos...

Ahora tenemos tres archivos en el servidor:
- test1.txt
- test2.txt
- demo.txt

[PARA CONFIGURACIÓN AVANZADA 1 o 2]:
Estos archivos están almacenados en el [volumen hostPath / almacenamiento NFS] 
que es compartido entre [todas las réplicas en el nodo / todos los pods en 
todos los nodos]."
```

---

###  VERIFICACIÓN INTERMEDIA (Solo Avanzada 1 o 2)

#### Para Avanzada 1 - Verificar hostPath
```bash
# En otra terminal, conectar al nodo worker
ssh -i "tu-clave.pem" ubuntu@<WORKER_IP>

ls -la /data/FileManagerDir
```

#### Qué Decir
```
"Para demostrar que el almacenamiento compartido funciona, voy a conectarme 
directamente al nodo worker y listar el contenido del directorio hostPath...

Como pueden ver, los archivos que subió el cliente están físicamente en 
/data/FileManagerDir del nodo. Todos los pods en este nodo acceden a este 
mismo directorio."
```

#### Para Avanzada 2 - Verificar NFS
```bash
# Conectar al servidor NFS o cualquier nodo
ssh -i "tu-clave.pem" ubuntu@<NFS_SERVER_IP>

ls -la /mnt/nfs-share/FileManagerDir
```

#### Qué Decir
```
"Ahora me conecto al servidor NFS para verificar que los archivos están 
allí...

Perfecto, los archivos están en el almacenamiento NFS. Desde aquí son 
accesibles por todos los pods en todos los nodos del cluster. Esto 
proporciona persistencia real y compartición de datos."
```

---

###  CLIENTE 1 - Cerrar Conexión

#### Comando: exit
```
> exit
```

#### Qué Decir
```
"Ahora voy a cerrar este cliente con el comando 'exit'...

El cliente se ha desconectado del servidor y del broker correctamente."
```

---

###  CLIENTE 2 - Segunda Conexión

#### Conectar
```bash
./clienteFileManager <IP_DEL_NODO>
```

#### Qué Decir
```
"Voy a iniciar un SEGUNDO cliente para demostrar la persistencia de datos...

[Esperar conexión]

El nuevo cliente se ha conectado. 

[PARA AVANZADA 1/2]:
Es posible que este cliente se haya conectado a una réplica diferente del 
servidor gracias al balanceo de carga de Kubernetes."
```

#### Comando: lls
```
> lls
```

#### Qué Decir
```
"Listo los archivos remotos con el nuevo cliente...

¡Excelente! Puedo ver todos los archivos que subió el cliente anterior:
- test1.txt
- test2.txt  
- demo.txt

Esto demuestra que:

[PARA BÁSICA]:
- Los archivos persisten en el servidor entre diferentes conexiones de clientes
- El sistema mantiene el estado correctamente

[PARA AVANZADA 1]:
- El almacenamiento hostPath funciona correctamente
- Todos los pods acceden al mismo directorio compartido
- Los datos persisten entre conexiones y réplicas

[PARA AVANZADA 2]:
- El almacenamiento NFS funciona correctamente
- Los datos están disponibles desde cualquier pod en cualquier nodo
- Hay persistencia real incluso si los pods se reinician o mueven de nodo
"
```

#### Comando: download test1.txt
```
> download test1.txt
```

#### Qué Decir
```
"Ahora voy a descargar uno de los archivos del servidor usando el comando 
'download test1.txt'...

[Esperar confirmación]

El archivo se ha descargado correctamente del servidor a mi directorio local."
```

#### Comando: exit
```
> exit
```

---

### Verificar Descarga

```bash
ls -la test1.txt
cat test1.txt
```

#### Qué Decir
```
"Voy a verificar que el archivo descargado es correcto...

[Mostrar archivo]

Perfecto, el archivo descargado contiene el texto esperado: 
'Este es el archivo de prueba 1'

El ciclo completo funciona correctamente:
- Cliente 1 sube archivos → Servidor los almacena
- Cliente 2 se conecta → Ve los archivos del Cliente 1
- Cliente 2 descarga → Recupera los archivos correctamente
"
```

---

###  DEMOSTRACIÓN EXTRA (Opcional para Avanzada 1/2)

#### Mostrar Balanceo de Carga
```bash
# Ver logs de diferentes pods
kubectl logs <server-pod-1> --tail=10
kubectl logs <server-pod-2> --tail=10
kubectl logs <server-pod-3> --tail=10
```

#### Qué Decir
```
"Para demostrar el balanceo de carga, voy a ver los logs de las diferentes 
réplicas del servidor...

Como pueden ver, las peticiones se están distribuyendo entre las diferentes 
réplicas. Cada pod ha procesado algunas conexiones de clientes."
```

#### Demostrar Alta Disponibilidad (Solo Avanzada 2)
```bash
# Eliminar un pod
kubectl delete pod <server-pod-name>

# Ver que se crea uno nuevo
kubectl get pods -w
```

#### Qué Decir
```
"Para demostrar la alta disponibilidad, voy a eliminar uno de los pods...

[Esperar]

Como pueden ver, Kubernetes detecta que falta un pod y automáticamente crea 
uno nuevo para mantener las 3 réplicas deseadas. Durante este proceso, el 
servicio sigue disponible porque las otras 2 réplicas continúan funcionando.

Cuando el nuevo pod se inicia, se monta automáticamente al volumen NFS y 
tiene acceso inmediato a todos los archivos existentes."
```

---

##  PARTE 7: CONCLUSIONES (1-2 minutos)

#### Qué Decir

```
"Para concluir, en esta práctica he implementado exitosamente:

 CONTAINERIZACIÓN:
- Creé Dockerfiles para el broker y servidor
- Las imágenes son ligeras y contienen solo lo necesario
- Están publicadas en Docker Hub para fácil acceso

 INFRAESTRUCTURA:
- Cluster de Kubernetes en AWS EC2 con [X] nodos
- 1 nodo master con el control-plane
- [X-1] nodos worker para las aplicaciones
- Configuración de red con Flannel

 ORQUESTACIÓN:
- Deployments de Kubernetes para gestionar los pods
- Services de tipo NodePort para acceso externo
- [Para avanzada]: Múltiples réplicas con balanceo de carga automático

 ALMACENAMIENTO:
[PARA BÁSICA]:
- Volúmenes emptyDir para almacenamiento temporal

[PARA AVANZADA 1]:
- Volúmenes hostPath para almacenamiento compartido en un nodo
- Affinity para colocar pods en el mismo nodo
- Persistencia de datos entre reinicios de pods

[PARA AVANZADA 2]:
- Servidor NFS para almacenamiento en red
- PersistentVolume y PersistentVolumeClaim
- Acceso ReadWriteMany desde múltiples nodos
- Alta disponibilidad y persistencia real
- Distribución de pods en diferentes nodos físicos

 FUNCIONALIDAD:
- Los clientes se conectan correctamente al broker
- El broker coordina las conexiones con los servidores
- Los clientes pueden listar, subir y descargar archivos
- Los datos persisten entre diferentes conexiones
- [Para avanzada]: El balanceo de carga distribuye las peticiones
- [Para avanzada 2]: El sistema es tolerante a fallos

APRENDIZAJES CLAVE:
- Comprensión profunda de contenedores Docker
- Uso práctico de Kubernetes en producción
- Configuración de redes y servicios
- Gestión de almacenamiento persistente
- [Para avanzada 2]: Implementación de sistemas distribuidos reales

Todos los archivos de configuración (Dockerfiles, YAMLs) están documentados 
y disponibles en el repositorio de la práctica.

Muchas gracias por su atención."
```

---

##  CHECKLIST ANTES DE GRABAR

### Preparación Técnica
- [ ] Cluster de Kubernetes funcionando correctamente
- [ ] Todos los pods en estado Running
- [ ] Servicios creados y accesibles
- [ ] Imágenes Docker en Docker Hub
- [ ] Cliente compilado y funcional
- [ ] Archivos de prueba creados
- [ ] [Si avanzada 1]: Directorio hostPath creado con permisos
- [ ] [Si avanzada 2]: Servidor NFS funcionando y montable

### Preparación del Entorno
- [ ] Todos los archivos necesarios en ubicaciones correctas
- [ ] Conexiones SSH probadas y funcionando
- [ ] IPs de los nodos anotadas
- [ ] Nombres de pods anotados
- [ ] Comandos preparados y probados
- [ ] Terminal con fuente legible (tamaño 14-16pt)
- [ ] Editor de texto listo para mostrar archivos

### Preparación de la Grabación
- [ ] Resolución de pantalla: 1920x1080 mínimo
- [ ] Micrófono configurado y probado
- [ ] Software de grabación listo
- [ ] Navegador cerrado (distracciones minimizadas)
- [ ] Notificaciones desactivadas
- [ ] Guión impreso o en segunda pantalla
- [ ] Agua a mano

### Prueba Final (¡IMPORTANTE!)
- [ ] Ejecutar TODA la demo de principio a fin
- [ ] Verificar que cada comando funciona
- [ ] Medir el tiempo (debe ser 15-20 min)
- [ ] Probar audio y claridad de voz
- [ ] Verificar que la pantalla se ve clara
- [ ] Revisar que no hay errores inesperados

---

##  CONSEJOS DE GRABACIÓN

### Técnicos
1. **Resolución:** 1920x1080 (1080p) o superior
2. **FPS:** 30 fps mínimo
3. **Audio:** Bitrate 192 kbps o superior
4. **Formato:** MP4 (H.264)
5. **Tamaño:** Máximo según Blackboard (verificar límite)

### De Presentación
1. **Voz Clara:** Habla despacio y pronuncia bien
2. **Pausas:** Respira entre secciones
3. **Sin Muletillas:** Evita "ehh", "umm", etc.
4. **Explicaciones:** Asume que la audiencia no sabe nada
5. **Errores:** Si cometes uno pequeño, continúa; si es grave, edita

### De Edición
1. **Cortar Esperas:** Acelera partes donde se ejecutan comandos largos
2. **Zoom:** Si algo es pequeño, haz zoom en la edición
3. **Transiciones:** Suaves entre secciones
4. **Texto:** Añade títulos para cada parte (opcional)
5. **Música:** Opcional, pero no debe distraer

---

##  ERRORES COMUNES A EVITAR

### En la Configuración
-  No tener los pods en Running antes de grabar
-  Security groups sin los puertos correctos abiertos
-  Olvidar crear el directorio hostPath
-  NFS sin exportar correctamente
-  Usar IPs incorrectas para conectar

### En la Presentación
-  Ir demasiado rápido
-  No explicar QUÉ haces, solo mostrarlo
-  Asumir conocimiento previo de la audiencia
-  No verificar que algo funcionó antes de continuar
-  Saltarse la demostración práctica con clientes

### En el Video
-  Audio inaudible o con ruido
-  Pantalla ilegible (letra muy pequeña)
-  Video demasiado largo (>25 min) o corto (<12 min)
-  No mostrar los Dockerfiles y YAMLs
-  No demostrar persistencia de datos

---

##  PLAN B (Si algo falla durante la grabación)

### Si un pod no inicia:
```bash
kubectl delete pod <pod-name>
# Esperar a que se recree
kubectl get pods -w
```

### Si el cliente no conecta:
```bash
# Verificar servicios
kubectl get services

# Ver logs del broker
kubectl logs <broker-pod>

# Probar con IP diferente
kubectl get nodes -o wide
```

### Si falla la descarga/subida:
```bash
# Reintentar el comando
# Ver logs del servidor
kubectl logs <server-pod>

# Verificar permisos del directorio
kubectl exec -it <server-pod> -- ls -la /app/FileManagerDir
```

### Si algo sale muy mal:
- Pausa la grabación
- Arregla el problema
- Resume desde el último punto estable
- Edita el video para eliminar la pausa

---

##  LISTA FINAL DE ARCHIVOS A ENTREGAR

```
AEC4_[TuNombre].zip
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
    nfs/ (si aplica)
        nfs-server.yaml
        nfs-pv-pvc.yaml
 README.md (opcional pero recomendado)
 video/
     AEC4_Demo_[TuNombre].mp4
```

---

##  ÚLTIMA REVISIÓN

Antes de entregar, verifica:
- [ ] Todos los archivos YAML están incluidos
- [ ] Los Dockerfiles están incluidos
- [ ] El video se reproduce correctamente
- [ ] El video tiene audio claro
- [ ] El video muestra TODA la demo requerida
- [ ] El tamaño del ZIP es aceptable para Blackboard
- [ ] Has guardado copia de seguridad

---

**¡Mucha suerte con tu presentación!** 

Recuerda: La práctica hace al maestro. Ensaya varias veces antes de grabar la versión final.
