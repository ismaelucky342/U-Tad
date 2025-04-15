# Unidad 3 

Para comprender lo que puede hacer una base de datos SQL hay que conocer los diferentes tipos de comandos que tiene, que veremos en el desarrollo de este apartado:

- DDL (Data Definition Language)
- DML (Data Manipulation Language)
- DCL (Data Control Language)
- TCL (Transaction Control Language)

## **¿Qué permite SQL sobre una base de datos relacional?**

SQL está diseñado para la administración de SGBD de tipo relacional por lo que no lo podemos considerar un lengiaje de programación pese a tener variables, condicionales y elementos lógicos. 

Las últimas actualizaciones incluyen admeñas nuevas características como la integración de documentos XML o JSON y la búsqueda de filas en base a un patrón predefinido por una expresión regular. El núcleo de SQL es Open Source aunque algunas compañías han realizado ajustes para adecuarlo a sus productos lo cual ha originado las distintas versiones. 

![image.png](attachment:3c3a8d65-3ae4-4b91-aecf-547843da2f79:image.png)

Cuando un SGBD relacional implementa el lenguaje SQL, todas las acciones que se pueden llevar a cabo sobre el sistema se realizan mediante sentencias de este lenguaje.

“Las sentencias de SQL se pueden escribir tanto en mayúsculas como en minúsculas y terminan siempre con el carácter punto y coma (;).”

## Tipos de Datos

En SQL existen una amplia variedad de tipos de datos, si bien, en este apartado se hará una descripción de los tipos de datos SQL aplicables a MySQL, de forma que posteriormente el alumno pueda aplicarlo de forma práctica.

Los tres tipos de datos básicos en MySQL son:

### Tipo texto

![image.png](attachment:48e8f7b0-1317-4360-b634-6f72f46d6acf:image.png)

### Tipo numérico

![image.png](attachment:b27ff7ea-c459-42fc-8d6a-2ee9fd1db0f3:image.png)

### Tipo fecha

![image.png](attachment:da506192-e58f-49c5-a4dd-4b77f69428e6:image.png)

Además de estos tipos de datos, también existe el tipo de datos BOOLEAN (True/False). También recordar, que el nulo no es un valor, sino que implica ausencia de valor.

El nulo se representa mediante NULL y cuando se imprime no se muestra nada.

## Operadores SQL

Los **operadores SQL en MySQL** son símbolos o palabras clave que se usan en las consultas para realizar operaciones sobre los datos. Se pueden clasificar en varias categorías:

### Operadores Lógicos

Los operadores lógicos son AND, OR y NOT. SQL utiliza una lógica booleana de tres valores y la evaluación de las expresiones con estos operadores es la que se muestra en la siguiente tabla:

![image.png](attachment:a22547bc-3b25-4dc8-aff9-22d7548ab36e:image.png)

![image.png](attachment:5e31331f-88b7-4a7f-92d9-09308c2f2c4e:image.png)

Ejemplo: 

```sql
SELECT TRUE, 1, FALSE, 0, NULL;
```

### Operadores de comparación

Los operadores de comparación se utilizan con la cláusula WHERE para determinar qué registros seleccionar.

![image.png](attachment:3e38eb9f-aa28-4eb8-851d-0847028c0550:image.png)

### Operadores matemáticos

+ (suma), - (resta), * (multiplicación), / (división). La división calcula el resultado con decimales; si queremos trabajar con números enteros, también tenemos los operadores DIV (división entera) y MOD (resto de la división).

Ejemplo: 

```sql
SELECT 5/2, 5 div 2, 5 mod 2; 
```

Se pueden realizar también operaciones a nivel de bits (bits trabajan con enteros BIGINT, es decir con 64 bits): >> para desplazar los bits varias posiciones a la derecha, << para desplazar a la izquierda, | para una suma lógica bit a bit (equivalente al operador OR de álgebra de Boole), & para un producto lógico bit a bit y ^ para una operación XOR (equivalente al operador XOR de álgebra de Boole). A modo de ejemplo:

```sql
select 25 >> 1, 25 << 1, 25 | 10, 25 & 10, 25 ^ 10
```

### Operadores de asignación

Permiten la creación de variables de usuario en MySQL, que almacenan datos para ser utilizados en la sesión del usuario. Estas variables cuando termina la sesión se borrar automáticamente.

- Existen 2 formas de crear variables, con la sentencia SET o dentro de la sentencia SELECT usando el operador @.
- Estas variables no tienen tipo, sino que cogen el que asignamos en el valor correspondiente.

Ejemplo: 

```sql
SET @ahora= CURRENT_TIMESTAMP(); 

SELECT @ahora;
```

![image.png](attachment:f93e32a7-b9a0-4e74-af69-94ab288de426:image.png)

```sql
SELECT @variable:="Buneos dñias INSD";
SELECT @variable; 
```

![image.png](attachment:c7ccc2a9-821f-4614-8e5f-75e550c887be:bacf766c-1e75-44d2-8704-62b9f4529dbb.png)

