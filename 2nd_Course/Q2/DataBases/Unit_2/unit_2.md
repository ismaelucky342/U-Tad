# Unidad 2

# Modelo de Datos Relacional

## Reglas de Codd

Durante los comienzos de las bases de datos Relacionales no había un consenso de lo que era o nbo una base de datos relacional hasta que Edgar Codd desarrolló una serie de pautas “Las reglas codd” . 

Codd demostró que estas bases de datos limitaban en gran medida los tipos de operaciones que los usuarios podían realizar sobre los datos, que estas eran muy vulnerables a cambios en el entorno físico y que si se añadían controladores de un nuevo disco al sistema los datos para su movimiento de una localización física a otra requerían de una conversión. 

Nace así la primera generación de los SGBD referenciando 13 reglas fundamentales (la 0 incluida): 

**Regla 0**

- El sistema de base de datos relacional debe utilizar sus facilidades relacionales (exclusivamente) para manejar la base de datos.
- Todo en una base de datos está guardado en un sistema relacional y cualquier elemento (usuario, tabla, índice, etc.) se guarda dentro de la misma base de datos.

**Regla 1. Regla de la información**


- Toda la información en la base de datos es representada unidireccionalmente, por valores en posiciones de las columnas dentro de filas de tablas.
- Toda la información en una base de datos relacional se representa explícitamente como valores en tablas. No hay información que no esté en tablas.
- Los metadatos (diccionario, catálogo) se representan y se manipulan exactamente igual que los datos de usuario, pudiéndose usar el mismo lenguaje.
- Todo atributo en una tabla tiene un dominio, el cual representa el conjunto de valores que el mismo puede tomar.

**Regla 2. Del acceso garantizado**

- Todos los datos deben ser accesibles sin ambigüedad. Cada valor individual en la base de datos debe ser direccionable especificando el nombre de la tabla, la columna que lo contiene y la clave primaria.
- Significa que todo dato puede ser ubicado teniendo el nombre de la tabla, el nombre del campo y el registro del que se trate.

**Regla 3. Tratamiento de valores nulos**

- El sistema de gestión de base de datos debe permitir que haya campos nulos.
- Debe tener una representación de la «información que falta y de la información inaplicable», distinto de todos los valores regulares.
- Los valores nulos *(que son distintos de la cadena vacía, blancos, 0)* se soportan en los SGBD totalmente relacionales para representar información desconocida o no aplicable de manera sistemática, independientemente del tipo de datos.
- En la práctica es decisión del que diseña la base de datos el utilizar esta posibilidad o no.
- Hay problemas para soportar los valores nulos en las operaciones relacionales, especialmente en las operaciones lógicas ya que se juega con tres valores (veremos en el tema de SQL)

**Regla 4. Catálogo basado en el modelo relacional**

- El sistema debe soportar un catálogo en línea (la estructura misma de la base de datos).
- El catálogo relacional debe ser accesible a los usuarios autorizados.
- En varios motores de base de datos se denomina **esquema.**
- La información de tablas, campos, índices, vistas, permisos de acceso de usuarios autorizados, etc., debe ser almacenada exactamente de la misma manera que los datos de la base de datos, es decir, en tablas específicas.

**Regla 5. Regla comprensiva del sub-lenguaje de los datos**

- El SGBD debe soportar por lo menos un lenguaje relacional que:
    - Tenga una sintaxis lineal.
    - Pueda ser utilizado de manera interactiva.
    - Soporte operaciones de definición de datos, operaciones de manipulación de datos (actualización, así como la recuperación), seguridad e integridad y operaciones de administración de transacciones.
    - Disponga de interfaces amigables (siempre debe de haber una manera de hacerlo todo de manera textual) para hacer consultas, etc.

Este punto es el punto de partida del lenguaje SQL tal y como se conoce actualmente.

**Regla 6. Regla de actualización**

- Todas las vistas que son teóricamente actualizables deben ser actualizables por el sistema, de manera transparente; es decir, que, si en la base de datos se crea una vista de una tabla, se podría añadir un registro a la vista y eso significaría que se daría de alta el registro en la tabla original

**Regla 7**

- Alto nivel de inserción, actualización y borrado, permitiendo el sistema realizar manipulación de datos de alto nivel, es decir, sobre conjuntos de registros.
- Esto significa que, además de leer muchos registros, se puede actualizar más de un registro a la vez, no sólo sobre registros individuales.
- Las cláusulas **SELECT, UPDATE, DELETE** e **INSERT** deben estar disponibles y operables sobre los registros, independientemente del tipo de relaciones y restricciones que haya entre las tablas.

**Regla 8. Independencia física de los datos**

- Los clientes (aplicaciones, sistemas) permanecen inalterados a nivel lógico cuando se realicen cambios en las representaciones de almacenamiento o métodos de acceso.
- Ante cualquier cambio en la ubicación física de los datos, las querys escritas y probadas no deben requerir modificaciones por dichos cambios en la ubicación física.
- El modelo relacional es un modelo lógico de datos, y oculta las características de su representación física.

**Regla 9. Independencia lógica de los datos**

- La independencia lógica de los datos especifica que los programas de aplicación deben ser independientes de la estructura lógica, por lo tanto, los cambios en la estructura lógica (tablas, columnas, índices,…) no deben modificar estos programas de aplicación.
- La independencia de datos lógica es más difícil de lograr que la independencia física de datos, pero también debe ser posible que las querys que ya están escritas (si se modifica un tipo de dato, se añaden campos, se eliminan campos que no se requieren) no requieran cambios.

