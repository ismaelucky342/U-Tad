# Unidad 1 

# Introducción a las Bases de Datos

Una base de datos es un conjunto de datos almacenados en memoria externa que están organizados mediante una estructura de datos. Cada base de datos ha sido diseñada para satisfacer los requisitos de información de una empresa u otro tipo de organización, como, por ejemplo, una universidad o un colegio.  Antes de la aparición de las bases de datos se trabajaba con sistemas de ficheros, creados a partir de la digitalización de archivadores y documento físicos (papel), de forma que, con dichos sistemas de ficheros digitales, los accesos a los datos fueran más eficientes.

- **Modelos descentralizados,** donde cada departamento o área de una empresa u organización, almacena y gestiona sus propios datos mediante, programas/aplicaciones o scripts, escritos específicamente para realizar determinadas tareas sobre los datos del área almacenados.
- Los programas, el almacenamiento y la gestión de los datos **son independientes** en cada departamento y por tanto no hay compartición de aplicaciones y datos entre departamentos o bien es muy limitada.
- Este modelo genera **inconsistencias** de los datos, **incoherencias, duplicidades,** …
- En la gestión de datos sobre un sistema de ficheros, también **se complica la sincronización de los datos,** cuando estos están repartidos en varios ficheros.
- Cuando se genera un cambio en la estructura física de almacenamiento, todas las aplicaciones realizadas sobre esta estructura de ficheros deben de ser actualizadas y probadas de nuevo (Coste y Tiempo). Este punto vislumbra la **no dependencia entre la estructura lógica de los datos y la estructura física de almacenamiento.**

Una base de datos es un gran almacén de datos (datos de todos los departamentos de la organización) que se define en su creación, se almacenan los datos con mínima duplicidad y que es explotada por diferentes usuarios que pertenecerán a los distintos departamentos de la empresa. Las bases de datos permiten compartir la información de la empresa entre los diferentes departamentos y también almacena lo que se conoce como **“metadatos”** que describen un diccionario o catálogo que hace que exista una independencia entre la definición lógica de la base de datos y la estructura física de almacenamiento de la misma, cosa que en los sistemas de ficheros no se podía conseguir.

```agda
📌 Antes de las bases de datos:
Se usaban sistemas de ficheros, similares a archivadores digitales.
Cada departamento almacenaba y gestionaba sus datos por separado.
No había compartición eficiente de datos entre departamentos.

📌 Problemas de los sistemas de ficheros:
Duplicidad e incoherencia de datos entre departamentos.
Dificultad en la sincronización cuando los datos estaban en varios ficheros.
Alto coste de mantenimiento: Un cambio en la estructura obligaba a modificar todas las aplicaciones relacionadas.

📌 Ventajas de las bases de datos:
Un único almacén centralizado de datos con mínima duplicidad.
Compartición de información entre los departamentos.
Uso de metadatos para independencia entre la estructura lógica y física.
```

### Sistema gestor de bases de datos

El sistema gestor de base de datos (**SGBD** o **DBMS**: DataBase Management System) es una aplicación que permite a los usuarios:

- Definir, crear y mantener la base de datos, así como proporcionar un acceso controlado a dicha base de datos.
- También proporciona una especificación externa de los objetos de la base de datos a los usuarios, de forma que estos no se deben de preocupar de cómo se implementa internamente el objeto al que acceden.

Los sistemas de bases de datos separan la definición de la estructura física de los datos de su estructura lógica, y almacenan esta definición en la base de datos.  Para tener esta independencia se apoyan en los SGBD, que se sitúan entre la base de datos y los programas de aplicación o aplicaciones.

![image.png](attachment:ea2c9d7c-7723-45b8-bc96-b303121bd39e:image.png)

Este modelo, conocido como abstracción de datos, permite cambiar la implementación interna de un objeto de la base de datos sin afectar a sus usuarios (procesos, programas/aplicaciones) ya que la especificación externa, la visible por los usuarios, no se ve alterada.

**Los SGBD ofrecen diversas facilidades a los usuarios**

- Proporciona  mediante un sistema de seguridad, de modo que los usuarios no autorizados no puedan acceder a la base de datos.
    
    un acceso controlado a la base de datos
    
- Un  accesible por el usuario, que contiene la descripción de los datos de la base de datos.
    
    diccionario de datos o catálogo,
    
- Ofrecen  de forma que los usuarios responsables, puedan conocer en todo momento el estado de las mismas. Esto es muy importante ya que muchas bases de datos son críticas para determinados negocios y/o aplicaciones.
    
    sistemas en tiempo real de monitorización y rendimiento sobre las bases de datos
    
- Un  que mantiene la integridad y la consistencia de los datos.
    
    sistema de integridad
    
- Proporcionan un  que permite que cada usuario tenga su propia vista o visión de la base de datos para preservar las restricciones de acceso a los datos.
    
    mecanismo de vistas
    
- Un  que permite el acceso compartido a la base de datos.
    
    sistema de control de concurrencia
    
- Un  que restablece la base de datos después de que se produzca un fallo del hardware o del software.
    
    sistema de control de recuperación
    
- El SGBD permite la definición de la base de datos mediante un lenguaje de definición de datos **(LDD-Lenguaje de Definición de Datos - DDL Data Definition Language)**. Este lenguaje permite especificar la estructura y el tipo de los datos, así como las restricciones sobre los datos.
- El SGBD permite la inserción, actualización, eliminación y consulta de datos mediante un lenguaje de manejo de datos (LMD – Lenguaje Manipulación de Datos – DML Data Manipulation Language).

```agda
📌 ¿Qué es un SGBD?
Un Sistema Gestor de Bases de Datos (SGBD) es una aplicación que permite definir, crear, gestionar y controlar el acceso
a una base de datos.

📌 Ventajas y funciones clave:
✅ Independencia entre la estructura física y lógica de los datos.
✅ Acceso controlado y seguridad para evitar accesos no autorizados.
✅ Diccionario de datos que describe la estructura de la base de datos.
✅ Monitorización en tiempo real para garantizar el rendimiento.
✅ Mecanismos de integridad para mantener datos consistentes.
✅ Vistas personalizadas según permisos de los usuarios.
✅ Control de concurrencia para acceso simultáneo seguro.
✅ Recuperación ante fallos de hardware o software.

📌 Lenguajes utilizados en SGBD:
LDD (DDL - Data Definition Language) → Define estructura de datos.
LMD (DML - Data Manipulation Language) → Permite insertar, actualizar y eliminar datos.
```

**Ejemplo 1 (LDD):**

```sql
**CREATE TABLE Empleados (**

**ID int,**

**Apellidos varchar(255),**

**Nombre varchar(255),**

**Direccion varchar(255),**

**);**
```

**Ejemplo 2 (LMD):**

```sql
**SELECT CodProducto, Producto FROM Productos;**
```

### Perfiles de usuarios que interactuan con bases de datos

Podemos establecer cuatro grandes grupos de perfiles que intervienen en este entorno:

**El administrador**

- Selecciona los servidores hardware sobre los que la base de datos se ejecutará o si hablamos de un entorno Cloud, que capacidades (procesamiento, almacenamiento, memoria,….) van a ser necesarias en función de volumen de datos, usuarios, tiempos de respuesta,…..
- Decide acerca del almacenamiento físico de la base de datos (tipos de los ficheros de datos y de los índices que deben crearse, sistema de almacenamiento más adecuado, dónde deben ubicarse ficheros e índices,…)
- Configura la política de seguridad y del acceso concurrente.
- Proporciona los permisos y privilegios adecuado a cada usuario de la base de datos.
- Se debe preocupar de que el sistema se encuentre siempre operativo y proveer de los medios necesarios para que usuarios y aplicaciones obtengan buenas prestaciones.

**Los diseñadores de la base de datos**

- Realizan el diseño de la base de datos, debiendo identificar los datos, las relaciones entre ellos y las restricciones sobre los datos y sobre sus relaciones.
- Este perfil debe tener un profundo conocimiento de los datos de la empresa y también debe conocer sus reglas de negocio. Las reglas de negocio describen las características principales sobre el comportamiento de los datos en el contexto de la organización.
- El trabajo del diseño de la base de datos, no lo realiza de forma independiente, sino que debe implicar a todos los usuarios de la base de datos para conocer la explotación de la base de datos que van a llevar a cabo.

