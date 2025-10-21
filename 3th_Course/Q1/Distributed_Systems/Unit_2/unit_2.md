# Unidad 2 

*Definimos los sistemas distribuidos de tipo Cluster como un conjunto de computadoras (nodos) interconectadas que trabajan de manera coordinada como si fueran un único sistema, con el objetivo de ofrecer mayor disponibilidad, escalabilidad y rendimiento.*

## Diseño de un sistema de memoria distribuida

Los sistemas de memoria distribuida se componen de nodos de cómputo conectados entre sí, pero trabajan de forma independiente. Se denominan ”sistemas multicomputador”, ofreciendo capacidad de cómputo paralela.

Para poder aprovechar estos sistemas se deben usar enfoques de programación basados en “procesamiento de datos distribuidos”:

- Los ordenadores se encuentran dispersos a lo largo de un área.
- La parte más lenta del sistema suele ser la red de comunicaciones. Procesamiento de datos en zonas de memoria privadas por nodo.
- Se debe aprovechar las capacidades de procesamiento paralelo y hardware replicado.
    - Puede haber nodos iguales (clónicos) o nodos especializados en algún tipo de función.
    - Se pueden usar nuevos enfoques para recuperación de datos ante pérdida de conectividad, fallos hardware, etc...

Además, los sistemas de procesamiento distribuido permiten conexión remota para poder ofrecer distintos servicios. En el caso de servicios ofrecidos por datacenters o sistemas tipo clúster de ordenadores en general, los clientes deben disponer de algunas métricas para comparar calidad de 
servicio. 

En un **sistema distribuido con memoria aislada**, cada nodo actúa como un sistema independiente con su propio sistema operativo y recursos locales. No existe un espacio de memoria compartido, por lo que la comunicación entre procesos se realiza mediante **técnicas de paso de mensajes**: cuando un nodo necesita información de otro, le envía una solicitud por red y recibe la respuesta correspondiente.

Esta independencia implica que cada nodo debe ser **autónomo y capaz de autogestionarse**, minimizando los accesos a la red. Si varios nodos comparten recursos (archivos, dispositivos, etc.), deben **sincronizarse** para evitar conflictos y pérdida de datos, lo que requiere **protocolos de coordinación más complejos** que los semáforos o cerrojos usados en sistemas con memoria compartida.

En este contexto surgen distintos **modelos de programación distribuida**:

- **Modelo Cliente–Servidor:** el servidor ofrece servicios o recursos, y los clientes los solicitan mediante peticiones. Es el esquema más común en redes y aplicaciones distribuidas, como servidores web o de bases de datos.
- **Modelo Maestro–Esclavo:** un nodo maestro reparte las tareas entre varios nodos esclavos, que las ejecutan y devuelven los resultados. Este modelo es típico en clústeres de computación y sistemas de procesamiento paralelo. Aunque es fácil de programar, puede generar **desequilibrios de carga**, ya que el maestro suele permanecer inactivo mientras los esclavos procesan los datos.

### **Sistemas tipo Cluster y redes de ordenadores**

Un **cluster** es un sistema de procesamiento basado en la unión de varias máquinas en red que trabajan coordinadamente para ofrecer mayor rendimiento, disponibilidad o capacidad de cómputo. Este tipo de arquitecturas se popularizó en los años 90 y 2000 en empresas, universidades y centros de investigación.

### **Factores que impulsaron su adopción**

1. **Procesadores potentes y de bajo coste:** Es fácil disponer de ordenadores con gran capacidad de cálculo sin necesidad de recurrir a supercomputadoras.
2. **Redes de alto rendimiento:** Protocolos y hardware de red mejoran constantemente, permitiendo conexiones rápidas (LAN, Infiniband, etc.) con poca inversión.
3. **Herramientas de software:** Existen soluciones de software libre que facilitan la administración de clusters por un único administrador.

---

### **Configuraciones típicas**

- **Red de alta velocidad con ficheros compartidos:** Es barato de implementar, pero el acceso a datos puede convertirse en **cuello de botella**.
- **Almacenamiento distribuido paralelo:** Sistemas complejos con múltiples discos y protocolos RAID, múltiples conexiones de red de alta velocidad, evitando cuellos de botella en lectura/escritura.

---

### **Tipos de clusters**

1. **Según propósito:**
    - **Clusters dedicados:** Hardware y recursos específicos para tareas concretas.
    - **Clusters de propósito general:** Para cualquier tarea de cómputo o almacenamiento.
2. **Según homogeneidad:**
    - **Homogéneos:** Todos los nodos son idénticos.
    - **Heterogéneos:** Combinan hardware antiguo y nuevo, reutilizando recursos o adaptándose a distintas funciones (cómputo intensivo vs almacenamiento).
3. **Ejemplos prácticos:**
    - **Granjas de render/GPUs:** Para renderizado de películas 3D, efectos visuales, simulaciones físicas.
    - **Sistemas de almacenamiento de bases de datos distribuidas:** Nodos optimizados para transmisión y almacenamiento rápido de datos.
