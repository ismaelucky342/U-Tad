//## EJERCICIO 5 (VARIANTE 3) — Spark SQL + HDFS (2 puntos)
//
//**Enunciado general:**
//Vamos a trabajar con Spark SQL utilizando el dataset `sales_products.csv` (sobre ventas de productos) para realizar una serie de consultas. Debes escribir el código limpio en tu archivo `.scala`, asegurándote de comentar los comandos de terminal para que no den errores de compilación.
//
//### Apartados del ejercicio
//
//* **Apartado 1 (0,1 pts):** Descargar el fichero `sales_products.csv` y explorar su contenido en el sistema local (por ejemplo, con el comando `head`).
//* **Apartado 2 (0,2 pts):** Arrancar HDFS y copiar el fichero `sales_products.csv` desde el entorno local a la ruta `/data/sales/` de HDFS.
//* **Apartado 3 (0,1 pts):** Comprobar con un comando nativo de `hdfs` que el fichero está correctamente creado en la ruta pedida.
//* **Apartado 4 (0,2 pts):** Arrancar Spark y leer el fichero `sales_products.csv` de HDFS en una variable RDD llamada `SalesRDD`.
//* *Nota:* La ruta en HDFS es `hdfs://localhost:9000/data/sales/sales_products.csv` y el archivo contiene una línea de cabecera que debes filtrar de forma segura.
//
//
//* **Apartado 5 (0,4 pts):** Usando exclusivamente el RDD limpio creado en el paso anterior, sus transformaciones y acciones, responde a la siguiente pregunta: **¿cuántas ventas (registros) se han realizado por cada categoría de producto (`Category`)?**
//* *Resultado esperado (ejemplo de formato):*
//```text
//(Electronics,540)
//(Clothing,320)
//(Home,115)
//...
//
//```
//
//
//
//
//* **Apartado 6 (0,2 pts):** Cargar el mismo CSV desde HDFS como un **DataFrame** (en una variable llamada `dfSales`), infiriendo automáticamente el tipo de datos y usando la primera fila como cabecera.
//* **Apartado 7 (0,1 pts):** Registrar el DataFrame `dfSales` como una tabla/vista temporal para consultas SQL llamada `sales`.
//* **Apartado 8 (0,4 pts):** Realizar una **consulta SQL** (sobre la tabla `sales`) para obtener los productos de la categoría Electrónica (`Category = 'Electronics'`) que tengan un precio mayor o igual a 500 (`Price >= 500`). El resultado debe ordenarse por el precio de forma descendente, guardarse en la variable `electronicaTop` y mostrarse por pantalla.
//* **Apartado 9 (0,3 pts):** Usando la **API de DataFrames** (no SQL), obtener los productos cuyo estado de stock (`Stock_Status`) sea *"In Stock"* y cuya cantidad vendida (`Quantity`) sea superior a 10 unidades. Muestra el resultado final por pantalla (evita usar el símbolo `$` para que no dependa de imports implícitos).

// Resolución del ejercicio:

// Apartado 1
// Descargar el fichero `sales_products.csv` y explorar su contenido en el sistema local (ejemplo):
// wget https://example.com/sales_products.csv
// head sales_products.csv  

// Apartado 2
// Arrancar HDFS y copiar el fichero `sales_products.csv` desde el entorno local a la ruta `/data/sales/` de HDFS (ejemplo):
// start-dfs.sh
// hdfs dfs -mkdir -p /data/sales
// hdfs dfs -put sales_products.csv /data/sales/

// Apartado 3
// Comprobar con un comando nativo de `hdfs` que el fichero está correctamente creado en la ruta pedida (ejemplo):
// hdfs dfs -ls /data/sales
// hdfs dfs -cat /data/sales/sales_products.csv | head

// Apartado 4 (cuidado con los filtrados agresivos para eliminar la cabecera, es mejor usar un filtrado seguro)
// Arrancar Spark y leer el fichero `sales_products.csv` de HDFS en una variable RDD llamada `SalesRDD` (ejemplo):
val SalesRDD = sc.textFile("hdfs://localhost:9000/data/sales/sales_products.csv")
val header = SalesRDD.first()
val datos = SalesRDD.filter(linea => linea != header) // Filtrado seguro para eliminar la cabecera del RDD      

// Apartado 5
// Usando exclusivamente el RDD limpio creado en el paso anterior, sus transformaciones y acciones, responde a la siguiente pregunta: **¿cuántas ventas (registros) se han realizado por cada categoría de producto (`Category`)?** (ejemplo):
val ventasPorCategoria = datos.map(line => line.split(",")(2)) // Asumiendo que la categoría está en la tercera columna
val conteoPorCategoria = ventasPorCategoria.map(categoria => (categoria, 1)).reduceByKey((a, b) => a + b)
val resultado = conteoPorCategoria.collect()
resultado.foreach(println)

// Apartado 6
// Cargar el mismo CSV desde HDFS como un **DataFrame** (en una variable llamada `dfSales`), infiriendo automáticamente el tipo de datos y usando la primera fila como cabecera (ejemplo):
val dfSales = spark.read.option("header", "true").option("inferSchema", "true").csv("hdfs://localhost:9000/data/sales/sales_products.csv")  

// Apartado 7
// Registrar el DataFrame `dfSales` como una tabla/vista temporal para consultas SQL llamada `sales` (ejemplo):
dfSales.createOrReplaceTempView("sales")    

// Apartado 8
// Realizar una **consulta SQL** (sobre la tabla `sales`) para obtener los productos de la categoría Electrónica (`Category = 'Electronics'`) que tengan un precio mayor o igual a 500 (`Price >= 500`). El resultado debe ordenarse por el precio de forma descendente, guardarse en la variable `electronicaTop` y mostrarse por pantalla (ejemplo    ):
val electronicaTop = spark.sql("SELECT * FROM sales WHERE Category = 'Electronics' AND Price >= 500 ORDER BY Price DESC")
electronicaTop.show()

// Apartado 9
// Usando la **API de DataFrames** (no SQL), obtener los productos cuyo estado de stock (`Stock_Status`) sea *"In Stock"* y cuya cantidad vendida (`Quantity`)              
// sea superior a 10 unidades. Muestra el resultado final por pantalla (ejemplo):
val productosInStock = dfSales.filter($"Stock_Status" === "In Stock" && $"Quantity" > 10)
productosInStock.show()