**Regla 10. Independencia de la integridad**

- Las reglas de integridad se deben especificar por separado de los programas o aplicaciones y se almacenan en la base de datos.
- Debe ser posible cambiar esas reglas sin afectar innecesariamente las aplicaciones existentes.

**Regla 11. Independencia de la distribución**

- El sistema debe poseer un lenguaje de datos que pueda soportar que la base de datos esté distribuida físicamente en distintos lugares sin que esto afecte o altere a los programas de aplicación y sea transparentes para los usuarios.
- Los usos existentes deben continuar funcionando con éxito:
    - Cuando una versión distribuida del DBMS se introduce por primera vez.
    - Cuando los datos existentes se redistribuyen de forma completa.
    - En términos reales, el usuario final o el desarrollador no debe de preocuparse por la partición en la que estén los datos, el motor de base de datos debe saber dónde se encuentra cada dato y extraerlo o manipularlo cuando una query lo requiera.

**Regla 12. Regla de la no subversión**

- Si un sistema relacional tiene un lenguaje de bajo nivel (un registro de cada vez), ese bajo nivel no puede ser usado para saltarse (subvertir) las reglas de integridad y los limitantes expresados en los lenguajes relacionales de más alto nivel (una relación (conjunto de registros) de cada vez).

## Esquema y ocurrencia en una base de datos

Como se había comentado en el tema anterior, a la descripción de una base de datos mediante un modelo de datos se le denomina ***esquema de la base de datos.*** El esquema de base de datos son colecciones de esquemas de relaciones junto con las restricciones de integridad que se definen sobre las relaciones.

Este esquema se especifica durante el diseño y dicho diseño no suele sufrir importantes modificaciones a diferencia de los datos que se almacenan en la base de datos, que sí cambian con mucha frecuencia: se insertan datos, se actualizan, se borran, etc. Los datos que la base de datos contiene en un determinado instante conforman el ***estado de la base de datos*** o también llamada ***ocurrencia de la base de datos.***

**Ejemplo**

Cuando se define una nueva base de datos, especificamos su esquema al SGBD y en este instante el **estado de la base de datos es vacío,** es decir que no tiene datos.

Cuando se cargan datos por primera vez, **la base datos pasa al *estado inicial.*** De ahí en adelante, siempre que se realice una operación de actualización de la base de datos, se tendrá un nuevo estado.

Como ya se había comentado, el SGBD almacena el esquema en su ***catálogo o diccionario de datos,*** de modo que sea accesible siempre que sea necesario.

***El modelo relacional representa la segunda generación de los SGBD donde todos los datos están estructurados a nivel lógico como tablas formadas por filas y columnas, aunque a nivel físico pueden tener una estructura completamente distinta.***


**Relación:** Cuentas bancarias con columnas, “numero_cuenta” y “saldo” y que contiene 7 tuplas de datos. 

Un punto a favor del modelo relacional es la ***sencillez de su estructura lógica*** que tiene por detrás un fundamento teórico sólido, del que carecen los SGBD de primera generación.

Las relaciones manejan tres elementos básicos:

- **Atributo (Ai):** Elemento susceptible de tomar valores (cada una de las columnas de la tabla).
- **Dominio (Di):** Conjunto de valores que puede tomar un atributo (se considera finito).
- **Tupla:** Cada uno de los elementos que contiene una instancia de la relación (filas).

En una relación hay que distinguir dos aspectos:

- **Esquema de la relación:** Los atributos A1..An
    - Ejemplo: Trabajadores (id_trabajador, nombre, horario, puesto, provincia)
- **Instancia de la relación:** El conjunto de tuplas {(x1,x2,..,xn)} ⊆ D1×D2×..×Dn que la componen en cada momento.

Como se indicaba anteriormente, una instancia u ocurrencia sobre un esquema (R), formalmente se denota como r(R), es referida a los valores actuales de dicha relación especificada a través de una tabla.

# Estructura de datos relacional

La estructura de datos del modelo relacional es la ***relación.*** Veremos a continuación esta estructura de datos junto con sus propiedades, tipos de relaciones y qué papel juegan las claves en las relaciones. Para facilitar la comprensión a los alumnos primero describiremos las definiciones “informales” para después pasar a las definiciones formales.

### Relaciones

El modelo relacional (definición informal) se basa en el concepto matemático de relación, que gráficamente se representa mediante una tabla, como la vista en la imagen anterior.

***Una relación es una tabla con columnas y filas.***

El SGBD tiene como función que el usuario perciba la base de datos como un conjunto de tablas.

Esta percepción del usuario afecta sólo a la estructura lógica de la base de datos, no se aplica a la estructura física de la base de datos, que se puede implementar con distintas estructuras de almacenamiento físico dependiendo del medio de almacenamiento.

***Un atributo es el nombre de una columna de una relación.***

En el modelo relacional, las relaciones se utilizan para almacenar información sobre los objetos que se representan en la base de datos.

Una relación se representa gráficamente como una tabla bidimensional en la que las filas corresponden a registros individuales y las columnas corresponden a los campos o atributos de

esos registros.

Los atributos pueden aparecer en la relación en cualquier orden.

**Ejemplo práctico:**

La información de los clientes de una empresa determinada se representa mediante la relación **CLIENTES:**


Columnas/Atributos:

- **codCliente** (código del cliente)
- **nombre_apellidos** (nombre y apellidos del cliente)
- **direccion** (calle y número donde se ubica el cliente)
- **codPostal** (código postal correspondiente a la dirección del cliente)
- **codLocalidad** (código de la localidad o población del cliente)

