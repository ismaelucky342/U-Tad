# Test Unidad 3: Fuentes de Datos de Tipo Texto con Python

## 1. APIs de Redes Sociales

**1.** ¿Qué significa la sigla API?
- [ ] A) Advanced Programming Interface
- [ ] B) Application Programming Interface
- [ ] C) Advanced Process Integration
- [ ] D) Application Process Interaction

**2.** ¿Cuál es el formato típico de respuesta de las APIs de redes sociales?
- [ ] A) XML
- [ ] B) CSV
- [ ] C) JSON
- [ ] D) YAML

**3.** ¿Qué librería de Python se usa comúnmente para hacer peticiones HTTP a APIs?
- [ ] A) urllib
- [ ] B) requests
- [ ] C) http
- [ ] D) web

**4.** ¿En qué se diferencia un API REST de otros tipos de APIs?
- [ ] A) Es más antiguo
- [ ] B) Funciona sin internet
- [ ] C) Utiliza principios REST con métodos HTTP
- [ ] D) No tiene autenticación

**5.** ¿Qué es un Bearer Token en autenticación de APIs?
- [ ] A) Una contraseña simple
- [ ] B) Un token usado en OAuth para autenticar peticiones
- [ ] C) Un nombre de usuario
- [ ] D) Una clave pública

**6.** ¿Cuál es el endpoint típico para buscar tweets en la API de X (Twitter)?
- [ ] A) /tweets/search
- [ ] B) /search/tweets
- [ ] C) /2/tweets/search/recent
- [ ] D) /api/search

**7.** ¿Qué cambio ha sufrido la API de X (Twitter) en años recientes?
- [ ] A) Se ha vuelto más abierta
- [ ] B) Se ha vuelto más restrictiva y requiere planes de pago
- [ ] C) Desaparició completamente
- [ ] D) Se unificó con Facebook

**8.** ¿Qué es RapidAPI?
- [ ] A) Un operador de telefonía
- [ ] B) Una plataforma de agregación de APIs con endpoints de prueba
- [ ] C) Un navegador web
- [ ] D) Un gestor de bases de datos

**9.** Para usar la API de Reddit con PRAW, ¿qué credencial es necesaria?
- [ ] A) Solo usuario y contraseña
- [ ] B) client_id y client_secret
- [ ] C) Token de Facebook
- [ ] D) API Key de Google

**10.** ¿En qué URL se registran las aplicaciones para acceder a la API de Reddit?
- [ ] A) reddit.com/dev
- [ ] B) reddit.com/prefs/apps
- [ ] C) api.reddit.com/register
- [ ] D) reddit.com/api/apps

---

## 2. Librerías para APIs

**11.** ¿Cuál es la librería oficial de Python para acceder a la API de Reddit?
- [ ] A) redditapi
- [ ] B) PRAW (Python Reddit API Wrapper)
- [ ] C) reddit-py
- [ ] D) reddit

**12.** ¿Cómo se instala PRAW?
- [ ] A) pip install reddit
- [ ] B) pip install praw
- [ ] C) pip install reddit-api
- [ ] D) pip install reddit-wrapper

**13.** En PRAW, ¿qué es un subreddit?
- [ ] A) Una publicidad
- [ ] B) Un subforo temático dentro de Reddit
- [ ] C) Una API de Reddit
- [ ] D) Un usuario

**14.** ¿Cómo se obtiene un objeto Reddit con PRAW?
- [ ] A) reddit = PRAW()
- [ ] B) reddit = praw.Reddit(client_id=..., client_secret=..., user_agent=...)
- [ ] C) reddit = connect_reddit()
- [ ] D) reddit = Reddit.init()

**15.** En PRAW, ¿qué método obtiene los posts más calientes de un subreddit?
- [ ] A) subreddit.top()
- [ ] B) subreddit.hot()
- [ ] C) subreddit.new()
- [ ] D) subreddit.best()

**16.** ¿Qué es httpx en comparación con requests?
- [ ] A) Lo mismo que requests
- [ ] B) Una alternativa más moderna con soporte async
- [ ] C) Un protocolo de red
- [ ] D) Una base de datos

**17.** ¿Cuál es una importancia de usar requests para APIs?
- [ ] A) Es incapaz de autenticar
- [ ] B) Permite controlar headers y parámetros de forma flexible
- [ ] C) Solo funciona con XML
- [ ] D) No maneja códigos de estado HTTP

**18.** ¿Qué método HTTP se usa generalmente para obtener datos en APIs REST?
- [ ] A) POST
- [ ] B) PUT
- [ ] C) GET
- [ ] D) DELETE

