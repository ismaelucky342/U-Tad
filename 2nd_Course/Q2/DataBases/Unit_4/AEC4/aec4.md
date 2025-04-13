## EJERCICIO 1 - `ejercicio4_1.sql`

### a) Crear la base de datos y la tabla

> En esta parte empiezo eliminando la base de datos si ya existía, para asegurarme de que todo esté limpio antes de crearla de nuevo. Luego, creo una tabla llamada libros con varias columnas como título, autor, año de publicación y género. También añado una restricción CHECK para asegurar que el año no sea mayor al actual (2025), para mantener los datos realistas.
> 

```sql
-- ejercicio4_1.sql

DROP DATABASE IF EXISTS Unidad4;
CREATE DATABASE Unidad4;
USE Unidad4;

CREATE TABLE libros (
    id_libro INT NOT NULL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    año_publicacion INT NOT NULL CHECK (año_publicacion <= 2025),
    genero VARCHAR(20) NOT NULL
);
```

---

### b) Insertar 2000 registros (usando Python)

> Aquí uso Python junto con la librería Faker para generar datos aleatorios y simular una base de datos más realista con 2000 libros. Uso random para variar los años y géneros. Me conecto a MySQL con mysql.connector y voy insertando los datos uno a uno con un bucle. Esto me permite probar el rendimiento de la base de datos con una cantidad considerable de información.
> 

Creo un archivo `insertar_libros.py`:

```python
import mysql.connector
import random
from faker import Faker

fake = Faker()
generos = ["Ficción", "No Ficción", "Ciencia", "Historia", "Fantasía", "Terror", "Biografía"]

conn = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="Unidad4"
)

cursor = conn.cursor()

for i in range(1, 2001):
    titulo = fake.sentence(nb_words=4)
    autor = fake.name()
    año = random.randint(1950, 2025)
    genero = random.choice(generos)
    cursor.execute("""
        INSERT INTO libros (id_libro, titulo, autor, año_publicacion, genero)
        VALUES (%s, %s, %s, %s, %s)
    """, (i, titulo, autor, año, genero))

conn.commit()
cursor.close()
conn.close()
```

Instalamos dependencias `faker`:

```bash
pip install faker mysql-connector-python
```

---

### c) Consulta con `EXPLAIN`

> Esta consulta me ayuda a ver cómo MySQL ejecuta la búsqueda. Como todavía no hay ningún índice, el motor de base de datos tiene que recorrer toda la tabla (type = ALL), lo que es poco eficiente. Esta es la línea base para comparar luego cuándo sí aplicamos un índice.
> 

```sql
EXPLAIN SELECT * FROM libros
WHERE año_publicacion > 2000 AND genero = 'Ficción';
```

- Sin índice, MySQL hará un **table scan** (examinará todos los registros).
- Columna `type` será `ALL` (peor rendimiento).

---

### d) Crear índice y volver a ejecutar

> Ahora creo un índice sobre la columna año_publicacion para mejorar el rendimiento de la consulta anterior. Al volver a ejecutar EXPLAIN, espero que MySQL use ese índice y que en la salida aparezca key=idx_libros_publicacion, lo que indicaría que se está beneficiando del índice y la búsqueda es más rápida (tipo range en lugar de ALL).
> 

```sql
CREATE INDEX idx_libros_publicacion ON libros(año_publicacion);

-- Repetir la consulta
EXPLAIN SELECT * FROM libros
WHERE año_publicacion > 2000 AND genero = 'Ficción';
```

- Ahora MySQL usará el índice `idx_libros_publicacion`.
- Mejora en el campo `type` (posiblemente `range`), y aparece `key=idx_libros_publicacion`.

---

## EJERCICIO 2 - `ejercicio4_2.sql`

### a) Crear tablespace

> Aquí empiezo trabajando con tablespaces, que son como espacios de almacenamiento dedicados dentro de MySQL. Aseguro que la opción innodb_file_per_table esté activa, ya que es necesaria para que cada tabla pueda estar en su propio archivo. Luego creo un nuevo tablespace llamado tbs_libros.
> 

> Nos aseguramos primeramente de que  MySQL esté en modo file-per-table (innodb_file_per_table = 1)
> 

```sql
-- ejercicio4_2.sql

USE Unidad4;

CREATE TABLESPACE tbs_libros
    ADD DATAFILE '/var/lib/mysql/tbs_libros.ibd'
    ENGINE=InnoDB;

```