4. **Según licencias:**
    - **Beowulf:** Hardware y software libre (licencias GNU).
    - **Propietarios:** Software con licencias privativas, hardware especializado.

**Usos destacados**

- Renderizado y simulación 3D en cine:
    - Ejemplo histórico: **Toy Story (1995)** utilizó un cluster de 53 nodos para renderizar 114.000 imágenes en 20 meses, reduciendo un trabajo que habría tardado 43 años en un solo ordenador.
    - Hoy en día, Pixar utiliza clusters con **más de 23.000 procesadores**, capaces de renderizar en tiempo real.

### **Middleware**

En sistemas distribuidos tipo **cluster**, la diversidad de hardware, sistemas operativos y librerías hace difícil desarrollar aplicaciones portables que funcionen en todos los entornos. Para resolver esto, se utilizan **capas de software intermedio**, llamadas **middleware**, que abstraen a los programas de los detalles de bajo nivel del sistema y la red.

**Funciones principales del Middleware**

1. **Uniformidad de ejecución:**
    
    Permite que aplicaciones similares se ejecuten en diferentes nodos de cómputo sin necesidad de adaptaciones específicas a cada sistema operativo o protocolo de comunicación.
    
2. **Acceso unificado a datos:**
    
    Facilita el acceso a la información distribuida entre nodos, independientemente de dónde se encuentre, similar a cómo un sistema operativo abstrae operaciones de disco a nivel de aplicación.
    
3. **Portabilidad de aplicaciones:**
    
    Aísla el “núcleo” de la aplicación del hardware subyacente, permitiendo que programas escritos en distintos lenguajes o ejecutándose en sistemas distintos se comuniquen y funcionen correctamente.
    

**Ejemplos de Middleware**

- **Librerías portables de UI y comunicaciones:**
    
    Ej. QT, que permite crear interfaces y acceder a funciones del sistema operativo de forma transparente entre Linux, Mac y Windows.
    
- **Lenguajes con máquinas virtuales o intérpretes:**
    
    Ej. Java, Python; proporcionan entornos portables, siempre que el intérprete o JVM estén instalados.
    
- **Servicios del sistema operativo:**
    
    Gestión de memoria, multiproceso, threads, sistema de ficheros y drivers que facilitan la programación sin acceder a bajo nivel.
    

**Aplicación práctica**

- En un **cliente**, el middleware traduce las operaciones de la aplicación a protocolos de comunicación de red y manejo del sistema operativo.
- En un **servidor**, recibe paquetes de datos del cliente, los interpreta y los entrega a la aplicación, incluso si el cliente y servidor usan sistemas diferentes.

## Computación en Red

La computación en red se puede definir como el conjunto de técnicas, métodos y sistemas que permiten compartir recursos de hardware, software y datos entre varias computadoras conectadas mediante una red para trabajar de manera coordinada.

### El modelo Cliente-Servidor

Los modelos “cliente-servidor” están pensados para aplicaciones con necesidades de compartición de datos y sincronización. En este caso, lo que tenemos son redes de ordenadores conectados entre sí usando un modelo “centralizado”:

- Un ordenador actúa de servidor.
- Varios ordenadores se conectan al servidor para poderse sincronizar.

![image.png](attachment:9680e8c3-c245-4123-a858-087ebf215dc5:image.png)

Bajo estos esquemas el principal cuello de botella es la comunicación con el propio servidor, ya que con demasiados clientes conectados se corre el riesgo de saturar el servidor y que no de servicios. 

Las soluciones clásicas pasan por crear nuevos servidores “clónicos” para 
dar soporte a más conexiones, pero esa solución genera nuevos problemas:

- El servidor originariamente debía dar soporte de acceso/modificación de datos (una Base de Datos por ejemplo)
- En el momento que hay demasiados usuarios, se decide añadir un segundo servidor:
    - ¿Cómo comparten la base de datos?
    - ¿Cómo se sincronizan las actualizaciones?

En el modelo de programación “cliente-servidor” podemos encontrar diversas configuraciones que se pueden adaptar a las necesidades de programas más comunes:

- **Procesamiento tipo host:** Toda la carga se encuentra en el servidor, el cliente no es más que un “terminal tonto”. Los ejemplos de estas aplicaciones suelen ser programas de tipo “control remoto”, donde el terminal de usuario recibe una señal de video y actúa como interfaz de usuario.
    - Ejemplo: Remote play, juegos “cloud”, aplicación “TeamViewer”...
- **Procesador tipo servidor:** El cliente tiene cierta capacidad de procesamiento de datos y proporciona una interfaz gráfica con las opciones a realizar al usuario. Mediante mensajes al servidor éste realiza las operaciones.
    - Ejemplo: Clientes con un navegador web (uso de javascript), acceso/procesado de datos conectados a servidores de bases de datos.
