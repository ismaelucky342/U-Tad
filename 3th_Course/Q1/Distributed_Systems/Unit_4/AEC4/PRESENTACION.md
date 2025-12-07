# GUION DE PRESENTACION AEC4
## Video 15-20 minutos - CONFIGURACION AVANZADA 2: NFS (10 PUNTOS)

---

## PASO 1 - INTRODUCCION (2 min)

Bueno, hola a todos. Soy Ismael y voy a presentar la AEC4 de Sistemas Distribuidos.

Para esta practica he montado una aplicacion de gestion de archivos distribuida usando Docker para containerizar, Kubernetes para orquestar todo, y AWS EC2 como infraestructura base.

La aplicacion basicamente tiene tres componentes principales:
- Un BROKER que se ejecuta en el puerto 32002 y que coordina todas las conexiones entre clientes y servidores
- Varios SERVIDORES que corren en el puerto 32001 y que son los que realmente gestionan los archivos
- Y los CLIENTES que se conectan para subir y descargar archivos

He implementado la configuracion mas avanzada, que es la Avanzada 2, que vale 10 puntos. Esta configuracion incluye un cluster con 1 master y 3 workers, con 3 replicas del servidor distribuidas en diferentes nodos fisicos. He montado un servidor NFS para tener almacenamiento compartido en red, y he configurado PersistentVolume y PersistentVolumeClaim para que todo funcione. Esto me da alta disponibilidad, tolerancia a fallos, y balanceo de carga automatico entre las replicas.

Basicamente es la configuracion mas compleja que se podia hacer, asi que vamos a ver como funciona todo.

---

## PASO 2 - MOSTRAR EL CLUSTER (3 min)

Primero voy a conectarme al nodo master para mostrar el cluster:

```bash
ssh -i "tu-clave.pem" ubuntu@<IP_MASTER>
```

Y ahora voy a ver los nodos que tengo:

```bash
kubectl get nodes -o wide
```

Vale, aqui podeis ver mi cluster completo. Tengo 4 nodos en total: 1 master que ejecuta el control-plane de Kubernetes, y 3 workers donde corren las aplicaciones. Todos estan en estado Ready, lo cual significa que estan operativos y listos para ejecutar pods.

Lo importante aqui es que las 3 replicas del servidor estan repartidas entre estos 3 workers. Esto me da alta disponibilidad real, porque si uno de los nodos se cae o falla, los otros dos siguen funcionando sin problema.

Si quereis ver mas detalles, puedo ejecutar:

```bash
kubectl describe nodes | grep -E "Name:|Roles:|Internal IP:"
```

Aqui vemos las IPs internas que Kubernetes usa para que los pods se comuniquen entre si. Esto es la red overlay que monta Kubernetes internamente.

---

## PASO 3 - DOCKERFILES (2 min)

Ahora os voy a ensenar como he containerizado las aplicaciones. Empiezo con el Dockerfile del broker:

```bash
cat docker/broker/Dockerfile
```

El Dockerfile del broker es bastante sencillo. He usado Ubuntu 20.04 como imagen base porque es la que mejor compatibilidad tiene con los binarios que me dieron. Instalo libstdc++6 que es una dependencia necesaria para que el ejecutable funcione, copio el binario del broker al contenedor, expongo el puerto 32002, y ejecuto el broker. Es una imagen bastante ligera, solo con lo necesario.

Ahora el del servidor:

```bash
cat docker/server/Dockerfile
```

El Dockerfile del servidor es muy similar, con la diferencia de que aqui creo el directorio /app/FileManagerDir donde se van a almacenar los archivos. El puerto es el 32001 en este caso. Una cosa importante es que uso ENTRYPOINT en lugar de CMD porque el servidor necesita recibir la IP del broker como parametro cuando arranca.

Estas imagenes las he construido localmente y las he subido a Docker Hub bajo mi usuario, para que Kubernetes pueda descargarlas desde cualquier nodo del cluster.