- Existe otras variables (datos de configuración de la base de datos, de la instalación, de las sesiones….), asociadas al sistema MySQL que si son **permanentes y no desaparecen al terminar la sesión..** (SHOW VARIABLES)

```sql
SELECT * FROM performance_schema.user_variables_by_thread; 
```

![image.png](attachment:cb2374c3-6903-48e9-a8ec-9c222374cea7:351c9b83-0d36-40ee-bcda-65f3be51aff1.png)

## Tipos de Comandos

### **DDL (Data Definition Language)**

Los comandos **DDL** se utilizan para definir y modificar la estructura de la base de datos, incluyendo tablas, índices y relaciones entre datos. Este tipo de comandos permiten la creación, modificación y eliminación de objetos dentro de la base de datos.

Ejemplos de comandos **DDL**:

- `CREATE` – Crea nuevas bases de datos, tablas, índices o vistas.
- `ALTER` – Modifica la estructura de una tabla existente.
- `DROP` – Elimina una base de datos, tabla, índice o vista.
- `TRUNCATE` – Elimina todos los registros de una tabla sin afectar su estructura.
- `COMMENT` – Agrega comentarios a los metadatos de la base de datos.
- `RENAME` – Cambia el nombre de una tabla u objeto de la base de datos.

El término **DDL** también se usa en un sentido más amplio para referirse a cualquier lenguaje formal utilizado para describir datos o estructuras de información, como los esquemas XML.

---

### **DML (Data Manipulation Language)**

Los comandos **DML** permiten manipular los datos almacenados en la base de datos. Son utilizados para la inserción, actualización, eliminación y recuperación de datos.

Ejemplos de comandos **DML**:

- `SELECT` – Recupera datos de una o más tablas.
- `INSERT` – Agrega nuevos registros a una tabla.
- `UPDATE` – Modifica registros existentes en una tabla.
- `DELETE` – Elimina registros de una tabla.

A diferencia de los comandos **DDL**, los **DML** operan sobre los datos en lugar de la estructura de la base de datos.

---

### **DCL (Data Control Language)**

Los comandos **DCL** se utilizan para gestionar los permisos y el acceso a los datos dentro de la base de datos, asegurando que solo los usuarios autorizados puedan realizar determinadas acciones.

Ejemplos de comandos **DCL**:

- `GRANT` – Concede permisos a un usuario o rol.
- `REVOKE` – Revoca permisos previamente otorgados.

Estos comandos son esenciales en sistemas multiusuario donde es necesario definir restricciones de acceso a los datos para garantizar la seguridad.

---

### **TCL (Transaction Control Language)**

Los comandos **TCL** se utilizan para gestionar transacciones en la base de datos, asegurando que los cambios en los datos se realicen de manera consistente y controlada.

Ejemplos de comandos **TCL**:

- `COMMIT` – Guarda de forma permanente los cambios realizados en una transacción.
- `ROLLBACK` – Revierte los cambios de una transacción no confirmada.
- `SAVEPOINT` – Establece un punto de restauración dentro de una transacción.
- `SET TRANSACTION` – Configura las propiedades de una transacción, como el nivel de aislamiento.

Estos comandos son fundamentales en sistemas donde la integridad de los datos debe garantizarse mediante la ejecución atómica de operaciones.

## Motores de almacenamiento en MySQL

Un motor de almacenamiento, en MySQL, es el encargado de almacenar, gestionar y recuperar toda la información de una tabla.

Aunque se tratará con mas detalle en una siguiente unidad de contenidos, si es importante conocer, que MySQL permite trabajar con varios motores entre los que destacan MyISAM e InnoDB y cuando se crean objetos en la base de datos, se permite especificar, qué motor de almacenamiento lo va a gestionar.

El utilizar uno u otro motor de almacenamiento puede mejorar de forma considerable el performance de nuestras aplicaciones.

![image.png](attachment:f17acaf7-cde8-4a79-ba37-e378d777323f:image.png)

## **MyISAM**

MyISAM es el motor por defecto de MySQL:

- Una de las principales ventajas de este motor es la velocidad al momento de recuperar información.
- Excelente opción cuando las sentencias predominantes en nuestra aplicación sean de consultas.
- Uso extensivo para recuperar datos en aplicaciones web.
- La principal desventaja es la ausencia de atomicidad, ya que no se comprueba la integridad referencial de los datos. Se gana tiempo en la inserción, sí, pero se pierde confiabilidad en los datos.

## **InnoDB**

Por otro lado, tenemos el motor de almacenamiento InnoDB:

- La principal ventaja de este motor recae en la seguridad de las operaciones.
- Permite la ejecución de transacciones, esto nos garantiza que los datos se persisten de forma correcta y si existe algún error podamos revertir todos los cambios realizados.
- Este motor realiza un bloqueo total sobre una tabla cuando es ejecutada una se las siguientes sentencias.*Select | Insert |Update|Delete*
- Si nuestra aplicación necesita trabajar con transacciones e integridad de los datos, utilizaremos InnoDB.