- **Procesamiento basado en cliente:**
 En este caso, casi toda la carga de proceso recae en el cliente. El 
servidor se usa para tareas de validación de datos, pero es el terminal 
del cliente el que realiza las operaciones.
    ◦ Ej: Juegos en red que necesiten de una tarjeta gráfica potente.
- **Procesamiento cooperativo (P2P):**
 En este caso, tanto los clientes como el servidor realizan parte del 
trabajo, repartiéndolo de forma equilibrada entre las estaciones.
    ◦ Ej: Una base de datos con un sistema de ficheros distribuido entre los clientes, redes bittorrent

En los esquemas “cliente-servidor” las aplicaciones implementadas suelen necesitar únicamente compartir una parte de información para sincronizar la red de programas. Sin embargo, también existen “peticiones de ejecución”, que son representadas programas tipo “servicio”. 

## Llamadas a procedimientos remotos

Las **llamadas a procedimientos remotos (RPC)** son la forma en que un programa puede **pedirle a otro ordenador que haga algo por él**, como si fuese una función normal de su propio código. Esto sirve cuando:

- El cliente no tiene suficiente capacidad de cálculo.
- La lógica de la aplicación o los datos están en otro ordenador (el servidor).

El **flujo básico** es:

1. El usuario usa la interfaz del programa en su ordenador.
2. El programa envía la petición al servidor para ejecutar un cálculo o acceder a datos.
3. El servidor ejecuta la función solicitada y devuelve el resultado.
4. El programa cliente sigue funcionando como si todo se hubiera hecho localmente.

### Programación basada en paso de mensaje

En sistemas de procesamiento distribuido para comunicar y sincronizar procesos se usan tecnicas basadas en el intercambio de mensajes. Esos mensajes suelen contener la totalida de la informacion necesaria para poder realizar algún tipo de operación. Además, suele ser necesario establecer un “protocolo” para poder traducir los mensajes enviados. Para ello, se definen dos funciones básicas:

- Send(NODE_ID, DATA): Operación que implementa los pasos necesarios para mandar un mensaje de un nodo a otro nodo de la red. Lo normal es que cada nodo tenga asignado un “identificador” para poderle mandar la información, y se le adjunta un “buffer” de datos que contenga los parámetros necesarios para ejecutar la petición.
- Receive(NODE_ID, DATA): Recepción del mensaje emitido por el nodo con el identificador indicado, y guardado en un “buffer” de datos.

Para facilitar las llamadas a estas funciones se suele usar o implementar un “middleware” orientado a paso de mensajes. Esta capa software se usaría para abstraer de los detalles de comunicación con red y pondría en contacto las aplicaciones “cliente-servidor” que se hayan implementado.

![image.png](attachment:11b1ba36-8a40-4590-a13d-3dab0fccdc73:image.png)

### Sistemas de mensajes

- **Fiables**: Garantizan que el mensaje llegue (ej. **TCP**). Usan acuses de recibo, control de errores y reordenamiento.
- **No fiables**: No garantizan la entrega (ej. **UDP**), pero son más simples y rápidos. Si quieres fiabilidad, la aplicación debe gestionarla.

### Llamadas bloqueantes vs no bloqueantes

- **Bloqueantes**: La función que envía/recibe **se detiene hasta que termina la operación**. Es simple, pero puede dejar parado al programa mientras espera.
- **No bloqueantes**: La función **devuelve el control inmediatamente**, y se usa un “recibo” o indicador de estado para comprobar cuando termina la operación. Esto permite **seguir haciendo otras cosas mientras se envía/recibe el mensaje**, aprovechando mejor el tiempo.

## LLamadas a procedimientos Remotos (RPC)

![image.png](attachment:039cb5d7-c969-4a36-b1ed-2c676a9d0126:image.png)

### Programación basada en paso de mensajes y RPC

- **Paso de mensajes:** El programa envía mensajes entre procesos o máquinas para que se ejecuten servicios de forma remota.
- **RPC (Remote Procedure Call):** Es una forma de paso de mensajes que **oculta la complejidad de la red**. Para el programador, llamar a un RPC es **igual que llamar a una función local**.

### Ventajas de las RPC

1. **Interfaces claras:** Se definen operaciones con nombres y tipos de datos, facilitando documentación y validación de errores.
2. **Código automático y portable:** A partir de la interfaz, se puede generar el código de comunicación cliente/servidor y reutilizarlo en distintas arquitecturas.

### Objetivo principal

- Separar la **interfaz de usuario del núcleo de la aplicación**.
- Transformar una llamada local a función en una **llamada remota**, empaquetando datos, enviándolos y recibiendo resultados.
- Permite que la aplicación sea distribuida en red sin que el cliente necesite saber dónde se ejecutan realmente los servicios.

💡 **Idea clave:** RPC = “función normal que se ejecuta en otro ordenador, sin que el programador tenga que preocuparse de la red”.