---

## PASO 4 - YAMLS DE KUBERNETES (4 min)

### Deployment del Broker

Vale, ahora vamos con los archivos YAML que definen como se despliega todo en Kubernetes:

```bash
cat kubernetes/broker/deployment.yaml
```

El deployment del broker es relativamente simple. Solo necesito 1 replica porque no tiene sentido tener varios brokers. Uso mi imagen de Docker Hub, expongo el puerto 32002, y le he puesto algunos limites de recursos para que el scheduler de Kubernetes sepa cuantos recursos necesita.

El service del broker es de tipo NodePort, lo que significa que puedo acceder a el desde fuera del cluster usando la IP de cualquier nodo y el puerto 32002.

### Configuracion NFS del Servidor

Ahora viene la parte mas interesante, que es toda la configuracion del almacenamiento compartido con NFS:

```bash
cat kubernetes/nfs/nfs-pv-pvc.yaml
```

Aqui es donde esta todo el tema del almacenamiento distribuido. He montado un servidor NFS independiente que exporta el directorio /mnt/nfs-share.

El PersistentVolume, que es el nfs-pv, es basicamente la definicion del volumen que conecta con el servidor NFS usando su IP. Tiene 5Gi de capacidad y lo mas importante: ReadWriteMany, que significa que multiples pods pueden leer y escribir en el simultaneamente. Esto es lo que me permite tener las replicas compartiendo datos.

El PersistentVolumeClaim, el nfs-pvc, es la solicitud de acceso a ese volumen. Los pods no montan el PV directamente, sino que montan el PVC, lo cual abstrae un poco los detalles de implementacion.

Ahora el deployment del servidor:

```bash
cat kubernetes/server/deployment-advanced2.yaml
```

Este es el deployment avanzado 2. Aqui tengo 3 replicas del servidor, y Kubernetes las distribuye automaticamente en diferentes nodos. No necesito configurar affinity ni nada porque por defecto Kubernetes intenta repartirlas.

Cada replica monta el PVC nfs-pvc en /app/FileManagerDir, entonces las 3 replicas acceden exactamente al mismo almacenamiento NFS. Los archivos son accesibles desde cualquier pod en cualquier nodo.

Las ventajas de esto son enormes: tengo alta disponibilidad porque si un nodo falla los otros continuan, persistencia real porque los datos estan en red y sobreviven a cualquier reinicio, y escalabilidad porque puedo anadir mas replicas facilmente.

El service es NodePort en el puerto 32001 y Kubernetes automaticamente balancea las peticiones entre las 3 replicas.
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
---

## PASO 5 - ESTADO DEL CLUSTER (2 min)

Ahora voy a mostrar el estado actual de todo lo que tengo desplegado:

```bash
kubectl get deployments
kubectl get pods -o wide
kubectl get services
```

Vale, aqui podeis ver que los deployments estan listos. El broker-deployment tiene 1/1 ready, y el server-deployment tiene 3/3 ready, las tres replicas funcionando.

Si miramos los pods con detalle, vemos que el pod del broker esta corriendo en uno de los workers, y lo mas importante: las 3 replicas del servidor estan repartidas en los 3 workers diferentes. Cada replica esta en un nodo distinto, lo cual me da la maxima disponibilidad posible. Si cualquier nodo se cae, siempre tengo al menos 2 replicas funcionando.

Los services que tengo expuestos son el broker-service en el puerto 32002 y el server-service en el puerto 32001. El server-service automaticamente balancea las peticiones entre las 3 replicas.

Ahora voy a verificar el almacenamiento NFS:

```bash
kubectl get pv,pvc
```

Perfecto. El PersistentVolume nfs-pv esta en estado Bound, vinculado al PVC. Tiene 5Gi disponibles y el modo ReadWriteMany activo. El PersistentVolumeClaim nfs-pvc tambien esta Bound, conectado al PV, y esta montado por los 3 pods del servidor. Todos acceden al mismo almacenamiento compartido.