---

### b) Crearmos tabla en el tablespace

> A continuación, creo una tabla nueva llamada libros_tbs y la asigno al tablespace que acabo de crear. Esto ayuda a separar físicamente los datos de esta tabla de las demás, lo cual es útil para organización, rendimiento o mantenimiento.
> 

```sql
CREATE TABLE libros_tbs (
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(50),
    año_publicacion INT
) TABLESPACE tbs_libros STORAGE DISK ENGINE=InnoDB;
```

---

### c) Verificamos que fue creada

> Aquí hago una consulta al information_schema.tables para confirmar que la tabla libros_tbs realmente está usando el tablespace que le asigné. Es una forma sencilla de comprobar que todo salió bien.
> 

```sql
SELECT TABLE_NAME, TABLESPACE_NAME
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'Unidad4';
```

---

### d) Ver tablespaces existentes

> En este paso reviso todos los tablespaces existentes y sus archivos asociados, mirando directamente en information_schema.FILES. Me sirve para confirmar qué files están activos y dónde están ubicados.
> 

```sql
SELECT * FROM information_schema.FILES
WHERE FILE_TYPE = 'DATAFILE';
```

---

### e) Movemos la tabla a otro tablespace

> Ahora practico mover la tabla a otro tablespace. Primero creo uno nuevo (tbs_nuevo) y luego uso ALTER TABLE para mover la tabla. Esto puede servir si quiero reorganizar mi almacenamiento o distribuir las tablas en discos diferentes.
> 

```sql
-- Crear nuevo tablespace
CREATE TABLESPACE tbs_nuevo
    ADD DATAFILE '/var/lib/mysql/tbs_nuevo.ibd'
    ENGINE=InnoDB;

-- Mover tabla (requiere ALTER con DISCARD/IMPORT)
ALTER TABLE libros_tbs TABLESPACE tbs_nuevo;
```

---

### f) Verificamos el movimiento

> Repito la consulta de antes a information_schema.tables para asegurarme de que la tabla efectivamente se movió al nuevo tablespace tbs_nuevo.
> 

```sql
SELECT TABLE_NAME, TABLESPACE_NAME
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'Unidad4';
```

---

### g) Eliminamos tablespace

> Por último, si ya no necesito el tablespace original, lo elimino. Pero antes, me aseguro de eliminar cualquier tabla que lo esté usando, ya que MySQL no me dejará borrarlo si está en uso.
> 

```sql
-- Primero elimina la tabla del tablespace si aún existe
DROP TABLE IF EXISTS libros_tbs;

-- Luego elimina el tablespace
DROP TABLESPACE tbs_libros;
```

## EJERCICIO 3 - `ejercicio4_3.sql`

> Aquí centralizo la creación de una base de datos completa llamada biblioteca_db con dos tablas: autores y libros. Están relacionadas por una clave foránea (autor_id), lo que me permite manejar autores y sus respectivos libros de forma estructurada y relacional.
> 

Este archivo contiene todas las sentencias SQL necesarias para crear la base de datos y las tablas:

```sql
-- ejercicio4_3.sql

DROP DATABASE IF EXISTS biblioteca_db;
CREATE DATABASE biblioteca_db;
USE biblioteca_db;

CREATE TABLE autores (
    autor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre_autor VARCHAR(100),
    apellido_autor VARCHAR(100)
);

CREATE TABLE libros (
    libro_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo_libro VARCHAR(150),
    fecha_publicacion DATE,
    precio DECIMAL(10,2),
    autor_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id)
);

```

---

## Archivos Python con MySQLdb

> Para trabajar con esta base de datos desde Python, uso el conector mysqlclient, que es una interfaz compatible con la librería MySQLdb. En mi caso, para poder compilarlo e instalarlo, también tuve que instalar algunas dependencias del sistema como libmysqlclient-dev.
> 

Antes de continuar, instalamos el conector:

```bash
pip install mysqlclient
```

en mi caso adicionalmente me faltaba el `libmysqlclient-dev`, en Ubuntu se instala como:

```bash
sudo apt install libmysqlclient-dev python3-dev
```

---

### 1. `conexion_db.py` — Conexión a la base de datos

> En este archivo defino una función sencilla para conectarme a la base de datos biblioteca_db. Así puedo reutilizarla en todos los scripts sin repetir el código de conexión.
> 