**19.** ¿Qué status code HTTP indica una petición exitosa?
- [ ] A) 400
- [ ] B) 404
- [ ] C) 200
- [ ] D) 500

**20.** ¿Qué significa status code 401?
- [ ] A) Recurso no encontrado
- [ ] B) Servidor no disponible
- [ ] C) No autorizado
- [ ] D) Solicitud malformada

---

## 3. Web Scraping - Conceptos Básicos

**21.** ¿Qué es Web Scraping?
- [ ] A) Limpiar navegadores web
- [ ] B) Técnica para extraer información de páginas web
- [ ] C) Un lenguaje de programación
- [ ] D) Un servidor web

**22.** ¿Cuál es la diferencia entre sitios estáticos y dinámicos?
- [ ] A) No hay diferencia
- [ ] B) Los estáticos tienen HTML completo al responder; los dinámicos generan contenido con JavaScript
- [ ] C) Los dinámicos no tienen CSS
- [ ] D) Los estáticos requieren base de datos

**23.** ¿Para qué se usa BeautifulSoup?
- [ ] A) Preparar soup (sopa)
- [ ] B) Parsear y navegar documentos HTML
- [ ] C) Compilar código Python
- [ ] D) Crear bases de datos

**24.** ¿Para qué se usa Selenium?
- [ ] A) Un tipo de mineral
- [ ] B) Automatizar navegadores web para sitios dinámicos
- [ ] C) Crear servidores web
- [ ] D) Compilar código

**25.** ¿Cuál es la diferencia principal entre BeautifulSoup y Selenium?
- [ ] A) BeautifulSoup es más rápido
- [ ] B) BeautifulSoup parsea HTML estático; Selenium simula un navegador completo
- [ ] C) Selenium no funciona con Python
- [ ] D) BeautifulSoup requiere JavaScript

**26.** ¿Cómo se instala BeautifulSoup?
- [ ] A) pip install beautifulsoup
- [ ] B) pip install bs4
- [ ] C) pip install beautiful-soup
- [ ] D) pip install soup

**27.** ¿Cómo se instala Selenium?
- [ ] A) pip install selenium-web
- [ ] B) pip install selenium
- [ ] C) pip install web-automation
- [ ] D) pip install browser-automation

**28.** ¿Qué es un selector CSS?
- [ ] A) Un tipo de cookie
- [ ] B) Una forma de seleccionar elementos HTML específicos
- [ ] C) Un protocolo de red
- [ ] D) Un servidor

**29.** ¿Qué herramienta del navegador ayuda a identificar selectores?
- [ ] A) Inspector de elementos (Developer Tools)
- [ ] B) Consola de PHP
- [ ] C) Gestor de archivos
- [ ] D) Terminal del sistema

**30.** ¿Cómo se obtiene el HTML de una página web con requests?
- [ ] A) requests.html(url)
- [ ] B) response = requests.get(url); html = response.text
- [ ] C) requests.fetch(url)
- [ ] D) requests.download(url)

---

## 4. BeautifulSoup en Detalle

**31.** ¿Cómo se crea un objeto BeautifulSoup?
- [ ] A) soup = Beautiful(html)
- [ ] B) soup = BeautifulSoup(html, 'html.parser')
- [ ] C) soup = parse_html(html)
- [ ] D) soup = HTMLParser(html)

**32.** ¿Cuál es el parsers recomendado para BeautifulSoup?
- [ ] A) 'xml'
- [ ] B) 'lxml'
- [ ] C) 'html.parser' o 'lxml'
- [ ] D) 'json'

**33.** ¿Cómo se encuentra un elemento específico con BeautifulSoup?
- [ ] A) soup.find('tag')
- [ ] B) soup.select('selector')
- [ ] C) Ambas opciones
- [ ] D) ninguna

**34.** ¿Cuál es la diferencia entre find() y find_all()?
- [ ] A) No hay diferencia
- [ ] B) find() retorna el primer match; find_all() retorna una lista
- [ ] C) find_all() es más lento
- [ ] D) find() solo busca en texto

**35.** ¿Cómo se obtiene el texto dentro de una etiqueta HTML?
- [ ] A) element.html
- [ ] B) element.text o element.get_text()
- [ ] C) element.content
- [ ] D) element.string_value()

**36.** ¿Cómo se obtiene un atributo de una etiqueta HTML con BeautifulSoup?
- [ ] A) element.attributes['attr']
- [ ] B) element['attr'] o element.get('attr')
- [ ] C) element.attr
- [ ] D) element.get_attribute('attr')