Si quereis, puedo ver los logs del broker para verificar que todo esta funcionando:

```bash
BROKER_POD=$(kubectl get pods -l app=broker -o jsonpath='{.items[0].metadata.name}')
kubectl logs $BROKER_POD --tail=20
```

En los logs se ve que el broker se inicio correctamente, esta escuchando en el puerto 32002, y los 3 servidores se han registrado correctamente con el.

---

## PASO 6 - DEMOSTRACION PRACTICA (6-8 min)

Vale, ahora viene la parte practica donde voy a demostrar que todo funciona. Primero necesito obtener la IP de uno de los nodos:

```bash
kubectl get nodes -o wide
```

Y ahora voy a ejecutar el cliente:

```bash
./clienteFileManager <IP_DEL_NODO>
```

Perfecto, el cliente se ha conectado correctamente.

### Primera conexion de cliente

Voy a empezar listando los archivos locales:

```
> ls
```

Aqui tengo los archivos de prueba que prepare: test1.txt, test2.txt, y demo.txt.

Ahora voy a ver que hay en el servidor remoto:

```
> lls
```

[Si esta vacio] El directorio remoto esta vacio porque es la primera vez que ejecuto esto.
[Si hay archivos] Ya hay algunos archivos de ejecuciones anteriores.

Voy a subir el primer archivo:

```
> upload test1.txt
```

Vale, archivo subido correctamente. Voy a verificar que esta en el servidor:

```
> lls
```

Perfecto, ahora aparece test1.txt en el listado remoto. El archivo se ha transferido correctamente al servidor.

Voy a subir un par de archivos mas para tener varios en el servidor:

```
> upload test2.txt
> upload demo.txt
> lls
```

Excelente, ahora tengo 3 archivos en el servidor. Lo importante aqui es que estos archivos estan en el almacenamiento NFS compartido. Los 3 pods del servidor, que estan en 3 nodos diferentes, pueden acceder a estos mismos archivos. Si un cliente se conecta a cualquier replica, vera exactamente estos archivos.

### Verificacion del NFS

Ahora voy a conectarme al servidor NFS para verificar que los archivos estan alli fisicamente:

```bash
ssh ubuntu@<NFS_IP>
ls -la /mnt/nfs-share/FileManagerDir
```

Aqui estan los archivos, fisicamente almacenados en /mnt/nfs-share/FileManagerDir del servidor NFS. Desde aqui son accesibles por todos los pods en todos los nodos del cluster. Si un nodo falla, los datos siguen disponibles desde los otros nodos. Esto es persistencia real en un sistema distribuido.

### Segunda conexion de cliente

Voy a cerrar este cliente:

```
> exit
```

Y ahora voy a iniciar un segundo cliente para demostrar la persistencia de datos:

```bash
./clienteFileManager <IP_DEL_NODO>
```

Conectado. Este segundo cliente puede haberse conectado a una replica diferente del servidor gracias al balanceo de carga de Kubernetes. Voy a comprobar que ve los mismos archivos:

```
> lls
```

Perfecto! Este segundo cliente puede ver todos los archivos que subio el primer cliente: test1.txt, test2.txt, y demo.txt.

Esto demuestra varias cosas importantes:
1. El almacenamiento NFS funciona correctamente
2. Los datos estan disponibles desde cualquier pod en cualquier nodo
3. Hay persistencia real - los datos sobreviven entre diferentes conexiones
4. El balanceo de carga esta distribuyendo clientes entre las replicas
5. Todas las replicas acceden al mismo almacenamiento compartido

Es un sistema distribuido real con alta disponibilidad.

Ahora voy a descargar uno de los archivos:

```
> download test1.txt
```

Archivo descargado correctamente. Cierro el cliente:

```
> exit
```

Y verifico que el archivo se descargo bien:

```bash
ls -la client/
cat client/test1.txt
```

Aqui esta el archivo con su contenido correcto. Todo el ciclo funciona perfectamente.
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
---