Tenemos otra relación de LOCALIDADES:


Columnas/Atributos:

- **codLocalidad** (código de la localidad o población)
- **nombreLocalidad** (nombre de la localidad o población)
- **codProvincia** (código de la provincia en que se encuentra la localidad)

Un **dominio** es el conjunto de valores válidos de uno o varios atributos. Cada atributo de una base de datos relacional se define sobre un dominio, pudiendo haber varios atributos definidos sobre el mismo dominio.

Los dominios de los atributos de la relación CLIENTES serían:


Los dominios permiten a los usuarios definir, el significado y la fuente de los valores que los atributos pueden tomar. Esto hace que haya más información disponible para el sistema cuando éste va a ejecutar una operación relacional, de modo que las operaciones que son semánticamente incorrectas, no se puedan realizar.

Se exigirá que, para todas las relaciones, los dominios de todos los atributos deben ser atómicos.

Un dominio es atómico si los elementos del dominio se consideran unidades indivisibles.

Un valor de dominio que es miembro de todos los dominios posibles es el valor nulo, que indica que el valor es desconocido o no existe.

***Una tupla es una fila de una relación.*** Los elementos de una relación son las tuplas o filas de la tabla.

En la relación CLIENTES, cada tupla tiene cinco valores, uno para cada atributo.

Las tuplas de una relación no siguen ningún orden.

***El grado de una relación es el número de atributos que contiene.***

La relación CLIENTES es de grado cinco porque tiene cinco atributos. Esto quiere decir que cada fila de la tabla es una tupla con cinco valores. El grado de una relación puede cambiar al aumentar o disminuir los atributos de la tabla, pero su modificación es poco frecuente.

***La cardinalidad de una relación es el número de tuplas que contiene.*** Este número varia constantemente ya que en la relación se van borrando tuplas o insertando.

**En este punto podemos decir que una base de datos relacional es un conjunto relaciones normalizadas, esto es, que la intersección de cada fila con cada columna hay un solo valor.**

Si ahora nos centramos en una definición formal de relación, podemos decir que una relación R definida sobre un conjunto de dominios D1, D2 , . . . , Dn consta de:

***Cabecera:*** conjunto fijo de pares **atributo:dominio** {(A1 : D1), (A2 : D2), . . . , (An : Dn)} donde cada atributo Aj corresponde a un único dominio Dj y todos los Aj son distintos, es decir, no hay dos atributos que se llamen igual.

El grado de la relación R es n.

***Cuerpo:*** conjunto variable de tuplas. Cada tupla es un conjunto de pares *atributo:valor :*

{(A1 : vi1), (A2 : vi2), . . . , (An : vin)} con i = 1, 2, . . . , m, donde m es la cardinalidad de la relación R.

En cada par (Aj : vij ) se tiene que vij ∈ Dj .

Como ya se ha visto en la definición anterior, los nombres de las columnas corresponden a los nombres de los atributos, y las filas son cada una de las tuplas de la relación. Los valores que aparecen en cada una de las columnas pertenecen al conjunto de valores del dominio sobre el que está definido el atributo correspondiente.

### Propiedades de las Relaciones

Las relaciones tienen las siguientes características:

- Cada relación tiene un nombre, y éste es distinto del nombre de todas las demás relaciones.
- Los dominios sobre los que se definen los atributos son escalares, por lo que los valores de los atributos son atómicos. De este modo, en cada tupla, cada atributo toma un solo valor. Se dice que las relaciones están normalizadas.
- No hay dos atributos que se llamen igual.
- El orden de los atributos no importa: los atributos no están ordenados.
- Cada tupla es distinta de las demás: no hay tuplas duplicadas.
- El orden de las tuplas no importa: las tuplas no están ordenadas.

### Tipos de Relaciones

En un SGBD relacional hay dos tipos de relaciones:

- **Relaciones base.** Son relaciones reales que tienen nombre, y forman parte directa de la base de datos almacenada(Tablas).
- **Vistas.** También denominadas relaciones virtuales, es decir, que se obtienen a partir de otras relaciones; se representan mediante su definición en términos de esas otras relaciones. Las vistas no poseen datos almacenados propios, los datos que contienen corresponden a datos almacenados en relaciones base.

### Claves

Como en una relación no hay tuplas repetidas, éstas se pueden distinguir unas de otras, es decir, se pueden identificar de modo único. La forma de identificarlas es mediante los valores de sus atributos.

**Clave candidata**

Conjunto de atributos que permiten identificar de forma única cada tupla de la relación. Es decir, columnas cuyos valores no se repiten para esa tabla. Ejemplos: codCliente, DNI, NIF,…

Cuando una clave candidata está formada por más de un atributo, se dice que es una clave compuesta. Una relación puede tener varias claves candidatas.

**Clave primaria (Primary Key)**

Clave candidata que se escoge como identificador de las tuplas (identificación de forma única). Se elige como primaria la candidata que identifique mejor a cada tupla en el contexto de la relación.

Como una relación no tiene tuplas duplicadas, siempre hay una clave candidata y, por lo tanto, la relación siempre tiene clave primaria. En el peor caso, la clave primaria estará formada por todos los atributos de la relación, pero normalmente habrá un pequeño subconjunto de los atributos que haga esta función.

*Sólo puede haber una columna con clave primaria por tabla.*