**Los programadores de aplicaciones**

- Roles que se encargan de codificar las aplicaciones que servirán a los usuarios finales.
- Estos programas permiten consultar datos, insertarlos, actualizarlos y eliminarlos.

**Los usuarios**

- Los usuarios finales, son los clientes de la base de datos, es decir son las personas de la organización que van a explotar y trabajar con los datos de la misma.
- Analistas de datos, científicos de datos, comerciales, contables,…..
- Normalmente para la explotación de los datos se lleva a cabo mediante herramientas que se conectan a la base de datos como Power BI, Tableau, MicroStrategy, …. que proporcionan entornos gráficos con gran cantidad de funcionalidades

```agda
📌 1. Administrador de la Base de Datos (DBA)
👨‍💻 Gestiona la infraestructura, almacenamiento, seguridad y acceso concurrente.
✅️ Selecciona hardware/Cloud.
✅️ Configura seguridad y permisos.
✅️ Mantiene el sistema operativo y optimizado.

📌 2. Diseñadores de la Base de Datos
📊 Diseñan la estructura de la base de datos.
✅️ Identifican datos, relaciones y restricciones.
✅️ Conocen las reglas de negocio de la organización.
✅️ Colaboran con los usuarios para optimizar el diseño.

📌 3. Programadores de Aplicaciones
💻 Desarrollan software que interactúa con la base de datos.
✅️ Codifican consultas, inserciones, actualizaciones y eliminaciones.

📌 4. Usuarios Finales
📈 Utilizan los datos en su trabajo diario.
✅️ Perfiles: analistas, científicos de datos, comerciales, contables…
✅️ Usan herramientas como Power BI, Tableau, MicroStrategy.
```

## Niveles de Abstracción de una base de datos

Para que el sistema gestor de base de datos (SGBD) sea útil debe recuperar los datos de manera **eficiente** y como muchos usuarios de que utilizan las bases de datos no están familiarizados con el manejo de equipos informáticos y/o los interfaces ofrecidos por los SGBD, se esconde a los usuarios la complejidad de acceso a los datos a través de varios niveles de abstracción.

Se simplifica la estructura en **tres niveles de abstracción:**

**Nivel físico**

- El nivel más bajo de abstracción describe cómo se almacenan los datos. En el nivel físico se describen en detalle las estructuras de datos complejas de bajo nivel.
- En este nivel, un registro de cliente, cuenta o empleado se puede describir como un bloque de posiciones almacenadas consecutivamente (por ejemplo, palabras o bytes).
- Los SGBD ocultan detalles de almacenamiento de nivel inferior a los programadores de bases de datos. Los administradores de bases de datos normalmente si tienen conocimientos de la organización física de los datos, pero hasta cierto detalle.

**Nivel lógico**

- En este nivel se describen qué datos se almacenan en la base de datos y qué relaciones existen entre esos datos.
- En el nivel lógico, cada registro atiende a un determinado tipo y se define la relación entre estos tipos de registros.
- Este es el nivel donde los programadores o desarrolladores de aplicaciones trabajan y los administradores realizar las actividades de administración propias de su role

**Nivel de vistas**

- Los usuarios normalmente, por diversos motivos, no necesitan acceder a toda la base de datos, por este motivo se define este nivel de abstracción, basado en vistas, donde se ofrece al usuario los datos que necesita y así, además, se simplifica la interacción con el SGBD.
- Los usuarios ven única y exclusivamente las vistas a las que tiene acceso.
- Además de esconder detalles del nivel lógico de la base de datos, las vistas también proporcionan un mecanismo de seguridad para evitar que los usuarios accedan a ciertas partes de la base de datos.

*“Empleados de un banco que tienen acceso a la información de las cuentas de los clientes, pero no tienen acceso a las hipotecas y préstamos de los clientes”*

![image.png](attachment:94b5cad4-7ce1-4c99-8248-1d96579b277f:image.png)

```agda
Para ocultar la complejidad y facilitar el acceso a los datos, los SGBD utilizan tres niveles de abstracción:

📌 1. Nivel Físico 🖴
📌 Cómo se almacenan los datos en disco.
✅️ Describe estructuras de bajo nivel (bloques, bytes).
✅️ Solo los administradores suelen conocer estos detalles.

📌 2. Nivel Lógico 🛠️
📌 Qué datos existen y cómo se relacionan.
✅️ Define registros y relaciones.
✅️ Usado por programadores y administradores.

📌 3. Nivel de Vistas 👀
📌 Qué información ve cada usuario.
✅️ Muestra solo los datos necesarios.
✅️ Mejora la seguridad ocultando información sensible.

💡 Ejemplo: Empleados de un banco pueden ver cuentas de clientes, pero no hipotecas.
```

# Conceptos generales de las Bases de Datos Relacionales

## Modelos de Datos

Bajo la estructura de las bases de datos se encuentra el modelo de datos que describen los datos, relaciones, semántica, restricciones,…. de la base de datos. Los modelos de datos ofrecen un modo de describir el diseño de las bases de datos en los niveles físico, lógico y de vistas. Vamos a ver a continuación los 3 modelos de datos más relevantes:

**Modelo relacional**

- Modelo que usa un conjunto de tablas para representar tanto los datos como sus relaciones.
- Cada tabla tiene varias columnas, y cada columna tiene un nombre único.
- Es un modelo basado en registros almacenados en una tabla.
- Cada registro contiene un número fijo de campos, o atributos (Columnas).
- Es el modelo de datos más ampliamente usado y una gran mayoría de sistemas de bases de datos actuales se basan en el modelo relacional (MySQL está basada en este modelo de datos y será la que veremos durante el curso, exceptuando la última unidad)

**Modelo de datos entidad-relación**

- El modelo de datos E/R consiste en una colección de objetos básicos, denominados entidades, y de las relaciones entre ellos.
- Es una colección de objetos están asociados al mundo real.
- Como extensión del modelo E/R se puede considerar el modelo orientado a objetos.
- Este modelo se considera visto en el curso pasado por lo que no se hará profundizará en el mismo en este curso

**Modelo de datos semiestructurados**

- El modelo de datos semiestructurados permite la especificación de datos donde los elementos de datos individuales del mismo tipo pueden tener **diferentes** conjuntos de atributos, pero no tienen un esquema definido.
- Los datos de este modelo no encajan en tablas/filas/columnas y se organizan mediante etiquetas (tags) que permiten la agrupación y la creación de jerarquías.
- Normalmente el **lenguaje de marcas extensible** (XML, eXtensible Markup Language) y tipos específicos de este, se utiliza para representar este modelo de datos semiestructurados.

1. El modelo de datos semiestructurados permite la especificación de datos donde los elementos de datos individuales del mismo tipo pueden tener **diferentes** conjuntos de atributos, pero no tienen un esquema definido.

2. Los datos de este modelo no encajan en tablas/filas/columnas y se organizan mediante etiquetas (tags) que permiten la agrupación y la creación de jerarquías.

3. Normalmente el **lenguaje de marcas extensible** (XML, eXtensible Markup Language) y tipos específicos de este, se utiliza para representar este modelo de datos semiestructurados.

Existen otros modelos, como el **modelo de datos en red,** o **modelo de datos jerárquicos,** que no se va a profundizar en ellos, porque se consideran base inicial del modelo relacional.

```agda
Los modelos de datos describen cómo se organizan y relacionan los datos en una base de datos. Los tres modelos principales son:

📌 1.Modelo Relacional 📊
📌 Organiza los datos en tablas con filas y columnas.
✅️ Cada tabla representa una entidad con atributos.
✅️ Es el modelo más utilizado (Ej: MySQL).

📌 2.Modelo Entidad-Relación (E/R) 🔗
📌 Usa entidades y relaciones para representar datos del mundo real.
✅️ Representa datos como objetos y sus conexiones.
✅️ Es la base del diseño de bases de datos relacionales.

📌 3.Modelo Semiestructurado 🏷️
📌 No sigue un esquema rígido de tablas.
✅️ Los datos se representan en formatos como XML.
✅️ Se organiza en jerarquías con etiquetas (tags).

💡 Otros modelos:
📌 Modelo en Red 🌐 y Modelo Jerárquico 🌲, precursores del modelo relacional.
```

