// =======================================
//  ex04 — Primeras agregaciones
// =======================================
//
// Seguimos usando:
//
// studentsDF
//
// Columnas:
//
// student_id,name,age,course,grade
//
// 1) Obtener cuántos alumnos hay
// por curso.
//
// 2) Obtener la nota media
// de cada curso.
//
// 3) Ordenar el resultado anterior
// por nota media descendente.
//
// 4) Crear una nueva columna:
//
// result
//
// Reglas:
//
// grade < 5 → "Suspenso"
// grade >=5 → "Aprobado"
//
// 5) Mostrar:
//
// name
// grade
// result
//
// =======================================


// Cargamos el fichero como DataFrame

val studentsDF = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/students/students.csv")

// Apartado 1: Obtener cuántos alumnos hay por curso

studentsDF.groupBy("course").count().show()

// Apartado 2: Obtener la nota media de cada curso

studentsDF.groupBy("course").avg("grade").show()

// Apartado 3: Ordenar el resultado anterior por nota media descendente

studentsDF.groupBy("course").avg("grade").alias("avg_grade").orderBy($"avg_grade".desc).show()

// Apartado 4: Crear una nueva columna result con las reglas indicadas

val studentsWithResultDF = studentsDF.withColumn("result", when($"grade" < 5, "Suspenso").otherwise("Aprobado"))

// Apartado 5: Mostrar name, grade y result

studentsWithResultDF.select("name", "grade", "result").show()

