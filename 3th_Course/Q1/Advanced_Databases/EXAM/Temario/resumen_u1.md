# Unidad 1 - Introducción a las bases de datos NoSQL

## Introducción: tipos de datos

- Datos estrucutrados - bases de datos sql
- Datos Semiestrucutrados - páginas web, archivos json
- Datos no estructurados - audios y videos / lenguaje natural

> No estructurados: Se necesitan procesos inteligentes para poder acceder a la información
contenida: minería de datos y aprendizaje automático
Estructurados: La información es accesible de forma rápida a través de un sistema o
método de consulta: SQL.
> 

## BBDD Relacionales puntos fuertes

**Persistencia**

- Problema:
• Almacenaje en disco
• ¿Archivos?
- Solución:
• BBDD facilita el acceso a datos específicos
• Método de acceso: consultas

**Concurrencia**

- Problema:
    - Acceso a datos simultaneos
    - Corrupción de datos
- Solución: Transacciones
    - Las consultas se encapsulan en transacciones atómicas
    - Las consultas se ejecutan por completo sin que otras se ejecuten entre medias o se rechazan completamente volviendo al estado inicial.

**Aquí entran las propiedades ACID**

- Atomicidad: se ejecuta todo o nada
- Consistencia: solo se almacena información válida. La integridad de los datos debe
mantenerse una vez finalizado
- Aislamiento: asegura que la ejecución de consultas concurrentes tenga como
resultado el mismo que el de una ejecución secuencia.
- Durabilidad: Una vez finalizado, los datos permanecerán de forma indefinida, incluso
después de un fallo del sistema

Integración 

- Problema:
    - Acceso a la información desde múltiples aplicaciones
- Solución:
    - Interfaz de acceso común para todas las aplicaciones y usuarios.

Modelo Estandarizado

- Problema:
    - mismo problema para multitud de situaciones.
- Solución:
    - Normaliza el modelo relacional con metodologías y modelos conocidos y extensos.

## Impedance Mismatch

El **Impedance Mismatch** (desajuste de impedancia) es el conflicto que surge al intentar conectar dos modelos de datos con filosofías diferentes: el **Modelo Relacional** (tablas, filas y columnas en BD) y el **Modelo Orientado a Objetos** (clases, herencia y memoria).

### XRM - Mapeo Relacional

Proceso por el cual se crea una relación entre la estructura del modelo
relacional y el tipo (X) de modelo de datos en memoria.

- Problema:
    - Existen diferencias estructurales que dificultan encontrar una relación óptima entre
    una base de datos relacional normalizada y la forma de organizar los datos en
    memoria

> Ejemplo: Jerarquía de clases en orientación a objetos
> 

### ORM - Mapeo de objetos relacional

Es la técnica o proceso que crea un puente entre la estructura de la base de datos y los objetos en memoria. Su objetivo es automatizar la conversión de datos para que el desarrollador trabaje solo con objetos.

- **El Problema:** Las bases de datos relacionales son "planas" y normalizadas, mientras que los objetos en memoria suelen ser complejos y jerárquicos.
- **Ejemplo clásico:** La **jerarquía de clases**. SQL no entiende de forma nativa qué es una "subclase"; solo entiende de tablas relacionadas.

## Declive de las BBDD Relacionales

### 1. Aparicion de capas Intermedias

| Problemas  | Soluciones |
| --- | --- |
| El impedance mismatch es uno de los principales motivos del declive de las BBDD relacionales | Creación de Interfaces para eludir las restricciones de estas BBDD |
| Acceso Concurrente en Web | Coordinación de acceso concurrente |

### 2. La llegada de los Clusteres

La aparición del nuevo modelo de negocio en el que toda información recopilada es valiosa también conocido como big data nos ha llevado a incrementar el tamaño de las bbdd.

| Escalado Vertical | Máquinas mas grandes y potentes | Limitación de rendimiento y alto coste |
| --- | --- | --- |
| Escalado Horizontal | Cluster de máquinas estándar | Económico y alta redundancia lo que lo lleva a tolerar mas fallos |

> Por razones evidentes el sector ha optado por el segundo tipo de escalado, su principal problema es que las BBDD relacionales no están diseñadas para trabajar en clusteres.
> 

![image.png](attachment:125b183b-fa64-4bcb-9e59-8d0dba827f72:3ca5da7f-4fd0-4e6f-a5a4-209190587a1d.png)

## Introducción: NoSQL

NoSQL = Not only SQL = NoREL = BBDD no relacionales

¿Qué cambia respecto a sus predecesoras?

- Desaparece el modelado por tablas
- mismo tipo de datos para todos los elementos de una entidad
- Relaciones entre entidades

¿Lo malo?

