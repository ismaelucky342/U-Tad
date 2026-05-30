//## EJERCICIO 9 — Spark SQL + HDFS (2 puntos)
//
// Enunciado general:
//
// Vamos a trabajar con Spark SQL utilizando
// el dataset `employees.csv`.
//
// El fichero contiene:
//
// Employee_ID
// Name
// Department
// Salary
// Experience_Years
//
// ### Apartados
//
// * Apartado 1 (0,1 pts):
// Descargar el fichero y explorar su contenido
// localmente.
//
// * Apartado 2 (0,2 pts):
// Crear la ruta:
//
// /data/employees/
//
// y copiar el fichero a HDFS.
//
// * Apartado 3 (0,1 pts):
// Verificar que el fichero se encuentra
// correctamente almacenado en HDFS.
//
// * Apartado 4 (0,2 pts):
// Leer el fichero desde HDFS como DataFrame:
//
// employeesDF
//
// Configuración:
//
// - header=true
// - inferSchema=true
//
// * Apartado 5 (0,2 pts):
// Mostrar:
//
// - primeras filas
// - esquema
//
// * Apartado 6 (0,3 pts):
// Obtener cuántos empleados existen
// por departamento.
//
// Mostrar resultado.
//
// * Apartado 7 (0,3 pts):
// Obtener el salario medio por departamento.
//
// Ordenar el resultado de mayor a menor.
//
// * Apartado 8 (0,3 pts):
// Crear una nueva columna:
//
// experience_label
//
// Reglas:
//
// Experience_Years < 3 -> "Junior"
//
// Experience_Years >=3 y <8 -> "Mid"
//
// Experience_Years >=8 -> "Senior"
//
// * Apartado 9 (0,3 pts):
// Utilizando la columna creada anteriormente:
//
// Obtener cuántos empleados hay
// por categoría.
//
// Mostrar resultado.
//
// =======================================


// Apartado 1 

// wget -O employees.csv https://example.com/employees.csv

// head employees.csv

// Apartado 2

// start-dfs.sh

// hdfs dfs -mkdir -p /data/employees
// hdfs dfs -put employees.csv /data/employees/

// Apartado 3

// hdfs dfs -ls /data/employees/
// hdfs dfs -cat /data/employees/employees.csv | head

// Apartado 4

val employeesDF = spark.read
  .option("header", "true")
  .option("inferSchema", "true")
  .csv("hdfs://localhost:9000/data/employees/employees.csv")
  
// Apartado 5

employeesDF.show()

employeesDF.printSchema()

// Apartado 6

val departmentCount = employeesDF
  .groupBy("Department")
  .count()

departmentCount.show()

// Apartado 7 

val avgSalaryByDepartment = employeesDF
  .groupBy("Department")
  .avg("Salary")
  .orderBy($"avg(Salary)".desc)

avgSalaryByDepartment.show()

// Apartado 8

val employeesWithExperienceLabel = employeesDF.withColumn("experience_label", 
  when($"Experience_Years" < 3, "Junior")
  .when($"Experience_Years" >= 3 && $"Experience_Years" < 8, "Mid")
  .otherwise("Senior")
)

// Apartado 9

val experienceLabelCount = employeesWithExperienceLabel
  .groupBy("experience_label")
  .count()

experienceLabelCount.show()