**37.** ¿Cómo se navega entre elementos padres e hijos?
- [ ] A) element.parent, element.children
- [ ] B) element.up(), element.down()
- [ ] C) element.ancestor, element.descendants
- [ ] D) No es posible

**38.** ¿Qué método retorna un generador de hermanos de un elemento?
- [ ] A) element.siblings
- [ ] B) element.next_sibling / element.previous_sibling
- [ ] C) element.brothers()
- [ ] D) element.peers()

**39.** ¿Cómo se pueden combinar selectores CSS en BeautifulSoup?
- [ ] A) No es posible
- [ ] B) soup.select('sel1, sel2')
- [ ] C) soup.select('sel1 sel2')
- [ ] D) Solo con find()

**40.** ¿Cuál es el parser más rápido en BeautifulSoup?
- [ ] A) 'html.parser'
- [ ] B) 'lxml'
- [ ] C) 'html5lib'
- [ ] D) Todos igual

---

## 5. Selenium para Scraping Dinámico

**41.** ¿Para qué se utiliza Selenium en web scraping?
- [ ] A) Compilar Python
- [ ] B) Automatizar navegadores para sitios con JavaScript
- [ ] C) Crear APIs
- [ ] D) Almacenar datos

**42.** ¿Qué se necesita instalar además de Selenium?
- [ ] A) Un navegador (Chrome, Firefox, etc.) y su WebDriver
- [ ] B) Only Selenium
- [ ] C) Node.js
- [ ] D) PHP

**43.** ¿Cómo se inicia un navegador Chrome con Selenium?
- [ ] A) driver = Selenium.Chrome()
- [ ] B) driver = webdriver.Chrome()
- [ ] C) driver = Browser('Chrome')
- [ ] D) driver = start_browser('chrome')

**44.** ¿Cuál es el método para acceder a una URL con Selenium?
- [ ] A) driver.open(url)
- [ ] B) driver.get(url)
- [ ] C) driver.navigate(url)
- [ ] D) driver.request(url)

**45.** ¿Cómo se encuentran elementos en Selenium?
- [ ] A) driver.find_element(By.ID, 'id_value')
- [ ] B) driver.find('id_value')
- [ ] C) driver.select('id_value')
- [ ] D) driver.get_element()

**46.** ¿Qué es un wait en Selenium?
- [ ] A) Un descanso del programa
- [ ] B) Esperar a que un elemento esté presente en la página
- [ ] C) Un método para acelerar la ejecución
- [ ] D) Un tipo de error

**47.** ¿Cuál es la diferencia entre wait explícito e implícito?
- [ ] A) No hay diferencia
- [ ] B) Explícito espera a condiciones específicas; implícito espera siempre el mismo tiempo
- [ ] C) Implícito es más rápido
- [ ] D) Explícito no funciona con JavaScript

**48.** ¿Cómo se hace scroll en una página con Selenium?
- [ ] A) driver.scroll(x, y)
- [ ] B) driver.execute_script("window.scrollBy(x, y)")
- [ ] C) driver.scroll_to(x, y)
- [ ] D) No es posible

**49.** ¿Cómo se realiza un clic en un elemento con Selenium?
- [ ] A) element.click()
- [ ] B) element.press()
- [ ] C) element.activate()
- [ ] D) element.touch()

**50.** ¿Cómo se escribe texto en un campo con Selenium?
- [ ] A) element.type('texto')
- [ ] B) element.send_keys('texto')
- [ ] C) element.write('texto')
- [ ] D) element.input('texto')

---

## 6. Pandas - Operaciones Avanzadas

**51.** ¿Cuál es el comando para hacer un merge de dos DataFrames?
- [ ] A) df1.join(df2)
- [ ] B) pd.merge(df1, df2, on='key')
- [ ] C) df1.combine(df2)
- [ ] D) merge_dataframes(df1, df2)

**52.** ¿Qué tipos de merge existen?
- [ ] A) inner, outer
- [ ] B) left, right
- [ ] C) inner, left, right, outer (full outer)
- [ ] D) Solo uno

**53.** ¿Cuál es la diferencia entre join() y merge()?
- [ ] A) No hay diferencia
- [ ] B) join() usa índices; merge() usa columnas
- [ ] C) merge() es más lento
- [ ] D) join() no funciona con dos DataFrames