## PASO 7 - DEMOSTRACION DE ALTA DISPONIBILIDAD (2 min)

Para terminar la demo, voy a mostrar dos cosas importantes: el balanceo de carga y la tolerancia a fallos.

### Balanceo de carga entre replicas

Primero voy a ver los logs de las 3 replicas para demostrar que las peticiones se distribuyen:

```bash
kubectl get pods -l app=server
kubectl logs <server-pod-1> --tail=10
kubectl logs <server-pod-2> --tail=10
kubectl logs <server-pod-3> --tail=10
```

Como podeis ver en los logs, las peticiones se han distribuido entre los diferentes pods. Cada replica ha procesado conexiones de clientes. El balanceo de carga de Kubernetes esta funcionando perfectamente.

### Tolerancia a fallos de hardware

Ahora voy a hacer algo mas interesante. Voy a eliminar un pod para simular que un nodo se cae o tiene un problema:

```bash
kubectl delete pod <server-pod-name>
```

Y ahora observad lo que pasa:

```bash
kubectl get pods -w
```

Kubernetes detecta inmediatamente que falta un pod y empieza a crear uno nuevo automaticamente para mantener las 3 replicas que especifique en el deployment.

Mientras esto pasa, las otras 2 replicas siguen funcionando con total normalidad. Los clientes pueden seguir conectandose sin ningun problema. El servicio nunca se interrumpe.

Cuando el nuevo pod termina de arrancar, se monta automaticamente al volumen NFS, tiene acceso inmediato a todos los archivos que ya existian, y empieza a recibir peticiones del balanceador.

Esto es alta disponibilidad real. Tolerancia a fallos de hardware en un sistema distribuido de produccion.

---

## PASO 8 - CONCLUSION (1 min)

Bueno, para ir terminando, voy a hacer un resumen rapido de todo lo que he implementado.

He completado la configuracion Avanzada 2 con NFS, que es la mas compleja de toda la practica y vale 10 puntos.

En cuanto a containerizacion, he creado Dockerfiles optimizados tanto para el broker como para el servidor, y las imagenes estan publicadas en Docker Hub para que Kubernetes pueda descargarlas.

Para la infraestructura, he montado un cluster de Kubernetes en AWS EC2 con 4 nodos: 1 master y 3 workers. La red overlay esta gestionada con Flannel.

En orquestacion, tengo deployments con replicas distribuidas, services con NodePort y balanceo de carga, y las 3 replicas del servidor estan repartidas en nodos fisicos diferentes.

El almacenamiento distribuido es probablemente la parte mas compleja. He configurado un servidor NFS independiente, un PersistentVolume de 5Gi con modo ReadWriteMany, y un PersistentVolumeClaim que montan las 3 replicas. Los datos estan compartidos entre todos los nodos y tengo persistencia real en red.

Las funcionalidades avanzadas que esto me proporciona son: alta disponibilidad con tolerancia a fallos de nodos, balanceo de carga con peticiones distribuidas entre replicas, persistencia distribuida con datos en almacenamiento compartido en red, escalabilidad para anadir mas replicas facilmente, y basicamente un sistema distribuido real con multiples puntos de fallo cubiertos.

La demostracion que acabais de ver ha mostrado que puedo subir y descargar archivos sin problemas, que hay persistencia entre diferentes conexiones de clientes, que los datos son accesibles desde cualquier replica, que hay tolerancia a fallos con recreacion automatica de pods, y que el balanceo de carga esta distribuyendo las peticiones correctamente.

Todo funciona como un sistema distribuido de produccion real.

Y bueno, esto es todo. Gracias por la atencion.

---

## NOTAS Y PREPARACION

### Antes de grabar - Checklist tecnico

Asegurate de que todo esto funciona ANTES de empezar a grabar:

**Cluster y nodos:**
- [ ] Cluster funcionando: 1 master + 3 workers
- [ ] Todos los pods en estado Running
- [ ] Las 3 replicas del servidor estan en nodos DIFERENTES (verifica con `kubectl get pods -o wide`)