# DDL (Data Definition Language)

 En este tipo de lenguaje dentro de SQL permite: 

- Definición del esquema de cada relación
- Definición de restricciones de integridad
- Definición y gestión de índices
- Seguridad y autorización de acceso a determinados datos y operaciones
- Almacenamiento físico de cada relación

### **Bases de datos**

Para saber cuántas bases de datos existen en nuestro sistema:

```sql
show databases; 
```

Como se puede ver en la imagen anterior, aparece INDS_BBDD, que es la base de datos creada previamente. Ahora para seleccionar una base de datos, y trabajar con ella utilizaremos el comando USE.

### Creación de Tablas

La sentencia `CREATE TABLE` en MySQL es fundamental para definir la estructura de las tablas en una base de datos. A continuación, se presenta una explicación detallada de su sintaxis y opciones:

**Sintaxis básica:**

```sql
CREATE TABLE [IF NOT EXISTS] nombre_tabla (
    nombre_columna tipo_datos [restricciones] [opciones] [comentario],
    ...
) ENGINE=tipo_storage;
```

**Componentes principales:**

- **`[IF NOT EXISTS]`**: Evita errores si la tabla ya existe; si la tabla no existe, la crea.
- **`nombre_tabla`**: Nombre único de la tabla en la base de datos.
- **`nombre_columna`**: Nombre de cada columna en la tabla.
- **`tipo_datos`**: Especifica el tipo de datos que almacenará la columna (por ejemplo, `INT`, `VARCHAR(255)`, `DATE`).
- **`[restricciones]`**: Define reglas para los datos de la columna, como `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, entre otras.
- **`[opciones]`**: Configuraciones adicionales, como `AUTO_INCREMENT` para incrementos automáticos en columnas numéricas.
- **`[comentario]`**: Permite agregar una descripción o comentario sobre la columna.
- **`ENGINE=tipo_storage`**: Especifica el motor de almacenamiento que utilizará la tabla, como `InnoDB` o `MyISAM`.

**Ejemplo práctico:**

```sql
CREATE TABLE IF NOT EXISTS empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único del empleado',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombre del empleado',
    apellido VARCHAR(100) NOT NULL COMMENT 'Apellido del empleado',
    fecha_contratacion DATE NOT NULL COMMENT 'Fecha de contratación',
    salario DECIMAL(10,2) CHECK (salario > 0) COMMENT 'Salario del empleado',
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB;
```

**Explicación del ejemplo:**

- **`id_empleado`**: Columna entera que se incrementa automáticamente y actúa como clave primaria.
- **`nombre`** y **`apellido`**: Columnas de tipo cadena (`VARCHAR`) que almacenan el nombre y apellido del empleado; no permiten valores nulos.
- **`fecha_contratacion`**: Columna de tipo fecha que registra la fecha de contratación del empleado.
- **`salario`**: Columna decimal que almacena el salario del empleado; incluye una restricción `CHECK` para asegurar que el salario sea mayor que cero.
- **`id_departamento`**: Columna entera que actúa como clave foránea, referenciando la columna `id_departamento` de la tabla `departamentos`. Las acciones `ON UPDATE CASCADE` y `ON DELETE SET NULL` especifican que, al actualizarse el `id_departamento` en la tabla `departamentos`, se refleje en esta tabla, y al eliminarse un departamento, el campo correspondiente en la tabla `empleados` se establezca a `NULL`.
- **`ENGINE=InnoDB`**: Especifica que la tabla utilizará el motor de almacenamiento `InnoDB`, que soporta transacciones y claves foráneas.

### **Borrado de tablas**

El comando `DROP TABLE` en MySQL se utiliza para eliminar una o más tablas existentes en una base de datos, incluyendo toda la información almacenada en ellas. La sintaxis básica es:

```sql
DROP [TEMPORARY] TABLE [IF EXISTS] nombre_tabla [, nombre_tabla] ... [RESTRICT | CASCADE];
```

Donde:

- `TEMPORARY`: Indica que solo se eliminarán tablas temporales.
- `IF EXISTS`: Evita errores si la tabla no existe.
- `RESTRICT` y `CASCADE`: Estas opciones están reservadas para implementaciones futuras y actualmente no tienen efecto en MySQL.
    
    [dev.mysql.com](https://dev.mysql.com/doc/refman/5.7/en/drop-table.html?utm_source=chatgpt.com)
    

**Ejemplo de uso:**

```sql
DROP TABLE IF EXISTS tabla1, tabla2, tabla3;
```

Este comando eliminará `tabla1`, `tabla2` y `tabla3` si existen en la base de datos.

[w3schools.com](https://www.w3schools.com/mysql/mysql_drop_table.asp?utm_source=chatgpt.com)

**Consideraciones importantes:**

- Al eliminar una tabla, se borran tanto la estructura como los datos contenidos en ella de forma permanente.
- Es recomendable asegurarse de que la tabla ya no sea necesaria antes de eliminarla para evitar la pérdida de información importante.

**Tablas temporales en MySQL:**

Las tablas temporales son útiles para almacenar resultados intermedios o datos que solo se necesitan durante la sesión actual. Estas tablas se crean con la cláusula `TEMPORARY` y se eliminan automáticamente al finalizar la sesión o al cerrar la conexión.

[mysqltutorial.org](https://www.mysqltutorial.org/mysql-basics/mysql-temporary-table/?utm_source=chatgpt.com)

**Características de las tablas temporales:**

- Son visibles únicamente para la sesión que las creó.
- Dos sesiones diferentes pueden crear tablas temporales con el mismo nombre sin conflictos.
- No es posible tener una tabla temporal y una permanente con el mismo nombre en la misma sesión; la tabla temporal ocultará a la permanente mientras exista.
    
    [dev.mysql.com](https://dev.mysql.com/doc/refman/8.4/en/create-temporary-table.html?utm_source=chatgpt.com)
    

**Ejemplo de creación y uso de una tabla temporal:**

```sql
CREATE TEMPORARY TABLE creditos (
    numeroCliente INT PRIMARY KEY,
    limiteCredito DECIMAL(10,2)
);