**54.** ¿Cómo se unen DataFrames verticalmente?
- [ ] A) pd.merge(df1, df2)
- [ ] B) pd.concat([df1, df2], axis=0)
- [ ] C) df1.append(df2)
- [ ] D) df1.combine(df2)

**55.** ¿Cómo se convierten strings JSON en columnas?
- [ ] A) df['col'].json_decode()
- [ ] B) pd.json_normalize(df['json_col'])
- [ ] C) json.loads(df['col'])
- [ ] D) df['col'].parse_json()

**56.** ¿Cómo se aplica una función a cada elemento de una Series?
- [ ] A) series.map(function)
- [ ] B) series.apply(function)
- [ ] C) Both
- [ ] D) Neither

**57.** ¿Cómo se manejan valores NaN en Pandas?
- [ ] A) df.fill_na(value)
- [ ] B) df.fillna(value)
- [ ] C) df.replace_null()
- [ ] D) df.clean()

**58.** ¿Cómo se eliminan filas con NaN?
- [ ] A) df.drop_na()
- [ ] B) df.dropna()
- [ ] C) df.remove_null()
- [ ] D) df.clean_null()

**59.** ¿Cómo se convierten tipos de datos en Pandas?
- [ ] A) df.as_type()
- [ ] B) df.astype()
- [ ] C) df.convert_type()
- [ ] D) df.to_type()

**60.** ¿Cuál es el formato Parquet?
- [ ] A) Un tipo de texto
- [ ] B) Un formato columnar eficiente para Big Data
- [ ] C) Un protocolo de red
- [ ] D) Un tipo de JSON

---

## 7. Polars - Operaciones Avanzadas

**61.** ¿Cuál es la principal ventaja de Polars sobre Pandas?
- [ ] A) Mejor legibilidad
- [ ] B) Mejor performance y eficiencia en memoria con lazy evaluation
- [ ] C) Más antiguo
- [ ] D) No tiene ventajas

**62.** ¿Cómo se hace lazy evaluation en Polars?
- [ ] A) df.lazy()
- [ ] B) lazy_df = pl.LazyFrame(data); lazy_df.collect()
- [ ] C) Polars siempre es lazy
- [ ] D) No es posible

**63.** ¿Cuál es una ventaja de usar lazy evaluation?
- [ ] A) Es más lento
- [ ] B) Optimiza la query antes de ejecutar
- [ ] C) No hay beneficios
- [ ] D) Usa más memoria

**64.** ¿Cómo se hace un join en Polars?
- [ ] A) df1.bind(df2)
- [ ] B) df1.join(df2, on='key')
- [ ] C) pl.join(df1, df2)
- [ ] D) df1.merge(df2)

**65.** ¿Cuál es una operación common en Polars?
- [ ] A) .with_columns() para crear o modificar columnas
- [ ] B) .select() para seleccionar columnas
- [ ] C) .filter() para filtrar
- [ ] D) Todas

**66.** ¿Cómo se lee un archivo Parquet en Polars?
- [ ] A) pl.read_parquet('file.parquet')
- [ ] B) pl.load_parquet('file.parquet')
- [ ] C) Polars.import_parquet()
- [ ] D) pl.open_parquet()

**67.** ¿Cómo se convierte un DataFrame de Pandas a Polars?
- [ ] A) polars.from_pandas(df)
- [ ] B) pl.from_pandas(df)
- [ ] C) Ambas
- [ ] D) No es posible

**68.** ¿Cuál es una limitación de Polars comparado con Pandas?
- [ ] A) No tiene ninguna
- [ ] B) Menos librerías integradas y comunidad más pequeña
- [ ] C) No funciona en Python
- [ ] D) Solo funciona en Windows

**69.** ¿Cómo se agrupan datos en Polars?
- [ ] A) df.group_by('col').agg(...)
- [ ] B) df.groupby('col').agg(...)
- [ ] C) df.group('col')
- [ ] D) df.cluster('col')

**70.** ¿Qué ventaja tiene Polars en expresiones?
- [ ] A) No tiene expresiones
- [ ] B) Las expresiones de Polars son más eficientes y se pueden paralelizar
- [ ] C) Las expresiones de Pandas son mejores
- [ ] D) No hay diferencia

---

## 8. PySpark - Introducci​ón

**71.** ¿Qué es Apache Spark?
- [ ] A) Un servidor web
- [ ] B) Un framework para procesamiento distribuido de big data
- [ ] C) Una base de datos
- [ ] D) Un navegador

