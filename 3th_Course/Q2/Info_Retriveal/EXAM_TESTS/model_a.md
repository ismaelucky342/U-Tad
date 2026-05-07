# EXAMEN MODELO A: Minería de Texto e Información Retrieval

## Instrucciones
Este examen contiene 50 preguntas seleccionadas de los 5 temas principales del curso. Incluye los conceptos fundamentales e imprescindibles de cada unidad. Selecciona la respuesta correcta para cada pregunta.

---

## 1. ECOSISTEMA PYTHON (Preguntas 1-10)

**1.** ¿Cuál es el comando para verificar la versión de Python instalada?
 A) python --check
 B) python3 --version
 C) python -v
 D) python --info

**2.** ¿Qué es un entorno virtual?
 A) Un servidor remoto
 B) Un aislamiento de dependencias del proyecto
 C) Una máquina virtual
 D) Un repositorio de código

**3.** ¿Cuál es el comando para instalar una librería con pip?
 A) pip add nombre_libreria
 B) pip install nombre_libreria
 C) pip import nombre_libreria
 D) pip load nombre_libreria

**4.** ¿Para qué sirve requirements.txt?
 A) Documentar el proyecto
 B) Listar las dependencias del proyecto
 C) Almacenar variables de entorno
 D) Configurar el servidor

**5.** ¿Qué es un diccionario en Python?
 A) Una lista de palabras
 B) Una estructura que almacena pares clave-valor
 C) Un tipo de comentario
 D) Una función especial

**6.** ¿Cuál es el método constructor en POO de Python?
 A) constructor()
 B) __init__()
 C) create()
 D) init()

**7.** ¿Cuál es la palabra clave para manejar excepciones?
 A) catch
 B) handle
 C) try
 D) error

**8.** ¿Cuándo se ejecuta el bloque finally?
 A) Solo si hay error
 B) Solo si no hay error
 C) Siempre
 D) Nunca

**9.** ¿Cuál es la ventaja de JSON frente a CSV?
 A) Ocupa menos espacio
 B) Es más rápido
 C) Puede representar estructuras complejas y anidadas
 D) Es más antiguo

**10.** ¿Cuál es una ventaja de Parquet?
 A) Almacenamiento basado en columnas
 B) Compresión eficiente
 C) Mejora el rendimiento de lectura
 D) Todas las anteriores

---

## 2. MINERÍA DE TEXTO BÁSICA (Preguntas 11-20)

**11.** ¿Qué se entiende por minería de texto?
 A) Solo eliminar palabras duplicadas
 B) Extraer información o patrones de documentos y textos
 C) Traducir textos automáticamente
 D) Crear diccionarios de palabras

**12.** ¿Qué es tokenizar un texto?
 A) Traducirlo a otro idioma
 B) Dividirlo en pequeñas unidades analizables
 C) Eliminar palabras vacías
 D) Convertirlo a minúsculas

**13.** ¿Qué son las stopwords?
 A) Palabras que aparecen al inicio de un documento
 B) Palabras incorrectamente escritas
 C) Palabras frecuentes que no aportan significado
 D) Palabras que determinan el idioma

**14.** ¿Qué significa UTF-8?
 A) Unicode Transformation Format - 8 bits
 B) Universal Text Format 8
 C) Unit Text File 8
 D) Unified Trading Format 8

**15.** ¿Cuántos bytes puede usar UTF-8 para representar un carácter?
 A) Siempre 1 byte
 B) Siempre 2 bytes
 C) Siempre 4 bytes
 D) Entre 1 y 4 bytes (variable)

**16.** ¿Qué significa "\d" en una expresión regular?
 A) Cualquier carácter
 B) Espacios en blanco
 C) Dígitos (0-9)
 D) Letras

**17.** ¿Cuál es la función de Python para encontrar la primera aparición de un patrón?
 A) re.match()
 B) re.search()
 C) re.findall()
 D) re.compile()

**18.** ¿Cuál es la función para reemplazar todas las apariciones de un patrón?
 A) re.match()
 B) re.findall()
 C) re.sub()
 D) re.replace()

