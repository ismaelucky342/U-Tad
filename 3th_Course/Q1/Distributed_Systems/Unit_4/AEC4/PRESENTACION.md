# GUIÓN DE AUDIO - PRESENTACIÓN AEC4
## Configuración Avanzada 2: NFS (10 PUNTOS)

---

## 🎬 PARTE 1: INTRODUCCIÓN (1-2 min)

Hola, soy Ismael y voy a presentar la AEC4 de Sistemas Distribuidos.

He implementado un sistema de gestión de archivos distribuido usando Docker, Kubernetes y AWS EC2. La aplicación tiene tres componentes: un BROKER en el puerto 32002 que coordina las conexiones, varios SERVIDORES en el puerto 32001 que gestionan los archivos, y CLIENTES que interactúan con el sistema.

He implementado la Configuración Avanzada 2, la más compleja, que vale 10 puntos. Esta configuración incluye un cluster con 1 master y 3 workers, 3 réplicas del servidor distribuidas en diferentes nodos físicos, y almacenamiento compartido NFS con PersistentVolume y PersistentVolumeClaim. Esto proporciona alta disponibilidad, tolerancia a fallos y balanceo de carga automático.

---

## 🖥️ PARTE 2: MOSTRAR NODOS Y SERVICIOS (2-3 min)

### Al ejecutar: `kubectl get nodes -o wide`

Aquí podéis ver mi cluster completo. Tengo 4 nodos: 1 master que ejecuta el control-plane de Kubernetes y 3 workers donde corren las aplicaciones. Todos están en estado Ready, operativos y listos para ejecutar pods.

Las 3 réplicas del servidor están repartidas entre estos 3 workers. Esto me da alta disponibilidad real: si un nodo falla, los otros dos siguen funcionando.

### Al ejecutar: `kubectl get deployments`

Aquí vemos los deployments. El broker-deployment tiene 1/1 ready, y el server-deployment tiene 3/3 ready, las tres réplicas funcionando correctamente.

### Al ejecutar: `kubectl get pods -o wide`

En los pods con detalle, vemos que el pod del broker está corriendo en uno de los workers, y lo más importante: las 3 réplicas del servidor están repartidas en los 3 workers diferentes. Cada réplica está en un nodo distinto, lo cual maximiza la disponibilidad. Si cualquier nodo falla, siempre tengo al menos 2 réplicas funcionando.

### Al ejecutar: `kubectl get services`

Los servicios expuestos son el broker-service en el puerto 32002 y el server-service en el puerto 32001. El server-service automáticamente balancea las peticiones entre las 3 réplicas.

### Al ejecutar: `kubectl get pv,pvc`

El PersistentVolume nfs-pv está en estado Bound, vinculado al PVC. Tiene 5Gi disponibles y el modo ReadWriteMany activo, lo que permite que múltiples pods lean y escriban simultáneamente. El PersistentVolumeClaim nfs-pvc también está Bound y está montado por los 3 pods del servidor. Todos acceden al mismo almacenamiento compartido.

---

## 📦 PARTE 3: EXPLICAR DOCKERFILES Y YAMLS (3-4 min)

### Al mostrar: `cat docker/broker/Dockerfile`

El Dockerfile del broker es sencillo. He usado Ubuntu 20.04 como imagen base por compatibilidad con los binarios. Instalo libstdc++6 como dependencia necesaria, copio el binario del broker, expongo el puerto 32002 y ejecuto el broker. Es una imagen ligera con solo lo necesario.

### Al mostrar: `cat docker/server/Dockerfile`

El Dockerfile del servidor es similar, pero aquí creo el directorio /app/FileManagerDir para almacenar archivos. El puerto es el 32001. Uso ENTRYPOINT porque el servidor necesita recibir la IP del broker como parámetro al arrancar.

Estas imágenes están publicadas en Docker Hub para que Kubernetes pueda descargarlas desde cualquier nodo del cluster.

### Al mostrar: `cat kubernetes/broker/deployment.yaml`

El deployment del broker es simple. Solo necesito 1 réplica. Uso mi imagen de Docker Hub, expongo el puerto 32002, y le pongo límites de recursos para el scheduler de Kubernetes. El service es de tipo NodePort, accesible desde fuera del cluster.