**Almacenamiento NFS:**
- [ ] Servidor NFS funcionando y exportando /mnt/nfs-share
- [ ] nfs-common instalado en todos los workers
- [ ] PV y PVC en estado Bound
- [ ] Puedes verificar el montaje desde dentro de un pod: `kubectl exec -it <server-pod> -- df -h`

**Servicios y cliente:**
- [ ] Servicios broker y server accesibles
- [ ] Cliente compilado y funcional
- [ ] Archivos de prueba creados (test1.txt, test2.txt, demo.txt)

**Acceso y conectividad:**
- [ ] Tienes las IPs anotadas: master, workers, NFS
- [ ] SSH funciona al master y al NFS
- [ ] Security groups tienen abiertos los puertos: 32001, 32002, 2049 (NFS)
- [ ] Has probado todos los comandos kubectl

**Entorno de grabacion:**
- [ ] Terminal con letra grande (14-16pt minimo para que se lea bien)
- [ ] Notificaciones del sistema desactivadas
- [ ] Ambiente silencioso para grabar

### Equipo de grabacion

- [ ] Resolucion 1920x1080 minimo (mejor si es mas)
- [ ] Microfono configurado y probado (prueba de audio antes)
- [ ] Software de grabacion listo (OBS, Zoom, QuickTime, lo que uses)
- [ ] Guion impreso o en segunda pantalla donde puedas verlo
- [ ] Agua cerca por si te secas la boca

### Prueba completa OBLIGATORIA

Antes de grabar la version final:
- [ ] Ejecuta la demo COMPLETA de principio a fin al menos 2-3 veces
- [ ] Mide el tiempo (debe estar entre 15-20 minutos)
- [ ] Verifica que el audio se escucha claro
- [ ] Comprueba que la pantalla se ve legible
- [ ] Asegurate de que el acceso NFS funciona desde los pods
- [ ] Confirma que no hay errores inesperados

---

## Consejos para grabar

### Antes de empezar:
1. Verifica que el NFS esta funcionando: `showmount -e <NFS_IP>` debe mostrar /mnt/nfs-share
2. Verifica que los pods montan el NFS: `kubectl exec -it <server-pod> -- df -h` debe mostrar el NFS montado
3. Verifica la distribucion: `kubectl get pods -o wide` debe mostrar las 3 replicas en nodos diferentes
4. Ensaya 3-4 veces completas - esta config es compleja y necesitas dominar el flujo

### Durante la grabacion:
1. **Habla despacio y claro** - tienes mucho contenido tecnico que explicar
2. **Enfatiza que es la configuracion avanzada de 10 puntos** - que se note que es la mas compleja
3. **Muestra bien la distribucion de pods** - resalta que estan en nodos fisicos diferentes
4. **La demostracion de tolerancia a fallos es clave** - la parte de eliminar el pod y ver como se recrea
5. **Explica el POR QUE de cada cosa** - no solo muestres que funciona, explica por que lo haces asi

### Puntos importantes que destacar:
- "Sistema distribuido REAL con alta disponibilidad"
- "Almacenamiento compartido en RED, no es almacenamiento local"
- "Tolerancia a fallos de HARDWARE, no solo de pods"
- "Configuracion de PRODUCCION, no solo una demo academica"

---

## Si algo falla durante la grabacion

### Si un pod no arranca:
```bash
kubectl describe pod <pod-name>  # Ver que error tiene
kubectl logs <pod-name>  # Ver los logs del pod
kubectl delete pod <pod-name>  # Forzar que se recree
```

### Si el NFS no monta correctamente:
```bash
# Verificar desde dentro de un pod
kubectl exec -it <server-pod> -- mount | grep nfs
# Si falla, verifica los exports en el servidor NFS
showmount -e <NFS_IP>
# Verifica que nfs-common esta instalado en los workers
```