**19.** ¿Cuál es el comando para instalar la librería NLTK?
 A) pip install nltk
 B) pip install text-mining
 C) pip install natural-language
 D) pip install nlp

**20.** ¿Qué es spaCy?
 A) Un espacio en blanco
 B) Una librería de NLP moderna y rápida
 C) Un protocolo de red
 D) Una base de datos

---

## 3. FUENTES DE DATOS Y SCRAPING (Preguntas 21-30)

**21.** ¿Qué significa API?
 A) Advanced Programming Interface
 B) Application Programming Interface
 C) Advanced Process Integration
 D) Application Process Interaction

**22.** ¿Cuál es el formato típico de respuesta de las APIs?
 A) XML
 B) CSV
 C) JSON
 D) YAML

**23.** ¿Qué es un Bearer Token?
 A) Una contraseña simple
 B) Un token usado en OAuth para autenticar peticiones
 C) Un nombre de usuario
 D) Una clave pública

**24.** ¿Cuál es la librería oficial de Python para acceder a la API de Reddit?
 A) redditapi
 B) PRAW (Python Reddit API Wrapper)
 C) reddit-py
 D) reddit

**25.** ¿Qué es Web Scraping?
 A) Limpiar navegadores web
 B) Técnica para extraer información de páginas web
 C) Un lenguaje de programación
 D) Un servidor web

**26.** ¿Cuál es la diferencia entre sitios estáticos y dinámicos?
 A) No hay diferencia
 B) Los estáticos tienen HTML completo al responder; los dinámicos generan contenido con JavaScript
 C) Los dinámicos no tienen CSS
 D) Los estáticos requieren base de datos

**27.** ¿Para qué se usa BeautifulSoup?
 A) Preparar soup (sopa)
 B) Parsear y navegar documentos HTML
 C) Compilar código Python
 D) Crear bases de datos

**28.** ¿Para qué se usa Selenium?
 A) Un tipo de mineral
 B) Automatizar navegadores web para sitios dinámicos
 C) Crear servidores web
 D) Compilar código

**29.** ¿Cómo se realiza un merge de dos DataFrames en Pandas?
 A) df1.join(df2)
 B) pd.merge(df1, df2, on='key')
 C) df1.combine(df2)
 D) merge_dataframes(df1, df2)

**30.** ¿Cuál es una ventaja de Polars respecto a Pandas?
 A) Tiene más funciones
 B) Es más rápido y permite lazy evaluation
 C) Ocupa menos código
 D) Es más antiguo

---

## 4. MODELIZACIÓN Y ANÁLISIS (Preguntas 31-40)

**31.** ¿Qué significa LDA?
 A) Linear Discriminant Analysis
 B) Latent Dirichlet Allocation
 C) Large Data Architecture
 D) Learning Distribution Algorithm

**32.** ¿Cuál es el objetivo principal del LDA?
 A) Clasificar documentos por autor
 B) Descubrir automáticamente temas latentes en documentos
 C) Traducir textos
 D) Comprimir archivos

**33.** ¿Cuál es la librería de Python para implementar LDA?
 A) nltk
 B) gensim
 C) sklearn
 D) spacy

**34.** ¿Qué es análisis de sentimiento?
 A) Detectar emociones en texto
 B) Determinar si un texto es positivo, negativo o neutral
 C) Contar palabras
 D) Traducir textos

**35.** ¿Cuáles son los tres sentimientos básicos?
 A) Bueno, malo, indiferente
 B) Feliz, triste, asustado
 C) Positivo, negativo, neutral
 D) Amor, odio, miedo

**36.** ¿Qué es TextBlob?
 A) Un tipo de base de datos
 B) Una librería de Python para tareas NLP simples
 C) Un navegador web
 D) Un servidor

**37.** ¿Qué es POS tagging?
 A) Etiquetar mensajes de correo
 B) Anotar cada palabra con su parte del discurso
 C) Crear publicaciones
 D) Un tipo de archivo

**38.** ¿Qué es lematización?
 A) Contar palabras
 B) Reducir palabras a su forma base/lema
 C) Eliminar duplicados
 D) Traducir