### Al mostrar: `cat kubernetes/nfs/nfs-pv-pvc.yaml`

Aquí está toda la configuración del almacenamiento distribuido. El PersistentVolume nfs-pv conecta con el servidor NFS usando su IP. Tiene 5Gi de capacidad y ReadWriteMany, que permite que múltiples pods lean y escriban simultáneamente. Esto es lo que permite tener las réplicas compartiendo datos.

El PersistentVolumeClaim nfs-pvc es la solicitud de acceso a ese volumen. Los pods montan el PVC, lo cual abstrae los detalles de implementación.

### Al mostrar: `cat kubernetes/server/deployment-advanced2.yaml`

Este es el deployment avanzado 2. Tengo 3 réplicas del servidor, y Kubernetes las distribuye automáticamente en diferentes nodos. Cada réplica monta el PVC nfs-pvc en /app/FileManagerDir, entonces las 3 réplicas acceden al mismo almacenamiento NFS. Los archivos son accesibles desde cualquier pod en cualquier nodo.

Las ventajas son enormes: alta disponibilidad porque si un nodo falla los otros continúan, persistencia real porque los datos están en red y sobreviven a reinicios, y escalabilidad porque puedo añadir más réplicas fácilmente.

---

## 🧪 PARTE 4: DEMOSTRACIÓN PRÁCTICA (5-7 min)

### Al conectar el primer cliente

Voy a ejecutar el primer cliente. El cliente se ha conectado correctamente.

### Al ejecutar: `ls`

Aquí tengo los archivos de prueba locales: test1.txt, test2.txt y demo.txt.

### Al ejecutar: `lls`

El directorio remoto está vacío porque es la primera ejecución. [O: Ya hay algunos archivos de ejecuciones anteriores]

### Al ejecutar: `upload test1.txt`

Archivo subido correctamente. Voy a verificar.

### Al ejecutar: `lls`

Perfecto, ahora aparece test1.txt en el listado remoto. El archivo se ha transferido correctamente al servidor.

### Al ejecutar: `upload test2.txt` y `upload demo.txt`

Voy a subir un par de archivos más.

### Al ejecutar: `lls`

Ahora tengo 3 archivos en el servidor. Lo importante es que estos archivos están en el almacenamiento NFS compartido. Los 3 pods del servidor, en 3 nodos diferentes, pueden acceder a estos mismos archivos. Si un cliente se conecta a cualquier réplica, verá exactamente estos archivos.

### Al verificar en el servidor NFS

Voy a conectarme al servidor NFS para verificar que los archivos están ahí físicamente. Aquí están los archivos, almacenados en /mnt/nfs-share/FileManagerDir del servidor NFS. Desde aquí son accesibles por todos los pods en todos los nodos del cluster. Si un nodo falla, los datos siguen disponibles. Esto es persistencia real en un sistema distribuido.

### Al ejecutar: `exit` y conectar segundo cliente

Cierro este cliente y ahora inicio un segundo cliente para demostrar la persistencia de datos. Conectado. Este segundo cliente puede haberse conectado a una réplica diferente gracias al balanceo de carga de Kubernetes.

### Al ejecutar: `lls` en el segundo cliente

Perfecto! Este segundo cliente ve todos los archivos que subió el primer cliente: test1.txt, test2.txt y demo.txt.

Esto demuestra varias cosas: el almacenamiento NFS funciona correctamente, los datos están disponibles desde cualquier pod en cualquier nodo, hay persistencia real entre diferentes conexiones, el balanceo de carga distribuye clientes entre réplicas, y todas las réplicas acceden al mismo almacenamiento compartido. Es un sistema distribuido real con alta disponibilidad.

### Al ejecutar: `download test1.txt`

Voy a descargar uno de los archivos. Archivo descargado correctamente.

### Al ejecutar: `exit` y verificar el archivo descargado

Cierro el cliente y verifico que el archivo se descargó bien. Aquí está el archivo con su contenido correcto. Todo el ciclo funciona perfectamente.