### Si el cliente no puede conectar:
```bash
kubectl get services  # Verifica que los puertos esten bien
kubectl logs <broker-pod>  # Ver si hay errores en el broker
# Prueba con la IP de un nodo diferente
```

### Si PV/PVC no se conectan:
```bash
kubectl describe pv nfs-pv
kubectl describe pvc nfs-pvc
# Verifica que la IP del NFS en el YAML sea correcta
# Verifica que el servidor NFS esta exportando el directorio
```

---

## Archivos que tienes que entregar

Estructura del ZIP:
```
AEC4_TuNombre_Avanzada2.zip
├── docker/
│   ├── broker/
│   │   └── Dockerfile
│   └── server/
│       └── Dockerfile
├── kubernetes/
│   ├── broker/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── server/
│   │   ├── deployment-advanced2.yaml
│   │   └── service.yaml
│   └── nfs/
│       ├── nfs-server.yaml (si tienes el YAML del servidor NFS)
│       └── nfs-pv-pvc.yaml
├── scripts/ (opcional pero queda bien)
│   ├── build-images.sh
│   └── update-yamls.sh
├── README.md (explicando brevemente la config)
└── video/
    └── AEC4_Demo_TuNombre.mp4
```

### Checklist final antes de subir:
- [ ] Todos los YAML de NFS estan incluidos
- [ ] Has incluido el deployment-advanced2, NO el basic ni el advanced1
- [ ] Los Dockerfiles estan incluidos
- [ ] El video se reproduce correctamente
- [ ] El audio se escucha claro durante TODO el video
- [ ] La demo COMPLETA esta mostrada (incluyendo la parte de alta disponibilidad)
- [ ] Mencionas claramente que es la configuracion Avanzada 2 de 10 puntos
- [ ] El tamano del ZIP es aceptable para subirlo a Blackboard
- [ ] Tienes una COPIA DE SEGURIDAD guardada en otro sitio

---

## Estructura temporal del video

Intenta seguir mas o menos estos tiempos:

```
00:00 - 02:00  Introduccion (enfatiza que es config Avanzada 2)
02:00 - 05:00  Mostrar cluster y nodos (deja claro que tienes 4 nodos)
05:00 - 09:00  Explicar Dockerfiles y YAMLs (detalla bien NFS, PV, PVC)
09:00 - 11:00  Estado del cluster (muestra como estan distribuidos los pods)
11:00 - 17:00  Demo practica (upload, download, verificacion en NFS)
17:00 - 19:00  Alta disponibilidad (eliminar pod, ver recreacion)
19:00 - 20:00  Conclusion (resumen de todo lo implementado)
```

---

## Revision final antes de entregar

**El dia antes de entregar:**
1. Reproduce el video COMPLETO de principio a fin
2. Verifica que el audio sea claro SIEMPRE, sin cortes
3. Verifica que se vea TODO claramente, que el texto es legible
4. Comprueba que dura entre 15-20 minutos (ni muy corto ni muy largo)
5. Asegurate de que mencionas "Configuracion Avanzada 2" y "NFS" claramente
6. Confirma que se ven los 3 pods en nodos diferentes
7. Confirma que demuestras la alta disponibilidad eliminando un pod

**El dia de la entrega:**
- Sube el video ANTES de la hora limite, deja margen por si hay problemas de red
- Verifica que el ZIP no esta corrupto (abrelo y comprueba que todos los archivos estan)
- Guarda el email o confirmacion de entrega

---

## Recuerda

Esta es la configuracion MAS COMPLEJA y vale 10 puntos.

Con esto estas demostrando que dominas:
- Kubernetes a nivel avanzado
- Almacenamiento distribuido en sistemas reales
- Alta disponibilidad y tolerancia a fallos
- Configuraciones de sistemas en produccion

Ensaya varias veces, habla claro, explica bien lo que haces, y todo saldra perfecto.

¡Mucha suerte!

=== FIN DEL GUION ===
