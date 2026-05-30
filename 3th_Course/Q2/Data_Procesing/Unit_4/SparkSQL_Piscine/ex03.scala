// =======================================
//  ex03 — HDFS + SQL inicial
// =======================================
//
// Archivo: students.csv
//
// Columnas:
//
// student_id,name,age,course,grade
//
// 1) Descarga el fichero usando wget.
//
// 2) Crea en HDFS:
//
// /data/students/
//
// y copia el fichero dentro.
//
// 3) Comprueba que el fichero existe en HDFS.
//
// 4) Arranca Spark y carga el archivo desde HDFS
// en un DataFrame:
//
// studentsDF
//
// usando:
//
// - header=true
// - inferSchema=true
//
// 5) Muestra:
//
// - primeras filas
// - esquema
//
// 6) Registra el DataFrame como vista temporal:
//
// students
//
// 7) Utilizando Spark SQL:
//
// Obtener todos los alumnos con:
//
// grade >= 7
//
// Guardar el resultado en:
//
// goodStudents
//
// Mostrar resultado.
//
// 8) Utilizando la API de DataFrames
// (sin SQL):
//
// Mostrar únicamente:
//
// name
// course
//
// de los alumnos mayores de 20 años.
//
// 9) Ordenar los alumnos por nota
// de mayor a menor.
//
// =======================================

// Apartado 1

// wget -O students.csv https://example.com/students.csv

// Apartado 2

// hdfs dfs -mkdir -p /data/students 
// se añade dfs para indicar que se trata de una operación sobre HDFS

// hdfs dfs -put students.csv /data/students/

// Apartado 3

// hdfs dfs -ls /data/students/
// hdfs dfs -cat /data/students/students.csv | head

// Apartado 4

// spark-shell

val studentsDF = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/students/students.csv")

// Apartado 5

studentsDF.show()

studentsDF.printSchema()

// Apartado 6

studentsDF.createOrReplaceTempView("students")

// Apartado 7

val goodStudents = spark.sql("SELECT * FROM students WHERE grade >= 7")
goodStudents.show()

// Apartado 8

studentsDF.filter(studentsDF("age") > 20).select("name", "course").show()

// Apartado 9

studentsDF.orderBy(studentsDF("grade").desc).show()