---

## ⚡ PARTE 5: DEMOSTRACIÓN EXTRA (Opcional, 2-3 min)

### Al ver logs de réplicas

Voy a ver los logs de las 3 réplicas para demostrar que las peticiones se distribuyen. Como podéis ver, las peticiones se han distribuido entre los diferentes pods. Cada réplica ha procesado conexiones de clientes. El balanceo de carga de Kubernetes funciona perfectamente.

### Al eliminar un pod

Ahora voy a eliminar un pod para simular que un nodo falla. Kubernetes detecta inmediatamente que falta un pod y empieza a crear uno nuevo automáticamente para mantener las 3 réplicas especificadas.

Mientras esto pasa, las otras 2 réplicas siguen funcionando con normalidad. Los clientes pueden seguir conectándose sin problema. El servicio nunca se interrumpe.

Cuando el nuevo pod termina de arrancar, se monta automáticamente al volumen NFS, tiene acceso inmediato a todos los archivos existentes, y empieza a recibir peticiones del balanceador. Esto es alta disponibilidad real, tolerancia a fallos de hardware en un sistema distribuido de producción.

---

## 🎯 PARTE 6: CONCLUSIÓN (1 min)

Para terminar, he completado la Configuración Avanzada 2 con NFS, la más compleja de la práctica, que vale 10 puntos.

He creado Dockerfiles optimizados para broker y servidor, publicados en Docker Hub. He montado un cluster de Kubernetes en AWS EC2 con 4 nodos: 1 master y 3 workers, con red overlay gestionada por Flannel.

En orquestación tengo deployments con réplicas distribuidas, services con NodePort y balanceo de carga, y las 3 réplicas repartidas en nodos físicos diferentes.

El almacenamiento distribuido incluye un servidor NFS independiente, un PersistentVolume de 5Gi con ReadWriteMany, y un PersistentVolumeClaim montado por las 3 réplicas. Los datos están compartidos entre todos los nodos con persistencia real en red.

Esto proporciona: alta disponibilidad con tolerancia a fallos de nodos, balanceo de carga con peticiones distribuidas, persistencia distribuida en almacenamiento compartido en red, escalabilidad fácil, y básicamente un sistema distribuido real con múltiples puntos de fallo cubiertos.

La demostración ha mostrado que puedo subir y descargar archivos, hay persistencia entre conexiones, los datos son accesibles desde cualquier réplica, hay tolerancia a fallos con recreación automática de pods, y el balanceo de carga distribuye correctamente.

Todo funciona como un sistema distribuido de producción real.

Gracias por la atención.

---

## 📝 NOTAS PARA LA GRABACIÓN

### Tono y Ritmo
- Habla **despacio y claro** - hay mucho contenido técnico
- Enfatiza las palabras clave: "alta disponibilidad", "tolerancia a fallos", "NFS", "ReadWriteMany"
- Haz pausas cortas entre secciones para que sea más digerible
- No corras, tienes 15-20 minutos

### Puntos a Enfatizar
- ✨ "Configuración Avanzada 2 - 10 puntos"
- ✨ "3 réplicas en 3 nodos FÍSICOS diferentes"
- ✨ "Almacenamiento compartido en RED, no local"
- ✨ "Sistema distribuido de PRODUCCIÓN real"
- ✨ "Alta disponibilidad y tolerancia a fallos"

### Durante la Grabación
- Si te equivocas, **pausa, respira, y continúa** desde el inicio de esa frase
- Si un comando tarda, **llena el silencio** explicando qué esperas que pase
- **Muestra confianza** - conoces el sistema que has montado
- Si algo no funciona como esperabas, **explica el problema** y cómo lo resolverías

---

## ⏱️ TIMING APROXIMADO

```
00:00 - 02:00  Introducción
02:00 - 05:00  Mostrar nodos y servicios
05:00 - 09:00  Explicar Dockerfiles y YAMLs
09:00 - 16:00  Demostración práctica completa
16:00 - 18:00  Demostración extra (opcional)
18:00 - 20:00  Conclusión
```

Total: 18-20 minutos

---

**¡Buena suerte con la grabación!**