## Arquitectura de una Base de Datos

La arquitectura de las bases de datos SGBD tiene dependencia sobre las caracterícas HW y el sistema operativo sobre el que se vaya a ejecutar el sistema de base de datos, no es lo mismo si la base de datos se ejecuta en uan arquitectura centralizada o bien en una arquitectura distribuida en la cual los servidores estan distribuidos geográficamente y deben asegurar la atomicidad de las transacciones con controles y disponibilidad ante dallos en la DB. 

Así, tendremos dos tipos de arquitecturas:

**Arquitectura de dos capas (o niveles)**

- Es una arquitectura cliente-servidor, donde existe una capa o nivel de presentación (cliente o usuario con interfaz de presentación gráfica) y otra capa de datos.
- La lógica de negocio (algoritmos) pueden ejecutarse en la capa de presentación, en la capa de datos, o bien en ambas.
- Suelen ser utilizados los estándares de interfaces de programas de aplicación, como ODBC y JDBC para la interacción entre el cliente y el servidor.
- Sigue siendo utilizada por determinados sistemas o aplicaciones por herencia del pasado. Esta arquitectura no se utiliza para aplicaciones modernas.

![image.png](attachment:6388a71f-6ae5-4695-9fc5-1e9161efa39a:image.png)

**Arquitectura tres capas (o niveles)
–**

- No existe una llamada directa entre la capa de presentación y la capa de datos.
- El nivel de presentación o interfaz de usuario. El usuario final interactúa con la aplicación.
- El nivel de aplicación, donde se procesan los datos y se encuentra toda la lógica de negocio ejecutada sobre un servidor de aplicaciones. En este nivel, la información recopilada en el nivel de presentación se procesa, a veces contra otra información en el nivel de datos. El nivel de aplicación también puede añadir, suprimir o modificar datos en el nivel de datos. En esta capa la lógica de negocio normalmente se desarrolla utilizando lenguajes de alto nivel, como Python, Java, PHP,Ruby,…. y se comunica con el nivel de datos mediante llamadas API.
- El nivel de datos, donde se almacenan y gestionan los datos asociados con la aplicación.
- Cada una de las tres capas se ejecuta en su propia infraestructura, por lo que su evolución, disponibilidad y despliegue es independiente siempre que se cumplan los criterios de compatibilidad con el resto de elementos de la arquitectura.
- Este tipo de arquitectura es ampliamente utilizado, sobre todo para aplicaciones web **utilizando tecnologías nativa de la nube como contenedores y microservicios** así como en las migraciones hacia cloud públicas o privadas.
- Esta arquitectura, presenta varias ventajas, si bien aquí destacamos dos de las principales, relacionadas con la asignatura de base de datos, teniendo en cuenta que cada capa se ejecuta en su propia infraestructura:
    - **Escalabilidad:** cualquier capa se puede escalar independientemente de los demás según sea necesario.
    - **Seguridad:** como no hay comunicación directa entre la capa de presentación y de datos, la capa de aplicación bien diseñada puede hacer las veces de un firewall interno, lo que impide ataques de inyecciones SQL y otras vulnerabilidades maliciosas.

![image.png](attachment:ed339da6-4ef2-4b37-9e7d-3e30ebf3b588:image.png)

```agda
La arquitectura de un SGBD depende del propio HW y del SO, y garantiza la atomicidad de las transacciones y la disponibilidad ante fallos
destacando 2 arquitecturas: 

📌 1.Arquitectura de dos capas 🖥️➡️📊
📌 Modelo cliente-servidor que consta de dos capas, una capa de presentacion(GUI) y una de datos(Almacenamiento y gestión).
✅️ Puede ejecutarse en cualquiera de las capas o en ambas.
✅️ Utiliza estándares como ODBC y JDBC para la comunicación entre el cliente y el servidor.
✅️ Aunque aún se utiliza en ciertos sistemas por razones históricas, no es común en aplicaciones modernas.

📌 2.Arquitectura de Tres Capas 🌐
📌 No hay comunicación directa entre la capa de presentación y la capa de datos.
		- Capa de Presentación: Interfaz donde el usuario interactúa con la aplicación.
		- Capa de Aplicación: Procesa los datos y contiene la lógica de negocio, ejecutándose en un servidor de aplicaciones. Aquí se 
													utilizan lenguajes como Python, Java, PHP, Ruby, etc. Se comunica con la capa de datos a través de APIs.
		- Capa de datos: Almacena y gestiona los datos 
✅️ Cada capa opera en su propia infraestructura, permitiendo la evolución y despliegue de cada una sin afectar a las otras.
✅️ Muy común en aplicaciones web, especialmente con tecnologías en la nube, como contenedores y microservicios.
✅️ Ventajas:
			📈 Escalabilidad: Permite escalar cada capa de manera independiente según las necesidades.
			🔒 Seguridad: Al no haber comunicación directa entre la presentación y la capa de datos, se pueden implementar medidas de seguridad adicionales para proteger contra ataques, como inyecciones SQL.

```

## Estructura interna de una Base de Datos

- Usuarios: tenemos diferentes tipos que trabajan u operan con la base de datos.
- Gestor de Consultas: Dentro de este módulo se encuentran otra serie de submodulos que se encargan de diferentes funciones:
    - Interprete LDD: que interpreta las intrucciones LDD y registra las definiciones en el diccionario de datos.
    - Compilador LMD: traduce las instrucciones LMD en un conjunto de instrucciones de bajo nuvel que entienda el motor de evaluación de consultas. (Funciones de optimización de consultas)
    - Motor de evaluación de consultas: que ejecuta las instrucciones de bajo nivel generadas por el compilador LMD.
- Gestor de almacenamiento: Responsable de la iteracción con el gestor de archivos sobre el sistema operativo que se haya instalado la base de datos .
    - este módulo transcribe las diferentes instrucciones LMD a comandos de bajo nivel del sistema de archivos.
    - Es responsable del almacenamiento la recuperación y la actualización de los datos de la base de datos
    - Dentro del gestor se encuentran otros elementos:
        - gestor de autorizaciones e integridad
        - gestor de transacciones
        - gestor de archivos
        - gestor de la memoria intermedia
        
        Define una serie de estructuras de datos internamente para el almacenamiento del disco:
        
        - archivos de datos
        - diccionario de datos
        - estadisticas
        - indices

```agda
📌 1. Usuarios 👤
Existen diferentes tipos de usuarios que interactúan con la base de datos.

📌 2. Gestor de Consultas 🔍
✅️ Submódulos:
➡️Intérprete LDD: Interpreta instrucciones LDD y registra definiciones en el diccionario de datos. 📜
➡️Compilador LMD: Traduce instrucciones LMD a bajo nivel para el motor de evaluación de consultas (optimización de consultas). ⚙️
➡️Motor de Evaluación de Consultas: Ejecuta las instrucciones de bajo nivel generadas por el compilador. 🚀

📌 3. Gestor de Almacenamiento 💾
✅️ Responsabilidades: Interactúa con el gestor de archivos del sistema operativo, transcribe instrucciones LMD a comandos de bajo nivel y 
											 maneja almacenamiento, recuperación y actualización de datos. 🔄
✅️ Elementos Internos:
- Gestor de autorizaciones e integridad 🔑
- Gestor de transacciones 📊
- Gestor de archivos 🗂️
- Gestor de memoria intermedia 📦
✅️ Estructuras de Datos Internas:
- Archivos de datos 📁
- Diccionario de datos 📚
- Estadísticas 📈
- Índices 📊
```

## Transacciones y sus propiedades

Sobre las bases de datos relacionales se realizan operaciones, inserciones, actualizaciones, borrados, consultas,….El conjunto de operaciones ejecutadas como una única unidad atómica, es lo que se considera una **transacción** en base de datos. Esto significa que, o bien todas las operaciones de la transacción se completan con éxito, o bien ninguna de ellas se aplicará a la base de datos.