Se pasa a no garantizar plenamente las propiedades ACID ya que se potencia la facilitación de acceso a datos y almacenamiento en clusteres y solo es necesaria una consulta para acceder a estos datos agregados, por tanto este sistema predominante es el modelado de datos agregado. 

### Motivación de la BBDD NoSQL

- Simplicidad
    - Simplificación de las bases de datos
    - Simplificación del diseño de bases de datos
    - Simplificación del uso y mantenimiento de bases de datos
- Diseñado para modelar los datos como van a ser accedidos, no como van a ser almacenados
- Escalabilidad horizontal
- Desarrollo ágil
- Cambios continuos en los modelos
- Bases de datos no estructuradas (schemaless)
- Modelado relacional no resuelve el problema
- Rendimiento
    - Big data
    - Aplicaciones web en tiempo real
- Diseñado para los paradigmas de programación actuales

## The Polyglot persistence

La **persistencia políglota** (*polyglot persistence*) es un patrón de arquitectura de software que consiste en utilizar **múltiples tecnologías de almacenamiento de datos** dentro de una misma aplicación o sistema, seleccionando cada una según su capacidad para resolver un problema específico.

Pese a las ventajas de las BBDD noSQL las relacionales no significa que vayan a desaparecer, por ello siguiendo el patrón mencionado se usan con otro enfoque: 

- En puntos concretos y críticos
- Se incentiva el uso de otras eligiendo la óptima para cada problema
- Pasamos a combinar varias BBDD utiles dentro de un único sistema.

### Clasificación:

- Documentos
- Clave valor
- Columnas
- Grafos
- Orientadas a objetos
- Multimodales
- Grid y cloud
- XML
- Multi Dimensión
- Multi valor
- Eventos
- Red

## BBDD Orientadas a documentos

Nacen de la vertiente de bases no SQL, y se organizan en documentos (definidos como conjuntos de datos pertenecientes a una unidad), usan un modelado similar a JSON. 
Esto les permite ser mas accesibles frente a las relacionales añadiendo la posibilidad de agurpar datos dentro de un mismo documento y darles acceso por claves mediante identificadores y/o variables indexadas 

Ejemplos: MongoDB, RethinkDB…

![image.png](attachment:e6814235-6e44-4182-8405-07a4911a2091:image.png)

## BBDD Orientadas a clave-valor

Utilizan arrays asociativos clave - valor de tal manera que solo existe un valor para una misma clave, su principal metodo de implementación es mediante mapas hash y arboles binarios. 

Usan el modelo agregado pudiendo contener todo tipo de datos, sean variables, listas, conjuntos o otros arrays asociativos. 

Ejemplos: Redis o Riak. 

![image.png](attachment:f36ddc90-6bc3-49ac-9fe3-11d269748c40:image.png)

## BBDD Orientadas a Columnas

Tienen una cierta similitud con las bases de datos relacionales, poseen una tupla que consta de un nombre de columna único, un dato y un timestamp para verificar la validez del dato.

A diferencia de las BBDD relacionales, las filas aquí no tienen porque tener las mismas columnas, pudiendo existir una columna para una fila y no para otra, además las columnas pueden variar a lo largo del tiempo de vida del conjunto de datos y por último los datos se pueden agregar.

Ejemplos: Cassandra, Hbase..

![image.png](attachment:cc7f8dc8-91a6-4aa0-9e00-ce1111a0001b:image.png)

## BBDD Orientadas a Grafos

El objetivo de estas BBDD es el de modelar relaciones de forma sencilla, basan su estrucutra en la teoría de grafos donde se usan nodos, aristas y propiedades para modelar la información, siendo los nodos las entidades, las aristas las relaciones y las propiedades el tipo de relación. 

La busqueda de indices aqui pierde protagonismo ya que la información esta interconectada, siendo esto muy eficiente en conjuntos de datos asociativos. 

Ejemplos: Neo4J y Titan. 

![image.png](attachment:bf3d6fbf-43a0-4db9-8bc8-67ec468e1b83:image.png)

## BBDD Orientadas a Objetos

En este tipo de base de datos la información se almacena en forma de objetos y se aproxima a las bases de datos para progrmación orientada a objetos, siendo especialmente útiles para modelar datos de alta complejidad, las relaciones se representan mediante punteros entre objetos. 

Ejemplos: Cache, DB4o …

![image.png](attachment:89b84b12-4d32-4e18-bba5-5289fb379eb3:image.png)

## BBDD multimodales

Este tipo de base de datos combina técnicas pertenecientes a varios tipos de BBDD vistos en los puntos anteriores. 
Ejemplos: 

- Documentos - Clave Valor: Amazon DynamoDB
- Documentos y Grafos: OrientDB