**Ejemplo1:** En una relación EMPLEADOS, si tenemos DNI y codEmpleado, sería por contexto elegir codEmpleado como clave primaria.

**Ejemplo2:**


**Clave alternativa**

Cualquier clave candidata que no sea primaria y que también puede identificar de manera única una tupla. En el momento de crear la relación como tabla en la Base de Datos se debe definir una constraints de tipo UNIQUE.

**Clave externa, ajena o foránea (Foreign Key)**

Atributo cuyos valores coinciden con una clave candidata (normalmente primaria) de otra tabla.

Las claves ajenas representan *relaciones entre datos.*

Ejemplo:

En la relación LOCALIDADES, el atributo nombreLocalidad no es una clave candidata ya que hay localidades en España con el mismo nombre que se encuentran en distintas provincias.

Sin embargo, se ha asignado un código único a cada localidad, por lo que el atributo codLocalidad sí es una clave candidata de la relación LOCALIDADES.

Para identificar las claves candidatas de una relación no hay que fijarse en un estado u ocurrencia de la base de datos. El hecho de que en un momento dado no haya duplicados para un atributo o conjunto de atributos, no garantiza que los duplicados no sean posibles.

Sin embargo, la presencia de duplicados en un estado de la base de datos sí es útil para demostrar que cierta combinación de atributos no es una clave candidata.

El único modo de identificar las claves candidatas es conociendo el significado real de los atributos, ya que esto permite saber si es posible que aparezcan duplicados (contexto de los atributos).

Sólo usando esta información semántica se puede saber con certeza si un conjunto de atributos, forman una clave candidata.

Viendo la ocurrencia anterior de la relación CLIENTES se podría pensar que el atributo **nombre_apellidos** es una clave candidata. Pero ya que este atributo es el nombre+apellidos de un cliente y es posible que haya dos clientes con el mismo nombre+apellidos, el atributo no es una clave candidata.

En la relación CLIENTES sólo hay una clave candidata que es el atributo codCliente, por lo que esta clave candidata es la clave primaria.

Ejemplo:

El atributo codLocalidad de CLIENTES relaciona a cada cliente con su localidad.

Este atributo en CLIENTES es una clave ajena cuyos valores hacen referencia al atributo codLocalidad de LOCALIDADES (su clave primaria). Se dice que un valor de clave ajena representa una referencia a la tupla que contiene el mismo valor en su clave primaria (tupla referenciada).

Al hablar de claves primarias y de claves ajenas es importante darse cuenta de que los valores de una clave primaria no se pueden repetir, mientras que no sucede lo mismo con las claves ajenas que le hacen referencia.

Así, no es posible encontrar dos tuplas con el mismo valor en **LOCALIDADES.codLocalidad** (cada localidad debe aparecer en la relación una sola vez), pero sí es posible encontrar varias tuplas con el mismo valor en **CLIENTES.codLocalidad,** ya que es posible que haya varios clientes que se ubiquen en la misma localidad. (En los datos ejemplo no aparecen, pero podrían aparecer).

Ejemplo: En este ejemplo tenemos 3 relaciones (tablas) con:

ORDERS:

```
PK: orderNumber
```

ORDERDETAILS:

```
PK: orderNumber+productCode
FK: productCode(orderdetails) à productCode(products)
FK:orderNumber(orderdetails) à orders(orderNumber)
```

PRODUCTS:

```
PK: prodcutCode
```


## Diseño de la Bases de Datos Relacionales

La metodología de diseño de bases de datos relacionales de centra en mantener la independencia de la plataforma hardware/software. Dicha metodología se concreta en las siguientes etapas de diseño:

- Diseño conceptual: Su objetivo es definir las entidades y las relaciones entre ellas deforma abstracta, sin centrarse en ningún modelo lógico que posteriormente se vaya a utilizar. Se suele utilizar el modelo E/R para la realización de un esquema conceptual.
- Diseño lógico:  Su objetivo es definir el esquema de la base de datos según el modelo que implementa el SGBD objetivo. (En este nos centraremos). Se obtendrá un modelo lógico según el SGBD seleccionado y nos apoyaremos en un proceso de normalización (se verá en el último apartado de la unidad) para validar la calidad del mismo.
- Diseño físico: Su objetivo es definir el esquema físico de la base de datos de forma que se den todas las instrucciones para que un DBA pueda implementar la base de datos sin ninguna ambigüedad.


En la imagen anterior, se enmarca con un rectángulo rojo, donde vamos a centrar el desarrollo de este apartado, es decir en el diseño lógico, donde a partir de un modelo E/R se transforma en un conjunto de tablas del modelo relacional.


### **Transformación modelo E-R a un modelo relacional**

Para llevar a cabo la transformación se aplican un conjunto de reglas cuyo objetivo final es la obtención del modelo relacional.

**Entidades**

- **Entidad fuerte:**
    - Se debe crear una tabla para cada entidad fuerte, incluyendo todos sus atributos simples.
    - Cada uno de los identificadores de la entidad será una clave candidata.
    - De entre las claves candidatas hay que escoger la clave primaria; el resto serán claves alternativas.


Se generaría la siguiente tabla en el modelo relacional:

ALUMNO(id, nombre, apellido1, apellido2, nif, grupo)

- **Entidad débil:**
    - Atributos: Además de los atributos propios de la entidad débil, los atributos pertenecientes a la clave primaria de la entidad fuerte de la que depende existencialmente la entidad débil.


La entidad Apunte se convierte en una relación formada por los siguientes atributos Apunte (CCC, numero, descripción, importe)