**¿Por qué son necesarias las transacciones en una base de datos relacional?**

Porque se utilizan para garantizar la **coherencia e integridad de los datos,** asegurando que la base de datos siga siendo coherente incluso en caso de fallos o errores del sistema. La característica clave de las transacciones es que son ***atómicas, consistentes, aisladas y duraderas (ACID*** - **A**tomicity, **C**onsistency, **I**solation y **D**urability,), que son las cuatro **propiedades** clave que garantizan la fiabilidad de la base de datos.

**¿Cómo funcionan?**

Agrupando múltiples operaciones de bases de datos en una única unidad atómica. Cuando se inicia una transacción, el SGBD crea un nuevo contexto de transacción y lo asigna al hilo de ejecución actual. Cualquier operación de base de datos que se realice dentro de ese contexto se considera parte de la transacción. Una vez completadas las operaciones, la transacción puede ser confirmada o revertida.

- Si la transacción se  el SGBD aplica todas las operaciones de la transacción a la base de datos, haciéndolas permanentes (**commit** – sentencia que hace permanente en la base de datos los cambios realizados).
- Si la transacción se  (**rollback**), el SGBD deshace todas las operaciones de la transacción, devolviendo la base de datos a su estado anterior al inicio de la transacción.

Los cambios realizados por una transacción no son visibles para otras transacciones hasta que la transacción se confirma(commit). Este aislamiento ayuda a evitar conflictos entre transacciones simultáneas.

El SGBD utiliza una técnica llamada **bloqueo** para garantizar que sólo una transacción pueda acceder a la vez a una parte específica de los datos (bloquea objetos implicados en la transacción).

Esto evita que otras transacciones modifiquen los mismos datos, lo que podría causar conflictos.

El SGBD utiliza una técnica llamada **registro** para garantizar que los cambios realizados por una transacción puedan deshacerse en caso de fallo, dejando la base de datos en estado coherencia a como estaba previo al inicio de la transacción.

**¿Qué son las propiedades (ACID) de las transacciones?**

Este conjunto de propiedades garantiza la fiabilidad de las transacciones de bases de datos.

- **Atomicidad:** propiedad que garantiza que una transacción se trate como una unidad única e indivisible. Esto quiere decir que o bien todas las operaciones incluidas en la transacción se completan con éxito, o bien ninguna de ellas se aplica a la base de datos. En caso de fallo, la base de datos vuelve a su estado anterior a la transacción, manteniendo así la coherencia.
- **Consistencia:** propiedad que garantiza que la base de datos se mantiene en un estado coherente durante toda la transacción. El SGBD comprueba las restricciones de integridad antes y después de la transacción y revierte la transacción si se infringe alguna restricción.
- **Aislamiento:** propiedad que garantiza que los cambios realizados por una transacción no sean visibles para otras transacciones hasta que la transacción sea confirmada. Este aislamiento ayuda a evitar conflictos entre transacciones concurrentes.
- **Durabilidad:** propiedad que hace que una vez se haya llevado a cabo una determinada transacción de forma exitosa (commit), estas tengan la capacidad de persistir y no puedan ser revertidas, incluso si el sistema tuviese algún fallo o se cayese.

```agda
Las transacciones en bases de datos relacionales agrupan operaciones (inserciones, actualizaciones, borrados, consultas) como una única 
unidad atómica. Esto asegura que todas las operaciones se completen con éxito o ninguna se aplique.

📌 ¿Por qué son necesarias? ❓
Garantizan la coherencia e integridad de los datos, asegurando que la base de datos se mantenga consistente, incluso ante fallos.

📌 Propiedades ACID 🔑
✅️Atomicidad: La transacción se trata como una unidad indivisible; o se completa todo, o no se aplica nada. 🔄
✅️Consistencia: Mantiene la base de datos en un estado coherente, verificando restricciones de integridad. ✅
✅️Aislamiento: Los cambios no son visibles para otras transacciones hasta que se confirman (commit). 🛡️
✅️Durabilidad: Una vez confirmada, la transacción persiste, incluso ante fallos del sistema. 💾

📌 Funcionamiento ⚙️
✅️Se inicia una transacción y se crea un contexto de transacción.
✅️Al finalizar, se puede hacer commit (aplicar cambios) o rollback (deshacer cambios).
✅️El SGBD utiliza bloqueo para evitar conflictos entre transacciones simultáneas y registro para deshacer cambios en caso de fallo.
```

## Lenguajes de las bases de datos

Hemos comentado en apartado previo, sobre LDD y LMD, si bien en este apartado profundizaremos sobre estos dos sub-lenguajes. El diseño general de una base de datos relacional se denomina esquema de la base de datos (en nomenclatura MySQL es referido a database) y los SGBD proporcionan un LDD para diseñar el esquema de la base de datos y un **LMD** para expresar las consultas y las modificaciones de los datos necesarias. EL LDD contiene un conjunto de instrucciones que definen los detalles de implementación de los esquemas de las bases de datos, que normalmente se ocultan a los usuarios.

Ejemplo:

```sql
CREATE TABLE CUENTA (Num_Cta CHAR(10), Saldo INTEGER, Id_Cliente INTEGER);
```

Los valores de los datos almacenados en la base de datos deben satisfacer ciertas **restricciones de consistencia.** Estas restricciones de consistencia se dividen a su vez en:

**RESTRICCIONES DE DOMINIO**

Se debe asociar un dominio de valores posibles a cada atributo (datos de tipo entero, datos de tipo carácter, dato de tipo fecha/hora).

- La declaración de un atributo como parte de un dominio concreto actúa como restricción de los valores que puede adoptar.
- Las restricciones de dominio son la forma más elemental de restricción de integridad (No podemos insertar un carácter en un atributo de tipo entero)
- SGBD comprueba dichas restricciones cada vez que se inserten/modifiquen valores en la base de datos.

**INTEGRIDAD REFERENCIAL**

Escenarios en los que se requiere asegurar que un valor que aparece en una relación para un conjunto de atributos dado aparece también para un determinado conjunto de atributos en otra relación (integridad referencial).

Ejemplo:

```sql
CREATE TABLE Orders(
ID_Order int NOT NULL PRIMARY KEY,
CustomerID int FOREIGN KEY REFERENCES Customer(CustomerID)
 );
```

En el ejemplo anterior se crea una tabla “Orders” donde se establece una referencia del campo customberID al campo CustomberID de la tabla “Customber” lo cual significa que cualquier valor de ID tiene que estar previamente como valor en la tabla Customber.  Cuando se viola una restricción de integridad el procedimiento normal es rechazar la acción que ha causado esa violación, sin embargo en la clausula foreign key puede especificar acciones a tomar para restaurar la integridar referencial por ejemplo ON DELETE CASCADE. Autorización permite dar acceso a determinados valores u operativos sobre los datos de la DB a los usuarios. 

- Autorización de lectura
- Autorización de inserción
- Autorización de actualización
- Autorización de eliminación

ejemplo:

```sql
GRANT INSERT, UPDATE, DELETE ON Empleados  TO carlos@localhost;
```

En ejemplo anterior se otorga autorización al usuario “carlos@localhost” para hacer INSER,UPDATE,DELETE  (solamente estas operaciones) sobre la tabla EMPLEADOS. El resultado de ejecución de comandos del lenguaje LDD van conformando el diccionario de datos  de la base de datos. Dicho diccionario contiene metadados, es decir, datos sobre datos (información sobre las tablas, bases de datos, usuarios, permisos,...). En MySQL (SGDB de referencia para el curso) el diccionario está formado por varios esquemas (BBDD):

- Information Schema:
    - esquema que guarda toda la info de la BD
    - tablas que conforman el este esquema son realmente vistas
    - Info que podríamos obtener de esta base de datos
- Mysql
    - En esta base de datos se almacena información relacionada con los parametros del SGBD y los usuarios con los permisos de los mismos
