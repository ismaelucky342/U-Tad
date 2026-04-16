# Unidad 2. Minería de texto con Python.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Aspectos Básicos Del Texto](#2-aspectos-básicos-del-texto)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Naturaleza del texto](#22-naturaleza-del-texto)
  - [2.3 Procesamiento y representación](#23-procesamiento-y-representación)
  - [2.4 Tokenización y normalización](#24-tokenización-y-normalización)
- [3. Codificación De Caracteres](#3-codificación-de-caracteres)
  - [3.1 Introducción](#31-introducción)
  - [3.2 ASCII, Unicode y UTF-8](#32-ascii-unicode-y-utf-8)
  - [3.3 Manejo de codificaciones en Python](#33-manejo-de-codificaciones-en-python)
- [4. Expresiones Regulares En Python](#4-expresiones-regulares-en-python)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Estructura de las expresiones regulares](#42-estructura-de-las-expresiones-regulares)
  - [4.3 Uso básico de las expresiones regulares en Python](#43-uso-básico-de-las-expresiones-regulares-en-python)
  - [4.4 Enlaces de interés](#44-enlaces-de-interés)
- [5. Librerías Re Y Regex En Python](#5-librerías-re-y-regex-en-python)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Limitaciones de "re"](#52-limitaciones-de-re)
  - [5.3 Diferencias entre re y regex](#53-diferencias-entre-re-y-regex)
  - [5.4 Casos de uso con re y regex](#54-casos-de-uso-con-re-y-regex)
  - [5.5 Cuándo usar re o regex](#55-cuándo-usar-re-o-regex)
  - [5.6 Enlaces de interés](#56-enlaces-de-interés)
- [6. Librerías Nltk Y Spacy En Python](#6-librerías-nltk-y-spacy-en-python)
  - [6.1 Introducción](#61-introducción)
  - [6.2 Uso de librerías de NLP](#62-uso-de-librerías-de-nlp)
  - [6.3 NLTK (Natural Language Toolkit)](#63-nltk-natural-language-toolkit)
  - [6.4 spaCy](#64-spacy)
  - [6.5 Uso, buenas prácticas y optimización](#65-uso-buenas-prácticas-y-optimización)
  - [6.6 Enlaces de interés](#66-enlaces-de-interés)
- [7. Enfoque De Pandas/Polars Para Minería De Texto](#7-enfoque-de-pandaspolars-para-minería-de-texto)
  - [7.1 Introducción](#71-introducción)
  - [7.2 Pandas y Polars en el texto](#72-pandas-y-polars-en-el-texto)
  - [7.3 Minería de texto con DataFrames](#73-minería-de-texto-con-dataframes)
  - [7.4 Casos de uso en minería de texto](#74-casos-de-uso-en-minería-de-texto)
  - [7.5 Enlaces de interés](#75-enlaces-de-interés)
- [8. Visualización De Texto: Wordclouds En Python](#8-visualización-de-texto-wordclouds-en-python)
  - [8.1 Introducción](#81-introducción)
  - [8.2 Uso de wordclouds](#82-uso-de-wordclouds)
  - [8.3 Uso con Pandas y Polars](#83-uso-con-pandas-y-polars)
  - [8.4 Personalización](#84-personalización)
- [9. Conclusiones](#9-conclusiones)
  - [9.1 Conclusiones de la unidad](#91-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad didáctica, se explorará el concepto de minería de texto y cómo trabajar con él en Python. Al proceso que consiste en extraer información o patrones procedentes de documentos y textos, se le conoce como minería de texto (o text mining). Este proceso, también se conoce como NLP (Neuro-Linguistic Programming), el cual integra técnicas de lingüística computacional, aprendizaje automático y análisis estadístico.

El objetivo es convertir grandes volúmenes de texto en conocimiento estructurado que aporte valor en diversas aplicaciones como el análisis de sentimientos, la clasificación de documentos o la generación de resúmenes automáticos. Hoy en día, esto está ganando mucha relevancia gracias a su aplicación en soluciones de inteligencia artificial como pueden ser los modelos de LLM con ChatGPT, Claude o Gemini entre otros.

Python se ha convertido en uno de los lenguajes más populares para la minería de texto, gracias a su ecosistema que posee amplia gama de librerías, su sintaxis clara y legible y su extensa comunidad.

A lo largo de esta unidad, se profundizará en distintos aspectos de la manipulación y análisis de texto, prestando especial atención a la preparación de datos textuales, la codificación de caracteres, el uso de expresiones regulares, el aprovechamiento de librerías como NLTK y spaCy, y el tratamiento de los datos obtenidos con librerías como Pandas y Polars. Finalmente, se abordarán métodos de visualización de texto como las wordclouds, útiles para una identificación de palabras frecuentes.



- **Aspectos básicos del texto**  
  En este apartado vamos a conocer los principales aspectos del texto y sus diferencias con otros datos. La manipulación de datos textuales difiere notablemente del manejo de datos numéricos o categóricos. Mientras que en un dataframe con registros numéricos es sencillo aplicar operaciones aritméticas y resúmenes estadísticos, el texto está compuesto por secuencias de caracteres con significado lingüístico.
- **Codificación de caracteres**  
  En este apartado, profundizaremos en los fundamentos de la codificación, abordaremos estándares como ASCII, Unicode y UTF-8, y discutiremos las implicaciones a la hora de programar en Python. Mostraremos ejemplos de cómo leer y escribir archivos con distintas codificaciones y por qué UTF-8 se ha impuesto como un estándar en la mayoría de los proyectos modernos.
- **Expresiones regulares en Python**  
  En esta sección, profundizaremos en la lógica de las expresiones regulares en Python, explorando la sintaxis y el uso de funciones clave. Además, en el siguiente apartado entraremos en detalle de las librerías re y regex, que amplían las funcionalidades disponibles.
- **Librerías Re y Regex en Python**  
  Si en apartados anteriores se ha hablado de la base de las expresiones regulares, ahora vemos cómo se puede llevar esa capacidad al límite con regex, o incluso explotar mejor re en tareas más complejas que requieran lookbehind y otros patrones.
- **Librerías NLTK y Sapcy en Python**  
  Este apartado expone en detalle las funcionalidades clave de NLTK y spaCy, enfatizando su aplicabilidad en minería de texto. Se proporcionarán ejemplos de código detallados (tanto en Python puro como integrados en Pandas o Polars). También se comparará cuándo es preferible emplear NLTK o spaCy, así como posibles escenarios de combinación con otras herramientas (por ejemplo, re/regex y pipelines de preprocesamiento).
- **Enfoque de Pandas/Polars para minería de texto**  
  Pandas y Polars se han convertido en elementos básicos del ecosistema Python para la ciencia de datos. Si bien nacieron con un enfoque hacia datos numéricos y categóricos, sus potentes estructuras (DataFrames y Series) y operaciones vectorizadas resultan muy valiosas también en escenarios de minería de texto.
- **Visualización de texto: Wordclouds en Python**  
  En las etapas previas de esta unidad, hemos visto cómo limpiar, tokenizar y procesar el texto, y cómo manejarlo con herramientas como Pandas, Polars, NLTK o spaCy. Sin embargo, una pregunta clave al final de un pipeline de minería de texto es: ¿cómo comunicar o visualizar los resultados de manera efectiva?



#### Objetivos



En esta unidad se plantean los siguientes objetivos:



1. Comprender la naturaleza del texto y su importancia en el análisis de datos, diferenciando los aspectos semánticos y sintácticos que intervienen en la minería de texto.
2. Entender la relevancia de la codificación de caracteres (por ejemplo, UTF-8) y su impacto en la correcta manipulación de documentos en distintos idiomas.
3. Emplear expresiones regulares para la búsqueda y limpieza de patrones textuales, comprendiendo las diferencias entre librerías re y regex de Python.
4. Manejar librerías específicas de procesamiento de lenguaje natural, como NLTK y spaCy, identificando las fortalezas de cada una en tareas como tokenización y reconocimiento de entidades.
5. Aplicar enfoques con Pandas y Polars para leer, transformar y preparar texto de manera eficiente, integrando la manipulación tabular con la minería de texto.
6. Crear visualizaciones de texto, en particular wordclouds, y entender en qué casos resultan útiles para el análisis exploratorio de corpus extensos.



Esto sentará las bases para adentrarse en proyectos de análisis de texto, comprender las transformaciones previas al modelado lingüístico y aplicar métodos de procesamiento de lenguaje natural a contextos reales.



## 2. Aspectos Básicos Del Texto



### 2.1 Introducción



![image](assets/cm6w4zftr0061356zqxx7ifey-stock-image.jpg)



En este apartado vamos a conocer los principales aspectos del texto y sus diferencias con otros datos. La manipulación de datos textuales difiere notablemente del manejo de datos numéricos o categóricos. Mientras que en un dataframe con registros numéricos es sencillo aplicar operaciones aritméticas y resúmenes estadísticos, el texto está compuesto por secuencias de caracteres con significado lingüístico.

Para extraer valor del texto, es necesario realizar un procesamiento previo de segmentación, normalización y análisis de patrones que permitan la representación de la información contenida en un formato comprensible para algoritmos de aprendizaje automático o estadístico.



### 2.2 Naturaleza del texto



Podemos entender como texto a cualquier secuencia de caracteres que conforman palabras, oraciones o documentos. No obstante, desde un punto de vista computacional, lo que manejamos son bytes o unidades de código que representan esos caracteres. En la minería de texto buscamos transformar estas secuencias en objetos estructurados, como tokens o vocabularios, que faciliten la extracción de información relevante y permitan el análisis y manipulación.

Entre algunos de los aspectos clave de un texto, encontramos dos:



- **Longitud**  
  Un archivo de texto puede contener desde unas pocas líneas hasta millones de palabras. La escala de datos incide en la elección de la infraestructura de procesamiento (por ejemplo, PySpark para grandes volúmenes vs. scripts en Python puro para colecciones de menor tamaño).
- **Granularidad**  
  Dependiendo del objetivo, se pueden analizar fragmentos (palabras, oraciones) o documentos completos (páginas, libros). Esto condiciona las técnicas de parsing y normalización.



Antes de iniciar un análisis de texto, conviene definir qué nivel de detalle se desea (palabras, bigramas, oraciones…) y cuáles son las características más relevantes para la tarea específica (por ejemplo, si se requiere detectar nombres propios o analizar frecuencia de palabras).



### 2.3 Procesamiento y representación



Para poder trabajar con los datos de texto, será necesario hacer ese procesamiento. Para ello, debemos desarrollar un pipeline que se componga de:



![image](assets/cm6w57mva00cs356z3ns2m4it-Imagen1.jpg)

- **Recolección**  
  Obtención de documentos y texto desde fuentes diversas (archivos, páginas web, APIs, bases de datos).

  - Utilizaremos Pandas o Polars para leer archivos de texto teniendo en cuenta las diferentes codificaciones y así evitar problemas de caracteres ilegibles o inadecuados. Además, en próximas unidades veremos cómo extraer datos de fuentes de tipo API y web. Este paso nunca terminará ya que a mayor cantidad de datos, mejores análisis podremos realizar.
- **Preprocesado**  
  Limpieza de caracteres no deseados, normalización de mayúsculas, manejo de puntos y símbolos.

  - Haremos uso de expresiones regulares con las librerías re y regex para poder eliminar todo aquello que no deseemos de un texto o por el contrario, extraer lo que sí queremos, por ejemplo, obtener hashtags (“#” seguida de texto). Esto es una herramienta muy importante que se deberá combinar con otros pasos del proceso para seguir afinando nuestro resultado.
- **Tokenización**  
  Segmentación del texto en “trozos” (tokens) con significado.

  - Basándonos en herramientas como NLTK o spaCy utilizaremos modelos predefinidos para dividir nuestro texto en fragmentos que serán más manejables de cara a hacer una analítica más exacta y normalizada, por ejemplo, si en una frase aparece Coche, coche y COCHE, esto nos permitirá identificar que siempre es la misma palabra.
- **Limpieza de “stopwords”**  
  Eliminación de términos muy frecuentes y poco informativos como “el”, “la”, “de”.

  - Al igual que en el caso anterior, nos basaremos en herramientas ya creadas y disponibles para deshacernos de todo ese texto que genera ruido ya que no aporta información sobre el tema tratado en el corpus, es decir, si hablamos de patatas, las palabras como “la”, “de”, “con”, etc., generarán ruido de cara a identificar, por ejemplo, la frecuencia con la que aparecen las palabras más repetidas.
- **Modelado**  
  Representación del texto (por ejemplo, mediante conteo de palabras o embeddings de lenguaje).

  - De cara a definir un modelo de análisis, es muy importante que conozcamos los datos que vamos a utilizar para entrenarlo, es por ello que la visualización es un factor clave. Para ello, podremos utilizar librerías como WordCloud para visualizar la repetición de una misma palabra y de un vistazo conocer frecuencias. En unidades siguientes veremos cómo podemos utilizar todos los datos generados para entrenar modelos de análisis.
- **Análisis**  
  Aplicación de algoritmos o transformaciones (clasificación, extracción de entidades, resumen, etc.).

  - Gracias a NLTK y spaCy seremos capaces de identificar entidades como personas u organizaciones, resúmenes de texto y su clasificación que veremos con más detalle en las siguientes unidades. Todo esto acompañado de librerías como Pandas o Polars nos permiten hacer la analítica que deseemos, por ejemplo, para conocer que raíces de palabras se utilizan más (conocido como lema) o cómo está compuesta una frase a nivel de categorías gramaticales (sustantivos, verbos, ...).



Sin embargo, esta tarea no es fácil, pues nos encontramos numerosos desafíos. El ruido y la variabilidad son un factor importante ya que el texto puede contener errores ortográficos, abreviaturas, emoticonos, o incluso distintos alfabetos (latino, cirílico, kanji).

También encontramos problemas con idiomas y signos, pues cada lengua presenta su propia morfología y sintaxis, además de caracteres específicos que exigen un tratamiento especial en la codificación.

Por último, nos encontramos la ambigüedad debido a que las palabras pueden tener varios significados según el contexto, lo cual complica el análisis automático.

Para tratar de resolver estos desafíos, se usan librerías y técnicas de procesamiento de lenguaje natural que simplifican o reformatean el texto, con vistas a obtener un mejor rendimiento en las etapas posteriores.



### 2.4 Tokenización y normalización



Para proceder con el análisis y procesamiento de los datos, debemos entender el significado de “tokenizar”. Tokenizar es el paso en el que dividimos el texto en pequeñas unidades para poder analizar, típicamente llamadas “tokens”. En función del idioma, un token puede corresponder a una palabra completao o a pequeños segmentos de una palabra. Además, puede incluir signos de puntuación y otros símbolos si así se requiere.

Una vez tenemos el texto segmentado en tokens, debemos proceder a la normalización. Este es un proceso adicional en el que aplicamos unos estándares para el análisis. Por ejemplo, pasar todo a minúsculas, eliminar tildes, expandir contracciones (pasar “don’t” a “do not”), etc.

Estos pasos nos permiten analizar “Gato”, “gato” y “GATO” como la misma palabra y tener unas estadísticas más acertadas. Como ejemplo de lo que queremos conseguir podemos observar:



```ruby
# Ejemplo de tokenización:
texto = "¡Hola mundo! Me llamo Juan."
tokens = ["¡Hola", "mundo", "!", "Me", "llamo", "Juan", "."]
# Normalización, pasar a minúsculas y eliminar puntuación
tokens_normalizados = ["hola", "mundo", "me", "llamo", "juan"]
```



A estos pasos, se puede añadir la eliminación de “stopwords”. Las stopwords son palabras que no aportan un significado sustancial al contexto, como preposiciones, conjunciones o artículos (en español: “y”, “de”, “la”, “que”; en inglés: “and”, “the”, “of”, etc.). Se suelen eliminar antes de cualquier análisis cuantitativo para evitar que influyan en la estadística con su frecuencia.

Una vez tenemos el texto preprocesado, podemos almacenarlo en un DataFrame para su posterior tratamiento. Cada fila puede representar un documento o una sección de este, y las columnas pueden incluir la lista de tokens, la fecha de publicación, y otras características relevantes. En esta unidad utilizaremos tanto Pandas como Polars ya que permiten filtrar y manipular estos datos de forma eficiente.



```lua
import pandas as pd
from nltk import word_tokenize, download
download('punkt')

texto = "¡Hola mundo! Me llamo Juan."

def tokenize(text):
    return word_tokenize(text)

df_pandas = pd.DataFrame({
    "text": [texto]
})

df_pandas["tokens"] = df_pandas["text"].apply(tokenize)

df_pandas
```



```python
import polars as pl
from nltk import word_tokenize, download
download('punkt')

texto = "¡Hola mundo! Me llamo Juan."
# Función para tokenizer el texto
def tokenize(text):
    return word_tokenize(text)

df_polars = pl.DataFrame({
    "text": texto
})

df_polars = df_polars.with_columns(pl.col("text").map_elements(tokenize, return_dtype=pl.List(pl.Utf8)).alias("tokens"))

df_polars
```



![image](assets/cm6w5jzx700i3356ztzpe70jl-carousel1-Imagen2.jpg)

![image](assets/cm6w5jzx700i3356ztzpe70jl-carousel2-Imagen3.jpg)



## 3. Codificación De Caracteres



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



La codificación de caracteres es un factor crítico en la minería de texto. Si el texto proviene de fuentes internacionales o maneja alfabetos diversos (como el latino, cirílico, chino, japonés, árabe, etc.), se requiere un método unificado para representar cada símbolo. Un error típico al procesar texto es encontrar caracteres “extraños” o signos de interrogación si no hemos definido la codificación correcta.

En este apartado, profundizaremos en los fundamentos de la codificación, abordaremos estándares como ASCII, Unicode y UTF-8, y discutiremos las implicaciones a la hora de programar en Python. Mostraremos ejemplos de cómo leer y escribir archivos con distintas codificaciones y por qué UTF-8 se ha impuesto como un estándar en la mayoría de los proyectos modernos.



### 3.2 ASCII, Unicode y UTF-8



A lo largo del tiempo, se han desarrollado diferentes formatos de codificación. Entre ellos destacan ASCII, Unicode y UTF-8.

ASCII, conocido así por sus siglas en inglés de American Standard Code for Information Interchange, se desarrolló en la década de 1960 para representar caracteres en inglés. Es de 7 bits y contiene 128 códigos que incluyen letras mayúsculas/minúsculas, dígitos, signos de puntuación y algunos caracteres de control. Por ejemplo, la letra “A” se corresponde con el 65, representado de forma binaria como 01000001. Como se puede imaginar, resulta insuficiente para representar letras que puedan tener tildes u otros símbolos. Es por esto, que posteriormente surge una versión extendida de ASCII que utiliza 8 bits, lo que permite incluir hasta 256 caracteres, entre ellos la “ñ” y otros símbolos propios de diversos idiomas, ampliando notablemente la capacidad de representación de caracteres.

Por otro lado, encontramos Unicode, el cual surgió como un esfuerzo para unificar la representación de todos los alfabetos posibles. Asigna un “código de punto” (code point) único a cada carácter de prácticamente todos los idiomas y sistemas de escritura conocidos. Esto le permite incluir desde caracteres latinos con tilde hasta ideogramas chinos, pasando por emojis.

Finalmente, encontramos UTF-8, abreviatura de Unicode Transformation Format - 8 bits, es un esquema de codificación de caracteres ampliamente adoptado que emplea una cantidad variable de bytes, entre uno y cuatro, para la representación de cada carácter Unicode. Además, Es retro compatible con ASCII (los 128 primeros símbolos coinciden exactamente). Por todo ello, se ha convertido en el estándar en la mayoría de las aplicaciones modernas por su eficiencia y versatilidad.

Prueba de ello es que Python, en sus versiones recientes, por defecto utiliza UTF-8 al leer y escribir archivos. Esto evita problemas de visualización (como “Ã±” en lugar de “ñ”).



![image](assets/cm6w5x64b00ll356zee4mnwi5-Imagen4.png)



A continuación, veremos en detalle la necesidad de UTF-8:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651980_1/scormcontent/assets/INSD_BAIN_U2_Video1.mp4?v=1)



A pesar de los esfuerzos por crear un estándar ampliamente utilizado, sigue habiendo numerosos problemas en la codificación. Esto es debido a que no todos los sistemas utilizan UTF-8, existen otros como ANSI, ISO-8859-1, o incluso texto procedente de copiar y pegar sin respetar el formato utilizado. Es por ello, que podemos seguir observando caracteres no esperados en nuestros datos de texto.



### 3.3 Manejo de codificaciones en Python



Trabajar con Python nos da la ventaja de poder especificar la codificación de un archivo al abrirlo, tanto para lectura como para escritura. Por ejemplo:



```python
# Lectura de un archivo con codificación UTF-8
with open("documento_utf8.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# Escritura en un archivo con codificación ISO-8859-1
with open("datos_latin1.csv", "w", encoding="latin-1") as f:
    f.write('''title, character
char_1, á
char_2, é
char_3, í
char_4, ó
char_5, ú
char_6, ü''')    
# Lectura con codificación incorrecta que dará error
with open("datos_latin1.csv", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)
```



Si no se especifica el parámetro encoding, Python intentará utilizar la codificación predeterminada del sistema, lo que puede variar según la configuración regional del SO (Windows, Linux, macOS). Esto genera problemas si compartimos código con personas en distintos países o servidores.

Para trabajar con la minería de texto, es útil cargar los datos a un DataFrame para inspeccionar y transformar los datos. Tanto Pandas como Polars permiten especificar la codificación:



```r
import pandas as pd

df_pandas = pd.read_csv(
    "datos_latin1.csv",
    encoding="latin-1",
    sep=",",  
    header=0 # La primera fila contiene los nombres de las columnas
)
df_pandas
```



```python
import polars as pl

df_polars = pd.read_csv(
    "datos_latin1.csv",
    encoding="latin-1",
    sep=",",
    header=0 # La primera fila contiene los nombres de las columnas
)
df_polars
```



En caso de procesar erróneamente los datos, podremos observar caracteres como "[]"

También es habitual lidiar con varios alfabetos o idiomas simultáneamente, por ello es recomendado unificar los procesamientos en UTF-8 y, en caso de necesidad, utilizar librerías para detectar el idioma como langdetect, langid o APIs como las de Google Translator o las nuevas de LLMs como Gemini, OpenAI o Claude.

Un ejemplo para unificar la codificación de cara al procesamiento de los datos podría ser el siguiente:



```python
def convertir_latin1_a_utf8(ruta_entrada, ruta_salida):
    with open(ruta_entrada, "r", encoding="latin-1") as f_in:
        contenido = f_in.read()
    with open(ruta_salida, "w", encoding="utf-8") as f_out:
        f_out.write(contenido)

convertir_latin1_a_utf8("reporte_latin1.txt", "reporte_utf8.txt")
```



## 4. Expresiones Regulares En Python



### 4.1 Introducción



![image](assets/cm6w6bp6y00sm356zmxzdjq67-stock-image.jpg)



Las expresiones regulares (también conocidas como regex o patterns) constituyen una herramienta potente para buscar, filtrar y manipular cadenas de texto en función de patrones específicos. En la minería de texto resultan fundamentales para tareas de limpieza, normalización y extracción de información relevante. Desde la detección de correos electrónicos, URLs o números de teléfono, hasta la separación de campos en un formato complejo, las expresiones regulares proporcionan la flexibilidad necesaria para afrontar la gran variedad de formatos que pueden presentarse en un texto.

En esta sección, profundizaremos en la lógica de las expresiones regulares en Python, explorando la sintaxis y el uso de funciones clave. Además, en el siguiente apartado entraremos en detalle de las librerías re y regex, que amplían las funcionalidades disponibles.



### 4.2 Estructura de las expresiones regulares



Las expresiones regulares permiten describir, en una forma compacta, un conjunto de cadenas que queremos detectar o transformar. Se basan en una sintaxis de símbolos y operadores especiales, entre los cuales destacan:



- **Caracteres especiales**  
  - “.”: hace match con cualquier carácter (excepto salto de línea, por defecto).
  - “^” y “$”: delimitan el inicio y fin de la línea.
  - “*”, “+”, “?”: modificadores de repetición.
  - “[]”: define clases de caracteres, como [0-9] (cifras), [A-Za-z] (letras), o incluso [aeiou].
  - “\d”, “\w”, “\s”: shortcuts para dígitos, caracteres de palabra y espacios en blanco, respectivamente.
- **Agrupaciones y rangos**  
  - “( )”: agrupa un patrón y permite capturar los resultados en grupos para su uso posterior.
  - “{n,m}”: define un rango de repeticiones para el elemento anterior.



![image](assets/cm6w6gzna00vh356zvcx0z072-Imagen5.jpg)



Por ejemplo, si queremos encontrar direcciones de correo electrónico con el formato "nombre@dominio.ext", podemos usar un patrón sencillo como este:



```bat
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```



Para este ejemplo observamos que cada parte tiene una funcionalidad especifica:

- “^”: marca el inicio de la cadena. Asegura que el patrón solo haga match si comienza desde el principio de la cadena.
- “[A-Za-z0-9._%+-]+”: define el conjunto de caracteres válidos para la parte inicial del correo (antes del “@”).
  - “[A-Za-z0-9]”: permite letras mayúsculas (A-Z), minúsculas (a-z) y dígitos (0-9).
  - “._%+-“: incluye caracteres especiales comunes en nombres de usuario de correos electrónicos como punto (“.”), guion bajo (“_”), porcentaje (“%”), signo más (“+”) y guion (“-“).
  - El modificador “+” tras los corchetes requiere que haya al menos un carácter válido.
- “@”: es un carácter literal que separa la parte del nombre del usuario de la parte del dominio en un correo electrónico.
- “[A-Za-z0-9.-]+”: define el conjunto de caracteres válidos para la parte del dominio (después del “@” y antes del último punto “.”).
  - “[A-Za-z0-9]”: permite letras y dígitos.
  - “.-“: permite puntos (“.”) y guiones (“-“), comunes en nombres de dominios.
  - El modificador “+” tras los corchetes requiere que haya al menos un carácter válido.
- “\.”: coincide literalmente con un punto (“.”). Es obligatorio para separar el dominio de nivel superior (como .com, .org, etc.).
  - “[A-Za-z]{2,}”: define el dominio de nivel superior.
  - “[A-Za-z]”: permite solo letras (mayúsculas o minúsculas).
  - “{2,}”: especifica que debe tener al menos dos caracteres, pero no hay un límite superior explícito (por ejemplo, .com, .info).
- “$”: marca el final de la cadena asegurando que no haya caracteres adicionales después del patrón del correo electrónico.



### 4.3 Uso básico de las expresiones regulares en Python



El módulo re de Python proporciona funciones esenciales para trabajar con expresiones regulares. Entre las más utilizadas:

| Expresión | Función |
| --- | --- |
| re.match(patron, cadena) | Busca al principio del string si el patrón encaja. En caso de haber coincidencia, nos devuelve un objeto Match. Por el contrario, si no lo hay nos devuelve None |
| re.search (se abre en una nueva pestaña) (patron, cadena) | Busca la primera aparición del patrón en cualquier posición del string. Devuelve el objeto Match o None. |
| re.findall(patron, cadena) | Devuelve una lista con todas las apariciones que hacen match con el patrón. |
| re.sub(patron, reemplazo, cadena) | Reemplaza todas las apariciones del patrón en el string por el texto reemplazo. |
| re.split(patron, cadena) | Divide el string utilizando el patron como delimitador, retornando una lista. |

Además, se puede compilar la expresión regular para reutilizarla:



```python
import re

pattern = re.compile(r"\d{4}-\d{2}-\d{2}")  # Fechas en formato YYYY-MM-DD

texto = "La primera fecha es 2024-12-12, la segunda es 1900-01-01."
fechas = pattern.findall(texto)
print(fechas)
# Output: ['2024-12-12', '1900-01-01]
```



De esta forma, podemos definir expresiones generales en nuestro código y reutilizarlas cuando sea necesario.

Supongamos que hemos extraído una lista de tweets mediante la API de X. Si quisiésemos obtener los hashtags de cada uno, deberíamos hacerlo mediante:



```lua
import re
import pandas as pd

regex_hashtag = re.compile(r"#\w+")

tweets = [
    "Amo la ciencia de datos! #DataScience #Python",
    "Me encanta INSD en la U-Tad! #WorkHard #Focus",
]

df_pandas = pd.DataFrame({
    "text": tweets
})

df_pandas["hashtags"] = df_pandas["text"].str.findall(regex_hashtag)

df_pandas
```



```python
import re
import polars as pl

regex_hashtag = re.compile(r"#\w+")

tweets = [
    "Amo la ciencia de datos! #DataScience #Python",
    "Me encanta INSD en la U-Tad! #WorkHard #Focus",
]

df_polars = pl.DataFrame({
    "text": tweets
})

df_polars = df_polars.with_columns(pl.col("text").map_elements(lambda tweet: regex_hashtag.findall(tweet), return_dtype=pl.List(pl.Utf8)).alias("hashtags"))

df_polars
```



La expresión #\w+ nos permite obtener el texto que comience con # seguido de uno o más caracteres de palabra (letras, dígitos o subrayados). Esto sirve como punto de partida y junto con el análisis estadístico de la frecuencia de ciertos hashtags, puede ser útil para estudiar tendencias en redes sociales. Gracias al uso de DataFrames podemos comenzar nuestro análisis.



![image](assets/cm6w6u1tz011r356z9ddkf7g0-carousel1-Imagen6.jpg)

![image](assets/cm6w6u1tz011r356z9ddkf7g0-carousel2-Imagen7.jpg)



Sin embargo, por norma general nos encontramos diferentes símbolos de puntuación o erratas en el texto. Es por ello por lo que la etapa de preprocesamiento es crucial para hacer esta limpieza del texto. Por ejemplo:



```python
import re
import pandas as pd

def limpiar_texto(texto):
    texto_limpio = re.sub(r"\.{2,}", ".", texto) # Eliminamos signos de puntuación repetidos
    texto_limpio = re.sub(r"\s{2,}", " ", texto_limpio) # Reemplazamos múltiples espacios por uno
    return texto_limpio

tweets = [
    "Amo    la    ciencia... de datos! #DataScience #Python",
    "Me    encanta... INSD en      la U-Tad! #WorkHard #Focus",
]

df_pandas = pd.DataFrame({
    "texto original": tweets
})

df_pandas["texto limpio"] = df_pandas["texto original"].apply(limpiar_texto)

df_pandas
```



```python
import re
import polars as pl

def limpiar_texto(texto):
    texto_limpio = re.sub(r"\.{2,}", ".", texto) # Eliminamos signos de puntuación repetidos
    texto_limpio = re.sub(r"\s{2,}", " ", texto_limpio) # Reemplazamos múltiples espacios por uno
    return texto_limpio

tweets = [
    "Amo    la    ciencia... de datos! #DataScience #Python",
    "Me    encanta... INSD en      la U-Tad! #WorkHard #Focus",
]

df_polars = pl.DataFrame({
    "texto original": tweets
})

df_polars = df_polars.with_columns(
    pl.col("texto original").map_elements(limpiar_texto, return_dtype=pl.String()).alias("texto limpio")
)

df_polars
```



De esta manera, podemos evitar tokens innecesarios o que generan ruido, además de normalizar el texto para su análisis posterior.



![image](assets/cm6w6wh4g014y356zq8dzum8p-carousel1-Imagen8.jpg)

![image](assets/cm6w6wh4g014y356zq8dzum8p-carousel2-Imagen9.jpg)



Otro caso frecuente es el de identificar patrones que combinen números y letras, como puedan ser números de serie, números de pedidos, etc. Para ello podemos generar expresiones regulares para extraerlos. Por ejemplo, para números de serie del tipo “ABC-1234-DEF”:



```coffeescript
import re
import pandas as pd

exp_serie = re.compile(r"[A-Z]{3}-\d{4}-[A-Z]{3}")

lineas = [
    "Producto: ABC-1234-XYZ fecha: 2022-10-10",
    "ID: ZZZ-9999-AAA   Producto: Ordenador",
    "Texto irrelevante: AAA 3333 BBB",
]

def extract_serial(line):
  match = exp_serie.findall(line)
  return match if match else None

df_pandas = pd.DataFrame({
    "text": lineas
})

df_pandas["serial number"] = df_pandas["text"].apply(extract_serial)

df_pandas
```



```coffeescript
import re
import polars as pl

exp_serie = re.compile(r"[A-Z]{3}-\d{4}-[A-Z]{3}")

lineas = [
    "Producto: ABC-1234-XYZ fecha: 2022-10-10",
    "ID: ZZZ-9999-AAA   Producto: Ordenador",
    "Texto irrelevante: AAA 3333 BBB",
]

def extract_serial(line):
  match = exp_serie.findall(line)
  return match if match else None

df_polars = pl.DataFrame({
    "text": lineas
})

df_polars = df_polars.with_columns(pl.col("text").map_elements(extract_serial, return_dtype=pl.List(pl.Utf8)).alias("serial number"))

df_polars
```



![image](assets/cm6w6y4fi017e356zbdl6e7tm-carousel1-Imagen10.jpg)

![image](assets/cm6w6y4fi017e356zbdl6e7tm-carousel2-Imagen11.jpg)



Como nos podemos imaginar, la cantidad de variantes y de casos de uso que nos podemos encontrar es muy elevada, incluso cabe pensar la opción de que sean prácticamente infinitos. Es por ello, que debemos tener en cuenta la eficiencia en nuestro código, el uso de “re.compile()” permite reutilizar compilando una sola vez. Además, no se recomienda el uso de patrones ambiguos o usar excesivamente comodines como “.*”. Por último, todo procesamiento previo o segmentación que se pueda hacer antes de aplicar esos análisis nos permitirá trabajar con bloques más pequeños de manera más eficiente.

A continuación, veremos qué impacto puede tener el uso de re o regex en nuestro código:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651980_1/scormcontent/assets/INSD_BAIN_U2_Video2.mp4?v=1)



### 4.4 Enlaces de interés



> Documentación oficial de re en Python
>
> [Link](https://docs.python.org/3/library/re.html)

> Tutorial de expresiones regulares (en inglés)
>
> [Link](https://www.regular-expressions.info/)

> Herramientas online para testear expresiones (regex101)
>
> [Link](https://regex101.com/)

> Herramientas online para testear expresiones (regexr)
>
> [Link](https://regexr.com/)

> Cheatsheet de expresiones regulares
>
> [Link](https://www.datacamp.com/cheat-sheet/regular-expresso)



## 5. Librerías Re Y Regex En Python



### 5.1 Introducción



![image](assets/cm6wgx59l01ao356zj884ovx6-stock-image.jpg)



En el apartado anterior, abordamos el uso de expresiones regulares en Python con el módulo estándar re. Sin embargo, la comunidad de Python también ha desarrollado librerías adicionales que ofrecen una ampliación o mejora de las funcionalidades disponibles, destacando la librería regex.

Debido a que en minería de texto podemos hallar documentos que mezclan idiomas, símbolos y otros caracteres poco usuales, el uso de funcionalidades ampliadas (o correcciones de bugs conocidos) puede resultar determinante para el éxito de nuestro pipeline. Si en apartados anteriores se ha hablado de la base de las expresiones regulares, ahora vemos cómo se puede llevar esa capacidad al límite con regex, o incluso explotar mejor re en tareas más complejas que requieran lookbehind y otros patrones.



### 5.2 Limitaciones de "re"



El módulo re, cubre la mayoría de las necesidades cotidianas relacionadas con las expresiones regulares. Sin embargo, existen limitaciones documentadas que en ciertos escenarios pueden volverse problemáticas:



- **Lookbehind fijo**  
  En re, las llamadas lookbehind assertions requieren que la longitud de la subexpresión sea fija. Por ejemplo, (?<=abc)\w+ funciona, pero (?<=\w+)\w+ no, porque \w+ es de longitud variable.
- **Compatibilidad con ciertos estándares**  
  Re no implementa por completo todos los aspectos de la sintaxis de expresiones regulares que sí están presentes en librerías de otros lenguajes o en PCRE (Perl Compatible Regular Expressions).
- **Rendimiento**  
  Aunque re es eficiente para la mayoría de los casos, en ciertos patrones complejos con mucho backtracking, puede ser beneficioso contar con un motor de regex que maneje mejor los atajos o la optimización interna.



Como respuesta a estas limitaciones, la comunidad respondió con la librería regex como proyecto adicional. Al contrario que re, regex si es necesario instalar mediante:



```bat
pip install regex
```



### 5.3 Diferencias entre re y regex



La librería regex está pensada como un suplente (drop-in replacement) en muchos sentidos. Ofrece funciones similares a re.match, re.search, re.findall, re.sub, etc., pero con potencia adicional. Permite lookbehind de longitud variable, que en re no es viable. Soporta flag regex.VERSION1 que implementa funcionalidades extra, y otras flags que amplían la compatibilidad con distintos estándares.



#### Lookbehind



En minería de texto, la capacidad de lookbehind variable resulta interesante cuando se requiere, por ejemplo, capturar palabras precedidas por un prefijo variable, o en contextos donde la coincidencia depende de un número flexible de caracteres anteriores.

La principal crítica al módulo re es la imposibilidad de utilizar lookbehind con una longitud no fija. En re, la construcción (?<=\w+) no es válida porque \w+ puede coincidir con una secuencia de longitud variable (1, 2, 3 caracteres...). re exige que la longitud del patrón en el lookbehind sea constante.

En regex, en cambio, se admite:



```python
# Regex
import regex

pat = regex.compile(r"(?<=\d+)car")
texto = "123car 55car 9999car"

resultados = pat.findall(texto)
print("Coincidencias (regex):", resultados)
# Output: ['car', 'car', 'car']
```



```coffeescript
# Re
import re

pat = re.compile(r"(?<=\d+)car")
texto = "123car 55car 9999car"

resultados = pat.findall(texto)
print("Coincidencias (re):", resultados)
# Output: error look-behind requires fixed-width pattern
```



#### Soporte Unicode avanzado



La librería regex cuenta con un mejor soporte para propiedades Unicode. Por ejemplo, se puede solicitar coincidencias con propiedades de Unicode específicas. Esta capacidad es muy útil en un mundo cada vez más plagado de símbolos emergentes, especialmente si se analizan redes sociales o chats informales.

Los caracteres pueden provenir de prácticamente cualquier script: árabe, chino, cirílico, símbolos especiales, etc. El módulo re implementa un soporte Unicode razonable, pero regex:

- Implementa de manera más completa las propiedades definidas en el estándar Unicode, como \p{Letter}, \p{Extended_Pictographic}, etc.
- Permite filtrar o capturar emojis con mayor precisión.
- Maneja de forma más robusta la normalización de Unicode y la detección de secuencias de combinación.

Por ejemplo, para trabajar con emojis:



```coffeescript
# Regex
import regex

pattern_emoji = regex.compile(r"\p{Extended_Pictographic}+")

texto_emojis = "Hoy me siento feliz 😄 y triste 😢 a la vez."
emojis = pattern_emoji.findall(texto_emojis)
print(emojis) 
# Output: ['😄', '😢']
```



```coffeescript
# Re
import re

pattern_emoji = re.compile(r"\p{Extended_Pictographic}+")

texto_emojis = "Hoy me siento feliz 😄 y triste 😢 a la vez."
emojis = pattern_emoji.findall(texto_emojis)
print(emojis) 
# Output: error
```



#### Recursividad y anidación



Un caso complejo aparece cuando necesitamos emparejar paréntesis o corchetes anidados en un texto (por ejemplo, para parsear trozos con varios niveles de profundidad). La librería regex soporta expresiones recursivas ((?R)), mientras que re no. Esto es muy útil si se está minando texto que contenga expresiones matemáticas, HTML anidado, o literales con posibles contenidos anidados en corchetes:



```python
# Regex
import regex

par_patron = regex.compile(r"""
    \(
       (?: [^()]+ | (?R) )*
    \)
""", regex.VERBOSE)

texto_par = "Aquí (tenemos (un ejemplo) de (anidación (compleja))) y (otro)."

encontrados = par_patron.findall(texto_par)
print("Paréntesis anidados:", encontrados)
```



En el caso de re, no es posible ya que no soporta la recursión de forma directa.



### 5.4 Casos de uso con re y regex



#### ¿Qué habrás conseguido al finalizar?



En ciertos idiomas el separador de decimales puede ser coma, mientras que en inglés se usa el punto. Para capturar valores numéricos con decimal variable, se podría lograr mediante:



```python
import regex

pattern_numerico = regex.compile(r"(?<!\w)(\d+(?:[.,]\d+)?)(?!\w)")

texto_mixto = "Precio: 45,67 euros, o tal vez 100.50 USD, etc. Valor2=123"
coinc = pattern_numerico.findall(texto_mixto)
print(coinc)
# Output: ['45,67', '100.50', '123']
```



En el caso de re, no existe una solución directa debido a los lookbehind y lookahead (?!\w) y (?<!\w). Es por ello por lo que en este caso es más recomendable usar regex.



#### Extracción de subdominios



Supongamos que tenemos un texto con URLs que pueden tener subdominios arbitrarios y TLDs de distinta longitud. Queremos capturar la parte del dominio principal y la TLD, no la ruta:



```python
import regex

dom_pat = regex.compile(r"(?<=https?://)([\w.-]+)\.(\p{Letter}{2,})(?=/?)")

test_urls = [
    "https://sub.example.com/path/to/file",
    "http://mydomain.org/index.html",
    "https://xxx.co/short"
]

for url in test_urls:
    res = dom_pat.search(url)
    if res:
        print(f"URL: {url}")
        print(" Dominio principal:", res.group(1))
        print(" TLD:", res.group(2))
        print()
# Output
URL: https://sub.example.com/path/to/file
 Dominio principal: sub.example
 TLD: com

URL: http://mydomain.org/index.html
 Dominio principal: mydomain
 TLD: org

URL: https://xxx.co/short
 Dominio principal: xxx
 TLD: co
```



En este caso, de nuevo, encontramos limitaciones con re. Es por eso por lo que se prefiere el uso de regex debido a los lookbehind.



#### Detección de texto específico



Gracias a regex podemos identificar si el texto presenta caracteres de un rango concreto. Por ejemplo, si queremos identificar y obtener textos de un alfabeto como el cirílico, podríamos usar:



```ini
import regex

pattern_cyr = regex.compile(r"\p{Script=Cyrillic}+")

sample_text = "Texto con кириллица y latín mezclado"
found_cyr = pattern_cyr.findall(sample_text)
print("Cirílico:", found_cyr)
# Output: ['кириллица']
```



En el caso de querer usar re, deberíamos definir manualmente los rangos, por ejemplo: [А-яЁё]. Lo que lo convierte en una solución compleja de escalar.



### 5.5 Cuándo usar re o regex



La selección de la librería adecuada para manejo de expresiones regulares en Python puede marcar la diferencia en proyectos de minería de texto donde:

- Se requieran patrones complejos (p. ej., anidamiento o lookbehind variable).
- Se trabaje con grandes volúmenes y sea necesaria la optimización de ciertos aspectos de rendimiento.
- Se exploten propiedades avanzadas de Unicode, como la detección específica de emojis, pictogramas o scripts internacionales.

Mientras que el módulo re de la librería estándar cubre la mayoría de los casos, la librería regex ofrece funcionalidades adicionales que pueden ser decisivas cuando se trabaja con textos multilingües o que requieran validaciones especiales.

Tanto re como regex pueden integrarse sin problemas con Pandas y Polars para la manipulación tabular del texto, y constituyen un pilar importante antes de pasar a librerías de procesamiento de lenguaje natural más completas, como NLTK o spaCy, que es precisamente el enfoque del siguiente apartado. Al gestionar los patrones con regex, se puede realizar una prelimpieza o una extracción avanzada de entidades, preparando el corpus para técnicas de tokenización y análisis lingüístico en profundidad.

Así pues, la elección de librería dependerá de numerosos factores. Será necesario conocer nuestro caso de uso en detalle para hacer la mejor elección.



![image](assets/cm6whkcly01vj356zuaxrk91y-Imagen12.png)



Para saber cuál será la elección adecuada, analizaremos en detalle cada una en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651980_1/scormcontent/assets/INSD_BAIN_U2_Video3.mp4?v=1)



### 5.6 Enlaces de interés



> Repositorio y documentación oficial de la librería regex
>
> [Link](https://pypi.org/project/regex/)



## 6. Librerías Nltk Y Spacy En Python



### 6.1 Introducción



![image](assets/cm6widtv501yh356z06rjeyyc-stock-image.jpg)



En los apartados anteriores, hemos profundizado en la minería de texto desde la perspectiva de la codificación de caracteres y las expresiones regulares. Esas técnicas constituyen la base para la limpieza y preprocesamiento de datos textuales. Sin embargo, al momento de abordar tareas avanzadas de procesamiento de lenguaje natural (NLP), como tokenización lingüística, etiquetado de categorías gramaticales (POS-tagging), reconocimiento de entidades (NER) o incluso lematización, es recomendable utilizar librerías más específicas.

En el ecosistema Python, destacan dos librerías principales para el procesamiento de lenguaje natural:

- NLTK (Natural Language Toolkit): destaca como una de las bibliotecas pioneras y más establecidas en el campo del Procesamiento del Lenguaje Natural. Proporciona un conjunto completo de herramientas para tareas como la tokenización, el etiquetado, el análisis gramatical, el análisis sintáctico y la gestión de grandes corpus.
- spaCy: es una biblioteca más reciente, creada con un enfoque pragmático y un alto rendimiento como prioridad. Sus pipelines de NLP optimizados en Cython agilizan tareas como el Reconocimiento de Entidades Nombradas (NER), el análisis de dependencias sintácticas y otros aspectos del análisis lingüístico a gran escala.

Este apartado expone en detalle las funcionalidades clave de NLTK y spaCy, enfatizando su aplicabilidad en minería de texto. Se proporcionarán ejemplos de código detallados (tanto en Python puro como integrados en Pandas o Polars). También se comparará cuándo es preferible emplear NLTK o spaCy, así como posibles escenarios de combinación con otras herramientas (por ejemplo, re/regex y pipelines de preprocesamiento).



### 6.2 Uso de librerías de NLP



La minería de texto no se limita a buscar patrones con expresiones regulares ni a limpiar datos. Una vez que se tienen los corpus depurados, normalmente se desea extraer información semántica o gramatical. Es ahí donde entran en juego los sistemas de Procesamiento de Lenguaje Natural. Dichos sistemas buscan imitar, en la medida de lo posible, la forma en que los humanos interpretamos el lenguaje:

- Tokenizar el texto, para dividirlo en unidades léxicas (palabras, signos de puntuación u otros elementos que tengan relevancia).
- Etiquetar cada token con su categoría gramatical (por ejemplo, adjetivo, verbo, sustantivo) para comprender cómo se relacionan las palabras en una oración.
- Reconocer entidades (nombres propios, organizaciones, lugares, cantidades, etc.), para extraer datos clave (por ejemplo, “Google”, “Madrid”, “$500”).
- Lematizar o stemmar las palabras. Así, “jugando” y “jugué” se convierten en su forma base “jugar” cuando corresponde, lo cual facilita el análisis.
- Segmentar el texto en oraciones o frases con significado completo.
- Detectar el idioma, en caso de que el corpus sea multilingüe, o se reciba texto de fuentes diversas.
- Realizar análisis de sentimientos, clasificación y extracción de temas, resúmenes automáticos, entre otras aplicaciones de mayor complejidad.

Tanto NLTK como spaCy cubren muchas de estas etapas, con diferencias de enfoque que iremos examinando. Antes de mostrar ejemplos concretos, describiremos brevemente las características principales de cada una.



![image](assets/cm6wijhhz020l356zswygoevw-Imagen13.png)



### 6.3 NLTK (Natural Language Toolkit)



El Natural Language Toolkit (NLTK) es una de las librerías pioneras en Python para NLP y fue desarrollada con un enfoque académico y didáctico. Posee un extenso conjunto de módulos para análisis léxico, sintáctico y semántico, así como colecciones de corpus y utilidades de aprendizaje automático orientadas a texto.

Entre los factores de NLTK, destacamos:

- Un amplio abanico de corpus integrados (textos de prueba) y de utilidades que permiten descargar corpus externos.
- Múltiples módulos para tokenización, etiquetado gramatical (PoS tagging), lemmatización, parsing, chunking y reconocimiento de entidades.
- Herramientas para análisis de collocations, n-gramas y varios métodos estadísticos clásicos en lingüística.
- Una gran comunidad y abundante documentación.



#### Instalación



Para instalar NLTK, en la mayoría de los entornos basta con:



```bat
pip install nltk
```



Adicionalmente, NLTK provee un gestor interno de descargas para corpus, modelos preentrenados y datos auxiliares. Como parte de importar la librería, es necesario descargar estos recursos mediante:



```bat
import nltk
nltk.download()
```



De esta manera obtendremos una interfaz gráfica para seleccionar los módulos.



![image](assets/cm6wingn2025o356z046hmh3a-Imagen14.jpg)



Sin embargo, NLTK también proporciona la posibilidad de descargar de manera selectiva evitando la interfaz:



```python
import nltk
nltk.download('punkt')  # Para la tokenización básica
nltk.download('wordnet')  # Para la lematización con WordNet
nltk.download('averaged_perceptron_tagger')  # Etiquetado de partes de la oración
nltk.download('averaged_perceptron_tagger_eng')  # Etiquetado de partes de la oración en inglés
```



#### Tokenización



El paso de tokenización es fundamental: si un texto no está tokenizado de forma adecuada, las siguientes fases (etiquetado, lematización) producirán errores o resultados menos precisos. NLTK ofrece varias versiones de tokenizadores (basados en reglas, en expresiones regulares, etc.), pero el más frecuente para texto en inglés o similar es word_tokenize:



```python
import nltk
from nltk.tokenize import word_tokenize

texto = "NLTK es una librería muy potente. !Es mi primer uso en la U-tad de NLTK!"
tokens = word_tokenize(texto)
print(tokens)
# Output: ['NLTK', 'es', 'una', 'librería', 'muy', 'potente', '.', '!', 'Es', 'mi', 'primer', 'uso', 'en', 'la', 'U-tad', 'de', 'NLTK', '!']
```



En este caso, word_tokenize se basa en un tokenizador estándar que separa palabras, signos de puntuación y caracteres especiales. Dada la variedad de lenguajes, la tokenización no siempre es trivial (por ejemplo, en chino no existen espacios entre palabras, y en algunos idiomas se necesitan reglas específicas para separar contracciones).

En este caso, observamos que los signos de exclamación y puntuación aparecen como tokens aparte. Esto es útil o no, según la aplicación. Para tareas de análisis de sentimientos, mantener los signos de exclamación puede ser importante, mientras que para un análisis más semántico en el que la puntuación no aporte valor, podríamos descartarlos.



#### Etiquetado gramatical (PoS Tagging)



Otra de las funcionalidades estrella de NLTK es el etiquetado de partes de la oración (PoS, Part of Speech Tagging). Esto significa asignar a cada token una etiqueta que indique su función gramatical (sustantivo, verbo, adjetivo, adverbio, etc.). Su importancia reside en:

- Permite filtrar tokens según su categoría (por ejemplo, extraer solo sustantivos para análisis de contenido).
- Contribuye a la lematización o stemming con mayor precisión, pues el significado y la forma base de una palabra pueden depender de su categoría gramatical.
- Es la base para sistemas de análisis sintáctico más profundos.



```python
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

texto = "Pedro runs fast and Mary sings."
tokens = word_tokenize(texto)
etiquetas = pos_tag(tokens, lang='eng')  # NLTK no soporta español de forma directa para tagging
print(etiquetas)
# Output: [('Pedro', 'NNP'), ('runs', 'VBZ'), ('fast', 'RB'), ('and', 'CC'), ('Mary', 'NNP'), ('sings', 'NNS'), ('.', '.')]
```



En el caso de pos_tag, se basa en modelos estadísticos, como el “average perceptron tagger”. Para este output vemos que NNP denota “Proper Noun” (nombre propio), VB es verbo, RB adverbio, etc. En idiomas distintos del inglés, se requieren descargarse otros modelos o utilizar librerías específicas.

Por ejemplo, la implementación en español podría ser algo como:



```python
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.tag import tnt
from nltk.corpus import cess_esp

nltk.download('cess_esp')
texto_es = "Pedro corre rápido y María canta hermosas canciones."
tokens = word_tokenize(texto_es, language='spanish')

cess_tagged = cess_esp.tagged_sents()
trainer = tnt.TnT()
trainer.train(cess_tagged)

etiquetas = trainer.tag(tokens)
print(etiquetas)
# Output: [('Pedro', 'Unk'), ('corre', 'vmip3s0'), ('rápido', 'aq0ms0'), ('y', 'cc'), ('María', 'Unk'), ('canta', 'vmip3s0'), ('hermosas', 'Unk'), ('canciones', 'ncfp000'), ('.', 'Fp')]
```



En este caso vemos como hay tags que hacen referencia a desconocido (“Unk”) y las tags poseen códigos más difíciles de interpretar.



#### Lematización y stemming



En minería de texto, querer agrupar palabras según su raíz léxica es muy frecuente. Para ello contamos con dos aproximaciones principales.

Por un lado, tenemos el Stemming, que recorta las palabras a sus radicales sin tener en cuenta si la palabra existe o no en el vocabulario. Por ejemplo, “corriendo”, “corrieron” y “correrá” podrían convertirse en “corr” usando un stemmer muy sencillo.

Por otro lado, tenemos la Lematización, que utiliza diccionarios (como WordNet en inglés) o reglas lingüísticas para devolver la forma canónica (o lema) de una palabra. Por ejemplo, “corriendo” → “correr” (en español). Esto es mucho más preciso, pero requiere más recursos.

Para hacer ambas, es necesario que utilicemos diferentes algoritmos y diccionarios. Por ejemplo, para usar stemming en inglés tenemos PorterStemmer (en español podremos usar SnoballStemmer(‘spanish’)), para la lematización es necesario usar WordNet y sus diccionarios.



```python
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet') 
nltk.download('omw-1.4')  # Descargamos para sinónimos del wordnet

texto = "playing played plays player"

tokens = word_tokenize(texto)
print("Tokens:", tokens)

# Stemming
stemmer = PorterStemmer()
stems = [stemmer.stem(token) for token in tokens]
print("Stemming:", stems)

# Lematización
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token, pos='v') for token in tokens]
print("Lematización:", lemmas)
# Output: Tokens: ['playing', 'played', 'plays', 'player']
Stemming: ['play', 'play', 'play', 'player']
Lematización: ['play', 'play', 'play', 'player']
```



De esta forma, “playing”, “played” y “plays” se reducen a “play” usando lematización, y “player” permanece sin cambios.



#### Uso y limitaciones



NLTK es ideal para fines educativos, prototipado rápido y experimentación con corpus en inglés. Permite implementar flujos complejos (tokenización, etiquetado, lematización, reconocimiento de entidades, etc.) y ofrece numerosas utilidades estadísticas (distribuciones de frecuencia, entropía, etc.).

Sin embargo, para trabajar con grandes volúmenes de datos, su rendimiento puede ser inferior en comparación con librerías más optimizadas como spaCy.

Además, el soporte para el español y otros idiomas no es tan avanzado (aunque existen stemmers y algunos etiquetadores, la calidad varía).

Por último, en entornos productivos donde se requiera gran velocidad o un pipeline muy optimizado, a menudo se recurre a spaCy. Sin embargo, NLTK sigue siendo muy recomendable para la docencia, la investigación y proyectos donde la flexibilidad y la disponibilidad de corpus integrados sean prioritarias.



### 6.4 spaCy



spaCy es una librería relativamente más joven que NLTK, desarrollada con un enfoque orientado a la producción y el rendimiento. Está escrita tanto en Python como en Cython (para compilar y ganar velocidad), y cuenta con modelos de procesamiento entrenados para diversos idiomas, incluido el español.

Entre sus objetivos destacamos:

- Proporcionar métodos rápidos y eficientes para tokenizar, etiquetar, parsear y reconocer entidades.
- Estar lista para entornos empresariales, integrándose fácilmente con otras librerías de machine learning.
- Simplificar el pipeline de procesamiento y la administración de modelos, asegurando compatibilidad con Transformers y el uso de GPU para tareas más complejas.

Como consecuencia, spaCy es muy popular en aplicaciones donde la velocidad es esencial, como el análisis de streams de redes sociales, la clasificación de grandes volúmenes de texto en tiempo real, chatbots, etc.

Cabe destacar que spaCy divide el pipeline de procesamiento de nlp en las siguientes etapas: tokenizer, tagger, parser, ner, lemmatizer, textcat, custom.



![image](assets/cm6wivukt02i2356z9oyunn5n-Imagen15.png)



Veamos en más detalle estas etapas y su significado en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651980_1/scormcontent/assets/INSD_BAIN_U2_Video4%20%281%29.mp4?v=1)



#### Instalación



Para instalar spaCy, en la mayoría de los entornos basta con:



```bat
pip install spacy
```



Sin embargo, spaCy por sí mismo no contiene modelos de lenguaje; se deben descargar. Para el español, se sugiere alguno de los siguientes:

- es_core_news_sm: small, versión ligera (alrededor de 11 MB).
- es_core_news_md: medium, más grande y precisa.
- es_core_news_lg: large, muy completa.

Lo mismo para inglés: en_core_web_sm, en_core_web_md, en_core_web_lg, etc. De igual modo hay modelos para alemán, francés, portugués, etc.

Para este curso, utilizaremos el small ejecutando el siguiente comando en la terminal:



```bat
python -m spacy download es_core_news_sm
```



#### Tokenización y tagging



Uno de los puntos fuertes de spaCy es la consistencia de su API. El flujo típico de trabajo, siguiendo el pipeline comentado previamente, es:

- Cargar el modelo (nlp = spacy.load("es_core_news_sm")).
- Procesar un texto para obtener un objeto Doc.
- Iterar o analizar los tokens y la información que spaCy asigna a cada uno.

Ejemplo de ello es:



```python
import spacy
import pandas as pd

nlp = spacy.load("es_core_news_sm")
texto = "Soy un alumno de la U-tad y me encanta la ciencia de datos."
doc = nlp(texto)

df_pandas = pd.DataFrame({
    "token": [token.text for token in doc],
    "token.pos_": [token.pos_ for token in doc],
    "token.tag_": [token.tag_ for token in doc]
})

print(df_pandas)
```



![image](assets/cm6wjhh64008a356zz83a2sv4-Imagen16.png)



```python
import spacy
import polars as pl

nlp = spacy.load("es_core_news_sm")
texto = "Soy un alumno de la U-tad y me encanta la ciencia de datos."
doc = nlp(texto)

df_polars = pl.DataFrame({
    "token": [token.text for token in doc],
    "token.pos_": [token.pos_ for token in doc],
    "token.tag_": [token.tag_ for token in doc]
})

print(df_polars) 
```



![image](assets/cm6wji7sj009d356zjox8uugp-Imagen17.jpg)



En este caso, el objeto doc encapsula el resultado del pipeline de spaCy, que por defecto incluye la tokenización, el etiquetado gramatical, la lematización y la segmentación en oraciones, entre otros pasos. pos_ nos devuelve la categoría gramatical general (verbo, sustantivo, adjetivo, etc.), mientras que tag_ puede ser más específica (tiempo verbal, número, género).



#### Lematización



Cada token en spaCy no solo tiene su categoría gramatical, sino que también cuenta con atributos como:

| Atributo | Descripción |
| --- | --- |
| token.lemma_ | la forma lematizada |
| token.is_stop: | indica si es una stopword |
| token.is_punct | chequea si es un signo de puntuación |
| token.dep_ | la relación sintáctica (por ejemplo, si es el sujeto, objeto, modificador, etc.) |

Gracias a esto, al recorrer cada token, es posible filtrar rápidamente aquellos que sean stopwords o agrupar por pos_. Por otro lado, lemma_ es de gran ayuda para normalizar el vocabulario. Esto se puede observar en el siguiente ejemplo:



```elixir
import spacy
import pandas as pd

nlp = spacy.load("es_core_news_sm")
doc = nlp("Los estudiantes aprobaron todos los exámenes.")

df_pandas = pd.DataFrame({
    "token": [token.text for token in doc],
    "token.lemma_": [token.lemma_ for token in doc],
    "token.pos_": [token.pos_ for token in doc],
    "token.is_stop": [token.is_stop for token in doc],
    "token.dep_": [token.dep_ for token in doc]
})

print(df_pandas)
```



```python
import spacy
import polars as pl

nlp = spacy.load("es_core_news_sm")
doc = nlp("Los estudiantes aprobaron todos los exámenes.")

df_polars = pl.DataFrame({
    "token": [token.text for token in doc],
    "token.lemma_": [token.lemma_ for token in doc],
    "token.pos_": [token.pos_ for token in doc],
    "token.is_stop": [token.is_stop for token in doc],
    "token.dep_": [token.dep_ for token in doc]
})

print(df_polars)
```



![image](assets/cm6wjlsan00cw356z0lsv4xh6-carousel1-Imagen18.png)

![image](assets/cm6wjlsan00cw356z0lsv4xh6-carousel2-Imagen19.jpg)



#### Reconocimiento de entidades (NER)



El Reconocimiento de Entidades (NER, por sus siglas en inglés) es la capacidad de identificar, en un texto, entidades como nombres de persona, lugares, organizaciones, fechas, cantidades, etc. Con spaCy, es muy sencillo. spaCy utiliza modelos estadísticos entrenados en grandes corpus anotados. ent.label_ típicamente puede devolver categorías como PER (persona), LOC (lugar), ORG (organización), DATE (fecha), etc.



```lua
import spacy
import pandas as pd

nlp = spacy.load("es_core_news_sm")
texto = "El presidente del viajó de Madrid a Italia el 1 de febrero para reunirse con miembros de la ONU y con Elon Musk."
doc = nlp(texto)

df_pandas = pd.DataFrame({
    "ent.text": [ent.text for ent in doc.ents],
    "ent.label_": [ent.label_ for ent in doc.ents]
})

print(df_pandas)
```



![image](assets/cm6wjnipm00fc356zltadmxko-Imagen20.png)



```python
import spacy
import polars as pl

nlp = spacy.load("es_core_news_sm")
texto = "El presidente del viajó de Madrid a Italia el 1 de febrero para reunirse con miembros de la ONU y con Elon Musk."
doc = nlp(texto)

df_polars = pl.DataFrame({
    "ent.text": [ent.text for ent in doc.ents],
    "ent.label_": [ent.label_ for ent in doc.ents]
})

print(df_polars)
```



![image](assets/cm6wjo64800gf356zhd1mou9o-Imagen21.png)



Sin embargo, estos modelos suelen fallar. Es por ello, que es habitual refinar los modelos para contextos específicos (medicina, finanzas, marketing) mediante “entrenamiento adicional” (fine-tuning). De este modo, se pueden detectar entidades de nicho (p. ej., nombres de fármacos, códigos de cliente, etc.).



### 6.5 Uso, buenas prácticas y optimización



Aunque ya hemos visto varias características de NLTK y spaCy, conviene analizar las principales similitudes y diferencias de cara a tomar una decisión sobre cual utilizar:



![image](assets/cm6wjpbxe00ik356zh4p2az7i-Imagen22.png)



En general, si se quiere aprender los fundamentos del NLP o se requiere un acceso rápido a corpus clásicos, NLTK es estupendo. Si, en cambio, se trabajan pipelines con gran volumen de datos o se necesitan modelos robustos y rápidos para producción, spaCy suele ser la opción preferida.

También es muy importante conocer cómo podemos optimizar nuestro pipeline para tener un mejor rendimiento. Entre las acciones posibles, encontramos:

- Al trabajar con spaCy, cada ejecución de nlp(texto) activa el pipeline completo (tokenización, PoS tagging, NER, etc.). Si necesitamos reutilizar información, conviene guardar el objeto Doc o, en su defecto, realizar transformaciones mínimas para no recalcular.
- Selección de modelo adecuado:
  - Modelos “small” (sm): más rápidos, pero menos precisos para NER y PoS.
  - Modelos “large” (lg): más pesados, requieren más memoria, pero ofrecen mejor exactitud.
  - Modelos “transformers”: utilizan técnicas de vanguardia (BERT, etc.) y logran resultados superiores, a cambio de un consumo de recursos mayor.
- Uso de spaCy en modo batch: para grandes volúmenes, en vez de procesar cada texto en un bucle, conviene usar nlp.pipe que permite pasar un iterable de textos y aplica internamente optimizaciones. Esto puede ofrecer mejoras de rendimiento notables frente a un for text in texts: doc = nlp(text).



```coffeescript
texts = [
    "Me encantó visitar Lima.",
    "Bogotá es una ciudad interesante.",
    "El río Támesis está en Londres."
]

docs = list(nlp.pipe(texts))
for doc in docs:
    # Operar con doc...
    pass
```



- Desactivar componentes del pipeline: si solo necesitamos tokenizar, podemos desactivar el etiquetado y el NER para reducir costes de cómputo. Esta práctica es esencial cuando deseamos hacer un preprocesado ligero sin necesidad de todos los componentes.



```python
with nlp.disable_pipes("tagger", "parser", "ner"):
    for doc in nlp.pipe(lista_de_textos):
        # Solo haremos tokenización
        tokens = [token.text for token in doc]
```



### 6.6 Enlaces de interés



> Listado de módulos de NLTK
>
> [Link](https://www.nltk.org/py-modindex.html)

> Instalación de datos de NLTK
>
> [Link](https://www.nltk.org/data.html)

> spaCy 101
>
> [Link](https://spacy.io/usage/spacy-101)

> spaCy universe
>
> [Link](https://spacy.io/universe)



## 7. Enfoque De Pandas/Polars Para Minería De Texto



### 7.1 Introducción



![image](assets/cm6wjyjug00my356z9vkh3owh-stock-image.jpg)



En las secciones anteriores, abordamos la preparación del texto (tokenización, limpieza, expresiones regulares), así como el procesamiento lingüístico con librerías como NLTK y spaCy. Sin embargo, en muchos casos de minería de texto, la fase de análisis y transformación masiva de los datos se beneficia enormemente de herramientas que permitan manipular grandes volúmenes de información de forma tabular.

Pandas y Polars se han convertido en elementos básicos del ecosistema Python para la ciencia de datos. Si bien nacieron con un enfoque hacia datos numéricos y categóricos, sus potentes estructuras (DataFrames y Series) y operaciones vectorizadas resultan muy valiosas también en escenarios de minería de texto

Dado que un corpus textual puede alcanzar fácilmente millones de registros (por ejemplo, tweets, reseñas de productos, logs de sistemas con mensajes), la manipulación eficiente se vuelve esencial. Tanto Pandas como Polars permiten filtrar, agrupar, agregar y transformar datos con un estilo declarativo, acercándose mucho a la potencia de SQL para datos estructurados. Sin embargo, en este caso, cada celda del DataFrame puede contener texto, listas de tokens o incluso diccionarios con anotaciones lingüísticas. Exploraremos cómo aprovechar estas herramientas para llevar a cabo la minería de texto de forma organizada y escalable.



### 7.2 Pandas y Polars en el texto



La minería de texto, sobre todo cuando manejamos colecciones de documentos extensas (decenas de miles o millones de filas), requiere métodos para almacenar y manipular la información de forma eficiente. Las librerías orientadas a DataFrames han demostrado ser ideales para el análisis exploratorio, la transformación y la fusión de datos de distinta naturaleza.

En un DataFrame, podemos filtrar rápidamente los documentos por ciertos criterios (por ejemplo, fecha, presencia de determinada palabra, clasificación previa, etc.), ordenar según su longitud o agruparlos según características. Esto simplifica la definición de subconjuntos de datos textuales específicos.

Pandas y Polars se integran de forma nativa con múltiples librerías de Python (Matplotlib, Seaborn, Plotly, scikit-learn, statsmodels, NLTK, spaCy, etc.), lo que permite construir pipelines completos sin tener que cambiar drásticamente de entorno.

En minería de texto, es común ver que cada fila del DataFrame represente un documento (tweet, reseña, noticia, etc.), y se incluyan columnas con diferentes atributos. Por ejemplo:

- text_original: el texto tal cual se extrajo.
- texto_limpio: el texto luego de una limpieza con expresiones regulares.
- tokens: una lista de tokens (por ejemplo, generada con NLTK o spaCy).
- pos_tags: las etiquetas gramaticales correspondientes.
- entidades: una lista de entidades reconocidas, etc.



### 7.3 Minería de texto con DataFrames



Tras las primeras fases de recolección de datos, será necesario trabajar con ellos para limpiarlos, normalizarlos, etc. Finalmente, podremos utilizar esos datos para realizar diferentes análisis en función de nuestro caso de uso.

Supongamos que queremos limpiar el texto de caracteres no deseados (comas, puntos repetidos, secuencias de espacios, etc.) y normalizar a minúsculas. Previo a un análisis con NLTK o spaCy, conviene un DataFrame con una columna “texto_limpio”.

Por ejemplo, si queremos convertir todo a minúsculas y hacer cierta limpieza de ruido:



```lua
import re
import pandas as pd

textos_sucios = [
    "Texto con espacios al final  ",
    "Texto   con   múltiples   espacios   entre   palabras.",
    "Texto\tcon\tnuevos\tlíneas\ty tabulaciones.",
    "Texto.Con.Puntos.Separados.",
    "Texto..Con..Doble..Punto..",
    "Texto...Con...Triple...Punto...",
    "TEXTO EN MAYÚSCULAS",
    "Mix de MaYúScUlAs y minúsculas",
    "Texto con   muchos   espacios   y...puntos...",
    "Texto con puntuación al final.......",
    ".........Muchos puntos al principio",
    "Texto con puntos ... entre palabras",
    "Texto con \n saltos de linea \r y retornos de carro \r\n",
    "Texto con espacios \t \n \r combinados",
    "Texto con     muchos espacios seguidos"]

df_pandas = pd.DataFrame({
    "texto": textos_sucios
})

df_pandas["texto_limpio"] = df_pandas["texto"].apply(lambda txt: re.sub(r"\s+", " ", txt.lower()))

df_pandas["texto_limpio"] = df_pandas["texto_limpio"].apply(lambda txt: re.sub(r"\.{2,}", ".", txt))

df_pandas
```



```lua
import re
import polars as pl

textos_sucios = [
    "Texto con espacios al final  ",
    "Texto   con   múltiples   espacios   entre   palabras.",
    "Texto\tcon\tnuevos\tlíneas\ty tabulaciones.",
    "Texto.Con.Puntos.Separados.",
    "Texto..Con..Doble..Punto..",
    "Texto...Con...Triple...Punto...",
    "TEXTO EN MAYÚSCULAS",
    "Mix de MaYúScUlAs y minúsculas",
    "Texto con   muchos   espacios   y...puntos...",
    "Texto con puntuación al final.......",
    ".........Muchos puntos al principio",
    "Texto con puntos ... entre palabras",
    "Texto con \n saltos de linea \r y retornos de carro \r\n",
    "Texto con espacios \t \n \r combinados",
    "Texto con     muchos espacios seguidos"]

def clean_text(txt: str) -> str:
    txt_lower = txt.lower()
    txt_spaces = re.sub(r"\s+", " ", txt_lower)
    return re.sub(r"\.{2,}", ".", txt_spaces)

df_polars = pl.DataFrame({
    "texto": textos_sucios
})

df_polars = df_polars.with_columns(
    pl.col("texto").map_elements(clean_text, return_dtype=pl.String).alias("texto_limpio")
)

df_polars
```



Una vez que se ha normalizado el texto y limpiado, podemos pasar a las siguientes etapas del pipeline, tokenizar para posteriormente obtener tags o realizar los análisis necesarios:



```python
# Continuando el código anterior, ejemplo de pandas con nltk
import nltk

nltk.download('punkt')

def tokenize_nltk(text):
    return nltk.word_tokenize(text)

df_pandas["tokens"] = df_pandas["texto_limpio"].apply(tokenize_nltk)
df_pandas
```



```python
# Continuando el código anterior, ejemplo de polars con spaCy
import spacy

nlp_es = spacy.load("es_core_news_sm")

def tokenize_spacy(text: str):
    doc = nlp_es(text)
    return [token.text for token in doc if not token.is_punct]

df_polars = df_polars.with_columns(
    pl.col("texto_limpio").map_elements(tokenize_spacy, return_dtype=pl.List(pl.Utf8)).alias("tokens")
)

df_polars
```



En este punto, obtendremos un DataFrame con una nueva columna con los tokens correspondientes. Es en este momento cuando podemos comenzar a aplicar diferentes analíticas y transformaciones.

Un uso muy frecuente tras el preprocesamiento es agrupar o agregar estadísticas basadas en el texto. Por ejemplo:

- Calcular la longitud en tokens.
- Agrupar por categoría y obtener la media de tokens o la frecuencia de una palabra.



```ruby
# Continuando el código anterior
df_pandas["num_tokens"] = df_pandas["tokens"].apply(lambda tok_list: len(tok_list))

agg_results_pandas = df_pandas.groupby("categoria")["num_tokens"].mean()
print(agg_results_pandas)
```



![image](assets/cm6wk8gxv00u6356zv9kmnr3w-Imagen23.png)



```coffeescript
# Continuando el código anterior
df_polars = df_polars.with_columns(
    (pl.col("tokens").list.len()).alias("num_tokens")
)

agg_results_polars = df_polars.group_by("categoria").agg([
    pl.col("num_tokens").mean().alias("mean_tokens")
])
print(agg_results_polars)
```



![image](assets/cm6wk8wxf00us356z48vztcvn-Imagen24.png)



En este caso, observamos diferencias en los resultados. Esto se debe principalmente a cómo cada librería, NLTK y spaCy, identifican y procesan los textos. Esto hace que cada una proporcione un listado de tokens ligeramente diferente y, por ende, un resultado distinto.



### 7.4 Casos de uso en minería de texto



Como hemos visto previamente, tanto Pandas como Polars nos proporcionan funcionalidades que facilitan el análisis de texto. Gracias a la posibilidad de creación de columnas y aplicar tanto NLTK como spaCy, incluso combinado con re o regex, podemos crear flags, normalizar y limpiar datos, etc.

El orden o detalle de los pasos que se realicen dependerá del caso de uso. Por ejemplo, podemos considerar:



- **Análisis de redes sociales (ej. miles de tweets por hora)**  
  Se descarga vía API, se guardan en un CSV, se filtran retweets, se normaliza texto, y se extraen tokens/hashtags. Luego se computa la frecuencia de cada hashtag por franja horaria.
- **Clasificación de reseñas**  
  Cada fila es una reseña de un producto, con su puntaje y texto. Se limpian y tokenizan con spaCy, se genera una columna “lemmas”, y luego se vectoriza para un modelo de clasificación.
- **Detección de fraude en logs**  
  Se poseen registros de logs con cadenas de texto, se aplican expresiones regulares para extraer códigos de error y se combinan con la información del usuario. Se busca correlacionar patrones de error con la categoría “fraud.”
- **Investigación lingüística**  
  Se importan capítulos de libros, se etiquetan partes gramaticales con NLTK, y se extraen estadísticas de complejidad lingüística (ej. densidad de verbos, ratio adjetivos/sustantivos, etc.) usando “groupby autor”.



### 7.5 Enlaces de interés



> Documentación oficial de Pandas
>
> [Link](https://pandas.pydata.org/docs/)

> Documentación de Polars
>
> [Link](https://docs.pola.rs/)

> Comparativa de rendimientos
>
> [Link](https://pola.rs/posts/benchmarks/)



## 8. Visualización De Texto: Wordclouds En Python



### 8.1 Introducción



![image](assets/cm6wkf3is00yx356z17ui66tp-stock-image.jpg)



En las etapas previas de esta unidad, hemos visto cómo limpiar, tokenizar y procesar el texto, y cómo manejarlo con herramientas como Pandas, Polars, NLTK o spaCy. Sin embargo, una pregunta clave al final de un pipeline de minería de texto es: ¿cómo comunicar o visualizar los resultados de manera efectiva?

Uno de los métodos más populares y atractivos de visualización de texto es la wordcloud (nube de palabras). Una wordcloud es una representación gráfica de las palabras más frecuentes en un corpus o documento; cada palabra se muestra con un tamaño proporcional a su frecuencia o relevancia. Esta técnica, si bien no siempre provee un análisis profundo o cuantitativo, resulta sumamente útil para:

- Descubrir rápidamente qué palabras destacan en un conjunto de texto.
- Ilustrar de forma visual y llamativa la temática central de un corpus.
- Realizar presentaciones o dashboards en donde un vistazo a la nube de palabras ayude a los usuarios a identificar patrones, palabras clave o temáticas.



### 8.2 Uso de wordclouds



La forma más común de generar wordclouds en Python es mediante la librería wordcloud. Para instalarla simplemente deberemos ejecutar el siguiente comando:



```bat
pip install wordcloud
```



Entre sus funcionalidades principales, destacan:

- width, height: dimensiones de la imagen resultante.
- background_color: color de fondo (por defecto "white").
- max_words: número máximo de palabras que aparecerán.
- mask: una matriz (array) en la que se definen zonas donde “pintar” texto (permite formas personalizadas).
- stopwords: conjunto de palabras a ignorar.
- colormap: paleta de colores (ej. "viridis", "plasma", "rainbow", "Blues", etc.).
- max_font_size: tamaño máximo de letra.

El flujo típico es:

- Preparar un diccionario {“palabra”: frecuencia} o un string con todo el texto preprocesado.
- Instanciar un objeto WordCloud(...).
- Generar la nube de palabras con .generate(...) (en caso de usar string) o .generate_from_frequencies(...) (en caso de usar un diccionario).
- Mostrar con matplotlib o guardar en un archivo con .to_file("mi_wordcloud.png").

Supongamos que, tras la fase de limpieza y tokenización, hemos concatenado todas las palabras en un único string, por ejemplo, crear un string con los tokens obtenidos tras usar NLTK o spaCy.

Podemos generar un wordcloud de la siguiente manera:



```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = """
Estoy estudiando en la U-Tad. Dentro de la universidad estudio Python.
Python es un lenguaje de programación muy potente y versátil.
Gracias a Python puedo hacer análisis de datos y visualizaciones.
Además, aprendo a usar librerías como Pandas, Polars, NLTk y spaCy.
"""

wordcloud = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=100
)

# Generamos la nube desde un string
wordcloud.generate(texto)

# Visualizar
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
```



Esto nos mostrará una imagen que nos permitirá ver de manera rápida las palabras más repetidas:



![image](assets/cm6wkjo7f013h356z5p69din5-Imagen25.jpg)



Además de con un simple string, se puede utilizar wordclouds con diccionarios que posean por ejemplo la frecuencia de repetición. Esto nos permitiría crear un dataframe donde una columna fuese el token, otra el número de veces que aparece y gracias a esto crear un wordcloud de la siguiente forma:



```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

freqs = {
    "python": 10,
    "datos": 8,
    "analisis": 5,
    "nlp": 4,
    "machine": 3,
    "learning": 3,
    "visualizacion": 2,
    "text": 6
}

wordcloud_freq = WordCloud(
    width=800,
    height=600,
    background_color="white"
).generate_from_frequencies(freqs)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud_freq, interpolation="bilinear")
plt.axis("off")
plt.show()
```



### 8.3 Uso con Pandas y Polars



Dado que en minería de texto solemos tener un DataFrame con una columna de tokens, podemos procesar su frecuencia de la siguiente manera:



```python
import pandas as pd
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nlp = spacy.load("es_core_news_sm")
texto = """Estoy estudiando en la U-Tad. Dentro de la universidad estudio Python. Python es un lenguaje de programación muy potente y versátil. Gracias a Python puedo hacer análisis de datos y visualizaciones. Además, aprendo a usar librerías como Pandas, Polars, NLTk y spaCy."""
doc = nlp(texto)

df_pandas = pd.DataFrame({
    "token": [token.text for token in doc]
})

freq_counter = Counter(df_pandas["token"])

wordcloud_data = dict(freq_counter.most_common(100))  # top 100 palabras

wordcloud_pandas = WordCloud(width=800, height=600, background_color="white").generate_from_frequencies(wordcloud_data)
wordcloud_pandas.generate_from_frequencies(wordcloud_data)

plt.figure(figsize=(10,6))
plt.imshow(wordcloud_pandas, interpolation="bilinear")
plt.axis("off")
plt.show()
```



```python
import polars as pl
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nlp = spacy.load("es_core_news_sm")
texto = """Estoy estudiando en la U-Tad. Dentro de la universidad estudio Python. Python es un lenguaje de programación muy potente y versátil. Gracias a Python puedo hacer análisis de datos y visualizaciones. Además, aprendo a usar librerías como Pandas, Polars, NLTk y spaCy."""
doc = nlp(texto)

df_polars = pl.DataFrame({
    "token": [token.text for token in doc]
})

freq_counter = Counter(df_polars["token"])

wordcloud_data = dict(freq_counter.most_common(100))  # top 100 palabras

wordcloud_polars = WordCloud(width=800, height=600, background_color="white").generate_from_frequencies(wordcloud_data)
wordcloud_polars.generate_from_frequencies(wordcloud_data)

plt.figure(figsize=(10,6))
plt.imshow(wordcloud_polars, interpolation="bilinear")
plt.axis("off")
plt.show()
```



### 8.4 Personalización



Aunque la librería wordcloud incluye stopwords en inglés por defecto, probablemente deseemos agregar un conjunto propio de palabras a ignorar, especialmente si trabajamos en español u otro idioma, o tenemos nombres de usuario irrelevantes:



```python
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

texto = """
Estoy estudiando en la U-Tad. Dentro de la universidad estudio Python.
Python es un lenguaje de programación muy potente y versátil.
Gracias a Python puedo hacer análisis de datos y visualizaciones.
Además, aprendo a usar librerías como Pandas, Polars, NLTk y spaCy.
"""
custom_stops = set(["datos", "ciencia", "etc", "python"])  # palabras que no queremos mostrar
all_stops = STOPWORDS.union(custom_stops)

wc_custom = WordCloud(
    stopwords=all_stops,
    background_color="white",
    max_words=200
)
wc_custom.generate(texto)

# Visualizar
plt.figure(figsize=(10, 8))
plt.imshow(wc_custom, interpolation="bilinear")
plt.axis("off")
plt.show()
```



De esta manera, no mostramos en la imagen generada las palabras definidas, como podemos ver python ha desaparecido:



![image](assets/cm6wknmgq0191356ziaebc9qn-Imagen26.jpg)



Además, también podemos modificar las formas de la imagen mediante máscaras o los colores. Esto se realiza mediante el uso de:

- mode="RGBA" y background_color=None permiten que la parte transparente no se pinte.
- mask=mask_img define el contorno dentro del cual se acomodan las palabras.
- colormap="viridis" para usar paletas predefinidas o personalizadas.

En el video a continuación, veremos un pipeline completo desde la carga del archivo hasta la representación en wordclouds:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651980_1/scormcontent/assets/INSD_BAIN_U2_Video5.mp4?v=1)



## 9. Conclusiones



### 9.1 Conclusiones de la unidad



A lo largo de esta unidad, nos adentramos en la minería de texto con Python y sus herramientas, explorando cada parte del proceso: desde la naturaleza misma del texto y su complejidad, hasta las técnicas de procesamiento avanzadas y la visualización final mediante wordclouds.

Iniciamos revisando los aspectos básicos del texto, comprendiendo cómo la longitud, la granularidad y la ambigüedad lingüística influyen en el análisis y en la selección de técnicas apropiadas. Seguidamente, abordamos la codificación de caracteres, destacando la relevancia de Unicode y UTF-8 para unificar alfabetos y evitar problemas de visualización (\“Ã±\” en lugar de \“ñ\”). En esa etapa, aprendimos a abrir y guardar archivos con la codificación correcta, así como a convertir entre formatos (\“latin-1\” a \“utf-8\”)

Al introducirnos en las expresiones regulares, constatamos lo crucial que resulta limpiarlas y modelar el texto. Con el módulo re y la librería regex, se mostró cómo buscar, filtrar y transformar patrones, así como manejar escenarios más complejos (lookbehind variable, recursividad, soporte Unicode avanzado). El dominio de estas técnicas acelera la eliminación de ruido (URLs, menciones, símbolos) y la extracción de secuencias relevantes (hashtags, números de serie, etc.).

En seguida, profundizamos en las librerías de procesamiento de lenguaje natural: NLTK y spaCy. Con NLTK, comprendimos la amplitud de sus herramientas académicas, su variedad de corpus y la facilidad para prototipar con tokenización, etiquetado gramatical (PoS-tagging), lematización y reconocimiento de entidades rudimentario. Por otro lado, spaCy nos ofreció un pipeline optimizado y modelos preentrenados para diferentes idiomas, capaces de realizar rápidamente etiquetado y NER de forma robusta. Esta comparación resaltó cómo la elección de librería depende del volumen de datos, la precisión deseada, el idioma y el escenario de producción o investigación.

El enfoque con Pandas y Polars demostró la conveniencia de almacenar y manipular datos textuales en DataFrames, tanto para filtrar documentos como para generar columnas de tokens, longitudes, entidades o frecuencias. Ambos se integran sin problemas con re/regex, NLTK, spaCy o cualquier otra librería de análisis.

Para culminar, exploramos la visualización de texto con wordclouds. Estas nubes de palabras sintetizan de manera rápida y atractiva la presencia relativa de términos en un corpus. Partimos del conteo de tokens (con NLTK o spaCy), elaboramos diccionarios de frecuencias y luego generamos wordclouds con la librería wordcloud. Se mostraron opciones para personalizar la apariencia: colores, máscaras (formas), filtrado de stopwords. Aunque es un recurso principalmente ilustrativo y no brinda información contextual profunda, la wordcloud resulta muy efectiva para presentaciones, resúmenes o análisis exploratorios.

En conjunto, la unidad ilustró un pipeline integral de minería de texto:

- Limpieza y normalización (codificación, expresiones regulares, eliminación de ruido).
- Procesamiento lingüístico (tokenización, etiquetado PoS, lematización, NER) con NLTK o spaCy.
- Manipulación tabular (Pandas o Polars) para agrupar y agregar.
- Visualización final (wordclouds) para comunicar hallazgos de forma clara y llamativa.

Esta serie de pasos permite abordar múltiples aplicaciones: análisis de sentimiento, clasificación de documentos, extracción de entidades en grandes volúmenes de texto, creación de visualizaciones dinámicas o resúmenes. Con el conocimiento adquirido, se sientan las bases para construir sistemas de NLP más complejos, incorporando eventualmente técnicas de aprendizaje automático, modelos basados en embeddings (Word2Vec, BERT) o herramientas de big data para corpus de enorme escala.



Nota final:

Practicar con diferentes corpus (tweets, reseñas, artículos) y aplicar todo el pipeline, desde la limpieza hasta la wordcloud.

Ajustar la selección de librerías (re vs regex, NLTK vs spaCy, Pandas vs Polars) según las necesidades de cada proyecto.

Explorar personalizaciones de wordclouds y la integración con entornos de visualización más amplios (Streamlit) si se requiere un producto final interactivo.

Mantener un enfoque de experimentación constante, probando la eficiencia de cada paso (tokenización, etiquetado) y comparando rendimientos.

Con estas herramientas y metodologías, los estudiantes y profesionales están preparados para enfrentar proyectos de minería de texto en múltiples dominios, aprovechando el rico ecosistema de Python para obtener conocimiento valioso a partir de datos textuales.