- Claves:

La **clave primaria** de la entidad débil, Apunte, sería, la clave primaria de la entidad fuerte más un conjunto de atributos propio de la entidad débil (discriminante). En este caso CCC+numero

Apunte (**CCC, número,** descripcion, importe)

La **clave externa** sería una, haciendo referencia a la entidad fuerte de la que depende existencialmente la entidad débil.


- En las **relaciones 1:N**  y la clave primaria de la entidad que participa con cardinalidad 1 pasará a formar parte de la tabla de entidad que participa con cardinalidad N, y además pasará como un atributo.
    
    No generan una tabla
    
En este caso la clave primaria de la entidad que participa en la relación con cardinalidad **1** se guarda en la tabla de la entidad que participa con cardinalidad **N.**

USUSARIO(**id,** email, password, nombre, apellido1, apellido2)

VÍDEO(**id**, nombre, descripción, duración, id_usuario)

id_usuario (FK) à USUARIO(id)

- **En una relación 1:1**  y la clave primaria de una entidad pasará a formar parte de la tabla de la otra entidad, y pasará como un atributo.
    
    No genera tabla nueva
    

Ejemplo:


Como la participación de **Usuario** es de **(1,1)** y la de **Canal YouTube** es de **(0,1)**, la clave primaria de **Usuario** se almacena en la tabla de **Canal YouTube** como un atributo. El atributo id_usuario que se añade en la tabla **Canal_YouTube** es una **clave ajena(FK)** de la tabla **Usuario.**

Las tablas del modelo relacional quedarían así:

**USUARIO(id,** email, password, nombre, apellido1, apellido2)

**CANAL_YOUTUBE(id**, nombre, descripción, fecha_creación, id_usuario)

*id_usuario* (FK) - USUARIO(id)

**Excepción:** Sólo existe un caso donde una relación con cardinalidad 1:1 genera una nueva tabla, y será cuando la participación de las dos entidades sea de tipo (0,1)..(0..1).


Cuando la participación de las dos entidades es de (0,1), se puede crear una nueva tabla donde se almacenan las claves primarias de las dos entidades que participan en la relación. La clave primaria de la nueva tabla será́ una de las dos claves ajenas que se reciben.

En este ejemplo tendríamos:

ALQUILER(**id**, fecha_inicio, fecha_fin, importe, fianza)

ALQUILER_RENUEVA_ALQUILER(**id_alquiler**, *id_alquiler_anterior*)

*id_alquiler* (FK) -  ALQUILER(id)

*id_alquiler_anterior* (FK) - ALQUILER(id)

• Toda **relación N:M** en este caso se crea una nueva tabla donde se almacenan las claves primarias de las dos entidades que participan en la relación. Las claves primarias de las entidades también serán claves primarias de la nueva tabla. Si la relación contiene algún atributo, se deberán añadir a la nueva tabla.


Las tablas en el modelo relacional quedarían:

ALUMNO(**id**, nombre, apellido1, apellido2, nif, grupo)

EXAMEN_TEÓRICO(**id**, título, número_preguntas, fecha)

ALUMNO_HACE_EXAMEN_TEÓRICO(**id_alumno, id_examen,** nota)

*id_alumno* (FK) -  ALUMNO(id)

*id_examen* (FK) - EXAMEN(id)

## Restricciones de Integridad

Una vez definida la estructura de datos del modelo relacional, veremos a continuación las reglas de integridad que los datos almacenados en la estructura de datos deben cumplir para garantizar que son válidos. Al definir cada atributo sobre un dominio se imponer una restricción sobre el conjunto de valores permitidos. 

Además existen dos reglas de integridad que deben cumplir en todas las bases de datos relacionales y en todos su estados: 

- Regla de integridad de entidades
- Regla de Integridad referencial

En las reglas de integridad es importante tener en cuenta los valores nulos.

### Valores Nulos

Cuando en una tupla un atributo es desconocido, se dice que es *nulo. **Un nulo no representa el valor cero ni la cadena vacía ya que éstos son valores que tienen significado.*** El nulo implica ausencia de información, bien porque al insertar la tupla se desconocía el valor del atributo, o bien porque para dicha tupla el atributo no tiene sentido.

Ya que los nulos no son valores, deben tratarse de modo diferente, lo que causa problemas de implementación y trabajar con los lenguajes de consulta.

MySQL soporta nulos, pero en la práctica, no todos los SGBD relacionales soportan los nulos.

### Regla de integridad de entidades

La primera regla de integridad se aplica a las claves primarias de las relaciones base: ***ninguno de los atributos que componen la clave primaria puede ser nulo.***

Por definición, una clave primaria es una clave que se utiliza para identificar de modo único las tuplas. Las claves primarias son irreductibles, es decir, que ningún subconjunto de la clave primaria sirve para identificar las tuplas de modo único.

Si se permitiese que parte de la clave primaria fuera tuviera valores nulos, se estaría indicando que no todos sus atributos son necesarios para distinguir las tuplas, con lo que se estaría contradiciendo la premisa anterior (irreductible). Esta regla de integridad solamente se aplica a las relaciones base y a las claves primarias, no a las claves alternativas.

### Regla de integridad Referencial

Esta regla de integridad referencial se aplica a las claves ajenas: si en una relación hay alguna clave ajena, sus valores deben coincidir con valores de la clave primaria a la que hace referencia, o bien, deben ser completamente nulos.

**Ejemplo:**