- Sys y Performance Schema
    - Sys contiene una serie de objetos que posibilitan al DBA a analizar la información recogida sobre el rendimiento del SGBD de la base de datos performance schema. En este se almacena la información a bajo nivel sobre la ejecución de consultas procesos, estadisticas y operaciones E/S.

```sql
SELECT CLIENTE.NOMBRE_CLIENTE
FROM CLIENTE
WHERE CLIENTE.CIUDAD_CLIENTE = ’Madrid’
```

Hay dos tipos de lenguajes de manejo de datos: **los procedurales y los no procedurales.** Estos dos tipos se distinguen por el modo en que acceden a los datos. Los lenguajes procedurales manipulan la base de datos registro a registro, mientras que los no procedurales operan sobre conjuntos de registros. El lenguaje no procedural más utilizado es el SQL (Structured Query Language) que, de hecho, es un estándar y es el lenguaje de los SGBD relacionales.

**NOTA:** Tanto LDD como LMD se verá con más detalle, asociados a la base de datos relacional MySQL, con mayor profundidad en las siguientes unidades. Hay también otros dos subtipos: **DCL** (Data Control Language) y **TCL** (Transaction Control Language)  que también se describirán en siguientes unidades, y que cubren todos los comandos SQL que se permiten en un SGBD como MySQL.

```agda
📌 Esquema y Sub-lenguajes 🔍
✅️LDD (Lenguaje de Definición de Datos): Define el esquema de la base de datos.
✅️LMD (Lenguaje de Manipulación de Datos): Expresa las consultas y modificaciones necesarias.

📌Restricciones de consistencia📏
 ✅️ Restricciones de dominio: Asociar un dominio a cada atributo (ej. entero, carácter, fecha/hora) que actúa como restricción de valores
														  posibles y donde el SGBD verifica estas restricciones al insertar/modificar valores.
 ✅️ Integridad referencial: Asegura que los valores en una relación aparecen en otra relación.

📌 Autorizaciones: 🛡️
✅️Autorización de lectura 📖
✅️Autorización de inserción 📝
✅️Autorización de actualización 🔄
✅️Autorización de eliminación 🗑️

📌 Diccionario de datos: 📚
✅️ Information Schema: Guarda toda la info de la BD, tablas son vistas.
✅️ Mysql: Información de parámetros del SGBD y usuarios.
✅️ Sys y Performance Schema: Análisis y rendimiento del SGBD.

📌 Tipos de LMD: 💻
✅️ Procedurales: Manipulan la BD registro a registro.
✅️ No procedurales: Operan sobre conjuntos de registros (ej. SQL).

💡 NOTA: DCL y TCL se verán en detalle en las siguientes unidades.
```

# Evolución de las Bases de datos

Fruto de la diversidad de contenidos que se generan actualmente, resultantes de la interacción entre seres humanos y máquinas, unido a un cambio de paradigma en la toma de decisiones empresariales han provocado que los datos que se generan estén en continuo cambio. Este dinamismo en la creación y generación en los datos implica necesariamente una evolución y adaptación de las bases de datos, de forma que permitan almacenar y procesar esta nueva tipología de datos de forma que pueda obtenerse información que ayude a las empresas en la toma de decisiones.

La primera premisa que tenemos que tener presente, es que todos los datos no son iguales. Esto significa que los datos generados por las aplicaciones de redes sociales son completamente diferentes de los datos generados por los sistemas de una empresa de telecomunicaciones o un banco.

La forma en que se recopilan, procesan y analizan estos datos depende de su formato, naturaleza, volumen,….. es decir, de ciertas características asociadas a los mismos.

## **Datos estructurados**

En general están referidos a valores que se ajustan a campos y columnas fijos en una base de datos relacional (por ejemplo MySQL), hojas de cálculo,….  Son de un determinado tipo (carácter, numérico, lista de valores,…) y de un tamaño máximo prefijado.

Estos datos estructurados permiten realizar búsquedas, actualizaciones y manipulaciones con rapidez y de forma sencilla, normalmente a través de lenguajes de consulta, como puede ser SQL, que sigue siendo el lenguaje más utilizado.

Ejemplos de datos estructurados:

- Una tabla Excel
- Datos de una base de datos relacional – SQL
- Cuestionarios tipo test.
- Formularios web.
- Fichas estandarizadas de clientes.

A día de hoy, las fuentes de datos estructuradas generan datos en tiempo real y en altos volúmenes. Los datos estructurados pueden tener naturaleza muy dispar, generación de datos por parte de humanos, de máquinas – IoT (Internet of Things), de servidores informáticos (aplicaciones, bases de datos, web,…),…

El análisis de todos datos estructurados, permite determinar comportamientos de clientes, compras online, creación de campañas de marketing, patrones de compra,….

## **Datos semi-estructurados**

Se encuentran a medio camino entre los estructurados y los no estructurados.

Tienen un cierto nivel de estructura, jerarquía y organización, aunque carecen de un esquema fijo.

En lugar de estructuras esquemáticas, como en el caso de los estructurados, estos presentan una estructura de árbol, con etiquetas para facilitarte el manejo.

Entre sus principales características está, también, que tienen algunas propiedades organizativas que facilitan su análisis y contienen metadatos (etiquetas y elementos) que se utilizan para agruparlos y describir cómo se almacenan.

Al no contener tantos metadatos como en el caso de los estructurados, su gestión y automatización resulta mucho más complicada.

Ejemplos:

- Correos electrónicos
- Archivos comprimidos.
- **XML:** cuya flexible estructura, basada en etiquetas, permite universalizar la estructura de datos, el almacenamiento y el transporte en la Web.
- **JSON:** (JavaScript Object Notation), otro formato de intercambio de datos semi-estructurados que se utiliza mucho en la transmisión de datos entre aplicaciones web y servidores.
- **Paquetes TCP / IP.**

Algunos servicios muy conocidos basados en este tipo de datos son el sistema de recomendación de **Amazon** o los servicios de **Linkedin.**

## **Datos no estructurados**

Los datos no estructurados son prácticamente todo lo demás.

Estos tipos de datos tienen una estructura interna, pero no están estructurados a través de modelos o esquemas de datos fijos y predefinidos. Pueden ser texto o no, y generación de cualquier naturaleza, pudiendo almacenarse en bases de datos NoSQL.

Suponen un alto del volumen de todos los datos generados, y el porcentaje no deja de crecer. Estos datos no se pueden usar en una base de datos relacional, ya que sería imposible ajustarlos a las filas y columnas prefijadas en la definición. Existen aplicaciones que pueden procesar varias centenas de tipos de formatos de datos no estructurados.

Ejemplos:

- Documentos en archivos de texto (doc,txt,cnf,…)
- Archivos de imágenes (jpg, png,bmp,…)
- Archivos PDF
- Archivos de registro y de datos de aplicaciones como .ini o .dll.
- Datos de redes sociales como Facebook y Twitter o de plataformas como YouTube.
- Datos de ubicaciones y mensajería instantánea.
- Grabaciones telefónicas, archivos de audio como MP3.

Trabajar, no sólo con datos no estructurados, sino con enormes volúmenes de ellos supone un auténtico desafío, al que las empresas dan respuesta con nuevas herramientas, nuevos modelos de almacenamiento y computación, siendo tendencia **sistemas cloud,** cambios en las estrategias tradicionales de ingeniería de datos (de modelos ETL -Extract, Transform, Load- a ELT - Extract, Load, Transform), integración de soluciones nativas y opensource etc.

A todo ello se suma la complejidad añadida de dar respuesta en **tiempo real** a un creciente número de aplicaciones como las basadas en dispositivos IoT, el comercio online etc.

La capacidad de extraer valor de los datos no estructurados es uno de los principales motores del rápido crecimiento del **Big Data** y junto a técnicas de data mining que implican métodos de **machine learning, inteligencia artificial y estadística,** permiten a las empresas conocer mejor, a través de la información no estructurada, los hábitos y los ritmos de compra, los patrones de comportamiento o las afinidades con determinados productos, lo cual genera una **ventaja competitiva** para dichas empresas.

