# Unidad 3. Fuentes de datos de tipo texto con Python.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Apis De X (Twitter)/Reddit Y Otras Redes Sociales](#2-apis-de-x-twitterreddit-y-otras-redes-sociales)
  - [2.1 Introducción](#21-introducción)
  - [2.2 APIs de X (Twitter)](#22-apis-de-x-twitter)
  - [2.3 APIs de Reddit](#23-apis-de-reddit)
  - [2.4 Otras redes sociales](#24-otras-redes-sociales)
- [3. Web Scraping Tradicional Y Scraping De Interfaces Con Beautifulsoup Y Selenium](#3-web-scraping-tradicional-y-scraping-de-interfaces-con-beautifulsoup-y-selenium)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Estructura de los sitios web (HTML, CSS, JavaScript)](#32-estructura-de-los-sitios-web-html-css-javascript)
  - [3.3 Herramientas de inspección (Dev Tools y BurpSuite)](#33-herramientas-de-inspección-dev-tools-y-burpsuite)
  - [3.4 Query selectors](#34-query-selectors)
  - [3.5 Scraping tradicional (HTML estático) con BeautifulSoup](#35-scraping-tradicional-html-estático-con-beautifulsoup)
  - [3.6 Scraping dinámico con Selenium](#36-scraping-dinámico-con-selenium)
  - [3.7 Selenium VS BeautifulSoup](#37-selenium-vs-beautifulsoup)
  - [3.8 Ética y legalidad](#38-ética-y-legalidad)
  - [3.9 Enlaces de interés](#39-enlaces-de-interés)
- [4. Manejo Detallado De Formatos Tabulares Con Pandas/Polars](#4-manejo-detallado-de-formatos-tabulares-con-pandaspolars)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Pipelline de datos: cómo obtener y analizar datos](#42-pipelline-de-datos-cómo-obtener-y-analizar-datos)
- [5. Formatos Tabulares En Cómputo Distribuido Con Pyspark](#5-formatos-tabulares-en-cómputo-distribuido-con-pyspark)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Cómputo distribuido vs Cómputo tradicional](#52-cómputo-distribuido-vs-cómputo-tradicional)
  - [5.3 Uso básico de PySpark](#53-uso-básico-de-pyspark)
  - [5.4 PySpark vs Pandas/Polars](#54-pyspark-vs-pandaspolars)
- [6. Conclusiones](#6-conclusiones)
  - [6.1 Conclusiones de la unidad](#61-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En las unidades anteriores, se abordaron el ecosistema Python, la manipulación de datos y diversas técnicas iniciales de minería de texto (como la limpieza y normalización, expresiones regulares, aproximaciones a librerías de NLP, etc.). Sin embargo, para cualquier proyecto real en el campo de la ingeniería de software o ciencia de datos, surge la necesidad de obtener los datos textuales de alguna fuente externa, ya sea un servicio de redes sociales, un sitio web, o un repositorio masivo de ficheros.

Esta unidad se centra en las fuentes de datos de tipo texto que se pueden explotar con Python:

- APIs de redes sociales (X (Twitter), Reddit, u otras), donde se extraen datos mediante peticiones REST y autenticaciones (OAuth, tokens, etc.).
- Web Scraping, tanto en su forma estática (HTML, parseado con BeautifulSoup) como dinámica (interacción con JavaScript/DOM mediante Selenium).
- Manejo detallado de formatos tabulares con Pandas y Polars, perfeccionando lo aprendido y resolviendo escenarios complejos de merges y transformaciones, específicamente en proyectos textuales.
- Formatos tabulares en entornos distribuidos con PySpark, presentando la arquitectura de Spark y los fundamentos de RDDs y DataFrames para procesar grandes volúmenes de datos textuales de manera escalable.

Con un enfoque ingenieril, se explicarán aspectos técnicos de autenticación (tokens, claves), la estructura interna de páginas web (HTML, CSS, JavaScript) y sus implicaciones en el scraping, la configuración de herramientas de developer para la extracción de selectores, y la organización de pipelines de datos en tabular (local con Pandas/Polars, o distribuido con PySpark).



- **APIs de X (Twitter)/Reddit y otras redes sociales**  
  Las APIs (son las siglas en inglés de: Application Programming Interfaces) nos permiten interactuar como usuarios con un servidor remoto. Estos pueden ser el de X (Twitter, el de Reddit u otros, permitiéndonos consultar datos de forma estructurada (normalmente con un formato JSON). Python nos sirve como herramienta para conectarnos a estas APIs mediante el uso de librerías de HTTP como requests o httpx.
- **Web Scraping tradicional y Scraping de interfaces con Beautifulsoup y Selenium**  
  En caso de no disponer de una API que nos permita acceder a datos textuales en un sitio web, o si la información que nos ofrece la plataforma no se encuentra expuesta de forma estructurada, tenemos la opción de usar web scraping. Es una técnica que consiste en obtener información de forma directa de las páginas, gracias a la interpretación de la estructura y el contenido del documento HTML. Una vez descargado o renderizado el HTML, podemos apuntar a secciones o nodos específicos para extraer texto, enlaces u otros atributos.
- **Manejo detallado de formatos tabulares con pandas/polars**  
  En Python, las librerías Pandas y Polars se han consolidado como opciones de referencia para trabajar con datos estructurados. A lo largo de las unidades anteriores ya se introdujeron sus capacidades principales, pero en este apartado se profundizará en situaciones más complejas y se mostrarán ejemplos prácticos que aprovechan los datos recogidos en el apartado de scraping y de APIs de redes sociales. El objetivo es ilustrar cómo construir un pipeline que vaya desde la obtención de datos crudos hasta la producción de informes o la persistencia en formatos avanzados como Parquet.
- **Formatos tabulares en computo distribuido con Pysark**  
  En este apartado se explicará qué es PySpark, cómo instalarlo y configurarlo en un entorno local, y se mostrarán ejemplos de lectura, manipulación y escritura de archivos tabulares. Además, se abordará la conexión con datos provenientes de APIs o de scraping, y cómo integrarlos en un flujo de trabajo distribuido.



#### Objetivos



Al concluir esta unidad, el estudiante será capaz de:



1. Conocer las opciones de acceso a datos textuales mediante APIs de redes sociales como Twitter o Reddit, incluyendo la posibilidad de usar APIs gratuitas o entornos mockeados.
2. Dominar el web scraping a distintos niveles.
3. Comprender la estructura HTML, etiquetas comunes y cómo se combina con CSS/JavaScript.
4. Emplear BeautifulSoup para parsear sitios estáticos.
5. Emplear Selenium para interactuar con sitios dinámicos o que requieran login/formularios.
6. Ampliar el manejo de datos tabulares con Pandas y Polars, profundizando en la lectura/escritura de formatos y en transformaciones avanzadas.
7. Conocer PySpark para procesar datos tabulares (incluyendo texto) en un entorno de cómputo distribuido, sentando las bases para escalabilidad en grandes proyectos de NLP.
8. Familiarizarse con buenas prácticas de extracción y almacenamiento, como la conversión de estructuras JSON a tablas, la limpieza de valores nulos e inconsistentes, y la planificación de pipelines robustos para análisis textual avanzado.



## 2. Apis De X (Twitter)/Reddit Y Otras Redes Sociales



### 2.1 Introducción



![image](assets/cm7uc9c870054356zb2h73zsg-stock-image.jpg)



En la actualidad, gran parte de la información textual proviene de plataformas online y redes sociales. X (Twitter), Reddit y otros sitios ofrecen datos muy valiosos para análisis de tendencias, minería de sentimientos o clasificación de documentos. Sin embargo, la obtención de datos desde dichos servicios requiere comprender las APIs que cada plataforma pone a disposición.

Las APIs (son las siglas en inglés de: Application Programming Interfaces) nos permiten interactuar como usuarios con un servidor remoto. Estos pueden ser el de X (Twitter, el de Reddit u otros, permitiéndonos consultar datos de forma estructurada (normalmente con un formato JSON). Python nos sirve como herramienta para conectarnos a estas APIs mediante el uso de librerías de HTTP como requests o httpx.

No obstante, existen limitaciones:

- Restricciones de acceso (claves, tokens de autenticación, cuotas de uso).
- Cambio de políticas (X (Twitter), por ejemplo, ha restringido su API en versiones recientes).
- Formatos de respuesta o endpoints en continuo cambio.

Para sortear estas dificultades, podemos recurrir a APIs abiertas de otras redes, o a servicios de agregación como RapidAPI, donde se encuentran endpoints de prueba o datos simulados. De igual forma, si no se desea consumir datos “en vivo,” se puede optar por un dataset preexistente (CSV/JSON con tweets antiguos) para fines de prototipado.



### 2.2 APIs de X (Twitter)



Hasta hace unos años, X (Twitter) disponía de planes gratuitos bastante amplios para desarrolladores, lo que permitía obtener grandes volúmenes de tuits. Sin embargo, el modelo ha cambiado y la API es ahora más restrictiva, requiriendo planes de pago incluso para determinados usos académicos. Esto hace más compleja la extracción de tuits en tiempo real si no se dispone de un presupuesto.

Proceso típico de conexión a la API de X (Twitter):

- Registrar una app en el panel [X (Twitter) Developer](X%20(Twitter)%20Developer) ([https://developer.x.com/](https://developer.x.com/))
- Obtener credenciales (API Key, API Secret, Access Token, Access Token Secret).
- Usar librerías como requests para autenticar.
- Llamar a endpoints (p. ej. GET /2/tweets/search/recent), pasando parámetros para filtrar hashtags, fechas, geolocalizaciones, etc.
- Recibir los resultados en formato JSON, parsearlos y almacenarlos.



![image](assets/cm7ucp5th00e6356zey7c8r1b-INSD_BAIN_U3_Imagen1.png)



Un ejemplo de cómo buscar tweets sería:



```javascript
import requests

bearer_token = "TU_BEARER_TOKEN"  # O la que obtengas al crear la app

headers = {
    "Authorization": f"Bearer {bearer_token}"
}

params = {
    "query": "datascience",
    "max_results": 1,
    "tweet.fields": "created_at,lang,public_metrics"
}

url = "https://api.twitter.com/2/tweets/search/recent"
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()

    print(data)
else:
    print("Error:", response.status_code, response.text)
```



Dando como output:



```coffeescript
{'data': [{'id': '1878761593665646904', 'edit_history_tweet_ids': ['1878761593665646904'], 'text': 'How to Build a Knowledge Graph in Minutes (And Make It Enterprise-Ready) https://t.co/nijdrcK8vP', 'lang': 'en', 'created_at': '2025-01-13T11:10:44.000Z', 'public_metrics': {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 1}}], 'meta': {'newest_id': '1878761593665646904', 'oldest_id': '1878760050992594949', 'result_count': 1, 'next_token': 'b26v89c19zqg8o3frr6u0vu0xver0glb6aj37vu6xuwl9'}}
```



Dado el panorama restrictivo de Twitter, conviene explorar APIs abiertas o datos simulados para proyectos educativos o de prototipado:



- **RapidAPI**  
  - [https://rapidapi.com/](https://rapidapi.com/)
  - Un marketplace donde se puede encontrar un endpoint que devuelva tweets ficticios o datos parecidos.
  - Se registra una cuenta, se busca una API con una mayor cuota disponible (por ejemplo: [https://rapidapi.com/alexanderxbx/api/twitter-api45](https://rapidapi.com/alexanderxbx/api/twitter-api45)), se obtienen las credenciales, y se llama a la URL con requests.get(...).
- **Datasets estáticos (CSV/JSON con tweets pasados)**  
  - Kaggle u otros repositorios de investigación publican archivos con tweets históricos o recortados.
  - Ideal para minería de texto sin depender de cuotas o credenciales cambiantes.
- **Otros repos**  
  - GitHub con “mock Twitter data” en formato JSON.
  - Scripts que generan tuits de prueba.
- **Inteligencia artificial**  
  - Obtén al menos un tweet con el contenido deseado para proporcionar de ejemplo.
  - Utiliza LLMs como ChatGPT, Gemini, Copilot, Claude, … para pedir que genere tweets en base al ejemplo proporcionado.



Veamos un ejemplo utilizando RapidAPI:



```python
import requests

url = "https://twitter-api45.p.rapidapi.com/search.php"
headers = {
    "x-rapidapi-key": "df8d187692mshbfb8dce733aa39cp1559b8jsn2fa8403013db",
    "x-rapidapi-host": "twitter-api45.p.rapidapi.com"
}
params = {
    "query": "datascience",
    "search_type":"Top"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    for tweet in data["timeline"]:
        user = tweet.get("user_info", {}).get("screen_name", "Unknown User")
        text = tweet.get("text", "No Text")
        print(f"User: {user}\nContent:\n{text}\n")
    else:
        print("Error:", response.status_code, response.text)
# Output
User: Python_Dv
Content:
Data Structures in Python

#dsa #datastructures #algorithms  #python #programming #developer #morioh #programmer #coding #coder #softwaredeveloper #computerscience #webdev #webdeveloper #webdevelopment #pythonprogramming #pythonquiz #ai #ml #machinelearning #datascience https://t.co/1iE85lVNNd

User: rhoda_lee_
Content:
I said I want to challenge myself this year
Here we go!🎉🙏🏾

#alxaccepted #alx #datascience #Tech https://t.co/6aWXpYFtYA
```



En el video a continuación, veremos en detalle cómo utilizar RapidAPI y sus diferentes soluciones:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651983_1/scormcontent/assets/INSD_BAIN_U3_Video1.mp4?v=1)



### 2.3 APIs de Reddit



Reddit es un foro masivo con subreddits temáticos donde los usuarios comparten posts y comentarios. La extracción de datos textuales puede realizarse mediante la API oficial o librerías como PRAW (Python Reddit API Wrapper). La referencia a su API se puede encontrar en:  [https://www.reddit.com/dev/api/](https://www.reddit.com/dev/api/).

En el caso de usar PRAW, para poder hacer llamadas a la API de Reddit deberemos seguir el siguiente proceso:

1. ![image](assets/cm7ucxj7400ne356zq1qj1obo-step1-INSD_BAIN_U3_Imagen2.png)
   [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/)
2. ![image](assets/cm7ucxj7400ne356zq1qj1obo-step2-INSD_BAIN_U3_Imagen3.png)
   Especificaremos la “url de redirección” como [https://localhost:8080](https://localhost:8080)
3. ![image](assets/cm7ucxj7400ne356zq1qj1obo-step3-Captura_20de_20pantalla_202025-03-04_20114629.jpg)
   El client_secret lo podemos obtener de la web tras crear la app, mientras el el client_id nos deberá llegar por email con el que hayamos creado la cuenta.
4. pip install praw.
5. Por ejemplo: posts más recientes en un subreddit



```markdown
import praw

reddit = praw.Reddit(
    # client_id="TU_CLIENT_ID",
    # client_secret="TU_CLIENT_SECRET",
    # user_agent="TU_NOMBRE "
)

subreddit = reddit.subreddit("datascience")
for post in subreddit.hot(limit=10):
    print(f"Post Title: {post.title}\nPost URL: {post.url}\nPost Content: {post.selftext}")
# Output:
Post Title: Weekly Entering & Transitioning - Thread 13 Jan, 2025 - 20 Jan, 2025
Post URL: https://www.reddit.com/r/datascience/comments/1i06k3y/weekly_entering_transitioning_thread_13_jan_2025/
Post Content:  

Welcome to this week's entering & transitioning thread! This thread is for any questions about getting started, studying, or transitioning into the data science field. Topics include:

* Learning resources (e.g. books, tutorials, videos)
* Traditional education (e.g. schools, degrees, electives)
* Alternative education (e.g. online courses, bootcamps)
* Job search questions (e.g. resumes, applying, career prospects)
* Elementary questions (e.g. where to start, what next)
…
```



Por contra, si queremos utilizar una solución más independiente y personalizada, podemos utilizar la librería requests de la siguiente manera:

1. Registrar la app en Reddit y obtener las credenciales de la misma forma
2. Autenticar y consumir endpoints usando requests.



```python
import requests
import base64

# Reddit API credentials
client_id = "TU_CLIENT_ID"
client_secret = "TU_CLIENT_SECRET"

# Encode credentials for Basic Auth
auth_string = f"{client_id}:{client_secret}".encode("utf-8")
auth_b64 = base64.b64encode(auth_string).decode("utf-8")

# Request an access token
url_auth = "https://www.reddit.com/api/v1/access_token"
headers_auth = {
    "User-Agent": "<TU_APP> by <TU_USUARIO>",
    "Authorization": f"Basic {auth_b64}"
}
data_auth = {
    "grant_type": "client_credentials"
}

resp_auth = requests.post(url_auth, headers=headers_auth, data=data_auth)

if resp_auth.status_code == 200:
    token_json = resp_auth.json()
    access_token = token_json["access_token"]

    # Access subreddit data
    url_subreddit = "https://oauth.reddit.com/r/datascience/hot"
    headers_api = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": "<TU_APP> by <TU_USUARIO>"
    }
    params = {"limit": 5}
    resp_data = requests.get(url_subreddit, headers=headers_api, params=params)

    if resp_data.status_code == 200:
        posts_json = resp_data.json()
        for post in posts_json["data"]["children"]:
            print(f"Post Title: {post["data"]["title"]}\nPost URL: {post["data"]["url"]}\nPost Content: {post["data"]["selftext"]}\n")
    else:
        print("Error subreddit:", resp_data.status_code, resp_data.text)
else:
    print("Error auth:", resp_auth.status_code, resp_auth.text)
# Output
Post Title: Weekly Entering &amp; Transitioning - Thread 13 Jan, 2025 - 20 Jan, 2025
Post URL: https://www.reddit.com/r/datascience/comments/1i06k3y/weekly_entering_transitioning_thread_13_jan_2025/
Post Content:  

Welcome to this week's entering &amp; transitioning thread! This thread is for any questions about getting started, studying, or transitioning into the data science field. Topics include:

* Learning resources (e.g. books, tutorials, videos)
* Traditional education (e.g. schools, degrees, electives)
* Alternative education (e.g. online courses, bootcamps)
* Job search questions (e.g. resumes, applying, career prospects)
* Elementary questions (e.g. where to start, what next)

While you wait for answers from the community, check out the [FAQ](https://www.reddit.com/r/datascience/wiki/frequently-asked-questions) and Resources pages on our wiki. You can also search for answers in [past weekly threads](https://www.reddit.com/r/datascience/search?q=weekly%20thread&amp;restrict_sr=1&amp;sort=new).
…
```



Como podemos ver, la implementación con requests es algo más compleja. Sin embargo, puede darnos mayor flexibilidad a la vez que reducimos dependencias con otras librerías.

En cada post, se tienen campos de texto como title, selftext (cuerpo del post), comments, etc. Similarmente, se pueden obtener comentarios e información de usuarios.



### 2.4 Otras redes sociales



Además de X (Twitter) y Reddit, existen numerosas redes sociales que exponen sus APIs. De igual forma, cada una tiene peculiaridades en cuanto a la información que sirven, límites, precios, etc.

Las principales redes y sus referencias son:



- **Facebook e Instagram**  
  Son más restrictivas a nivel de API, se necesita permiso expreso o planes específicos. Tienen límites y requieren apps registradas. El contenido textual suele estar en posts, captions, comentarios.

  - Facebook Graph API: [https://developers.facebook.com/docs/graph-api](https://developers.facebook.com/docs/graph-api)
  - Instagram API: [https://developers.facebook.com/docs/instagram-platform](https://developers.facebook.com/docs/instagram-platform)
- **YouTube**  
  Brinda API para extraer títulos, descripciones y comentarios de videos (posible caso de texto). Se autentica con Google Cloud credentials.

  - YouTube Data API: [https://developers.google.com/youtube/v3](https://developers.google.com/youtube/v3)
- **LinkedIn**  
  Bastante restrictiva, orientada a planes “Talent Solutions” o “Marketing Developer”. No es habitual como fuente gratuita de datos, pero si se cuenta con permisos, el flujo es similar.

  - LinkedIn developer portal: [https://developer.linkedin.com/product-catalog](https://developer.linkedin.com/product-catalog)
  - LinkedIn Postman collections: [https://www.postman.com/linkedin-developer-apis](https://www.postman.com/linkedin-developer-apis)



En todos los casos, el formato de la respuesta es típicamente JSON. Se parsea con response.json() y luego se manipula según la estructura devuelta. Si queremos almacenar localmente, optamos por CSV o un formato más potente (Parquet, Avro) para su posterior análisis. Todo ello se puede realizar mediante el uso de librerías como Pandas o Polars como ya hemos visto en unidades anteriores, y que exploraremos en mayor profundidad a lo largo de esta unidad.



## 3. Web Scraping Tradicional Y Scraping De Interfaces Con Beautifulsoup Y Selenium



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



En caso de no disponer de una API que nos permita acceder a datos textuales en un sitio web, o si la información que nos ofrece la plataforma no se encuentra expuesta de forma estructurada, tenemos la opción de usar web scraping. Es una técnica que consiste en obtener información de forma directa de las páginas, gracias a la interpretación de la estructura y el contenido del documento HTML. Una vez descargado o renderizado el HTML, podemos apuntar a secciones o nodos específicos para extraer texto, enlaces u otros atributos.

En el contexto de la ingeniería de software, la habilidad de “raspar” sitios (scraping) resulta valiosa para recopilar corpus de texto, datos de reseñas, foros de discusión, listados de productos, entre otros. El scraping puede presentarse en dos grandes escenarios:

- Sitios estáticos, en los que el HTML contiene la mayoría o la totalidad de la información deseada en el momento de la respuesta HTTP inicial.
- Sitios dinámicos, sustentados por JavaScript, lo que implica que parte del contenido se genere tras la carga de la página, o requiera la simulación de acciones del usuario (clics, scroll, inicios de sesión).

Para el primer caso, BeautifulSoup suele ser suficiente; para el segundo, suele necesitarse un navegador automatizado como Selenium. Existen situaciones híbridas donde, antes de decidir utilizar Selenium, conviene analizar las llamadas de red a través de BurpSuite o las Developer Tools del navegador, a fin de discernir si el contenido se podría obtener con requests directamente desde un endpoint interno.



### 3.2 Estructura de los sitios web (HTML, CSS, JavaScript)



#### Fundamentos de la estructura HTML



Un sitio web se describe con HTML (HyperText Markup Language). Este lenguaje define los nodos que componen la página, usualmente organizados de manera jerárquica (árbol DOM). Cada nodo se compone de:

1. Etiqueta de inicio (p. ej., <div class="post">), que incluye el nombre del elemento y atributos.
2. Contenido interno: puede ser texto crudo, otros nodos anidados (hijos) o ambos.
3. Etiqueta de cierre (p. ej., </div>), excepto en elementos vacíos (e.g. <img />).

La organización de HTML se clasifica a menudo en varios tipos de etiquetas, que cada desarrollador o framework utiliza para fines semánticos o de maquetación:



- **Estructura y disposición general**  
  Páginas modernas suelen utilizar <header>, <nav>, <main>, <section>, <article>, <aside> y <footer> para señalar la intención de cada bloque. Por ejemplo, un <header> se encuentra al inicio de la página, un <footer> al final, <nav> para menús, <article> para contenido principal
- **Agrupación de contenido**  
  Etiquetas como <div> y <span> son elementos genéricos de bloque o en línea, respectivamente, para agrupar contenido. <p> indica párrafos. Muchas webs reusan <div> para todo tipo de “cajas” y <span> para “fragmentos en línea.”
- **Semántica y resaltado**  
  Etiquetas como <h1>, <h2>, <h3> indican encabezados en distintos niveles. <b>, <strong> y <i> realzan palabras, aunque <strong> e <em> tienen un significado semántico distinto al meramente visual de <b> o <i>.
- **Inserción de contenido externo**  
  Se hallan elementos como <audio>, <video>, <iframe> y <img>. De hecho, un <iframe> puede embeber otra página entera. Estos pueden presentar retos para scraping si el contenido real se aloja en un documento adicional o en un streaming.
- **Tablas**  
  Se definen con <table>, <tr> (fila), <td> (celda). En sitios antiguos, las tablas se usaban para maquetar la página entera; en sitios modernos, se reservan para datos tabulares genuinos. Por ejemplo, una tabla de precios de productos o un ranking de usuarios.
- **Formularios**  
  <form> abarca todo el bloque de campos, <input> define un campo (texto, checkbox, etc.), <select> para menús desplegables, <button> o <input type="submit"> para enviar. Para scraping, es clave entender cómo enviar datos al servidor (p. ej. un login) o cómo se estructuran los parámetros que se envían (e.g. name="username").



![image](assets/cm7uduv8100y0356z24qkqw73-INSD_BAIN_U3_Imagen6.png)



En el siguiente código de HTML se ilustra una estructura sencilla:



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Web U-Tad</title>
</head>
<body>
  <header>
    <h1>Bienvenido a la U-tad!</h1>
    <nav>
      <ul>
        <li><a href="/index.html">Inicio</a></li>
        <li><a href="/about.html">Sobre nosotros</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section class="blog-entry">
      <h2>Primer post</h2>
      <p>Estudiar en la U-Tad es genial!</p>
      <span class="author">Creado por Jesús</span>
      <aside>Más información</aside>
    </section>
    <section class="blog-entry">
      <h2>Segundo post</h2>
      <p>Estoy mejorando mucho mi conocimiento en Python!</p>
      <span class="author">Creado por Jesús</span>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 U-Tad.</p>
  </footer>
</body>
</html>
```



Este ejemplo refleja cómo se usan <header> y <footer> para la cabecera y pie de página. El <nav> aloja enlaces de navegación, <main> contiene el contenido principal, dividido en <section> con clase blog-entry y, dentro, <h2> para el título y <p> para el texto. Nodos como <aside> añaden información extra.



#### El rol de CSS y JavaScript



El CSS (Cascading Style Sheets) define la apariencia de los nodos (colores, márgenes, tipografía). Para el scraping, lo importante es poder localizar elementos a través de selectores. Por ejemplo, un bloque con clase blog-entry se selecciona con .blog-entry en CSS. Si deseamos un <span> de autor con clase author, en CSS se define .author. Al usar librerías como BeautifulSoup o Selenium, esos selectores simplifican la extracción: soup.select(".blog-entry .author")

CSS se caracteriza por ser un lenguaje simple, permitir el anidamiento de instrucciones, ser estándar en todos los navegadores y permitir personalizar la apariencia de las páginas. Además, se puede insertar dentro de una etiqueta HTML o en un fichero aparte.

La estructura de CSS pues se compone de selectores, reglas y valores como:



```css
    /* Selector: p (selecciona todos los párrafos) */
    p {
      /* Regla: color con el valor azul */
      color: blue;
    }
```



JavaScript, se trata de un lenguaje de programación interpretado que nos permite interactuar con los elementos de la web y "darles vida". Gracias a esto, la web, internet y las redes sociales se han desarrollado hasta el nivel en el que se encuentran hoy en día.

Los sitios dinámicos usan JavaScript para alterar el DOM (Document Object Model, interfaz que facilita la representación, manteniendo una estructura definida, del documento) en tiempo de ejecución, insertar datos o responder a eventos. Este factor es crucial para el scraping: un requests.get(url) puede devolver un HTML vacío si la mayor parte del contenido se inyecta tras la carga con JavaScript. En tal caso, se requiere Selenium (o alguna técnica que reproduzca llamadas AJAX) para obtener el estado final del DOM.

JavaScript se caracteriza por ser un lenguaje de alto nivel, orientado a objetos y estar débilmente tipado. Además, es un lenguaje Interpretado que interactúa con el DOM y se ejecuta en cliente.



### 3.3 Herramientas de inspección (Dev Tools y BurpSuite)



Las Developer Tools (Chrome/Firefox) son el método más directo para explorar la estructura y el tráfico de una página. Nos ayudan a:

- Ver el DOM real en la pestaña “Elements” (o “Inspector” en Firefox).
- Seleccionar elementos y ver sus atributos, clases y estilos.
- Revisar peticiones HTTP en “Network,” confirmando si hay endpoints JSON, tokens, o secuencias de requests para la paginación.

Esta exploración inicial permite definir la estrategia de scraping: “¿está todo en un <div class="post">, o necesito descubrir requests AJAX con JSON?”

BurpSuite es una suite más avanzada orientada a pruebas de seguridad, pero muy útil para scraping. Configurando el navegador para pasar por el proxy de BurpSuite, podemos interceptar cada request y respuesta. Esto revela:

- Tokens en cabeceras o formularios.
- Endpoints internos que devuelven datos en JSON.
- Redirecciones a otros dominios.

Una vez hallamos esos endpoints internos, a menudo podemos replicar la petición con requests sin necesidad de Selenium ni parseo HTML. Por ejemplo, si la aplicación Angular llama a GET /api/posts?page=2, podríamos interceptar esa request en Burp, ver qué parámetros y cookies requiere, y replicar en Python. De esta forma, podemos ser capaces de autenticarnos o hacer otras acciones incluso aunque las APIs no estén pensadas o preparadas para ello mediante el uso o modificación de cookies, headers, etc.



![image](assets/cm7udzw4i013i356z5jys5m4j-INSD_BAIN_U3_Imagen7.jpg)



### 3.4 Query selectors



Para scrapear de forma efectiva, necesitamos seleccionar los nodos de interés dentro del DOM de la página. Los query selectors son la vía principal para decirle a nuestras herramientas (un navegador, BeautifulSoup o Selenium) qué elementos queremos. Estos selectores se basan en la misma sintaxis que utiliza CSS, combinando etiquetas, clases, ids, atributos y pseudoelementos para localizar con precisión cualquier nodo del árbol HTML.

Un query selector es una cadena que describe uno o varios elementos del DOM conforme a reglas definidas en el estándar CSS. Los selectores pueden combinarse jerárquicamente (div > p) o unirse por lógica (h2.title, p.description). El navegador, BeautifulSoup y Selenium ofrecen métodos para usarlos:

- En el navegador, en la consola de DevTools, podemos emplear document.querySelector("...") (devuelve el primer elemento) o document.querySelectorAll("...") (devuelve todos los que coincidan).
- En BeautifulSoup, disponemos de soup.select("...") para obtener una lista de elementos, y select_one("...") para un único elemento.
- En Selenium, se puede emplear driver.find_element("css selector", "...") o driver.find_elements("css selector", "...")

La sintaxis de los selectores es muy flexible. Entre los selectores más comunes encontramos:

| Tipo de selector | Símbolo / Ejemplo | Función | Ejemplo de uso |
| --- | --- | --- | --- |
| Por etiqueta (tag) | "p", "div", "span" | Selecciona todos los elementos de un tipo concreto de etiqueta. | CSS: p { color: blue; } JS: document.querySelectorAll("p") BeautifulSoup: soup.select("p") |
| Por id | #header, #main, #footer | Selecciona un elemento cuyo atributo id coincida con el especificado. (El id debería ser único en la página). | CSS: #header { background: black; } JS: document.querySelector("#header") BeautifulSoup: soup.select("#header") |
| Por clase | . blog-entry, .author | Selecciona todos los elementos que posean la clase dada. Una etiqueta puede tener varias clases: <div class="blog-entry post">. | CSS: .blog-entry { margin-bottom: 20px; } JS: document.querySelectorAll(".blog-entry") BeautifulSoup: soup.select(".blog-entry") |
| Combinado (clases) | .card.highlight | Selecciona elementos con ambas clases. <div class="card highlight">. | CSS: .card.highlight { border: 1px solid; } JS: document.querySelectorAll(".card.highlight") BS: soup.select(".card.highlight") |
| Jerárquico (descend.) | "div p" | Selecciona <p> que estén dentro de un <div> en cualquier nivel de anidación. | CSS: div p { color: red; } JS: document.querySelectorAll("div p") BS: soup.select("div p") |
| Jerárquico (hijo) | "div > p" | Selecciona <p> que sean hijos directos de <div>. | CSS: div > p { font-size: 14px; } JS: document.querySelectorAll("div > p") BS: soup.select("div > p") |
| Hermano adyacente | "div + p" | Selecciona <p> que aparezca justo después de un <div> (en el mismo nivel). | CSS: div + p { margin-top: 5px; } JS: document.querySelectorAll("div + p") BS: soup.select("div + p") |
| Hermano general | "div ~ p" | Selecciona todos los <p> posteriores al <div> dentro del mismo padre. | CSS: div ~ p { color: green; } JS: document.querySelectorAll("div ~ p") BS: soup.select("div ~ p") |
| Selector de atributo | img[src], a[href="..."] | Selecciona elementos que posean un atributo en particular. Se puede especificar el valor, p. ej. a[href="login.html"]. | CSS: img[src] { border: 1px solid #ccc; } JS: document.querySelectorAll('img[src]') BS: soup.select('img[src]') Combinado: soup.select('a[href="login.html"]') |
| Múltiple | "h2, p.desc, div.content" | Selecciona h2 o p.desc o div.content, es decir, la unión de tres criterios distintos. | CSS: h2, p.desc, div.content { margin:10px; } JS: document.querySelectorAll("h2, p.desc, div.content") BS: soup.select("h2, p.desc, div.content") |

Supongamos que queremos <a> con clase "button" y cuyo atributo href contenga la palabra "product" pero que, además, sea un hijo directo de un <li> que esté dentro de un <ul> de clase "nav-list". El selector podría ser:



```bat
ul.nav-list > li > a.button[href*="product"]
```



Una manera sencilla de validar los query selectors es desde la consola de desarrolladores del navegador. Para ello deberemos:

1. Para este ejemplo iremos a la web: [https://parascrapear.com/](https://parascrapear.com/)
2. Abrir las herramientas de desarrollador y buscar la consola con “F12”, “Ctrl+Shift+I”, dependerá de nuestro navegador.
3. En la consola debemos escribir document.querySelectorAll(“<TU_QUERY_SELECTOR>”). Antes de ejecutar el comando ya obtenemos una pequeña vista previa de cuanto vamos a obtener



![image](assets/cm7uek60n0164356zzme062vl-INSD_BAIN_U3_Imagen8.jpg)



1. Obtengamos diferentes secciones de la página:



```ini
# Citas
document.querySelectorAll("blockquote p > q")
## Output
```



![image](assets/cm7uelnm10195356z2leik7mp-carousel1-INSD_BAIN_U3_Imagen9.jpg)

![image](assets/cm7uelnm10195356z2leik7mp-carousel2-INSD_BAIN_U3_Imagen10.png)



```ini
# Categorias
document.querySelectorAll("blockquote > p a.cat")
# Autores
document.querySelectorAll(“blockquote > footer a.author”)
# Siguiente página
document.querySelectorAll(“a.next”)
```



De esta forma, podemos acceder a los nodos para posteriormente extraer sus datos. Si quisiésemos acceder al texto, deberíamos leer el elemento y la propiedad correspondiente. Por ejemplo:



```ini
# Texto de siguiente página
document.querySelectorAll("a.next")[0].text
# Output
'Siguiente →'
```



Veamos en el siguiente video como navegar por el HTML de una web y cómo recuperar datos:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651983_1/scormcontent/assets/INSD_BAIN_U3_Video2.mp4?v=1)



### 3.5 Scraping tradicional (HTML estático) con BeautifulSoup



BeautifulSoup es una librería Python para parsear HTML y XML de forma sencilla. Se encarga de convertir el HTML en un objeto DOM que podemos recorrer con métodos de búsqueda y selectores. Dado que en muchos sitios el contenido estático se encuentra en un HTML final, no necesitamos ejecutar JavaScript ni un navegador completo.

El proceso típico sería:

1. Descargamos la página con requests.get(url).text.
2. Creamos un BeautifulSoup(html, "html.parser").
3. Buscamos nodos con .find(), .find_all(), .select(), extrayendo texto o atributos.

Esta técnica es simple, rápida y eficiente, siempre que la página no requiera JS o interacción dinámica para mostrar el contenido. Gracias a los Query Selectors podremos identificar los nodos deseados y extraer su información.

En cuanto al uso, podemos extraer información de atributos mediante element["href"] o element.get("href"). También podemos tratar el texto gracias a .get_text(strip=True) quita espacios extra. Para navegar, tenemos las opciones de .parent, .children, .next_sibling, y .previous_sibling se recorre el árbol, si la estructura es compleja.

Para instalar la librería, simplemente deberemos ejecutar:



```bat
pip install beautifulsoup4
```



Si utilizamos el mismo ejemplo hecho con los Query Selectors, podemos obtener todo el contenido de los nodos identificados de la siguiente manera:



```python
import requests
from bs4 import BeautifulSoup

url = "https://www.parascrapear.com"
res = requests.get(url)
html = BeautifulSoup(res.text, 'html.parser')

citas = html.select("blockquote p > q")
citas = [x.text for x in citas]
print(f"Citas: {citas}")

categorias = html.select("blockquote > p a.cat")
categorias = [x.text for x in categorias]
print(f"Categorias: {categorias}")

autores = html.select("blockquote > footer a.author")
autores = [x.text for x in autores]
print(f"Autores: {autores}")

next_page_data = html.select("a.next")
next_page = f'{url}{[x["href"] for x in next_page_data][0]}'
print(f"Pagina siguiente: {next_page}")

# Output
Citas: ['Prefiero equivocarme creyendo en un Dios que no existe, que equivocarme no creyendo en un Dios que existe. Porque si después no hay nada, evidentemente nunca lo sabré, cuando me hunda en la nada eterna; pero si hay algo, si hay Alguien, tendré que dar cuenta de mi actitud de rechazo.', 'El hombre ha nacido libre y por doquiera se encuentra sujeto con cadenas.', 'Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.', 'Quisiera sufrir todas las humillaciones, todas las torturas, el ostracismo absoluto y hasta la muerte, para impedir la violencia.', 'La única simplicidad que vale la pena de conservar es la del corazón, la simplicidad que acepta y goza.', 'Las ideas audaces son como piezas de ajedrez. Pueden ser vencidas, pero también pueden iniciar una partida victoriosa.', 'No me dejes caer en el vulgar error de soñar que soy perseguido cada vez que alguien me contradice.', 'Un político divide a las personas en dos grupos: en primer lugar, instrumentos; en segundo, enemigos.', 'El más importante y principal negocio público es la buena educación de la juventud.', 'La literatura no es otra cosa que un sueño dirigido.', '¿Cuál es la tarea más difícil del mundo? Pensar.', 'Se piensa que lo justo es lo igual, y así es; pero no para todos, sino para los iguales. Se piensa por el contrario que lo justo es lo desigual, y así es, pero no para todos, sino para los desiguales.', 'Saber olvidar, más es dicha que arte.', 'Bueno es tener la alegría en casa y no haber menester de buscarla fuera.', 'No hace falta un gobierno perfecto; se necesita uno que sea práctico.', 'Los hombres son criaturas muy raras: la mitad censura lo que practica; la otra mitad practica lo que censura; el resto siempre dice y hace lo que debe.', 'Conviene siempre esforzarse más en ser interesante que exacto; porque el espectador lo perdona todo menos el sopor.', 'El peor pecado hacia nuestros semejantes no es odiarlos, sino tratarlos con indiferencia: esa es la esencia de la inhumanidad.', 'La vida es una serie de colisiones con el futuro; no es una suma de lo que hemos sido, sino de lo que anhelamos ser.', 'Dios es la evidencia invisible.']
Categorias: ['Sociedad', 'Sociedad', 'Naturaleza', 'Defectos', 'Miscelánea', 'Pensamiento y razón', 'Miscelánea', 'Sociedad', 'Sociedad', 'Arte', 'Pensamiento y razón', 'Sociedad', 'Miscelánea', 'Sentimientos', 'Sociedad', 'Sociedad', 'Sentimientos', 'Sentimientos', 'Naturaleza', 'Sociedad']
Autores: ['Blaise Pascal', 'Jean Jacques Rousseau', 'Blaise Pascal', 'Mahatma Gandhi', 'Gilbert Keith Chesterton', 'Goethe', 'Emerson', 'Friedrich Nietzsche', 'Platón', 'Jorge Luis Borges', 'Emerson', 'Aristóteles', 'Baltasar Gracián', 'Goethe', 'Aristóteles', 'Benjamin Franklin', 'Voltaire', 'George Bernard Shaw', 'José Ortega y Gasset', 'Victor Hugo']
Página siguiente: https://www.parascrapear.com/index-2
```



Como podemos ver en el caso anterior, una vez extraídos los datos, observamos que aún sigue habiendo una “Página siguiente” que probablemente tenga más información. Una manera muy común para scrapear, sería hacer un pipeline que vaya extrayendo información hasta que no haya más páginas. Lo podemos ver en el siguiente ejemplo:



```python
import polars as pl

def scrape_page(url):
    res = requests.get(url)
    html = BeautifulSoup(res.text, 'html.parser')

    blockquotes = html.select("blockquote")
    quotes = []
    cat = []
    authors = []
    for bq in blockquotes:
        citas = bq.select_one("p > q")
        quotes.append(citas.text)
        
        categorias = bq.select_one("p a.cat")
        cat.append(categorias.text)

        autores = bq.select_one("footer a.author")
        authors.append(autores.text)
    
    next_node = html.select("a.next")

    if len(next_node)>0:
        next_page = f'{url}{next_node[0]["href"]}'
    else:
        next_page = None

    return quotes, cat, authors, next_page

url = "https://www.parascrapear.com/"

total_quotes=[]
total_cats=[]
total_authors=[]
while url is not None:
    quotes, cat, authors, url = scrape_page(url)
    total_authors+= authors
    total_quotes += quotes
    total_cats += cat
df = pl.DataFrame({
    "quotes": total_quotes,
    "cats": total_cats,
    "authors": total_authors
})
df

# Output
```



![image](assets/cm7ufc82m01hp356z1u13uavz-INSD_BAIN_U3_Imagen11.png)



Veamos en el siguiente video cómo podríamos scrapear una tienda online:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651983_1/scormcontent/assets/INSD_BAIN_U3_Video3.mp4?v=1)



### 3.6 Scraping dinámico con Selenium



Selenium es un marco de automatización de navegadores que permite simular la interacción de un usuario real. Esto resulta necesario cuando las páginas dependen de JavaScript, realizan peticiones AJAX después de la carga inicial, o exigen iniciar sesión para mostrar contenido. Selenium abre un navegador (Chrome, Firefox, Edge) o su versión headless, y ejecuta el mismo código JS que el usuario vería en pantalla.

La razón de usar Selenium en lugar de requests + BeautifulSoup es que:

- Algunos sitios no cargan datos en el HTML inicial, sino que se los traen con JavaScript.
- Hay sitios que solicitan logins, captchas o clicks en botones de “Load More.”
- Se requieren acciones complejas, como seleccionar opciones en menús y esperar un response asíncrono.

Selenium provee métodos para encontrar elementos (driver.find_element(...)) y leer propiedades como .text. Tras la ejecución de scripts, la página deviene en un estado final que podemos examinar.

Además, Selenium dispone de dos modos principales:

- Headless=True, con este modo toda la interacción con el navegador se hace “por detrás” de tal modo que en pantalla no se aprecia nada.
- Headless=False, con este modo se abre una pestaña del navegador y se puede ver como Selenium interactúa con los componentes de la página web.

Para instalar selenium simplemente deberemos ejecutar:



```bat
pip install selenium
```



Además, será necesario tener instalado el ChromeDriver siguiendo: [https://developer.chrome.com/docs/chromedriver/get-started](https://developer.chrome.com/docs/chromedriver/get-started)

La configuración e inicialización de Selenium se puede resumir en:



```bat
from selenium import webdriver
# Inicializamos el ChromeDriver (o el driver que necesitemos según el navegador)
driver = webdriver.Chrome()
# Obtenemos la web deseada
driver.get('https://www.google.com')
# Cerramos el driver para liberar los recursos utilizados
driver.quit()
```



En cuanto a la navegación y localización de elementos, Selenium ofrece numerosas opciones. De entre ellas, las básicas son:

- driver.get(url): abre la página especificada.
- driver.back(): navega a la página anterior en el historial.
- driver.forward(): avanza a la siguiente página en el historial.
- driver.refresh(): recarga la página actual.
- Para la localización de elementos:
  - find_element(By.ID, "id")
  - find_element(By.NAME, "name")
  - find_element(By.XPATH, "xpath")
  - find_element(By.LINK_TEXT, "link text")
  - find_element(By.PARTIAL_LINK_TEXT, "partial link text")
  - find_element(By.TAG_NAME, "tag name")
  - find_element(By.CLASS_NAME, "class name")
  - find_element(By.CSS_SELECTOR, "css selector"), este sería el equivalente a los Query Selectors

¿Cómo se resolvería el caso de scrapeme.live con selenium? Veamos el siguiente ejemplo:



```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Configuramos el WebDriver
def create_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

url = "https://scrapeme.live/shop/Bulbasaur/"

driver = create_driver(headless=False)
driver.get(url)

pokemon_name = driver.find_element(By.CSS_SELECTOR, ".summary .product_title").text
print(f"Pokemon Name: {pokemon_name}")

pokemon_price = driver.find_element(By.CSS_SELECTOR, "p.price").text
print(f"Pokemon Price: {pokemon_price}")

# Debemos cerrar el driver, de lo contrario no liberaremos los recursos del PC
driver.quit()

# Output
Pokemon Name: Bulbasaur
Pokemon Price: £63.00
```



Del mismo modo, si queremos definir un pipeline en el que scrapear todas las páginas para obtener la información de todos los elementos:



```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Configuramos el WebDriver
def create_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Función para obtener la información de un Pokémon
def get_pokemon_info(url):
    driver = create_driver(headless=True)
    driver.get(url)

    try:
        pokemon_name_qs = ".summary .product_title"
        pokemon_price_qs = "p.price"
        pokemon_desc_qs = ".summary .woocommerce-product-details__short-description p"
        pokemon_stock_qs = ".summary .stock"
        pokemon_image_qs = ".woocommerce-product-gallery__image .wp-post-image"
        pokemon_price_curr_qs = ".woocommerce-Price-currencySymbol"

        pokemon_name = driver.find_element(By.CSS_SELECTOR, pokemon_name_qs).text
        print(f"Scraping {pokemon_name}")

        pokemon_price_curr = driver.find_element(By.CSS_SELECTOR, pokemon_price_curr_qs).text
        pokemon_price = driver.find_element(By.CSS_SELECTOR, pokemon_price_qs).text
        pokemon_price = float(pokemon_price.replace(pokemon_price_curr, "").strip())

        pokemon_desc = driver.find_element(By.CSS_SELECTOR, pokemon_desc_qs).text
        pokemon_stock = int(driver.find_element(By.CSS_SELECTOR, pokemon_stock_qs).text.split(" ")[0])
        pokemon_image = driver.find_element(By.CSS_SELECTOR, pokemon_image_qs).get_attribute("src")

    except Exception as e:
        driver.quit()
        return f"Error with page: {url}, {e}"

    driver.quit()
    return {"name": pokemon_name, 
            "image_url": pokemon_image, 
            "description": pokemon_desc,
            "price": pokemon_price, 
            "currency": pokemon_price_curr, 
            "stock": pokemon_stock}

# Función para obtener los elementos de la página
def get_page_elements(url):
    driver = create_driver(headless=True)
    driver.get(url)

    try:
        print(f"Scraping: {url}")

        urls_qs = "ul .product .woocommerce-LoopProduct-link"
        next_url_qs = ".page-numbers .next"

        urls = [elem.get_attribute("href") for elem in driver.find_elements(By.CSS_SELECTOR, urls_qs)]

        next_url_elem = driver.find_elements(By.CSS_SELECTOR, next_url_qs)
        next_url = next_url_elem[0].get_attribute("href") if next_url_elem else None

    except Exception as e:
        driver.quit()
        return f"Error with: {url}, {e}"

    driver.quit()
    return urls, next_url

# Scrapeamos todas las páginas
next_page = "https://scrapeme.live/shop/"
pokemons_list = []

while next_page is not None:
    try:
        urls, next_page = get_page_elements(next_page)
        for url in urls:
            pokemon_info = get_pokemon_info(url)
            pokemons_list.append(pokemon_info)
    except Exception as e:
        print(f"Error scraping page: {e}")

df = pd.DataFrame(pokemons_list)
print(df)
```



La principal diferencia que podremos observar si ejecutamos el código de ambos casos, es a nivel de rendimiento ya que Selenium va a tardar muchos minutos más que BeatifulSoup. Para el caso de los Pokemon en Scrapeme.live estamos hablando de que puede tardar del orden de horas en recorrer las casi 50 páginas.

Es un buen ejercicio ejecutar ambos casos con un logging adecuado para poder ver cómo está funcionando el proceso y tras un periodo prudencial interrumpir dicha ejecución. Ante una misma cantidad de tiempo podremos analizar en qué punto estamos con cada caso y apreciar esa diferencia de rendimiento.



### 3.7 Selenium VS BeautifulSoup



Elegir la herramienta adecuada es fundamental para garantizar la eficiencia y efectividad del proceso de extracción de datos. BeautifulSoup y Selenium son dos de las bibliotecas más populares utilizadas para el parsing de contenido web, cada una con sus propias ventajas y limitaciones. Mientras que BeautifulSoup destaca por su simplicidad y velocidad en el manejo de páginas estáticas, Selenium ofrece una capacidad superior para interactuar con sitios dinámicos que dependen de JavaScript y requieren acciones de usuario más complejas. Para facilitar la toma de decisiones informadas, analizaremos la siguiente tabla:



![image](assets/cm7uu02m801q0356zs3i4kxxt-INSD_BAIN_U3_Imagen12.png)



En la práctica, hay escenarios complejos donde la página expone parte de la información en JavaScript, y además requiere un token de sesión que se obtiene al iniciar la página. Para analizar el funcionamiento y saber qué solución debemos implementar, podremos realizar el siguiente proceso:

1. Configurar el navegador para redirigir el tráfico por el proxy de BurpSuite.
2. Navegar manualmente por la web e interceptar las requests. Si se detecta un GET /api/data?page=2 que devuelve un JSON con el contenido en lugar de HTML, podemos replicarlo en un script con requests.
3. Extraer el token “X-CSRF-Token” o “Authorization Bearer” desde el interceptado.
4. Probar con un script Python que incluya las cabeceras y parámetros descubiertos.
5. Descartar Selenium si no es preciso, o mantenerlo si la web requiere iniciar sesión mediante un formulario JS, en cuyo caso Selenium reproduciría la acción de login, y el proxy de BurpSuite confirmaría la existencia de cookies o tokens.

De esta manera, BurpSuite funciona como herramienta forense para descubrir qué pasa en el “backstage” de la aplicación web. Después, se decide si bastan requests y BeautifulSoup para parsear la respuesta HTML/JSON, o si se precisa Selenium para secuencias más intrincadas.



### 3.8 Ética y legalidad



La extracción masiva de datos puede topar con límites técnicos y legales. Ciertos sitios prohíben explícitamente el scraping o su reutilización en sus términos de servicio. Además, existe el archivo robots.txt, un mecanismo por el que se sugiere qué rutas el scraper no debe acceder. Aunque no es legalmente vinculante en todos los casos, se considera buena práctica respetarlo.

Saturar un sitio con demasiadas requests en poco tiempo puede considerarse un ataque (como un DDoS) o perjudicar su rendimiento. Se recomienda introducir pausas y no descargar miles de páginas simultáneamente. Por último, se recogen datos que identifiquen personas, se deben conocer las regulaciones (como GDPR en Europa) para no incurrir en violaciones de privacidad.



### 3.9 Enlaces de interés



> BurpSuite community edition
>
> [Link](https://portswigger.net/burp/communitydownload)

> BeautifulSoup documentation
>
> [Link](https://beautiful-soup-4.readthedocs.io/)

> Selenium documentation
>
> [Link](https://www.selenium.dev/documentation/)

> Ética en scraping
>
> [Link](https://www.meritdata-tech.com/resources/blog/data/web-scraping-best-practices-ethical-data-collection/)



## 4. Manejo Detallado De Formatos Tabulares Con Pandas/Polars



### 4.1 Introducción



![image](assets/cm7uu6aq501td356z4uyr9wg4-stock-image.jpg)



A medida que se avanza en la obtención de información textual a través de APIs o mediante técnicas de scraping, se genera la necesidad de almacenar y manipular esos datos de manera ordenada. Muy habitualmente, los resultados descargados con requests o provenientes de librerías como BeautifulSoup o Selenium llegan en forma de objetos JSON o bloques de texto no estructurado. Para procesarlos con eficacia, la organización en un formato tabular suele ser la estrategia preferida, ya que facilita la clasificación, filtrado y agregación.

En Python, las librerías Pandas y Polars se han consolidado como opciones de referencia para trabajar con datos estructurados. A lo largo de las unidades anteriores ya se introdujeron sus capacidades principales, pero en este apartado se profundizará en situaciones más complejas y se mostrarán ejemplos prácticos que aprovechan los datos recogidos en el apartado de scraping y de APIs de redes sociales. El objetivo es ilustrar cómo construir un pipeline que vaya desde la obtención de datos crudos hasta la producción de informes o la persistencia en formatos avanzados como Parquet.



### 4.2 Pipelline de datos: cómo obtener y analizar datos



Al usar requests para consumir servicios web o al recurrir a BeautifulSoup o Selenium, se corre el riesgo de terminar con un gran volumen de JSON o fragmentos dispersos de HTML. Es fundamental decidir en qué formato se guardarán estos datos y cómo se transformarán para luego cargarlos en estructuras tabulares.

Para datos en JSON, la ruta típica involucra un parseo inicial con el módulo json (en caso de haberlo recibido como cadena) o directamente response.json() si proviene de un requests.get(). Con esa información ya en un objeto Python (diccionarios o listas de diccionarios), podremos convertirlo a un DataFrame mediante Pandas o Polars.

Para datos extraídos vía scraping (donde, por ejemplo, hemos obtenido listas de títulos, enlaces y descripciones), lo usual es construir listas o diccionarios manualmente y luego transformarlos en tabular.



#### Obtener y almacenar datos "raw"



El primer paso del pipeline debería ser obtener los datos vía API o scraping y almacenarlos en crudo. Para ello, utilizaremos una llamada a API y almacenaremos los datos en formato JSON. Esto nos facilitará el posterior tratamiento con Pandas o Polars.

Veamos el proceso para extraerlo usando RapidAPI:



```python
import requests
import json

def fetch_tweets_mock(query="datascience", limit=5):
    url = "https://twitter-api45.p.rapidapi.com/search.php"
    headers = {
        "x-rapidapi-key": "TU_API_KEY",
        "x-rapidapi-host": "twitter-api45.p.rapidapi.com"
    }
    params = {
        "query": query,
        "search_type": "Top"
    }
    resp = requests.get(url, headers=headers, params=params)
    tweets_data = []
    if resp.status_code == 200:
        data = resp.json()
        timeline = data.get("timeline", [])
        for t in timeline:
            user_name= t.get("user_info", {}).get("screen_name", "unknown")
            text = t.get("text", "")
            tweets_data.append({"user": user_name, "content": text})
    return tweets_data

tweets = fetch_tweets_mock(query="datascience", limit=5)

# Guardamos en JSON

with open("tweets_datascience.json", "w") as f:
    json.dump(tweets, f)
print(tweets)
```



El resultado de este código será almacenar en local un archivo JSON con todo el contenido tal cual que hemos obtenido de la API. En este caso, hemos almacenado simplemente el nombre del usuario y el contenido del texto.



#### Lectura y transformación de datos



Una vez tenemos los datos almacenados, el siguiente paso será la lectura de estos para poder hacer las transformaciones necesarias. Finalmente, tras realizar todas las transformaciones, podremos almacenar los datos en la siguiente capa con los datos ya limpios.

Para este caso, usaremos tanto Pandas como Polars para hacer múltiples operaciones y guardar los resultados en una nueva capa ya preparada para analítica:



```ruby
# Pandas
import pandas as pd

df_pandas = pd.read_json("tweets_datascience.json")

# Si queremos contar el número de tweets por usuario
df_pandas_grouped = (
    df_pandas.groupby("user")
    .agg({"content": "count"})
    .rename(columns={"content": "number_of_tweets"})
    .sort_values("number_of_tweets", ascending=False)
)
# Almacenamos el número de tweets por usuario en un CSV
df_pandas_grouped.to_csv("tweets_count_pandas.csv", index=True)

# Si queremos filtrar por un hashtag
df_pandas_filtered = df_pandas[df_pandas["content"].str.contains("#ai", na=False)]
# Almacenamos los tweets filtrados en un CSV
df_pandas_filtered.to_csv("tweets_filtered_ai_pandas.csv", index=False)

# Si queremos contar el número de veces que aparece cada hashtag
df_pandas["hashtags"] = df_pandas["content"].str.findall(r"#\w+")
df_pandas_exploded = df_pandas.explode("hashtags").dropna(subset=["hashtags"])
df_pandas_hashtags_grouped = (
    df_pandas_exploded.groupby("hashtags")
    .size()
    .reset_index(name="hashtag_count")
    .sort_values("hashtag_count", ascending=False)
)
# Almacenamos el conteo de hashtags en un CSV
df_pandas_hashtags_grouped.to_csv("hashtags_count_pandas.csv", index=False)
```



```r
# Polars
Import polars as pl

df_polars = pl.read_json("tweets_datascience.json")

# Si queremos filtrar por un hashtag
df_polars_filtered= df_polars.filter(pl.col("content").str.contains("#ai"))

# Almacenamos los tweets filtrados en un CSV
df_polars_filtered.write_csv("tweets_filtered_ai.csv")

# Si queremos contar el número de tweets por usuario
df_polars_grouped = df_polars.group_by("user").agg([pl.count("content").alias("number_of_tweets")]).sort("number_of_tweets", descending=True)

# Almacenamos el número de tweets por usuario en un CSV
df_polars_grouped.write_csv("tweets_count.csv")

# Si queremos contar el número de veces que aparece cada hashtag
df_polars_hashtags_grouped = (
    df_polars.with_columns(
        # Extraemos los hashtags mediante expresiones regulares
        pl.col("content").str.extract_all(r"#\w+").alias("hashtags")
    )
    .explode("hashtags")  # Separamos los hashtags en filas
    .group_by("hashtags")
    .agg([
        pl.count("hashtags").alias("hashtag_count")  # Contamos las apariciones de cada hashtag
    ])
    .sort("hashtag_count", descending=True)
)

# Almacenamos el conteo de hashtags en un CSV
df_polars_hashtags_grouped.write_csv("hashtags_count.csv")
```



En este paso, estaremos almacenando los datos en la última capa para que estén listos para analítica. Gracias a ello, podemos leer estos últimos documentos y extraer información necesaria.

Por ejemplo, podemos utilizar la librería “matplotlib” para crear gráficas que nos ayuden a visualizar la información del número de tweets por usuario o el número de menciones de un hashtag:



```r
import matplotlib.pyplot as plt

# Leemos los CSVs limpios
tweets_count = pd.read_csv("tweets_count_pandas.csv")
hashtags_count = pd.read_csv("hashtags_count_pandas.csv")

# Gráfica del número de tweets por usuario
plt.figure(figsize=(10, 6))
plt.bar(tweets_count["user"], tweets_count["number_of_tweets"], color="blue")
plt.title("Tweets por usuario")
plt.xlabel("Usuario")
plt.ylabel("Número de tweets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfica del conteo de hashtags
top_15_hashtags = hashtags_count.head(15)
plt.figure(figsize=(10, 6))
plt.bar(top_15_hashtags["hashtags"], top_15_hashtags["hashtag_count"], color="green")
plt.title("Hashtags más utilizados")
plt.xlabel("Hashtags")
plt.ylabel("Conteo de hashtags")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```



![image](assets/cm7uuf0ae021b356z172odie0-carousel1-INSD_BAIN_U3_Imagen13.png)

![image](assets/cm7uuf0ae021b356z172odie0-carousel2-INSD_BAIN_U3_Imagen14.png)



Gracias a las gráficas, podemos apreciar que nuestra analítica es “case sensitive”, es decir, diferencia entre mayúsculas y minúsculas dando lugar a analíticas incorrectas. Por ejemplo, “#ai” y “#AI” aparecen por separado cuando en realidad quieren decir lo mismo.

Debido a esto, será necesario revisitar la solución para evitar estos problemas e incluso plantear el uso de lemmatizacion y stemming como vimos en unidades anteriores con spaCy o NLTK para tener un resultado más acertado.

Por otro lado, hemos estructurado nuestro pipeline siguiendo en cierto modo una estructura medallion, es decir, dividiendo por capas en función de la madurez del archivo generado.

La arquitectura Medallion se basa en la organización de los datos en múltiples capas, comúnmente denominadas Bronze, Silver y Gold, cada una representando un nivel progresivo de refinamiento y calidad. En la capa Bronze, los datos se almacenan en su forma más cruda, capturando toda la información original sin modificaciones significativas.

A medida que los datos avanzan a la capa Silver, se someten a procesos de limpieza y transformación, eliminando inconsistencias y estructurando la información para facilitar su análisis.

Finalmente, en la capa Gold, los datos están altamente refinados y optimizados para usos específicos, como informes avanzados, visualizaciones o aplicaciones de inteligencia artificial. Este enfoque escalonado no solo mejora la eficiencia en el manejo de grandes volúmenes de datos, sino que también asegura una mayor calidad y confiabilidad en los resultados obtenidos, permitiendo a las organizaciones tomar decisiones más informadas y estratégicas.

"Por ejemplo, podemos utilizar la librería “matplotlib” para crear gráficas que nos ayuden a visualizar la información del número de tweets por usuario o el número de menciones de un hashtag: "



![image](assets/cm7uuginw022t356zpb9qw2lv-INSD_BAIN_U3_Imagen15.png)



A continuación, veamos un video sobre como afrontar este problema en un pipeline completo siguiendo la arquitectura medallion.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651983_1/scormcontent/assets/INSD_BAIN_U3_Video4.mp4?v=1)



## 5. Formatos Tabulares En Cómputo Distribuido Con Pyspark



### 5.1 Introducción



![image](assets/cm7uujacg0256356z7k124ezs-stock-image.jpg)



Conforme los proyectos crecen en complejidad y en volumen de datos, se hace necesario adoptar enfoques de cómputo distribuido que permitan procesar grandes cantidades de información de forma escalable. Apache Spark es uno de los frameworks más populares para esta labor, ofreciendo una arquitectura que distribuye las tareas de manipulación y análisis de datos en múltiples nodos (máquinas) de un clúster.

Cuando se trabaja con datos textuales masivos (por ejemplo, millones de tweets o archivos de gran tamaño extraídos por scraping), la ejecución en un solo equipo puede demorarse significativamente o no llegar a completarse por limitaciones de memoria. En estos escenarios, PySpark, la interfaz de Python para Apache Spark, resulta de gran ayuda. Permite mantener la misma filosofía de manipulación tabular (similar a lo visto con Pandas/Polars) pero repartiendo el proceso en múltiples máquinas de un clúster.

En este apartado se explicará qué es PySpark, cómo instalarlo y configurarlo en un entorno local, y se mostrarán ejemplos de lectura, manipulación y escritura de archivos tabulares. Además, se abordará la conexión con datos provenientes de APIs o de scraping, y cómo integrarlos en un flujo de trabajo distribuido.



### 5.2 Cómputo distribuido vs Cómputo tradicional



A medida que se profundiza en el manejo y análisis de datos, tanto en la ingeniería de software como en la ciencia de datos, se distinguen dos paradigmas principales a la hora de procesar información: el cómputo tradicional, que corre en un solo equipo o proceso, y el cómputo distribuido, que reparte la carga de trabajo entre varias máquinas o nodos de un clúster.

En el cómputo tradicional, todo el procesamiento se lleva a cabo en un solo equipo (o, a lo sumo, en múltiples hilos de un único sistema). Herramientas como Pandas y Polars se enmarcan en este paradigma. Aunque Polars introduce la posibilidad de aprovechar multihilos en una sola máquina, el alcance sigue estando limitado por la memoria RAM y el poder de CPU de dicho equipo. Este método es excelente para conjuntos de datos de tamaño moderado —por ejemplo, centenares de miles o unos pocos millones de filas— y brinda una experiencia de programación sencilla, con bajo overhead y sin necesidad de gestionar un clúster.

Por otro lado, cuando la escala de datos excede la capacidad de procesamiento (memoria, CPU) de una sola máquina, o cuando se desea una mayor velocidad y resiliencia, se recurre al cómputo distribuido. En este caso, los datos y la carga de trabajo se reparten entre varios nodos (máquinas físicas o virtuales).

Cada nodo recibe una porción de la información y ejecuta tareas en paralelo. Al terminar, se combinan los resultados parciales para obtener la salida final. Apache Spark, y en particular PySpark para el uso de Spark desde Python, representa un claro ejemplo de esta aproximación.



![image](assets/cm7uulgxy027a356zycaswk19-INSD_BAIN_U3_Imagen16.png)



PySpark utiliza la infraestructura de Apache Spark, ofreciendo tolerancia a fallos, escalado horizontal (podemos añadir más nodos para incrementar capacidad) y un modelo de programación basado en transformaciones perezosas (o lazy en inglés). Este modelo resulta fundamental cuando hablamos de “big data”, es decir, volúmenes de información muy grandes para los que requerimos muchos recursos de cómputo.

La elección entre computo tradicional y distribuido no solo atiende al tamaño de los datos sino también a la necesidad de integrar soluciones en entornos de nube, orquestar pipelines de grandes volúmenes de logs, datos textuales recolectados de redes sociales o sistemas de archivos compartidos, y aprovechar la infraestructura empresarial (Hadoop, Databricks, AWS EMR, etc.).



#### Arquitectura de PySpark



Para comprender por qué PySpark resulta tan valioso en el cómputo distribuido, conviene adentrarse en la arquitectura interna de un clúster de Spark. Cuando hablamos de “Spark cluster”, solemos referirnos a un conjunto de máquinas físicas o virtuales que cooperan para ejecutar tareas en paralelo.

Los conceptos clave en esta arquitectura son:



- **Nodo maestro (Driver y/o Master)**  
  Spark define el “Driver” como el proceso principal que contiene la lógica de la aplicación. Allí se construye el plan de ejecución lógico (transformaciones y acciones sobre el DataFrame), se coordina la comunicación con los workers y se programan las tasks. En un entorno con un “Master Node”, este actúa como gestor global, monitoreando los recursos y asignando el trabajo a los workers.
- **Nodos Worker**  
  En el clúster distribuido, cada nodo worker recibe partes de los datos y ejecuta tareas concretas, como map, filter, join, etc. Cada worker posee uno o varios executors, encargados de alojar la parte de los datos y llevar a cabo transformaciones sobre estos, almacenando el resultado parcial en memoria o disco local. En muchos casos, se configuran varios workers en paralelo, de modo que las “porciones” del dataset se procesan simultáneamente.
- **Tasks**  
  Una tarea (task) es la unidad mínima de trabajo que Spark lanza a un executor en un worker. Generalmente se asocian a particiones de los datos. Por ejemplo, si un DataFrame está dividido en 200 particiones, Spark podrá lanzar 200 tasks en paralelo, siempre que haya suficientes cores y nodos disponibles. Al concluir las tasks, los resultados parciales se combinan para producir el resultado final.
- **Cluster Manager**  
  Spark es un motor de ejecución, pero requiere un gestor (cluster manager) que se encargue de la asignación de recursos (memoria, CPU) y la inicialización de los contenedores o procesos en cada nodo. Existen varios cluster managers:

  - Spark Standalone: un gestor básico proporcionado por Spark.
  - YARN: gestor de recursos típico de Hadoop.
  - Mesos: un gestor genérico para entornos de contenedores, algo menos común hoy en día.
  - Kubernetes: sistema muy popular para orquestar contenedores en la nube.



Dentro de este ecosistema, cuando se lanza una aplicación PySpark, el driver construye un DAG (Directed Acyclic Graph) que describe las etapas y transformaciones a realizar. El cluster manager crea o reutiliza executors en los nodos worker, y se reparten las tasks. Cada worker realiza su parte y, a través de la red, se sincroniza con el driver para devolver el resultado.



![image](assets/cm7uuq7i602bg356zw9cuvs9j-INSD_BAIN_U3_Imagen17.png)



### 5.3 Uso básico de PySpark



Como ya hemos comentado, Apache Spark es un motor de análisis distribuido, diseñado para manejar grandes volúmenes de datos de forma eficiente. Trabaja sobre un modelo de RDD (Resilient Distributed Dataset), un tipo de colección de datos inmutable, distribuida en el clúster, y que puede reconstruirse en caso de fallo en alguno de los nodos. A un nivel más alto, Spark ofrece la abstracción de DataFrame, muy parecida a la que se usa en Pandas o Polars.



- **RDD**  
  Son estructuras de datos inmutables que se distribuyen en el clúster. Son la base de Spark, aunque habitualmente se trabaja con DataFrames por su mayor facilidad y rendimiento.
- **DataFrame**  
  La interfaz preferida en PySpark, sobre todo tras Spark 2.x. Permite ejecutar operaciones tabulares (select, filter, groupBy…) con un lenguaje declarativo similar a SQL o DataFrame de Pandas.
- **Transformations y Actions**  
  Spark trabaja en modo perezoso. Las transformaciones (como filter, map, groupBy) definen un plan de ejecución, pero no se computan de inmediato. Solo cuando llega una action (por ejemplo, collect(), show(), count()) se ejecuta realmente ese plan.
- **Driver y Executors**  
  En un clúster real, existe un nodo driver que coordina y planifica tareas, y varios executors que procesan datos en paralelo. En un entorno local, Spark emula esta infraestructura dentro de un único proceso, pero sigue manteniendo la filosofía de transformaciones distribuidas.



Gracias a estas características, Spark puede escalar desde un escenario local (ejecución en un solo equipo con multiproceso) hasta decenas o cientos de nodos en la nube.



#### Instalación de PySpark



El uso de PySpark puede acometerse de múltiples maneras. Para experimentos locales o aprendizaje, bastará con una instalación “standalone”, lo cual no exige la configuración de un clúster real. Para entornos corporativos o proyectos de mayor envergadura, se acostumbra a usar un clúster administrado (Hadoop/YARN, Kubernetes, Databricks, EMR, etc.). Antes de comenzar la instalación de PySpark, es recomendable ver qué versión de Python tenemos instalada y la compatibilidad con PySpark. Para ello podemos referirnos a: [https://community.cloudera.com/t5/Community-Articles/Spark-Python-Supportability-Matrix/ta-p/379144](https://community.cloudera.com/t5/Community-Articles/Spark-Python-Supportability-Matrix/ta-p/379144)

Dada la complejidad para la instalación y compatibilidad de PySpark, utilizaremos Docker para asegurar un despliegue funcional:

- Instalar Docker Desktop: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)



![image](assets/cm7uuvt2e02fn356ztgw6dfd9-INSD_BAIN_U3_Imagen18.png)



- Reiniciar el ordenador para asegurar una correcta instalación
- Inicializar Docker Desktop y asegurar que el motor está en ejecución



![image](assets/cm7uuwiji02h0356zjbypu02u-INSD_BAIN_U3_Imagen19.png)



- En el mismo directorio donde teníamos los archivos JSON y CSV generados anteriormente, creamos una carpeta y dentro de ella un nuevo archivo llamado “docker-compose.yaml” con el siguiente contenido:



```yaml
version: "3.7"

services:
  jupyter:
    build: .
    ports:
      - 8889:8889
    volumes:
      - ..:/src
```



- En la misma carpeta, crear un nuevo archivo llamado “Dockerfile” con el siguiente contenido:



```dockerfile
FROM python:3.11-buster

# Actualiza los paquetes e instala Java (necesario para Spark)
RUN apt update && \
    apt install -y openjdk-11-jre wget && \
    apt clean

# Define el directorio de trabajo en /opt
WORKDIR /opt/

RUN wget --no-check-certificate https://archive.apache.org/dist/spark/spark-3.4.3/spark-3.4.3-bin-hadoop3.tgz && \
    tar -xvzf spark-3.4.3-bin-hadoop3.tgz && \
    mv spark-3.4.3-bin-hadoop3 spark && \
    rm spark-3.4.3-bin-hadoop3.tgz && \
    ls -la /opt/spark && \
    ls -la /opt/spark/bin


# Instala JupyterLab
RUN pip install jupyterlab 
RUN pip install pyspark
RUN pip install pandas
RUN pip install matplotlib

# Configura las variables de entorno para Spark y JupyterLab
ENV SPARK_HOME=/opt/spark/
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS="lab --allow-root --ip 0.0.0.0 --port 8889"
ENV PATH="${SPARK_HOME}/bin:${PATH}"

# Expone los puertos de Jupyter y Spark
EXPOSE 8889
EXPOSE 4040

# Define el directorio de trabajo para el usuario
WORKDIR /src

# Comando por defecto para ejecutar JupyterLab
CMD ["jupyter", "lab", "--allow-root", "--ip", "0.0.0.0", "--port", "8889"]
```



- Abrir un terminal en la carpeta donde estén ambos archivos y ejecutar:



```dockerfile
docker-compose up
```



- Una vez terminado, navegamos a la interfaz de Docker y accedemos al container que hemos levantado



![image](assets/cm7uv011002o2356zy4osmm8g-INSD_BAIN_U3_Imagen20.jpg)



- Tras hacer click en él, buscamos en los logs la URL que nos permita acceder con el token en ella



![image](assets/cm7uv0r5n02pf356zrekmkj31-INSD_BAIN_U3_Imagen21.png)



- Una vez aquí, podemos ejecutar código con PySpark en nuestras celdas de jupyter notebook.
- Para conocer más detalles sobre la instalación de PySpark tenemos la guía de inicio: [https://spark.apache.org/docs/latest/api/python/getting_started/install.html](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

También podemos recurrir a la web de Spark para descargar en función de nuestras necesidades: [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)



#### Lectura de ficheros



En proyectos reales, Spark se caracteriza por su habilidad para leer y escribir datos en gran variedad de formatos y ubicaciones (sistemas de archivos locales, HDFS, S3, etc.). El SparkSession proporciona métodos como spark.read.csv(...), spark.read.json(...) y spark.read.parquet(...), que devuelven un DataFrame distribuido.

Por ejemplo, si queremos leer un JSON local con tweets (o un JSON grande que hubiéramos obtenido con scraping) como los que hemos obtenido en los apartados anteriores:



```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("U-Tad-PySpark") \
    .master("local[*]") \
    .getOrCreate()


df_json = spark.read.json('tweets_datascience.json')
df.printSchema()
df_json.show(10)
spark.stop()
```



![image](assets/cm7uv3r2r02tv356z4cu5o64z-INSD_BAIN_U3_Imagen22.png)



Del mismo modo, si queremos leer CSV u otro tipo de formato podremos usar .read.CSV o el equivalente.



#### Transformaciones y escritura de ficheros



Spark difiere de las librerías locales en que trabaja con transformaciones perezosas. Es decir, el código no se ejecuta de inmediato, sino que define un plan de ejecución que solo se realizará cuando llega una action, como df.show(). Este show() dispara realmente la lectura y el procesamiento. Otras acciones típicas: count(), collect(), write, etc.

Por ejemplo, veamos una operación donde combinemos filtrado por un hashtag, agrupación por usuario y conteo de tweets que contentan ese hashtag y finalmente lo almacenamos en un csv:



```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("U-Tad-PySpark") \
    .master("local[*]") \
    .getOrCreate()


df_json = spark.read.json('tweets_datascience.json')

df_analysis = (df_json
    .filter(df_json.content.contains("#datascience"))
    .groupBy("user")
    .agg({"content": "count"})
    .withColumnRenamed("count(content)", "num_tweets")
    .orderBy("num_tweets", ascending=False)
)

# 'show' dispara la ejecución
df_analysis.show(10)

# Guardamos el archivo, esto genera un directorio con las diferentes partes generadas por los workers debido al cómputo distribuido
df_analysis.write.mode('overwrite').csv('tweets_transformed_spark')

spark.stop()
```



![image](assets/cm7uv5y2v02xn356zzw0yd75y-INSD_BAIN_U3_Imagen23.png)



Cabe destacar que debido a la arquitectura de Spark y el funcionamiento del cómputo distribuido, al escribir, éste genera un directorio con las diferentes partes del cálculo realizada por cada uno de los workers. Es por ello por lo que requiere algún procesamiento extra para unificar y renombrar el resultado final en uno solo.

Veamos en el siguiente ejemplo como sería un pipeline completo de extracción, transformación y guardado de datos con PySpark:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651983_1/scormcontent/assets/INSD_BAIN_U3_Video5.mp4?v=1)



### 5.4 PySpark vs Pandas/Polars



Antes de elegir una opción, conviene analizar cuándo es más apropiado utilizar Pandas o Polars (enfoques en memoria local) frente a la adopción de Spark (PySpark) en un entorno distribuido.

| Criterio | Pandas | Polars | PySpark |
| --- | --- | --- | --- |
| Arquitectura | Single node (generalmente en RAM local). | Single node, uso intensivo de CPU multicore. | Distribuida (múltiples nodos: master, workers, executors). |
| Volumen de datos | Adecuado hasta memoria local; decenas de millones de filas si la máquina lo permite. | Más eficiente que Pandas, maneja volúmenes medianos con menor consumo. | Se diseñó para escalas masivas, desde varios GB hasta TB o PB. |
| Velocidad | Buena para análisis exploratorios moderados. | Muy veloz en escenarios single-node con varios cores. | Overhead inicial mayor, pero su escalabilidad multiplica la velocidad en Big Data. |
| Escalabilidad | Limitada al equipo local, depende de la RAM total. | Igual, aunque Polars aprovecha mejor la CPU disponible. | Escalable horizontalmente, sumando nodos o ampliando cluster manager. |
| Soporte e integración | Muy extendido, enorme comunidad y librerías derivadas (scikit-learn, etc.). | Comunidad en crecimiento, con buena documentación y uso en Rust/Python. | Ecosistema completo (Spark SQL, MLlib, streaming) y gran adopción empresarial. |
| Sobrecarga (overhead) | Bajo overhead, instalar Python y Pandas es trivial. | Ligeramente superior a Pandas por la compilación en Rust. | Más complejo: se requiere instalar Spark, un cluster manager (YARN, K8s, etc.) y configuración. |
| Casos de uso típicos | Exploración de datos, ETL ligero, prototipos, scripts de <= 4-8 GB. | Procesos de tamaño mediano (hasta decenas de GB) donde se valora el rendimiento single-node. | Data lakes, Big Data (decenas/cientos de GB), pipelines en la nube y entornos distribuidos. |

En resumen, el cómputo distribuido con PySpark permite que proyectos que requieren procesar volúmenes de datos textuales muy grandes (como millones de tweets diarios o scrapers de foros extensos) resulten factibles en plazos razonables. Sin embargo, no siempre se necesita la complejidad y costo de un clúster. Herramientas como Polars y Pandas siguen siendo la elección natural en casos de volumen moderado o cuando se busca iterar con rapidez en prototipos.



## 6. Conclusiones



### 6.1 Conclusiones de la unidad



A lo largo de esta unidad, hemos explorado las distintas maneras de acceder a datos textuales, desde la obtención a través de APIs de redes sociales (X, Reddit, entre otras) hasta el web scraping en versiones estáticas y dinámicas. Nuestro objetivo ha sido adquirir habilidades para manejar información proveniente de sitios web y grandes repositorios de contenido, comprendiendo los mecanismos de autenticación (tokens, claves), la detección de endpoints JSON y la importancia de procesar estructuras HTML con BeautifulSoup o Selenium. En este proceso, hemos verificado que analizar las solicitudes de red (Network) y utilizar herramientas como BurpSuite facilita interceptar y replicar peticiones, abriendo la puerta a recopilar datos incluso en contextos avanzados o con requisitos de login.

Al limpiar, almacenar y transformar la información en un formato tabular, hemos hecho énfasis en librerías como Pandas y Polars, que resultan ágiles para volúmenes de datos moderados en un solo equipo. Al mismo tiempo, hemos comparado la escalabilidad y la potencia que ofrece PySpark cuando la cantidad de datos se dispara o se requiere un rendimiento en paralelo en un clúster de máquinas (master, workers, tasks). Con PySpark, hemos apreciado la relevancia de las transformaciones perezosas y la organización en RDDs y DataFrames distribuidos. También hemos visto cómo un clúster de Spark se gestiona a través de un driver y múltiples ejecutores, permitiendo procesar millones de registros sin saturar la memoria de una sola máquina.

Este recorrido proporciona un pipeline integral:

- Primero, hemos recopilado datos textuales mediante APIs o scraping.
- Luego, hemos almacenado la información en crudo (por ejemplo, JSON) y hemos realizado la limpieza y transformación básica.
- En tercer lugar, hemos trabajado en modo local con Pandas o Polars, idóneos para un caso de uso mediano.
- Por último, hemos analizado la escalabilidad de Spark, que resulta esencial en proyectos de Big Data o en escenarios empresariales donde es prioritario distribuir la carga.



Nota final:

Practicar la búsqueda de datos en diferentes APIs (gratuitas, mockeadas) y profundizar en el scraping, utilizando DevTools o BurpSuite para descubrir endpoints.

Decidir con criterio: Pandas/Polars en contextos de volumen moderado, PySpark cuando el procesamiento masivo lo exige.

Explorar arquitecturas de clúster (nodo maestro, workers, cluster manager) si se necesitan flujos altamente escalables.

Mantener un enfoque de prototipado y verificación constante, probando la robustez del pipeline y optimizando cada capa para un rendimiento fiable y eficiente.



Con esta combinación de metodologías, herramientas y buenas prácticas, fortalecemos la capacidad de afrontar proyectos de ingeniería de datos textuales en entornos variados, desde pequeños scripts locales hasta potentes despliegues en la nube con Spark y cómputo distribuido.
