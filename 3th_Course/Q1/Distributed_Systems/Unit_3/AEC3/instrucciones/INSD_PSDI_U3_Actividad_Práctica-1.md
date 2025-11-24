![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.001.png)![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.002.png)

**UNIDAD 3 \
![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.003.png)ACTIVIDAD PRÁCTICA      OBJETOS REMOTOS Y RPC** 

**Centro adscrito a ![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.004.png)![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.005.png)![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.006.png)**

Centro adscrito a ![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.007.png)![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.008.png)![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.009.png)

**ÍNDICE** 

[ORGANIZACIÓN DE LA ACTIVIDAD PRÁCTICA................................................................................ 3 ](#_page2_x54.00_y86.00)[DESCRIPCIÓN DE LA ACTIVIDAD PRÁCTICA ................................................................................... 3 ](#_page2_x54.00_y261.00)

[File Manager ....................................................................................................................................................................3 ](#_page2_x54.00_y477.00)[Proyecto CMake ...............................................................................................................................................................5 ](#_page4_x54.00_y108.00)[Implementación pedida ...................................................................................................................................................5 ](#_page4_x54.00_y290.00)[Proyecto “Broker de objetos FileManager”.....................................................................................................................6 ](#_page5_x54.00_y282.00)

[RECOMENDACIONES E INDICACIONES PARA LA ENTREGA ............................................................. 7 ](#_page6_x54.00_y137.00)[RÚBRICA DE CORRECCIÓN .......................................................................................................... 7 ](#_page6_x54.00_y323.00)[COMO REALIZAR LA ENTREGA ..................................................................................................... 8 ](#_page7_x54.00_y652.00)

<a name="_page2_x54.00_y86.00"></a>**ORGANIZACIÓN DE LA ACTIVIDAD PRÁCTICA** 

**Nombre de la práctica ![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.010.png)**

**Tipo de tarea**  Individual

**Entregables**  Proyecto de Linux/CMake  

Documento con imágenes de ejemplos de ejecución con varios Servidores, Clientes y Broker (según proceda)  

<a name="_page2_x54.00_y261.00"></a>**DESCRIPCIÓN DE LA ACTIVIDAD PRÁCTICA** 

En  esta  práctica  se  pretende  enseñar  una  forma  de  invocación  remota  de  funciones aprovechando interfaces de programación proporcionadas por objetos. Para ello se proporciona un programa monousuario ya implementado, el cual se pretende convertir en un programa distribuido con partes de código gestionadas por programas de tipo servidor 

En  concreto,  el  objetivo  del  alumno  debe  ser  mantener  en  la  medida  de  lo  posible  el funcionamiento  original del  código  proporcionado. Sólo  debe preocuparse  de  implementar  las llamadas a procedimientos remotos (RPC), para lo cual debe implementar las clases vistas en los ejemplos de la Unidad 3.  

<a name="_page2_x54.00_y477.00"></a>*File Manager* 

A  través  de  Blackboard  (Carpeta  Programas  Acceso  Remoto)  se  proporciona  el  programa “FileManager” ya implementado (Archivo “P2FileManager.zip) . Este programa sirve para listar los archivos  de  un  directorio  local  llamado  “FileManagerDir”,  y  realizar  funciones  básicas  de lectura/escritura sobre ellos. Está compuesto por los siguientes archivos: 

**Main\_fm.cpp:** 

Programa principal de prueba. Inicia una clase de tipo “fileManager” y ofrece un terminal para escribir comandos. Existen los siguientes comandos:  

- **ls**: Lista los ficheros locales al programa principal
- **lls**: lista los ficheros locales a la clase “fileManager”. Serán los ficheros que se encuentren en el directorio pasado por parámetros al constructor de esa clase. 
- **upload  <nombre  de  archivo  local>**:  Este  comando  copia  un  archivo  local  al  ejecutable (listado  por  “ls”)  al  directorio  local  a  la  clase  fileManager  (en  este  caso,  el  directorio “FileManagerDir”).  
- EJ: 
- Si se ejecuta el siguiente comando, se copiará el archivo “a.txt” al directorio local a FileManagerDir.  
- "upload a.txt” 
- **download <nombre de archivo remoto>**: Este comando copia un archivo local a la clase fileManager  (el  directorio  pasado  por  parámetros  al  constructor,  FileManagerDir)  al directorio local del ejecutable.  Usa el parámetro “nombre del archivo remoto”, que se encuentra en el directorio local a fileManager.  
  - EJ: 
  - Si se ejecuta el siguiente comando, se copiará el archivo “a.txt” al directorio local al ejecutable. 
  - "download a.txt” 
- **exit()**: Este comando cierra la terminal y acaba la ejecución del programa.  

**fileManager.h:**  

Esta  clase  implementa  las  funciones  de  administración  de  archivos  sobre  un  directorio  pasado  por parámetros al constrocutor. Estas funciones son: listado de un directorio local al ejecutable que contenga esta clase, lectura de un fichero en ese directorio, y  escritura de archivos en ese directorio.  Tiene las siguientes funciones: 

- **Constructores “fileManager”:**  Hay un constructor por defecto sin parámetros y un constructor con un parámetro que representa el nombre del directorio que debe administrar esta clase. En caso de usar el constructor por defecto, o de usar un nombre de directorio no válido, el resto de los métodos de la clase mostrarán por terminal un error de uso. 
- **ListFiles** : Devuelve un vector con los nombres de los ficheros encontrados en el directorio local. OJO, no es una lista dinámica, no se actualiza automáticamente si se modifican los archivos. Si se escriben/crean nuevos ficheros no se añadirán automáticamente, hay que volver a invocar la función para obtener la lista actualizada. 
- **ReadFile**: Si se le pasa el nombre de uno de los ficheros encontrados en el directorio (lista devuelta por “ListFiles”), leerá su tamaño y contenido. Lo almacenará en las variables pasadas por parámetros. 
- **WriteFile**: Análoga al anterior, escribirá el contenido fichero en el directorio local. Si el fichero no existía en el directorio, se añadirá a la lista de ficheros (hay que volver a llamar a “ListFiles” si se quiere mantener la lista actualizada). 

**LibFileManager.a:**  

Este archivo contiene la implementación de la clase mencionada anteriormente. Ya está compilado y el proyecto “CMakeLists.txt” está preparado para enlazarlo con el ejecutable. 

EL ALUMNO NO DEBE MODIFICAR NINGUNO DE LOS ARCHIVOS DESCRITOS ANTERIORMENTE. TAMPOCO DEBE CREAR UNA IMPLEMENTACIÓN DE LA CLASE FILEMANAGER QUE LEA/ESCRIBA/LISTE ARCHIVOS. ESO YA ESTÁ IMPLEMENTADO EN EL ARCHIVO LIBFILEMANAGER.A, SÓLO DEBE CENTRARSE EN INVOCAR LAS FUNCIONES DE LA CLASE DESDE UN PROGRAMA CLIENTE EN UN PROGRAMA SERVIDOR. 

<a name="_page4_x54.00_y108.00"></a>*Proyecto CMake* 

Se  proporciona  un  proyecto  cmake  ya  preparado  para  compilar  los  programas  para  esta  práctica.  En concreto, cuando se genere el proyecto y se compile, generará los siguientes programas: 

- FileManager: El programa original descrito anteriormente. Este programa se usa para mostrar la funcionalidad que debería tener el programa final distribuido. 
- Client: Programa vació, el alumno debe modificar este proyecto añadiendo los archivos necesarios para implementar las funcionalidades del cliente. En concreto, debe usar la interfaz de usuario proporcionada por en el programa original “fileManager”. 
- Server: Programa vació, el alumno debe modificar este proyecto con los archivos necesarios para implementar un servidor que gestione accesos a la librería “fileManager.a” 

<a name="_page4_x54.00_y290.00"></a>*Implementación pedida*  

El alumno debe distribuir el objeto “FileManager” entre varios servidores, y debe crear una interfaz de programación para que el programa “main” original acceda a los métodos de la clase distribuida sin cambiar el código original. Para ello, se pide lo siguiente: 

- Programa “cliente”: 
- Debe usar el archivo “main\_fm.cpp” como interfaz de usuario. Está prohibido cambiar o modificar este archivo, ya que es el que contiene la funcionalidad original para el modo de uso del programa. 
- Debe usar el archivo “fileManager.h” como interfaz de la clase FileManager. Dado que el programa “main” usa esta clase a través de esta interfaz, igualmente está prohibido realizar cambios en este archivo. 
- No debe usar el archivo “libFileManager.a”. En vez de este archivo, se debe crear un archivo nuevo llamado “**fileManagerRemoto**.**cpp**”. Este nuevo archivo implementará los métodos del archivo “fileManager.h”, transformando cada uno de ellos en llamadas RPC para invocar sus análogos en el servidor. En concreto se pide lo siguiente: 
  - Constructores:  Deben  iniciar  una  conexión  con  un  programa  Servidor  de  clases FileManager. El servidor tendrá una instancia de la clase FileManager en la que invocará las peticiones del cliente. 
  - Destructores: Cierran de forma segura la conexión con el servidor, pidiéndole que destruya las instancias de FileManager creadas en las llamadas de los constructores. 
  - Resto  de  métodos  de  clase:  Deben  ser  llamadas  a  procedimiento  remoto, empaquetando/desempaquetando y enviando/recibiendo los datos necesarios para que se invoquen en el servidor los métodos pedidos, y retornando las variables con los datos resultado.  
- Archivo “clientManager.h”: Como se vio en los ejemplos de la unidad 3, esta clase es usada para almacenar los datos de conexión del cliente. 
- Archivos “utils.h” y “utils.cpp”, para conexiones. 
- Programa “servidor”: 
- Archivo “server.cpp”: Contiene el programa main, y su trabajo es esperar a conexiones de clientes. Por cada conexión, se crea un hilo de ejecución paralela para atender las peticiones de ejecución de los programas “cliente” a través de la clase “clientManager”. Se puede usar el mismo visto en los ejemplos de clase. 
- Archivos  “clientManager.h/.cpp”:  Se  pueden  reutilizar  los  mismos  de  clase,  pero adaptándolos a la clase “FileManager”. En concreto, esta clase debe implementar el método “attendClient”  para  poder  recibir  peticiones  de  ejecución  sobre  instancias  de  la  clase “FileManager”. 
- Archivos “FileManager.h/.a”: Son la implementación original de la clase “FileManager”. El servidor contendrá instancias de esta clase, y llamará a sus funciones según lo pida el cliente a  través  de  llamadas  RPC.  En  concreto,  la  clase  “clientManager”  deberña  recibir  las peticiones del cliente para ejecutar los métodos de la clase “FileManager” impementados en los archivos “FileManager.h” y “FileManager.a”. 

<a name="_page5_x54.00_y282.00"></a>*Proyecto “Broker de objetos FileManager”* 

Además de lo anterior, se pide crear un sistema “Broker de objetos” para encontrar servicios  de tipo FileManager y balancear conexiones. Este programa sólo es obligatorio para sacar una nota máxima de 10 en la práctica, el mínimo que se pide es la implementación de cliente-servidor mediante llamadas RPC. El programa Broker actuará de la siguiente manera:  

- Los programas de tipo servidor de fileManager pueden encontrarse en un ordenador desconocido, por lo que el cliente necesitaría un sistema de búsqueda de servicios. Además, para equilibrar las conexiones entre varios ordenadores, puede haber varias instancias del programa servidor en el sistema.  
- Para poder solucionar estos problemas, se pide crear un programa tipo Servidor que funcionará como “Broker de objetos”, el cual tendrá la siguiente operación:  
  - Esperará a que se conecten programas clientes o servidor de fileManager:  
    - Si se conecta un servidor, se deberá identificar con si IP y el Broker lo almacenará  
    - Si se conecta un cliente, se le devolverá una IP almacenada de alguno de los servidores conectados anteriormente, y se apuntará esa conexión. Cada nuevo cliente que se conecte se le intentará dar el servidor con menos conexiones.  
  - Los programas cliente/servidor funcionarán de la siguiente manera:  
    - Programa servidor: Inicia una conexión con el broker y le envía su IP de red pública o privada. A continuación, queda esperando conexiones normales de clientes.  
    - Programa cliente: Antes de iniciar una conexión con el servidor, conectará con el Broker para pedirle una IP de algún servidor que esté encendido.  

Ambos programas cliente/servidor pueden conocer tanto su propia IP como la del Broker. Sin embargo, el cliente no conoce las IPs de los servidores y viceversa. El cliente sólo conoce al servidor si se lo da el Broker. 

Una vez el cliente recibe los datos de los servidores a través del broker, cierra su conexión con él y realiza todas las peticiones conectando directamente con los servidores. Las peticiones de creación, listado, etc... de FileManager no pasan por el programa Broker, ya que eso haría que las operaciones fueran muy lentas.  

Para poder probar esta parte se pide crear dos máquinas más. En total se deberían tener tres máquinas:  

- Dos para el servidor de fileManager 
- Una para el programa Broker. 

El programa cliente se puede ejecutar en cualquiera de las tres (o incluso el propio ordenador del alumno, fuera de la red de AWS/EC2), su único requisito es que tenga conexión con ellas y que sea el programa Broker el que le dé los datos de conexión de los servidores.  

<a name="_page6_x54.00_y137.00"></a>**RECOMENDACIONES E INDICACIONES PARA LA ENTREGA** 

Ante  cualquier  duda,  hablad  con  el  profesor  para  que  os  indique  la  mejor  manera  de implementar los programas pedidos. El alumno **NO DEBE** modificar los archivos “main\_fm.cpp”, “fileManager.h” y “libFileManager.a”. **TAMPOCO DEBE** crear código que liste ficheros, abra/escriba ficheros, etc... esa funcionalidad ya está implementada en la librería FileManager.  

**EL ALUMNO SOLO DEBE** crear las clases necesarias para implementar llamadas RPC desde el programa “main\_fm.cpp” a la librería libFileManager, que se encuentra en ordenadores distintos a los del cliente. Para ello, puede usar el código visto en clase, en concreto los archivos “server.cpp”, “clientManager.h/.cpp”. 

<a name="_page6_x54.00_y323.00"></a>**RÚBRICA DE CORRECCIÓN** 

La rúbrica para corregir el  ejercicio seguirá los criterios listados a continuación, que tienen distintos pesos respecto al total de la nota. 

**Criterios**  **Excelente**  **Satisfactorio**  **No satisfactorio**  **Insuficiente** ![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.011.png)![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.012.png)

Implementaci De 4.5 a 6 puntos  De 3 a 4.5 puntos  De  1.5  a  3  puntos  De  0  a  1.5 ón cliente- posibles  posibles  posibles   puntos servidor RPC Se han  Se  han  seguido  Se han seguido algunas  posibles (Máximo 6  implementado las  las directrices de  de las directrices dadas  El alumno no puntos) funciones pedidas y  desarrollo  para el desarrollo de la  ha creado las 

aparentemente  dadas,  pero  práctica.  funcionalida funciona todo.  algunas  No  se  ha  llegado  a  des  pedidas. Razones por no  funcionalidades  implementar  ninguna  No ha creado conseguir nota  (lls,  de  las  funcionalidades  las  clases máxima:  upload/downloa del programa original:  pedidas.

- Servidor no  d)  no  funcionan  -  No  lista  El  proyecto soporta  correctamente  archivos  en  no  sigue  las varias  -  El  cliente  directorios  indicaciones conexiones  llega  a  remotos  (no  dadas  para sucesivas de  conectar  funciona  su 

  clientes  con  el  comando lls)  desarrollo. 

- Errores  servidor  -  No  lee/escribe  Tiene menores en  y  realiza  en  directorios  problemas implementa alguna de  remotos  (  de 

  ción.  las  nofunciona  compilación 

- Errores  funcione comandos  y  no  realiza aleatorios  s  de  lo pedido 

  (mala  fileMana “upload/downl![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.013.png)![](Aspose.Words.826af8e6-af57-4693-8161-9b7f5d9342c5.014.png)

  gestión de  ger:  oad” 

  procesos o  -  Listfiles, 

  memoria)  writeFile 

o 

ReadFile 

Implementaci De  3  a  4  puntos  De 2 a 3 puntos  De  1  a  2  puntos  De  0  a  1 ón programa  posibles  posibles  posibles  puntos Broker  El  Broker  funciona  Clientes  y  Tanto  clientes  como  posibles (máximo 4  sin  problemas  y  Servidores  servidores  conectan  No  llegan  a puntos) gestiona  tanto  los  conectan  con  el  con el Broker, pero no  conectarse ni 

servidores  Broker,  y  luego  llega  a  funcionar  el  clientes  ni encendidos  como  un cliente puede  programa  servidores los  que  se  apagan.  conectar  al  con el broker Los  Servidor  con  los 

clientes/servidores  datos  recibidos 

funcionan  con  del broker.  

normalidad después 

de  haberse  No  se  ha 

desconectado  del  implementado 

broker. toda  la 

funcionalidad 

pedida: 

- Gestión 

  de  varios 

  servidore

  s 

- Gestión 

  de  varios 

  clientes 

- Gestión 

  para 

  seleccion

  ar  el 

  servidor 

  menos 

  cargado 

<a name="_page7_x54.00_y652.00"></a>**COMO REALIZAR LA ENTREGA** 

El alumno deberá entregar un archivo ZIP nombrado como “P2SISDISD\_Nombre\_Apellido.zip” y con el siguiente contenido: 

- Proyecto CMAKE con la solución a los ejercicios indicados. Sólo es necesario entregar el código fuente (archivos “.h”, “.cpp”, “.a” y archivo CMakeLists.txt” 
- Documento (docx o pdf) con capturas de pantalla que muestren la correcta ejecución de los programas. No es necesario realizar un documento con descripciones muy complejas, sólo lo suficiente para demostrar las funcionalidades implementadas: 
  - Ejecución con un servidor y dos clientes, donde se muestre que los clientes pueden ejecutar los comandos “lls”, “upload” , “download” y “exit()”. Se debe mostrar que  se  actualiza  el  directorio  “FileManagerDir”  que  se  encuentra  gestionado  por  el servidor. 
  - Ejecución  con  programa  Broker  (en caso  de  implementarlo):  Mostrar  que  se  ha lanzado  un  programa  “Broker”  y  dos  programas  “Server”  en  3  instancias  EC2 distintas. Mostrar cómo varios clientes se conectan al sistema a la vez, y mediante los  comandos  “lls”,  “upload/download”  se  actualizan  los  directorios “FileManagerDir” que se encuentran en distintas instancias EC2 donde están esos programas  “server”.  Dado  que  el  programa  broker  devuelve  datos  de  conexión distintos  a  cada  cliente,  los  contenidos  finales  de  sus  respectivos  directorios “FileManagerDir” deberían ser distintos. 
- No se debe entregar el directorio “bin” que contiene los archivos compilados y ejecutables. 
9