Los datos no estructurados se suelen almacenar en un **DataLake,** que es un repositorio de almacenamiento que contienen una gran cantidad de datos en crudo (raw data) y se almacenan hasta que resulten útiles. Utiliza una arquitectura plana para almacenar los datos.

A cada elemento del datalake se le asigna un identificador único y se etiqueta con un conjunto de etiquetas de metadatos extendidas.

El datalake se asocia a menudo con el almacenamiento de objetos orientado a **Hadoop.**

**Hadoop** es un framework opensource (Apache y con tecnología Java) para almacenar datos y ejecutar aplicaciones en clusters hardware. Proporciona un almacenamiento masivo para cualquier tipo de datos, gran capacidad de procesamiento y posibilidad de gestionar tareas manera flexible asociadas con los datos almacenados.

Las características más importantes de Hadoop de forma resumida:

- **Capacidad para almacenar y procesar grandes cantidades de cualquier tipo de datos rápidamente.** Permite a las aplicaciones trabajar con miles de nodos en red y petabytes de datos.
- Modelo de **procesamiento distribuido** en función del número de nodos que se utilicen. Arquitectura escalable y adecuada para dar respuesta a necesidades Big Data y Business Analytics.
- **Tolerancia a fallos:** Si un nodo en el modelo distribuido, presente problemas HW, los trabajos se redirigen automáticamente a otros nodos para asegurarse del procesamiento adecuado. Se almacenan automáticamente varias copias de todos los datos.
- **Flexibilidad:** A diferencia de las bases de datos relacionales tradicionales, no es necesario preprocesar los datos antes de almacenarlos. Se almacenan todos los datos que se necesite y en fases posteriores decidir cómo utilizarlos. Esto incluye datos no estructurados como texto imágenes y vídeo.
- **Bajo coste:** El framework de código abierto es gratuito y utiliza hardware básico para almacenar grandes cantidades de datos.

En este escenario, los datos de una organización se cargan en la plataforma Hadoop y a continuación, se aplican las herramientas de análisis y de minería de datos a los datos que residen en los nodos clúster de Hadoop.

![image.png](attachment:ff44b2cf-1c3b-42ef-8dc8-5c8d34e238e4:image.png)

El nodo maestro **(NameNode)** es el “cerebro” de la arquitectura ya controla el acceso por parte de los clientes (aplicaciones) a la información, a la vez que gestiona el almacenamiento y procesamiento de los datos en los **DataNodes** (nodos slaves también llamados workers).

Los DataNodes almacenan los bloques de datos y envían los datos solicitados en las diferentes consultase informan periódicamente los metadatos asociados a los bloques de datos al NameNode, para que este sepa en todo momento la ubicación de los datos.

```agda

📌 Datos estructurados:📊
✅️ Son valores que se ajustan a campos y columnas fijos en una base de datos relacional (por ejemplo MySQL) o hojas de cálculo.
✅️ Algunos tipos son carácter, numérico, lista de valores, etc.
✅️ Características: Tamaño máximo prefijado. Permiten búsquedas, actualizaciones y manipulaciones rápidas y sencillas con 
										 lenguajes de consulta como SQL.
✅️ Las fuentes de datos estructurados generan datos en tiempo real y en altos volúmenes, permitiendo analizar comportamientos de clientes,
	 compras online, campañas de marketing, etc.

Ejemplos:
📊 Tabla Excel
🗃️ Base de datos relacional (SQL)
📝 Cuestionarios tipo test
🌐 Formularios web
📇 Fichas estandarizadas de clientes

📌  Datos semi-estructurados:📂
✅️ Definición: Datos que tienen un cierto nivel de estructura, jerarquía y organización, pero sin un esquema fijo.
✅️ Características: Estructuran el árbol con etiquetas, contienen metadatos para agrupar y describir cómo se almacenan, por último gestionan
								 y automatizan más complicada que los datos estructurados.
✅️ Servicios como el sistema de recomendación de Amazon o LinkedIn se basan en datos semi-estructurados.

Ejemplos:
📧 Correos electrónicos
🗜️ Archivos comprimidos
🗂️ XML: Estructura flexible basada en etiquetas.
🔄 JSON: Formato de intercambio de datos muy usado en transmisión entre aplicaciones web y servidores.
📦 Paquetes TCP/IP

📌  Datos no estructurados: 📚
✅️ Definición: Datos con estructura interna, pero sin modelos o esquemas de datos fijos y predefinidos.
✅️ Características: No se pueden usar en bases de datos relacionales.Suponen un alto volumen de todos los datos generados. Utilizan 
								herramientas y modelos de almacenamiento y computación avanzados (e.g., sistemas cloud, ELT, DataLake).
✅️ El DataLake es un repositorio que contiene una gran cantidad de datos en crudo, almacenados hasta que resulten útiles. 
✅️ Hadoop es un framework opensource que se utiliza para almacenar y procesar grandes cantidades de datos en clusters.

Ejemplos:
📄 Documentos en archivos de texto (doc, txt, cnf)
🖼️ Archivos de imágenes (jpg, png, bmp)
📑 Archivos PDF
📋 Archivos de registro y datos de aplicaciones (ini, dll)
🌐 Datos de redes sociales (Facebook, Twitter, YouTube)
📍 Datos de ubicaciones y mensajería instantánea
🎧 Grabaciones telefónicas, archivos de audio (MP3)

✅️ Características de Hadoop:
Capacidad para almacenar y procesar grandes cantidades de datos rápidamente siendo un modelo de procesamiento distribuido por n nodos
- Tolerancia a fallos: Redirige trabajos automáticamente en caso de problemas HW.
- Flexibilidad: Permite almacenar todos los datos necesarios y decidir cómo utilizarlos después.
- Bajo coste: Framework gratuito y utiliza hardware básico.
- El NameNode: es el “cerebro” de la arquitectura de Hadoop y gestiona el acceso a la información y el almacenamiento/procesamiento 
							de los datos en los DataNodes (nodos esclavos o workers).
```

## Evolución

Las bases de datos constituyen un elemento clave en la generación de valor añadido para consumidores, operadores, empresas y organizaciones, cuya importancia ha ido creciendo incorporándose en todas las capas de la sociedad actual.
La incorporación de las bases de datos a los procesos productivos de la sociedad permite la captura organizada manual y/o automática de todos los datos relativos a las etapas que conforman el ciclo de vida del producto, servicio,….  aportando un orden con finalidad de consulta y análisis, facilitando su conversión en información útil y de valor añadido para todos los **stakeholders** (personal involucrado en sus diferentes roles con los datos/información generada, almacenada, procesada,consultada,…).

La elección del tipo de base de datos vendrá determinada por el grado de respaldo en términos de funcionalidad y rendimiento que nuestra aplicación de software necesite, si bien aspectos a considerar:
• Tipado, estructura, modelo o esquema y casos de uso previsto con los datos en el origen.
• Mecanismo de consulta informacional.
• Latencia o tiempo de entrega de servicio requerida.
• Nivel de consistencia de datos.
• Velocidad transaccional y/o procesamiento (Batch, Near Real-Time, Real Time).

Hoy en día ocupa un lugar privilegiado en toda propuesta digital (Transformación Digital), el predominio cada vez mayor en el uso profesional de servicios **«pay on demand»** a través de proveedores de **Cloud Computing** (computación en la nube), posibilita enormemente la disponibilidad de una amplia selección de bases de datos personalizadas multipropósito donde el modelo de costes (**OPEX** – pago por uso) suele ser mas adecuado para una gran mayoría de empresas.

Las bases de datos en la nube se pueden ofrecer como una base de datos como servicio administrado (***DBaaS – DataBase as a Service***) o implementada en una máquina virtual (VM) basada en la nube, y autoadministrada por un equipo informático de la propia empresa.

Entre los ejemplos de bases de datos relacionales, que se ofrecen en la nube se incluyen: SQL Server, Oracle, MySQL, PostgreSQL, Spanner y Cloud SQL.
Si hablamos de ejemplos de bases de datos no relacionales en la nube, se suelen ofrecer:  MongoDB, Redis, Cassandra y Hbase.
Como no podía ser de otra manera, también ha evolucionado la forma en desarrollar aplicaciones software, donde se han pasado de entornos más centralizados hacia arquitecturas cliente-servidor, donde el patrón de diseño software, MVC (Modelo-Vista-Controlador) se ha hecho relevante, convergiendo las aplicaciones hacia arquitecturas de microservicios con el uso de aplicaciones distribuidas. Lógicamente esta evolución de aplicaciones impacta en la evolución tecnológica de las bases de datos.