**39.** ¿Qué es parsing en minería de texto?
 A) Eliminar palabras comunes
 B) Analizar la estructura gramatical de un texto
 C) Traducir documentos
 D) Contar palabras

**40.** ¿Cuál es el objetivo de la tokenización?
 A) Traducir texto
 B) Dividir texto en componentes análizables
 C) Comprimir datos
 D) Encriptar contenido

---

## 5. ANÁLISIS DE REDES SOCIALES (Preguntas 41-50)

**41.** ¿Qué es un grafo?
 A) Una función matemática
 B) Un conjunto de nodos conectados por aristas
 C) Un tipo de base de datos
 D) Un algoritmo de búsqueda

**42.** ¿Qué es la teoría de grafos?
 A) Estudio de representaciones gráficas
 B) Estudio matemático de estructuras de redes
 C) Programación con gráficos
 D) Visualización de datos

**43.** ¿Qué es un nodo en una red?
 A) Una conexión
 B) Una entidad o punto en la red
 C) Un archivo
 D) Un servidor

**44.** ¿Qué es una arista o edge en una red?
 A) Un nodo importante
 B) Una conexión entre dos nodos
 C) Un atributo de datos
 D) Una etiqueta

**45.** ¿Cuál es la librería principal para análisis de redes en Python?
 A) netanalysis
 B) NetworkX
 C) graph-tools
 D) network-py

**46.** ¿Qué es el degree (grado) de un nodo?
 A) Su importancia en la red
 B) El número de conexiones que tiene
 C) Su color en la visualización
 D) Su edad

**47.** ¿Qué es centralidad?
 A) El centro geométrico de una red
 B) Una medida de importancia o influencia de un nodo
 C) Un algoritmo de compresión
 D) Un tipo de conexión

**48.** ¿Qué es community detection?
 A) Encontrar comunidades de desarrolladores
 B) Identificar grupos densos de nodos en una red
 C) Crear comunidades en línea
 D) Vigilancia de redes sociales

**49.** ¿Cuáles son las aplicaciones principales de análisis de redes sociales?
 A) Solo visualización
 B) Detección de fraude, influencers, propagación de información
 C) Traducción de textos
 D) Almacenamiento de datos

**50.** ¿Qué es el algoritmo de Louvain?
 A) Un algoritmo de ordenamiento
 B) Un algoritmo para detectar comunidades en redes
 C) Un protocolo de red
 D) Un servidor web

---

## SOLUCIONARIO

| Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta |
|----------|-----------|----------|-----------|----------|-----------|
| 1 | B | 18 | C | 35 | C |
| 2 | B | 19 | A | 36 | B |
| 3 | B | 20 | B | 37 | B |
| 4 | B | 21 | B | 38 | B |
| 5 | B | 22 | C | 39 | B |
| 6 | B | 23 | B | 40 | B |
| 7 | C | 24 | B | 41 | B |
| 8 | C | 25 | B | 42 | B |
| 9 | C | 26 | B | 43 | B |
| 10 | D | 27 | B | 44 | B |
| 11 | B | 28 | B | 45 | B |
| 12 | B | 29 | B | 46 | B |
| 13 | C | 30 | B | 47 | B |
| 14 | A | 31 | B | 48 | B |
| 15 | D | 32 | B | 49 | B |
| 16 | C | 33 | B | 50 | B |
| 17 | B | 34 | B |  |  |

---

## TEMAS CLAVE POR PREGUNTA

| Bloque | Tema | Preguntas Clave |
|--------|------|-----------------|
| Unidad 1: Python Ecosystem | Instalación, entornos, pip, estructuras datos, POO, excepciones, formatos | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| Unidad 2: Text Mining | Tokenización, stopwords, UTF-8, regex, NLTK, spaCy | 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 |
| Unidad 3: Data Sources | APIs, web scraping, BeautifulSoup, Selenium, Pandas, Polars | 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 |
| Unidad 4: Modeling & Analysis | LDA, sentiment analysis, TextBlob, POS tagging, parsing, lematización | 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 |
| Unidad 5: Social Networks | Grafos, teoría de grafos, nodos, aristas, NetworkX, centralidad, comunidades | 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 |