```python
import MySQLdb

def conectar():
    return MySQLdb.connect(
        host="localhost",
        user="tu_usuario",
        passwd="tu_contraseña",
        db="biblioteca_db"
    )
```

---

### 2. `crear_tablas.py` — Crear las tablas

> Aquí simplemente leo el archivo ejercicio4_3.sql y ejecuto las sentencias SQL que contiene, una por una. Esto me permite crear la estructura de la base de datos desde Python de forma automática.
> 

```python
from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

with open("ejercicio4_3.sql", "r") as f:
    script = f.read()

for statement in script.strip().split(';'):
    if statement.strip():
        cursor.execute(statement)

conn.commit()
cursor.close()
conn.close()
print("Tablas creadas correctamente.")
```

---

### 3. `insertar_autores_libros.py` — Insertar datos

> En este script inserto algunos autores y libros de ejemplo, conectando cada libro con su autor mediante el campo autor_id. Es una forma rápida de poblar la base de datos con datos reales y hacer pruebas.
> 

```python
from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

# Insertar autores
autores = [
    ("Gabriel", "García Márquez"),
    ("Isabel", "Allende"),
    ("Jorge", "Luis Borges")
]

cursor.executemany("INSERT INTO autores (nombre_autor, apellido_autor) VALUES (%s, %s)", autores)

# Insertar libros
libros = [
    ("Cien años de soledad", "1967-05-30", 18.50, 1),
    ("El amor en los tiempos del cólera", "1985-09-05", 21.00, 1),
    ("La casa de los espíritus", "1982-01-01", 19.90, 2),
    ("Eva Luna", "1987-11-11", 15.00, 2),
    ("Ficciones", "1944-01-01", 22.00, 3),
]

cursor.executemany("INSERT INTO libros (titulo_libro, fecha_publicacion, precio, autor_id) VALUES (%s, %s, %s, %s)", libros)

conn.commit()
cursor.close()
conn.close()
print("Autores y libros insertados correctamente.")
```

---

### 4. `consulta_libros_por_autor.py` — Consultar libros de un autor

> Aquí pido al usuario el apellido de un autor, y luego muestro todos los libros escritos por él. Hago un JOIN entre las tablas autores y libros para obtener la información deseada.
> 

```python
from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

autor = input("Introduce el apellido del autor: ")

query = """
SELECT titulo_libro FROM libros
JOIN autores ON libros.autor_id = autores.autor_id
WHERE apellido_autor = %s
"""

cursor.execute(query, (autor,))
resultados = cursor.fetchall()

print("Libros del autor:")
for libro in resultados:
    print("-", libro[0])

cursor.close()
conn.close()
```

---

### 5. `consulta_libros_baratos.py` — Libros con precio < 20.00

> Este script busca libros cuyo precio sea menor a 20.00. Es una consulta sencilla pero práctica para ver cómo manejar filtros desde Python.
> 

```python
from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

cursor.execute("SELECT titulo_libro, precio FROM libros WHERE precio < 20.00")
resultados = cursor.fetchall()

print("Libros con precio menor a 20.00:")
for titulo, precio in resultados:
    print(f"{titulo} - ${precio}")

cursor.close()
conn.close()
```

---

### 6. `actualizar_precio.py` — Actualizar precio de un libro

> Permito al usuario cambiar el precio de un libro. Si el libro existe, se actualiza y confirmo el cambio. Si no, informo que no se encontró el libro. Uso cursor.rowcount para saber si la actualización tuvo efecto.
> 

```python
from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

libro = input("Título del libro a actualizar: ")
nuevo_precio = float(input("Nuevo precio: "))

cursor.execute("UPDATE libros SET precio = %s WHERE titulo_libro = %s", (nuevo_precio, libro))
conn.commit()

if cursor.rowcount > 0:
    print("Precio actualizado correctamente.")
else:
    print("Libro no encontrado.")

cursor.close()
conn.close()
```

---

### 7. `eliminar_libro.py` — Eliminar un libro

> Por último, este script permite eliminar un libro por su título. Igual que antes, aviso si se eliminó correctamente o si el libro no existía en la base de datos.
> 

```python
from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

libro = input("Título del libro a eliminar: ")

cursor.execute("DELETE FROM libros WHERE titulo_libro = %s", (libro,))
conn.commit()

if cursor.rowcount > 0:
    print("Libro eliminado correctamente.")
else:
    print("Libro no encontrado.")

cursor.close()
conn.close()
```