INSERT INTO creditos (numeroCliente, limiteCredito)
SELECT customerNumber, creditLimit
FROM customers
WHERE creditLimit > 0;
```

En este ejemplo, se crea una tabla temporal llamada `creditos` que almacena el número de cliente y su límite de crédito para aquellos clientes cuyo límite es mayor que cero.

[mysqltutorial.org](https://www.mysqltutorial.org/mysql-basics/mysql-temporary-table/?utm_source=chatgpt.com)

**Eliminación de tablas temporales:**

Aunque las tablas temporales se eliminan automáticamente al finalizar la sesión, también es posible eliminarlas manualmente durante la sesión utilizando el comando `DROP TEMPORARY TABLE`:

```sql
DROP TEMPORARY TABLE IF EXISTS creditos;
```

Este comando elimina la tabla temporal `creditos` si existe en la sesión actual.

[mysqltutorial.org](https://www.mysqltutorial.org/mysql-basics/mysql-temporary-table/?utm_source=chatgpt.com)

Es importante destacar que las tablas temporales son una herramienta valiosa para gestionar datos provisionales y optimizar consultas complejas en MySQL.

### Modificación de Tablas

- **Añadir una columna al final de una tabla**: Al agregar una nueva columna, todas las filas existentes tendrán el valor `NULL` en esa columna.
    
    ```sql
    ALTER TABLE Customers ADD email VARCHAR(150);
    ```
    
- **Añadir una columna después de otra columna**: Es posible especificar la posición de la nueva columna utilizando `AFTER` o `FIRST` para colocarla al inicio.
    
    ```sql
    ALTER TABLE Customers ADD Apellidos VARCHAR(40) NOT NULL AFTER idCustomer;
    ```
    
- **Eliminar columnas de una tabla**: Se pueden eliminar múltiples columnas en una sola sentencia.
    
    ```sql
    ALTER TABLE Customers DROP COLUMN a, DROP COLUMN b;
    ```
    
- **Modificar el tipo de datos de una columna y asignar un valor por defecto**: Permite cambiar la definición de una columna y establecer un valor predeterminado.
    
    ```sql
    ALTER TABLE Equipos MODIFY precio DECIMAL(10,2);
    ALTER TABLE Equipos MODIFY precio DECIMAL(5,2) DEFAULT 10.50;
    ```
    
- **Renombrar una columna**: Cambia el nombre de una columna específica.
    
    ```sql
    ALTER TABLE Equipos RENAME COLUMN codEquipo TO idEquipo;
    ```
    
- **Cambiar el nombre y el tipo de una columna**: Permite renombrar y modificar el tipo de datos de una columna simultáneamente.
    
    ```sql
    ALTER TABLE Equipos CHANGE COLUMN id_equipo codEquipo NUMERIC(15) NOT NULL;
    ```
    
- **Eliminar una clave foránea (FK)**: Elimina una restricción de clave foránea existente.
    
    ```sql
    ALTER TABLE Equipos DROP FOREIGN KEY FK_equipos_detalle;
    ```
    
- **Añadir una clave foránea a una tabla existente**: Establece una nueva restricción de clave foránea.
    
    ```sql
    ALTER TABLE Pedidos ADD CONSTRAINT FK_Pedidos_Clientes FOREIGN KEY (idCliente) REFERENCES Clientes (idCliente);
    ```
    
- **Añadir una clave primaria (PK) a una tabla existente**: Define una o más columnas como clave primaria.
    
    ```sql
    ALTER TABLE Equipos ADD CONSTRAINT PRIMARY KEY (codEquipo, precio);
    ```
    
- **Añadir una clave única (UK) a una tabla existente**: Garantiza que los valores en una columna sean únicos.
    
    ```sql
    ALTER TABLE Clientes ADD CONSTRAINT UK_codcli UNIQUE (codcli);
    ```
    
- **Añadir una restricción CHECK a una columna**: Impone una condición que los datos deben cumplir.
    
    ```sql
    ALTER TABLE Pedido ADD CONSTRAINT Check_Ppto CHECK (ppto >= 0);
    ```
    
- **Cambiar el conjunto de caracteres de una tabla**: Modifica el charset utilizado por la tabla.
    
    ```sql
    ALTER TABLE Equipos CHARACTER SET = utf8mb4;
    ```
    
- **Renombrar una tabla**: Cambia el nombre de una tabla existente.
    
    ```sql
    ALTER TABLE Equipos RENAME equipos;
    ```
    
    También es posible mover una tabla a otra base de datos y renombrarla simultáneamente:
    
    ```sql
    RENAME TABLE bd1.equipos TO bd2.equipos_new;
    ```
    
- **Truncar una tabla**: Elimina rápidamente todos los registros de una tabla, similar a `DELETE`, pero más eficiente.
    
    ```sql
    TRUNCATE TABLE Equipos;
    ```
    
- **Añadir comentarios a una tabla o columna**: Proporciona descripciones útiles para la documentación.
    
    ```sql
    ALTER TABLE Equipos MODIFY idEquipo BIGINT DEFAULT 1 COMMENT 'identificador equipo';
    CREATE TABLE Test (id INT, nombre CHAR(30)) COMMENT 'Test iniciales';
    ```
    

**Vistas**

Una vista es una tabla virtual que almacena una consulta y muestra datos de una o varias tablas reales. Las vistas son de solo lectura y ofrecen varias ventajas:

- **Control de accesos**: Permiten compartir únicamente la información específica que se desea, restringiendo el acceso al resto de los datos.
- **Mejora del rendimiento**: Facilitan la creación de consultas basadas en vistas derivadas de `SELECT` complejos.
- **Pruebas seguras**: Ofrecen un entorno de prueba sin afectar la información real.
- **Reusabilidad de consultas**: Evitan la repetición de consultas complejas que requieren uniones.
- **Mantenimiento de la integridad**: Garantizan que las aplicaciones no se vean afectadas por cambios en la estructura de la base de datos.

Para crear una vista, se utiliza la siguiente sintaxis:

```sql
CREATE [OR REPLACE] [ALGORITHM = {MERGE | TEMPTABLE | UNDEFINED}] VIEW nombre_vista [(column_list)] AS consulta_SELECT;
```

- **OR REPLACE**: Reemplaza una vista existente si coincide en nombre.
- **ALGORITHM**: Especifica cómo MySQL procesará la vista.

**Algoritmos de procesamiento de vistas en MySQL:**

1. **MERGE:**
    - **Descripción:** Este algoritmo combina la consulta que se realiza sobre la vista con la definición de la vista en una sola consulta. Esto permite que la consulta resultante aproveche los índices de las tablas subyacentes, mejorando el rendimiento.
    - **Ejemplo:**
    Al consultar `Vista_Cursos_Merged`, MySQL combinará la consulta externa con la definición de la vista, ejecutándola directamente sobre las tablas base.
        
        ```sql
        CREATE ALGORITHM=MERGE VIEW Vista_Cursos_Merged AS
        SELECT t3.name AS Nombre, t3.dept_name AS Departamento, t1.course_id AS Codigo_curso, t2.semester AS Semestre, t2.year AS Año
        FROM course t1
        INNER JOIN teaches t2 ON t1.course_id = t2.course_id
        INNER JOIN instructor t3 ON t2.ID = t3.ID
        WHERE t2.year = 2018;
        ```
        
2. **TEMPTABLE:**
    - **Descripción:** Con este algoritmo, MySQL primero evalúa la definición de la vista y almacena el resultado en una tabla temporal. Luego, la consulta externa se ejecuta sobre esta tabla temporal. Este enfoque puede ser menos eficiente, ya que las tablas temporales no utilizan índices y añaden sobrecarga en la creación y manejo de dichas tablas.
3. **UNDEFINED:**
    - **Descripción:** Si no se especifica un algoritmo al crear la vista, MySQL selecciona automáticamente el más adecuado, generalmente prefiriendo `MERGE` por su eficiencia.

**Vistas actualizables:**

Las vistas actualizables permiten realizar operaciones de inserción, actualización y eliminación directamente sobre la vista, afectando las tablas subyacentes. Sin embargo, para que una vista sea actualizable, debe cumplir ciertas condiciones:

- No debe contener funciones de agregación como `COUNT()`, `SUM()`, `AVG()`, etc.
- No debe incluir las cláusulas `DISTINCT`, `GROUP BY`, `HAVING` o `UNION`.
- No debe tener subconsultas en la lista `SELECT`.
- Debe referirse a una sola tabla base.

Es importante destacar que las vistas creadas con el algoritmo `TEMPTABLE` no son actualizables.

[programmerclick.com](https://programmerclick.com/article/6820287214/?utm_source=chatgpt.com)

**Ejemplo de creación de una vista actualizable:**

```sql
CREATE VIEW Instructores_Vista AS
SELECT * FROM instructor;
```

En este ejemplo, `Instructores_Vista` es una vista sencilla que permite realizar operaciones `INSERT`, `UPDATE` y `DELETE`, siempre que se respeten las restricciones mencionadas anteriormente.

# DML (Data Manipulation Language)

Las consultas en DML se realizan de la siguiente forma, SELECT, manipula datos, pero en las salidas que devuelve, no los modifica en la base de datos, mientras que otros comandos si modifican datos sobre las bases de datos, y por esto estas están incluidas en el DML, como tal, aunque en algunos textos/autores, el SELECT también se incluye en DML.

Para practicar algunas de las consultas de este, se recomienda al alumno cargar estos dos archivos SQL.

## Funciones mas representativas

### **Funciones Matemáticas**

- **ABS(n):**
    
    Devuelve el valor absoluto de un número (es decir, el valor positivo).
    
    **Ejemplo:**
    
    ```sql
    SELECT ABS(0), ABS(12), ABS(-33);
    ```
    
    **Resultado:** 0, 12, 33
    
- **CEIL(numeric_expression):**
    
    Devuelve el entero más pequeño mayor o igual al número dado.
    
    **Ejemplo:**
    
    ```sql
    SELECT CEIL(2.69);  -- Resultado: 3
    SELECT CEIL(-2.69); -- Resultado: -2
    ```
    
- **FLOOR(expression):**
    
    Devuelve el entero más grande menor o igual al número dado.
    
    **Ejemplo:**
    
    ```sql
    SELECT FLOOR(2.69);   -- Resultado: 2
    SELECT FLOOR(-2.69);  -- Resultado: -3
    ```
    
- **MOD(dividendo, divisor):**
    
    Devuelve el resto de la división entre dos números.
    
    **Ejemplo:**
    
    ```sql
    SELECT MOD(11, 3); -- Resultado: 2
    SELECT MOD(11, 0); -- Resultado: NULL (división por cero)
    ```
    
- **TRUNCATE(X, D):**
    
    Trunca un número a un número específico de posiciones decimales.
    
    - **X:** número a truncar.
    - **D:** número de decimales.
        
        **Ejemplo:**
        
    
    ```sql
    SELECT TRUNCATE(1.555, 1);  -- Resultado: 1.5
    SELECT TRUNCATE(199.99, -2); -- Resultado: 100
    SELECT TRUNCATE(1.999, 1);   -- Resultado: 1.9
    SELECT ROUND(1.999, 1);      -- Resultado: 2.0
    ```
    

---

### **Funciones de Fecha y Hora**

- **CURDATE():**
    
    Devuelve la fecha actual.
    
    - **Contexto cadena:** `YYYY-MM-DD`
    - **Contexto numérico:** `YYYYMMDD`
        
        **Ejemplo:**
        
    
    ```sql
    SELECT CURDATE();      -- Resultado: 2023-07-11
    SELECT CURDATE() + 0;  -- Resultado: 20230711
    ```
    
- **DATEDIFF(date_expr1, date_expr2):**
    
    Devuelve el número de días entre dos fechas.
    
    **Ejemplo:**
    
    ```sql
    SELECT DATEDIFF('2022-08-08', '2022-08-28');  -- Resultado: -20
    SELECT DATEDIFF('2022-08-28', '2022-08-20');  -- Resultado: 8
    ```
    
- **DAY(date):**
    
    Devuelve el número de día del mes a partir de una fecha dada.
    
    **Ejemplo:**
    
    ```sql
    SELECT DAY('2023-01-15'); -- Resultado: 15
    SELECT DAY('2023-12-31'); -- Resultado: 31
    ```
    
- **NOW():**
    
    Devuelve la fecha y hora actuales.
    
    - **Contexto cadena:** `YYYY-MM-DD HH:MM:SS`
    - **Contexto numérico:** `YYYYMMDDHHMMSS`
        
        **Ejemplo:**
        
    
    ```sql
    SELECT NOW();        -- Resultado: 2023-03-04 10:21:14
    SELECT NOW() + 0;    -- Resultado: 20230304102206
    ```
    
- **MONTH(date):**
    
    Devuelve el número del mes de una fecha.
    
    **Ejemplo:**
    
    ```sql
    SELECT MONTH('2023-03-05'); -- Resultado: 3
    ```
    
- **YEAR(date):**
    
    Devuelve el año de una fecha.
    
    **Ejemplo:**
    
    ```sql
    SELECT YEAR('2023-01-01');  -- Resultado: 2023
    SELECT YEAR(CURDATE());     -- Resultado: 2023
    ```
    

---

### **Funciones de Agregación**

- **AVG:**
    
    Devuelve el promedio de un conjunto de valores.
    
    **Ejemplo:**
    
    ```sql
    SELECT TRUNCATE(AVG(salary), 2) FROM instructor;
    ```
    
- **MIN:**
    
    Devuelve el valor mínimo de un conjunto de valores.
    
    **Ejemplo:**
    
    ```sql
    SELECT MIN(salary) FROM instructor;
    ```
    
- **MAX:**
    
    Devuelve el valor máximo de un conjunto de valores.
    
    **Ejemplo:**
    
    ```sql
    SELECT MAX(salary) FROM instructor;
    ```
    
- **SUM:**
    
    Devuelve la suma de un conjunto de valores.
    
    **Ejemplo:**
    
    ```sql
    SELECT SUM(salary) FROM instructor WHERE dept_name = 'Finance';
    SELECT TRUNCATE(SUM(salary) / 12, 2) FROM instructor WHERE dept_name = 'Finance';
    ```
    
- **COUNT:**
    
    Cuenta el número de valores.
    
    **Ejemplo:**
    
    ```sql
    SELECT COUNT(*) FROM instructor;
    SELECT COUNT(DISTINCT ID) FROM teaches WHERE semester = 'Spring' AND year = 2018;
    ```
    

---

### **Funciones de Control de Flujo**

- **CASE:**
    
    Permite realizar condiciones dentro de una consulta.
    
    **Ejemplo:**
    
    ```sql
    SELECT name, COUNT(course_id) AS num_courses,
           CASE
               WHEN COUNT(course_id) > 4 THEN 'Buen profesor: más de 4 cursos'
               WHEN COUNT(course_id) BETWEEN 2 AND 4 THEN 'Buen profesor: entre 2-4 cursos'
               ELSE 'Imparte menos de 2 cursos'
           END AS result
    FROM teaches, instructor
    WHERE teaches.ID = instructor.ID
    GROUP BY name;
    ```
    
- **IF:**
    
    Evalúa una condición simple y retorna un valor basado en su resultado.
    
    **Ejemplo:**
    
    ```sql
    SELECT title, IF(credits > 3, 'Más de 3 créditos', 'Menor o igual a tres créditos')
    FROM course;
    ```
    
- **IFNULL:**
    
    Devuelve el primer valor si no es `NULL`, o el segundo valor si el primero es `NULL`.
    
    **Ejemplo:**
    
    ```sql
    SELECT IFNULL(credits, 0) FROM course;
    ```
    
- **NULLIF:**
    
    Devuelve el primer valor si no es igual al segundo, o `NULL` si ambos valores son iguales.
    
    **Ejemplo:**
    
    ```sql
    SELECT NULLIF(salary, 0) FROM instructor;
    ```
    

---

### **Funciones de Cadena de Caracteres**

- **ORD('A'):**
    
    Devuelve el código ASCII de un carácter.
    
    **Ejemplo:**
    
    ```sql
    SELECT ORD('A'); -- Resultado: 65
    ```
    
- **CHAR(65, 66, 67):**
    
    Devuelve los caracteres correspondientes a los códigos ASCII proporcionados.
    
    **Ejemplo:**
    
    ```sql
    SELECT CHAR(65, 66, 67); -- Resultado: 'ABC'
    ```
    
- **CONCAT():**
    
    Concatena dos o más cadenas de texto.
    
    **Ejemplo:**
    
    ```sql
    SELECT CONCAT('Buenos días, ', '--', 'INSD'); -- Resultado: 'Buenos días, --INSD'
    ```
    
- **FIND_IN_SET():**
    
    Busca una cadena dentro de una lista separada por comas.
    
    **Ejemplo:**
    
    ```sql
    SELECT FIND_IN_SET('Hola', 'Como esta Raúl, Hola, Buenos días'); -- Resultado: 2
    ```
    
- **LENGTH():**
    
    Devuelve la longitud de una cadena de texto.
    
    **Ejemplo:**
    
    ```sql
    SELECT LENGTH('Buenos días INSD'); -- Resultado: 18
    ```
    
- **INSTR():**
    
    Devuelve la posición de la primera ocurrencia de una subcadena en una cadena.
    
    **Ejemplo:**
    
    ```sql
    SELECT INSTR('Buenos días', 'os'); -- Resultado: 3
    ```
    
- **LEFT() / RIGHT():**
    
    Devuelven una subcadena desde la izquierda o derecha de la cadena original.
    
    **Ejemplo:**
    
    ```sql
    SELECT LEFT('Buenos días INSD', 8); -- Resultado: 'Buenos d'
    SELECT RIGHT('Buenos días INSD', 8); -- Resultado: 'os INSD'
    ```
    
- **SUBSTRING():**
    
    Extrae una subcadena de una cadena, comenzando en una posición específica.
    
    **Ejemplo:**
    
    ```sql
    SELECT SUBSTRING('Buenas tardes', 3, 5); -- Resultado: 'eas t'
    ```
    

## Tipos de Consultas

### **Consultas Sencillas**

Son las consultas más básicas, generalmente usan `SELECT` para recuperar datos de una sola tabla.

🔹 **Ejemplo:**

```sql
SELECT nombre, edad FROM empleados WHERE edad > 30;
```

🔹 **Explicación:**

Esta consulta recupera los nombres y edades de los empleados mayores de 30 años.

---

### **Consultas Agrupadas**

Usan `GROUP BY` para agrupar filas que tienen valores en común en una o más columnas y permiten aplicar funciones de agregación como `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`.

🔹 **Ejemplo:**

```sql
SELECT departamento, COUNT(*) AS total_empleados
FROM empleados
GROUP BY departamento;
```

🔹 **Explicación:**

Agrupa a los empleados por departamento y cuenta cuántos empleados hay en cada uno.

---

### **Consultas Multitabla (JOIN)**

Se usan para combinar datos de múltiples tablas mediante combinaciones (`JOIN`).

🔹 **Ejemplo:**

```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
JOIN departamentos ON empleados.id_departamento = departamentos.id;
```

🔹 **Explicación:**

Recupera el nombre del empleado junto con el nombre del departamento al que pertenece, uniendo ambas tablas con un `JOIN`.

---

### **Consultas Anidadas (Subconsultas)**

Son consultas dentro de otras consultas (`SELECT` dentro de otro `SELECT`).

🔹 **Ejemplo:**

```sql
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);
```

🔹 **Explicación:**

Selecciona a los empleados cuyo salario sea mayor que el salario promedio de todos los empleados.

---

### **Consultas de Conjuntos (UNION, INTERSECT, EXCEPT)**

Permiten combinar resultados de múltiples `SELECT`.

🔹 **Ejemplo (`UNION`):**

```sql
SELECT nombre FROM empleados_madrid
UNION
SELECT nombre FROM empleados_barcelona;
```

🔹 **Explicación:**

Une los nombres de empleados de ambas tablas sin repetir valores.

🔹 **Ejemplo (`INTERSECT` - si la base de datos lo soporta):**

```sql
SELECT nombre FROM empleados_madrid
INTERSECT
SELECT nombre FROM empleados_barcelona;
```

🔹 **Explicación:**

Devuelve los empleados que están en ambas ciudades.

🔹 **Ejemplo (`EXCEPT` o `MINUS` en Oracle):**

```sql
SELECT nombre FROM empleados_madrid
EXCEPT
SELECT nombre FROM empleados_barcelona;
```

🔹 **Explicación:**

Muestra los empleados que están en Madrid pero no en Barcelona.

---

### **Consultas con Cláusula WITH (Common Table Expressions - CTE)**

Permiten definir consultas temporales reutilizables dentro de una misma consulta.

🔹 **Ejemplo:**

```sql
WITH empleados_mayores AS (
    SELECT nombre, edad FROM empleados WHERE edad > 40
)
SELECT * FROM empleados_mayores;
```

🔹 **Explicación:**

Define una tabla temporal (`empleados_mayores`) con los empleados mayores de 40 años y luego consulta los datos de esa tabla.

## **Operaciones de Actualización de Datos**

### **INSERT**

Permite insertar nuevos registros en una tabla. Los valores deben coincidir con los tipos de datos de la tabla (cadena, numérico, fecha). Los valores de cadena deben estar entre comillas simples.

Ejemplos:

- **Insertar valores directos:**
    
    ```sql
    INSERT INTO course VALUES ('HH-888', 'IA', 'Comp. Sci.', 2);
    ```
    
- **Insertar valores específicos en columnas:**
    
    ```sql
    INSERT INTO course (course_id, title, dept_name, credits)
    VALUES ('HT-999', 'ChatGPT', 'Comp. Sci.', 4);
    ```
    
- **Insertar datos con SELECT:**
    
    ```sql
    INSERT INTO instructor
    SELECT ID+100, 'Carlos Resino', dept_name, 33000.34
    FROM student
    WHERE dept_name = 'Finance' and tot_cred > 4;
    ```
    

### **DELETE**

Elimina registros de una tabla. Puede eliminar todos los registros o solo los que cumplen ciertas condiciones.

Ejemplos:

- **Eliminar todos los registros:**
    
    ```sql
    DELETE FROM advisor;
    ```
    
- **Eliminar registros con condición:**
    
    ```sql
    DELETE FROM advisor
    WHERE s_id > 15000
    ORDER BY i_id
    LIMIT 3;
    ```
    

### **UPDATE**

Permite actualizar registros existentes en una tabla. Se especifica qué campo se va a modificar y el valor con el que se actualizará.

Ejemplos:

- **Actualizar un valor numérico:**
    
    ```sql
    UPDATE instructor
    SET salary = salary * 1.05
    WHERE salary < 80000;
    ```
    
- **Actualizar con CASE (condicional):**
    
    ```sql
    UPDATE course
    SET credits =
    CASE
      WHEN credits <= 3 THEN credits * 2
      ELSE credits * 1.5
    END;
    ```