En el ejemplo anterior con las relaciones ORDERS, ORDERSDETAILS y PRODUCTS, dado un pedido (orderNumber) se pueden saber los productos (productCode) que tiene dicho pedido cruzando las tablas ORDERS y ORDERSDETAILS mediante la FK orderNumber(orderdetails) à orders(orderNumber) y a continuación cruzando las tablas ORDERSDETAILS Y PRODUCTS mediante la FK productCode(orderdetails) à productCode(products)

La regla de integridad referencial exige que los valores que aparecen en la clave ajena ORDERSDETAILS.orderNumber aparezcan como clave primaria en ORDERS.orderNumber, de este modo, todos los detalles de los pedidos (orderNumber) ya existirán en la base de datos, dados de alta previamente en la tabla ORDERS. Esto es lógico, no podemos tener en una base de datos, detalles de un pedido que no tenemos dado de alta previamente.

La regla de integridad referencial se enmarca en términos de estados de la base de datos: indica lo que es un estado ilegal, pero no dice cómo puede evitarse.

Por lo tanto, una vez establecida la regla, hay que plantearse qué hacer si estando en un estado legal, llega una petición para realizar una operación que conduce a un estado ilegal.

Existen dos opciones: rechazar o aceptar la operación y realizar operaciones adicionales que conduzcan a un estado legal en la base de datos.

Para hacer respetar la integridad referencial se debe contestar, para cada clave ajena, a las tres preguntas que se plantean a continuación y que determinarán su comportamiento:

- *Regla de los nulos:* ¿Tiene sentido que la clave ajena acepte nulos?
- *Regla de borrado:* ¿Qué ocurre si se intenta borrar la tupla referenciada por la clave ajena?
    - *Restringir:* no se permite borrar la tupla referenciada.
    - *Propagar:* se borra la tupla referenciada y se propaga el borrado a las tuplas que la referencian mediante la clave ajena.
    - *Anular:* se borra la tupla referenciada y las tuplas que la referenciaban ponen a nulo la clave ajena (sólo si acepta nulos).
    - *Valor por defecto:* se borra la tupla referenciada y las tuplas que la referenciaban ponen en la clave ajena el valor por defecto establecido para la misma.
- *Regla de modificación:* ¿Qué ocurre si se intenta modificar el valor de la clave primaria de la tupla referenciada por la clave ajena?
    - *Restringir:* no se permite modificar el valor de la clave primaria de la tupla referenciada.
    - *Propagar:* se modifica el valor de la clave primaria de la tupla referenciada y se propaga la modificación a las tuplas que la referencian, mediante la clave ajena.
    - *Anular:* se modifica la tupla referenciada y las tuplas que la referenciaban ponen a nulo la clave ajena (sólo si acepta nulos).
    - *Valor por defecto:* se modifica la tupla referenciada y las tuplas que la referenciaban ponen en la clave ajena el valor por defecto establecido para la misma.

Si ahora continuamos con el ejemplo de las relaciones CLIENTES y LOCALIDADES y añadimos otra relación de FACTURAS con la siguiente estructura:


Tenemos que dado un cliente (codCliente) podemos averiguar las facturas emitidas hacia él y la fecha de la misma. FACTURAS.codCliente es una FK de CLIENTES.codCliente(PK).

Como decíamos, tenemos que determinar cuál es el comportamiento de cada clave ajena, pues bien, nos vamos a centrar en esta última indicada en las líneas anteriores. Plantearemos el siguiente comportamiento:

- *Regla de los nulos:* la clave ajena acepta nulos, por lo que es posible encontrar facturas cuyo cliente se ignore (esto se ha decidido así porque lo impone un requisito del usuario).
- *Regla de borrado:* anular. Cuando se elimine un cliente de la base de datos y se proceda a borrarlo de la relación CLIENTES, se deberán anular todas las referencias que hubiera desde FACTURAS.codCliente. De este modo, todas las facturas que tenía ese cliente pasarán a tener un nulo en el código del cliente.
- *Regla de modificación:* propagar. En caso de que se modifique el código a un cliente (quizá porque el sistema de codificación se cambie por parte de la empresa), todas las facturas de dicho cliente actualizarán el valor de FACTURAS.codCliente para continuar haciendo referencia a la misma tupla.

Del mismo modo, se deberá escoger reglas para el resto de las claves ajenas de la base de datos.

Una vez establecidas todas las reglas, el sistema se comportará de manera coherente obedeciendo a todas las reglas impuestas.

# Normalización

La normalización de base de datos es una técnica de modelado consistente en aplicar una serie de reglas a las relaciones obtenidas tras el paso del modelo entidad-relación al modelo relacional, de forma que se consigue una base de datos normalizada donde:

- Las actualizaciones se consiguen realizar con un número mínimo de operaciones (mejorando la eficiencia de la BD y reduciendo la posibilidad de que aparezcan inconsistencias).
- Se reduce al mínimo el espacio de almacenamiento necesario para almacenar los datos de la BD (ahorro económico).

La descomposición sin perdidas es indispensable, la descomposición que preserva las dependencias no siempre es posible.

En la práctica se usa hasta la forma normal de Boyce/Codd, aunque en general, los diseños prácticos exigen al menos 3FN (que será hasta donde veamos).

Para entender el proceso de normalización es necesario entender una serie de conceptos:

- **Dependencia Funcional:** Describe relaciones entre los atributos de una relación: B depende funcionalmente de A **(A→B)** cuando cada valor de A en una relación R aparece siempre asociado al mismo valor de B en R.

Ejemplo 1: DNI → Nombre_Apellidos