```agda
Importancia: Bases de datos son claves para generar valor añadido en todos los sectores.

🔄 Procesos productivos: 
Capturan y organizan datos para convertirlos en información útil para los stakeholders.

🔧 Elección de base de datos
✅️ Tipado y modelo: Ajuste a datos.
✅️ Consulta: Eficiencia.
✅️ Latencia: Tiempo de entrega.
✅️ Consistencia: Nivel requerido.
✅️ Velocidad: Batch, Near Real-Time, Real Time.

☁️ Transformación digital: 
Uso de servicios pay on demand y Cloud Computing facilita bases de datos personalizadas.

📊 Bases de datos en la nube: 
✅️ Relacionales: SQL Server, Oracle, MySQL, PostgreSQL, Spanner, Cloud SQL.
✅️ No relacionales: MongoDB, Redis, Cassandra, Hbase.

🖥️ Desarrollo de aplicaciones: 
✅️ De entornos centralizados a arquitecturas cliente-servidor y microservicios, impactando en la evolución de las bases de datos.
✅️ Espero que te sea útil este resumen. ¿Necesitas algo más? 😊
```

## Bases de datos Relacionales (SQL)

A continuación, se presentan algunas razones por las que decantarse hacia una base de datos relacional (SQL):

- Estándar SQL definido, comúnmente aceptado como estándar universal.
- Tecnologías maduras, documentadas y con una amplia comunidad de desarrollo.
- Compatibilidad ACID (explicado en apartados previos).
- Gran número de proveedores ofreciendo sistemas de gestión de bases de datos relacionales (RDBMS).
- Orientadas filas (row scores)

Dentro de las bases de datos relacionales tenemos dos grandes tipos:

**OLTP: Online Transactional Processing**

- El proceso transaccional es típico de las bases de datos operacionales.
- Bases de datos orientadas al procesamiento de transacciones.
- Una transacción es un proceso atómico, es decir se hace o no se hace (que debe ser validado con un *commit*, o invalidado con un rollback).
- Una transacción puede involucrar operaciones de inserción, modificación y borrado de datos.
- Los datos, al tener fuentes, naturalezas y tecnologías diferentes no suelen ser uniformes.
- El historial de los datos es limitado (días normalmente)
- Se realizan millones de transacciones que involucran tareas de lectura y escritura.
    - Ejemplo: Alto volumen de transacciones que soportan las bases de datos de los bancos.

**OLAP - On-Line Analytical Processing**

- Los sistemas OLAP son bases de datos orientadas al procesamiento analítico desde varias dimensiones (multidimensional)
- Este análisis suele implicar, generalmente, la lectura de grandes cantidades de datos para llegar a extraer algún tipo de información útil: tendencias de ventas, patrones de comportamiento de los consumidores, elaboración de informes complejos… etc.
- Estos sistemas son típicos los datamarts.
- Mantiene un histórico de datos de varios años.
- El acceso a los datos suele ser de sólo lectura con pequeño número de escrituras.
- Los datos se estructuran según las áreas de negocio, y los formatos de los datos están integrados de manera uniforme en toda la organización.
- Las bases de datos OLAP se suelen alimentar de información procedente de los sistemas operacionales existentes, mediante un proceso de extracción, transformación y carga (ETL).

![image.png](attachment:ca1c5ae6-b57e-4cab-802a-1327e0baa109:image.png)

Basándose en las tecnologías OLTP y OLAP tendremos:
****

**Datamart**
Un Datamart es una base de datos relacional de un área o departamento, especializada en el almacenamiento de los datos de un área de negocio concreta. Dicha base de datos **permite analizar la información al detalle desde todas las perspectivas (dimensiones)** que afecten a los procesos relacionados con dicha área o departamento.
Un datamart puede estar basado en OLTP u OLAP y la elección de una u otra tecnología dependerá de los datos, los requisitos y las características específicas de los usuarios del área de negocio que vaya a explotar dichos datos. Según lo anterior, podríamos tener dos tipos de datamarts:

• Datamart OLAP: basado en los cubos OLAP.
    ◦ Se construyen agregando, según los requisitos de cada área o departamento, las dimensiones y los indicadores necesarios de cada cubo relacional.
    ◦ El modo de creación, explotación y mantenimiento de los cubos OLAP es muy heterogéneo, en función de la herramienta final que se 

![image.png](attachment:a9bfc3aa-17d1-45d1-9cee-09e6eaa25761:image.png)

     En la imagen anterior, tenemos un cubo OLAP (base de datos relacional) donde los datos (Total ventas) tienen tres dimensiones de análisis:
• Producto
• Tiempo
• Almacén

Esto quiere decir que podríamos analizar el Total de Ventas realizado, desde una o varias dimensiones de análisis, es decir poder dar respuesta a diferentes cuestiones de negocio de dicho departamento:
     • ¿Cuántas ventas totales se han realizado con productos del almacén 3?
     • ¿Cuántas ventas totales se han realizado de ladrillos entre los meses de Enero y Febrero de este año?
     • ¿Cuántas ventas totales se han realizado del producto “Cemento” el día 3 de Febrero de 2022 y donde dicha mercancía se encontraba en el Almacén 
• Datamart OLTP: Extracciones para periódicas con agregaciones y filtrados orientadas a determinadas informaciones de un área empresarial concreta.
En general los Datamart presentan tres características muy comunes: 
     • El volumen de datos que manejan no es elevando
     • Las consultas realizadas son sencillas y 
     • Los tiempos de respuestas son reducidos.

**Datawarehouse**
Es una base de datos corporativa que se caracteriza por integrar y depurar información de varias fuentes distintas, tanto en naturaleza de información como en tecnología, para un procesamiento posterior una vez que los datos están depurados.
Cuando dicha base de datos ya tiene los datos procesados permite a los usuarios análisis desde diferentes puntos de vista y normalmente en tiempo real. La implantación de un datawarehouse en una compañía es el primer paso para la implantación de una sistema o plataforma de Business Intelligence.

La principal característica de este tipo de bases de datos, que manejan millones de transacciones o registros al día, dependiendo del volumen y sector al que se dedique la empresa, es que se almacena la información en modelos de tablas en:  estrella o en copo de nieve (existen algunos otros pero están menos extendidos)
Este tipo de persistencia de la información es homogénea y fiable, y permite la consulta y el tratamiento jerarquizado de la misma (siempre en un entorno diferente a los sistemas operacionales).

**Modelo de datos en estrella:** (modelo de datos similar a una estrella con N puntas)
     1. Dimensiones de análisis: Clientes, Producto y Fechas (Tiempo)
     2. Ventas: tabla de hechos donde se encuentra el dato simple (Importe Total). Puede hacer varios hechos, por ejemplo, Cantidad y Precio.
     3. Al ser un esquema simple, es rápido. Permite acceder tanto a datos agregados como de detalle.
     4. El diseño de esquemas en estrella permite la funcionalidad de una base de datos multidimensional utilizando una base de datos relacional

     5. Debido a que las condiciones solo relacionan la tabla de hechos con las dimensiones, las consultas a la base de datos no son complicadas.
     6. Son más simples de manejar que los modelos copo de nieve.

**Modelo de datos en copo de nieve (SnowFlake)**
Este modelo se diferencia principalmente del modelo de estrella en que no solo la tabla de hechos tiene relación con otras tablas, sino que hay otras tablas que se relacionan con las dimensiones sin tener relación con los hechos.
Para conseguir un esquema en copo de nieve se ha de tomar un esquema en estrella y conservar la tabla de hechos, centrándose únicamente en el modelado de las tablas de dimensión, que ahora se dividen en subtablas.
El modelo fue concebido para facilitar el mantenimiento de las dimensiones, sin embargo, esto hace que se vinculen más tablas, haciendo la extracción de datos más difícil, así como vuelve compleja la tarea de mantener el modelo.