**72.** ¿Cuál es la diferencia entre Spark y Hadoop?
- [ ] A) No hay diferencia
- [ ] B) Spark procesa en memoria; Hadoop en disco (generalmente)
- [ ] C) Hadoop es más rápido
- [ ] D) Spark no es distribuido

**73.** ¿Qué es PySpark?
- [ ] A) Una base de datos
- [ ] B) La interfaz de Python para Apache Spark
- [ ] C) Un lenguaje de programación
- [ ] D) Un servidor web

**74.** ¿Cómo se instala PySpark?
- [ ] A) pip install spark
- [ ] B) pip install pyspark
- [ ] C) pip install apache-spark
- [ ] D) Download desde apache.org

**75.** ¿Qué es un RDD en Spark?
- [ ] A) Una base de datos
- [ ] B) Resilient Distributed Dataset: colección inmutable distribuida
- [ ] C) Un tipo de archivo
- [ ] D) Un protocolo de red

**76.** ¿Cuál es la diferencia entre RDD y DataFrame en Spark?
- [ ] A) No hay diferencia
- [ ] B) RDD es más bajo nivel; DataFrame es más abstracto como SQL
- [ ] C) DataFrame es más antiguo
- [ ] D) RDD es más rápido

**77.** ¿Cómo se crea un SparkContext?
- [ ] A) sc = Spark()
- [ ] B) sc = SparkContext('local', 'app-name')
- [ ] C) sc = spark_init()
- [ ] D) sc = create_spark()

**78.** ¿Qué es un SparkSession?
- [ ] A) La interfaz antigua (RDD)
- [ ] B) La interfaz moderna unificada para Spark
- [ ] C) Un tipo de memoria
- [ ] D) Un archivo de configuración

**79.** ¿Cómo se crea un SparkSession?
- [ ] A) spark = SparkSession.builder.appName('app').getOrCreate()
- [ ] B) spark = Spark.session('app')
- [ ] C) spark = SparkSession.init()
- [ ] D) spark = create_session('app')

**80.** ¿Cuál es el modo de ejecución "local" en Spark?
- [ ] A) Solo ejecuta en un ordenador particular
- [ ] B) Ejecuta en múltiples máquinas de la red
- [ ] C) Ejecuta solo en servidores en la nube
- [ ] D) No existe

---

## 9. PySpark - DataFrames

**81.** ¿Cómo se lee un archivo CSV con PySpark?
- [ ] A) pd.read_csv('file.csv')
- [ ] B) spark.read.csv('file.csv', header=True)
- [ ] C) spark.load_csv('file.csv')
- [ ] D) spark.import_csv('file.csv')

**82.** ¿Cómo se lee un archivo JSON con PySpark?
- [ ] A) spark.read.json('file.json')
- [ ] B) spark.load_json()
- [ ] C) spark.import_json()
- [ ] D) json.load_spark()

**83.** ¿Cómo se escribe un DataFrame de PySpark a Parquet?
- [ ] A) df.save_parquet('path')
- [ ] B) df.write.mode('overwrite').parquet('path')
- [ ] C) df.to_parquet('path')
- [ ] D) spark.write_parquet(df, 'path')

**84.** ¿Qué es la partición en PySpark?
- [ ] A) Una sección de un archivo
- [ ] B) División lógica de datos distribuida en nodos
- [ ] C) Una columna de la tabla
- [ ] D) Un tipo de índice

**85.** ¿Cómo se filtra un DataFrame en PySpark?
- [ ] A) df.where(condition)
- [ ] B) df.filter(condition)
- [ ] C) Ambas
- [ ] D) Neither

**86.** ¿Cómo se seleccionan columnas en PySpark?
- [ ] A) df.select('col')
- [ ] B) df['col']
- [ ] C) df.select('col1', 'col2', ...)
- [ ] D) All of above

**87.** ¿Cómo se hace un join en PySpark?
- [ ] A) df1.join(df2, on='key')
- [ ] B) df1.merge(df2)
- [ ] C) spark.join(df1, df2)
- [ ] D) df1.bind(df2)

**88.** ¿Cómo se agrupa datos en PySpark?
- [ ] A) df.groupBy('col').agg(...)
- [ ] B) df.group_by('col')
- [ ] C) df.groupby('col')
- [ ] D) df.aggregate('col')

**89.** ¿Cuál es una transformación en PySpark?
- [ ] A) Una acción que retorna un resultado
- [ ] B) Una operación lazy que retorna otro RDD/DataFrame
- [ ] C) Solo puede ser filter
- [ ] D) No existen transformaciones