Ejemplo 2:


- **Dependencia funcional transitiva:** Una dependencia funcional X → Y es una dependencia funcional transitiva si existe un conjunto de atributos Z que ni forman clave candidata ni son subconjunto de ninguna clave y además se cumple X → Z y Z → Y.

**Ejemplo:**

Fecha de nacimiento → Edad

Edad → Conducir

***Fecha de nacimiento → Conducir***

### **Primera forma Normal (1FN)**

Una tabla está en primera forma normal si sus atributos contienen valores atómicos (esto quiere decir que tienen que ser indivisibles, se evitan atributos multivalorados, compuestos y sus combinaciones) y no hay registros repetidos (sin redundancia).

Si consideramos la relación CENTROS, con las columnas y tuplas indicadas a continuación, vemos que teléfono tiene varios valores y por tanto no cumpliría la premisa de “valores atómicos” sino que serían atributos multivalorado:


Solución para satisfacer la premisa y cumplir con la primera forma normal, hay tres opciones:

Eliminar el atributo teléfonos y crear una nueva relación que asocie en cada fila un centro con un teléfono. La clave de la primera relación debe formar parte de la clave de la segunda relación.

*En este caso, en la segunda relación la PK sería codCentro+teléfono.*


Ampliar la clave de la relación de manera que incluya al atributo multivalorado.

*En este caso, la PK sería codCentro+teléfono.*


Si se conoce la cardinalidad máxima del atributo multivalorado (números de teléfono máximo que puede tener un centro), se pueden crear tantas columnas como la cardinalidad máxima. Presenta como inconveniente el uso de valores Null.


### **Segunda forma Normal (2FN)**

Una tabla se considerará que está en 2FN cuando cumpla:

- Está en 1FN
- Si cada atributo que no forme parte de la clave primaria depende funcional y completamente de cada clave. Para recuperar un atributo no clave, se necesita acceder por la clave completa, no por una subclave.

Las 2FN aplican a las relaciones con **claves primarias compuestas por dos o más atributos.**

Un esquema que no se encuentre en segunda forma normal puede traducirse en varios esquemas que sí lo estén. El procedimiento de normalización es crear tantas nuevas relaciones como dependencias funcionales no sean completas.

Si partimos de la siguiente relación, siendo PK (codEmpleado):


A nivel de dependencias funcionales, la edad depende de codEmpleado, pero el puesto depende solamente de la categoría, por tanto, para solucionarlo:

- Eliminar los atributos con dependencias incompletas.
- Crear nueva tabla con los atributos y la clave de la que depende.


### **Tercera forma Normal (3FN)**

Una tabla está en 3FN si:

- Está en 2FN
- Todos los atributos que no son clave primaria no dependen transitivamente de ésta.

Por tanto, hay que buscar dependencias funcionales entre atributos que no estén en la clave.

El procedimiento para normalizar esta relación consiste en descomponerla en los atributos definidos por la dependencia funcional responsable de la transitividad.

Si completamos la relación que teníamos anteriormente:


En este caso, la dependencia transitiva que tenemos:

```
           codEmpleado → categoría
           categoría → puesto
```

En la dependencia categoria – puesto hay dependencia transitiva con la clave primaria(codEmpleado).

De esta manera para que esté la relación en 3FN actuamos sobre los atributos con dependencias transitivas:

- Separar en una tabla adicional los atributos que tienen dependencia transitiva con la clave (puesto) y establecer como Pk el campo que define la transitividad (categoria)


- Se añade el campo “categoria” como *Foreign Key:*


## Desnormalización para el rendimiento

A veces los diseñadores eligen esquemas redundantes (no normalizados), utilizan la redundancia para mejorar el rendimiento para aplicaciones concretas, la penalización sufrida por no emplear un esquema normalizado es el trabajo extra de mantener los datos redundantes consistentes. 

El proceso de tomar un esquema normalizado y hacerlo no normalizado se denomina desnormalización y los diseñadores lo utilizan para ajustar el rendimiento de los sistemas para dar soporte a operaciones críticas. 

Una alternativa mejor es el uso del esquema normalizado y de esta manera poder almacenar en forma de vista materializada toda la información necesaria ya cruzadas las tablas. Aún así esto sigue suponiendo sobrecargas de espacio y tiempo sin embargo conserva la ventaja de conservar la vista actualizada gracias al SGBD. 

# Algebra Relacional

Algebra es un sistema matemático constituido por:

- Operandos: Objetos (valores o variables) del sistema, a partir de los cuales se pueden construir nuevos objetos.
- Operadores: Símbolos del sistema, que generan nuevos objetos a partir de otros.

El álgebra relacional es importante por varias razones: 

- Proporciona un fundamento formal para las operaciones del modelo relacional
- Se utiliza como base para la implementación y optimización de consultas en SGBD relacionales

Este conjunto de operaciones básicas se les llama algebra relacional que permite al usuario especificar tareas de recuperación de datos. 

Una secuencia de operaciones de algebra genera una expresión de algebra relacional cuyo resultado será una nueva relación que represente el resultado de la consulta a la base de datos o una petición de recuperación. 

Por tanto este algebra relacional es un tipo de algebra que: 

- Tiene operandos relacionales o instancias y variables que representan relaciones
- Los operadores además están diseñados para hacer las diferentes tareas que necesitan para manipular relaciones en una DB.

Algebra relacional es un lenguaje de consulta procedimental basado en algebra de conjuntos. 

## Operaciones en Álgebra Relacional