En el caso de un modelo en copo de nieve tenemos una tabla de hechos (Sales Fact) con varias dimensiones de primer nivel: Customer (Cliente), Date (Tiempo), Store (Almacén) y Product(Producto).
A su vez, estas dimensiones de primer nivel tienen otras dimensiones de segundo nivel, que lógicamente permitirán el análisis también por estas dimensiones. La jerarquía de dimensiones no será igual en cada rama, pudiendo tener ramas de análisis con un solo nivel de análisis y otras ramas con varios niveles de análisis.

Ejemplo: Sales Fact - Customer - City.
Igualmente, se podrán realizar análisis sobre varias dimensiones cuando los datos estén preparados.
En los esquemas de copo de nieve se evita la redundancia de datos y con ello se ahorra espacio. Se puede usar un esquema de copo de nieve en un DataWarehouse, aunque estos sean grandes y complejos, pero nunca en sistemas donde el tiempo de respuesta sea un factor crítico para los usuarios.

![image.png](attachment:7d42ce3a-d562-4746-8699-372ed2090fc2:image.png)

Para comprender el concepto de datawarehouse, es importante entender cómo se lleva a cabo el proceso llamado, **ETL** (Extracción, Transformación y Carga), a partir de los sistemas operacionales de una compañía:
1. **Extracción:** obtención de información de las distintas fuentes tanto internas como externas.
2. **Transformación:** filtrado, limpieza, depuración, homogeneización y agrupación de la información.
3. **Carga:** organización y actualización de los datos y los metadatos en la base de datos.

## Bases de datos NoSQL

Aunque tendremos la última unidad de esta asignatura para las bases de datos NoSQL, se realiza en este item una introducción. 

**Las razones por las que decantarse por una base de datos NoSQL serían:**
• Soporte de grandes volúmenes de datos sin una estructura definida de antemano, contexto idóneo en productos y servicios de Big Data e Inteligencia Artificial.
• Requerimiento de menor administración al contar con capacidades de distribución (‘Sharding’) y replicación de datos como factores habilitadores de un sistema tolerante a fallos.
• Modelos de datos simplificados (‘Schemaless‘).
• Alta escalabilidad horizontal, ampliando la capacidad sin interrumpir la usabilidad y/o disponibilidad del servicio.
• Sin necesidad de servidores con gran cantidad de recursos para operar, pudiendo partir de una inversión baja, extensible a medida de ampliarse las necesidades.
• Utilizan APIs para diversas comunicaciones con aplicaciones, normalmente en formato JSON.
• No garantizan las propiedades ACID (Atomicity, Consistency, Isolation and Durability).
• Normalmente no soportan operaciones JOIN.
• Suelen ser distribuidas y de código abierto.

### Tipos de Bases de datos NoSQL

- **Clave Valor:** No tienen un esquema de datos predefinidos, se asimilan al concepto de array estructurándose las de dos columnas en clave y valor de registro. Los valor pueden tomar el tipo de dato que sea necesario incluso fichero json.
    - Su ventaja principal es la gran velocidad de lectura y escritura que permiten divisibilidad y escalado horizontal, por otra parte su principal desventaja es la poca capacidad de filtrar la información en las consultas. Sus mayores exponentes son DynamoDB y Redis.
- **Orientados a columnas:** Organizan los datos en columnas separadas de esta forma es mas sencillo y eficiente añadir nuevas columnas y realizar operaciones de búsqueda sobre ellas usando el concepto de espacio de claves que contiene todas las familias de columnas.
    - Dentro de una familia de columnas el número de ellas en cada fila puede variar siendo extremadamente populares en sistemas que ya funcionan de manera similar a lo que harían las tablas de las bases de datos relacionales aportando escalabilidad y una comprensión eficiente de los datos. Sin embargo cabe recalcar su ineficacia para consultar filas individualmente y registros repartidos en varias columnas.
- **Grafos**: En estas bases de datos los registros son almacenados en una estructura en forma de grafo donde las relaciones interconectan los datos entre si consistiendo en dos componentes principales: Los nodos que funcionan como los datos en si mismos y los enlaces que explican las relaciones, lo cual dependiendo de la información que contengan pueden indicar naturaleza de la relación y flujo.
- **Document**: estas bases de datos almacenan datos autocontenidos llamados documentos los cuales pueden definir su propio esquema en fomrato JSON de forma general utilizados en documentos XML y BSON siendo este último un formato de intercambio de datos usado principalmente para su almacenamiento y transferencia en la base de datos mongoDB, comportándose como una representación binaria de estructuras de datos y mapas. Asignan a cada documento un ID único y no es necesario definir relaciones entre ellos.
    - La naturaleza es flexible semi estructurada y jerárquica entre los documentos y las bases de datos basadas en documentos haciendo posible una posible evolucion a futuro dependiendo de las necesidades de las aplicaciones.

```agda
**Bases de Datos NoSQL**
📌 Ventajas:✅
✅️ Flexibilidad: Sin esquema predefinido, fácil adaptación a cambios. 🔄
✅️ Escalabilidad Horizontal: Añadir servidores para manejar más datos y tráfico. 📈
✅️ Tolerancia a Fallos: Replicación y sharding mantienen el sistema operativo. 🔧
✅️ Rendimiento: Rápidas operaciones de lectura y escritura, especialmente en bases de datos clave-valor. ⚡

📌 Desventajas:🚫
✅️ Consistencia Eventual: Pueden no garantizar la integridad de datos. ⚠️
✅️ Limitaciones en Consultas: Falta de soporte para operaciones complejas como JOIN. 🔍
✅️ Curva de Aprendizaje: Requiere nuevas estrategias de modelado y consultas. 📚

📌 Tipos de Bases de Datos NoSQL: 💽
✅️ Clave-Valor: Rápido acceso a datos simples. Ejemplos: Redis, DynamoDB. 🔑
✅️ Orientadas a Columnas: Eficientes para grandes volúmenes de datos relacionados. Ejemplos: Cassandra, HBase. 📊
✅️ Grafos: Adecuadas para relaciones complejas. Ejemplos: Neo4j, ArangoDB. 🌐
✅️ Documentales: Flexibles y semi-estructuradas. Ejemplos: MongoDB, Couchbase. 📄
💡 Conclusión: Las bases de datos NoSQL son ideales para Big Data y aplicaciones que requieren escalabilidad y flexibilidad en el manejo de datos. 🚀
```

### Resumen del Ranking de Bases de Datos

### **Bases de Datos Relacionales (SQL)**

- **Oracle**: Modelo relacional, herramientas gráficas intuitivas, alto control de acceso y seguridad, compatibilidad multiplataforma, y lenguaje PL/SQL. Es el motor objeto-relacional más utilizado.
- **MySQL (MariaDB)**: Código abierto, multiplataforma, escalabilidad, compatibilidad con múltiples tipos de datos y caracteres, y amplia documentación con comunidad activa. Soporta integración con diversos lenguajes de programación.
- **SQL Server**: Soporte de transacciones, alta escalabilidad y seguridad, procedimientos almacenados, y arquitectura cliente-servidor. Microsoft ofrece diferentes ediciones según las necesidades empresariales.
- **PostgreSQL**: Alta concurrencia, soporte nativo para diversos tipos de datos, triggers, bases de datos distribuidas y capacidades objeto-relacionales. Compatible con múltiples lenguajes de programación.

### **Bases de Datos NoSQL**

- **Clave-Valor** (alto rendimiento y escalabilidad, sin relaciones de datos): *Cassandra, Redis, HBase, Memcached, Riak*.
- **Columnas** (manejo eficiente de grandes volúmenes de datos): *Cassandra, HBase*.
- **Documentos** (flexibilidad en esquemas con formatos XML, JSON, BSON): *MongoDB, Couchbase, CouchDB, RethinkDB*.
- **Grafos** (redes sociales, geolocalización, optimización de rutas): *Neo4j, Titan, AllegroGraph, OrientDB, InfoGrid, HyperGraphDB*.