**90.** ¿Cuál es una acción en PySpark?
- [ ] A) select(), filter()
- [ ] B) collect(), show(), count()
- [ ] C) Ambas son acciones
- [ ] D) No existen acciones

---

## 10. PySpark - Operaciones Avanzadas

**91.** ¿Qué es una ventana (window function) en PySpark?
- [ ] A) Una interfaz gráfica
- [ ] B) Computar operaciones sobre grupos/particiones de datos
- [ ] C) Un tipo de archivo
- [ ] D) Un protocolo

**92.** ¿Cuál es el método show() en PySpark?
- [ ] A) Guarda los datos
- [ ] B) Muestra las primeras filas en formato tabular
- [ ] C) Calcula estadísticas
- [ ] D) Elimina la tabla

**93.** ¿Cómo se explora el schema de un DataFrame en PySpark?
- [ ] A) df.schema
- [ ] B) df.printSchema()
- [ ] C) df.dtypes
- [ ] D) All above

**94.** ¿Cómo se convierten datos entre RDD y DataFrame?
- [ ] A) rdd.toDF()
- [ ] B) spark.createDataFrame(rdd)
- [ ] C) amb​as
- [ ] D) No es posible

**95.** ¿Cuál es la ventaja de usar PySpark vs Pandas para big data?
- [ ] A) No tiene ventajas
- [ ] B) Puede procesar datos mayores que la memoria disponible
- [ ] C) Es más lento
- [ ] D) Solo para Windows

**96.** ¿Cómo se cachea un DataFrame en PySpark?
- [ ] A) df.cache()
- [ ] B) df.persist()
- [ ] C) Ambas
- [ ] D) No es posible

**97.** ¿Por qué es importante hacer cache en PySpark?
- [ ] A) No es importante
- [ ] B) Evita recalcular transformaciones en acciones múltiples
- [ ] C) Reduce el código
- [ ] D) Acelera always

**98.** ¿Cuál es la diferencia entre saveAsTable() y write.mode()?
- [ ] A) No hay diferencia
- [ ] B) saveAsTable crea tabla hive; write.mode controla sobrescritura
- [ ] C) write.mode es más antiguo
- [ ] D) Ambos hacen lo mismo

**99.** ¿Cómo se ejecuta SQL en PySpark?
- [ ] A) spark.sql('SELECT * FROM table')
- [ ] B) spark.query('SELECT * FROM table')
- [ ] C) spark.execute_sql()
- [ ] D) sql.run('SELECT * FROM table')

**100.** ¿Cuál es el factor más importante al usar PySpark?
- [ ] A) Tener muchas máquinas
- [ ] B) Entender lazy evaluation y optimizar queries
- [ ] C) No es importante
- [ ] D) Solo usar RDDs

---

## SOLUCIONARIO

| Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta |
|----------|-----------|----------|-----------|----------|-----------|
| 1 | B | 34 | B | 67 | B |
| 2 | C | 35 | B | 68 | B |
| 3 | B | 36 | B | 69 | A |
| 4 | C | 37 | A | 70 | B |
| 5 | B | 38 | B | 71 | B |
| 6 | C | 39 | C | 72 | B |
| 7 | B | 40 | B | 73 | B |
| 8 | B | 41 | B | 74 | B |
| 9 | B | 42 | A | 75 | B |
| 10 | B | 43 | B | 76 | B |
| 11 | B | 44 | B | 77 | B |
| 12 | B | 45 | A | 78 | B |
| 13 | B | 46 | B | 79 | A |
| 14 | B | 47 | B | 80 | A |
| 15 | B | 48 | B | 81 | B |
| 16 | B | 49 | A | 82 | A |
| 17 | B | 50 | B | 83 | B |
| 18 | C | 51 | B | 84 | B |
| 19 | C | 52 | C | 85 | C |
| 20 | C | 53 | B | 86 | D |
| 21 | B | 54 | B | 87 | A |
| 22 | B | 55 | B | 88 | A |
| 23 | B | 56 | C | 89 | B |
| 24 | B | 57 | B | 90 | B |
| 25 | B | 58 | B | 91 | B |
| 26 | B | 59 | B | 92 | B |
| 27 | B | 60 | B | 93 | D |
| 28 | B | 61 | B | 94 | C |
| 29 | A | 62 | B | 95 | B |
| 30 | B | 63 | B | 96 | C |
| 31 | B | 64 | B | 97 | B |
| 32 | C | 65 | D | 98 | B |
| 33 | C | 66 | A | 99 | A |
| | | | | 100 | B |