### **Operación de Selección o Restricción**

- Operación que permite seleccionar
    
    un subconjunto de tuplas de una relación que cumplen una condición.
    
- Se puede considerar esta operación como un filtro que obtiene solamente las tuplas que satisfacen el criterio de selección o predicado indicado (WHERE condición).
- Si pensamos en la relación R como una tabla, esta operación devuelve las filas que cumplan la condición indicada en el WHERE.
- Podemos ver esta operación como una proyección horizontal sobre la relación.
- Notación:


Donde:

- R es una expresión del álgebra relacional (nombre de una relación, variable o resultado de operación previa).
- CondicionDeSeleccion: predicado o criterio para filtrar tuplas de R.


**Ejemplo 1 práctico:**

Siendo R la siguiente relación llamada “empleados”, obtener los empleados del departamento de “Finance”.


En la condición de selección se pueden incorporar distintos tipos de operadores:

- Operadores relacionales: (=, ¹, >, ³ , <, £ ). Ejemplo: x > 3
- Operadores lógicos: Ù (and), Ú (or), Ø (not. Ejemplo: x > 3 AND y = ‘Hola’. Ejemplo: (x > 3 Ù y = ‘Hola’)

**Ejemplo 2 práctico:**

Obtener los empleados cuyo salario sea mayor de 80000 y pertenezcan al departamento de Finance.


### **Operación de Proyección**

- Esta operación, siguiendo con el símil entre relación (R) y tabla, devolvería los datos que cumplan las condiciones indicadas, de algunas columnas de la tabla.
- Se
    
    *eliminan resultados duplicados en la relación resultante.*
    
- Esta operación se utiliza cuando requerimos ciertos atributos de la relación y por tanto la podemos ver como una proyección vertical sobre la relación.
- Notación:


Donde:

- **R** es una expresión del álgebra relacional (nombre de una relación, variable o resultado de operación previa).
- **ListaDeAtributos:** atributos de R que vamos a obtener.


**Ejemplo 1 práctico:**

Obtener los name y salary de la relación de empleados.


### **Operación de Renombrado**

Notación: ρ nuevo_nombre(relacion)

Se pueden realizar dos operaciones de renombrado:

- Los atributos de una relación se pueden renombrar para facilitar el manejo de los mismos. En este caso renombramos el atributo ID a ID1 de la relación “empleados”. Nos apoyamos en la operación de asignación (←)

ρ ID1←ID(empleados)

- Es también posible realizar copias de relaciones renombrando o no sus atributos. Renombramos la relación “empleados” a “Nueva_Relacion”.

ρ Nueva_Relacion(empleados)

### **Operación de Unión**

Esta operación recupera todas las tuplas que estén en ambas o en una de ellas, eliminando los duplicados.

- Notación: U
- Hay que tener en cuenta que la unión solo se puede dar con relaciones compatibles. **¿Qué significa que sean compatibles?**
    - La relación R(A1, A2, . . .,An) y S(B1,B2, . . . ,Bn) deben tener la misma aridad, es decir, que ambas relaciones tengan el mismo número de atributos.
    - Los dominios de los atributos i- ésimos de A y de B deben ser iguales.


Ejemplo 2 práctico: Encontrar todos los cursos que han sido enseñados en el semestre “Summer” y año 2017 o los enseñados en semestre “Spring” y año 2018, o en ambos

### **Operación de Intersección**

Esta operación recupera todas las tuplas que estén en ambas relaciones o expresiones de álgebra relacional.

**Ejemplo 1 práctico:**

### **Operación de Diferencia**

La notación es R – S  **(R minus S)** e incluye todas las tuplas que están en R pero no están en la relación S.

- R y S deben ser relaciones compatibles.
- Si existen tuplas duplicadas, se eliminan.
- Si un atributo aparece en ambas relaciones, en el resultado se antepondrá el nombre de la relación de la cual procede para su distinción de otros con mismo nombre.

**Ejemplo 1 práctico:**


### **Operación de Producto Cartesiano**

Denotado por x, permite combinar la información de dos relaciones cualquiera.

Combina cada tupla de una relación con las tuplas de la otra relación. R(A1,A2,…,An) x S(B1,B2,…,Bm) es una relación con n + m atributos Q(A1,A2, . . . ,An,B1,B2, . . . ,Bm).

Dadas las siguientes dos relaciones


### **Operación JOIN**

Esta operación también se puede nombrar como “reunión natural” (Natural Join).

- Se utiliza el símbolo ⋈

Es una operación binaria que permite combinar la selección y producto cartesiano en una sola operación:

- El producto cartesiano de las relaciones indicadas en el argumento.
- Además, se lleva a cabo una selección forzando la igualdad de atributos que en este caso será la clave presente en ambas relaciones (clave y clave foránea)
- Por último, se eliminan los atributos duplicados.

Si tenemos en cuenta las relaciones anteriores, esta operación se escribiría:

**instructor ⋈ instructor.ID = teaches.ID teaches**


### **Operación ASIGNACIÓN**

Se utiliza el operador  ← (En relax utiliza el =)

En ocasiones resulta conveniente escribir una expresión del álgebra relacional por partes utilizando la asignación a una variable de relación temporal. Funciona como una asignación a una variable haciendo un símil con un lenguaje de programación.

Con la operación de asignación, una consulta de álgebra relacional puede ser escrita como un programa con un conjunto de asignaciones seguido de una expresión, que cuando es ejecutada/evaluada muestra los valores resultados de dicha query.

