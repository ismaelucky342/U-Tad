# Test Unidad 2: Minería de Texto con Python

## Instrucciones
Este test contiene aproximadamente 100 preguntas sobre los contenidos de la Unidad 2. Selecciona la respuesta correcta para cada pregunta. Las preguntas pueden tener 4 o 5 opciones de respuesta.

---

## 1. Aspectos Básicos del Texto

**1.** ¿Qué se entiende por minería de texto?
 A) Solo eliminar palabras duplicadas
 B) Extraer información o patrones de documentos y textos
 C) Traducir textos automáticamente
 D) Crear diccionarios de palabras

**2.** ¿Cuál es la diferencia principal entre trabajar con datos numéricos y textuales?
 A) No hay diferencia
 B) Los datos textuales son números convertidos
 C) Los datos textuales requieren procesamiento lingüístico especial
 D) Los datos numéricos no se pueden procesar

**3.** ¿Qué es un token en minería de texto?
 A) Un archivo de texto
 B) Una unidad pequeña del texto (palabra, símbolo, etc.)
 C) Un diccionario de palabras
 D) Una codificación de caracteres

**4.** ¿Qué significa "tokenizar" un texto?
 A) Traducirlo a otro idioma
 B) Dividirlo en pequeñas unidades analizables
 C) Eliminar palabras vacías
 D) Convertirlo a minúsculas

**5.** ¿Qué son las stopwords?
 A) Palabras que aparecen al inicio de un documento
 B) Palabras incorrectamente escritas
 C) Palabras frecuentes que no aportan significado (artículos, preposiciones)
 D) Palabras que determinan el idioma

**6.** ¿Cuál es el objetivo de la normalización en minería de texto?
 A) Aumentar el número de palabras
 B) Aplicar estándares para análisis consistentes (minúsculas, eliminar tildes, etc.)
 C) Eliminar todos los números
 D) Solo eliminar puntuación

**7.** ¿Cuál es el primer paso del pipeline de minería de texto?
 A) Tokenización
 B) Modelado
 C) Recolección de datos
 D) Análisis

**8.** Si un texto contiene "Gato", "gato" y "GATO", después de normalización cuántas versiones diferentes habrá?
 A) 3
 B) 2
 C) 1
 D) 0

---

## 2. Codificación de Caracteres

**9.** ¿Qué significa ASCII?
 A) Advanced System Code Interface
 B) American Standard Code for Information Interchange
 C) Automatic Stream Coding Interface
 D) Application System Conversion Integration

**10.** ¿Cuántos bits utiliza ASCII estándar?
 A) 4 bits
 B) 8 bits
 C) 7 bits
 D) 16 bits

**11.** ¿Cuántos caracteres puede representar ASCII estándar?
 A) 64
 B) 128
 C) 256
 D) 512

**12.** ¿Cuál es el principal problema de ASCII para idiomas no ingleses?
 A) Es demasiado rápido
 B) No puede representar caracteres especiales como "ñ" o acentos
 C) Solo funciona con números
 D) Ocupa demasiado espacio

**13.** ¿Qué es Unicode?
 A) Un sistema de compresión de texto
 B) Un formato para emails
 C) Un estándar que asigna código único a cada carácter de prácticamente todos los idiomas
 D) Un protocolo de red

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

**16.** ¿Por qué UTF-8 es retrocompatible con ASCII?
 A) Porque es más antiguo
 B) Porque los 128 primeros caracteres coinciden exactamente con ASCII
 C) Porque USA lo requiere
 D) Porque es un estándar internacional

**17.** ¿Cuál es el estándar de codificación por defecto en Python 3 para leer archivos?
 A) ASCII
 B) ISO-8859-1
 C) UTF-8
 D) Unicode

**18.** En Python, ¿cómo se especifica la codificación al abrir un archivo?
 A) open("archivo.txt", "r")
 B) open("archivo.txt", "r", encoding="utf-8")
 C) open("archivo.txt", UTF-8)
 D) open("archivo.txt", "utf8")

**19.** Si lees un archivo con codificación UTF-8 usando encoding="latin-1", ¿qué puede pasar?
 A) Funcionará perfectamente
 B) Mostrará caracteres incorrectos o ilegibles
 C) Se perderán todos los datos
 D) Python lo convertirá automáticamente

**20.** ¿Qué librería de Python puede detectar el idioma de un texto?
 A) re
 B) langdetect
 C) nltk
 D) pandas

---

## 3. Expresiones Regulares - Conceptos Básicos

**21.** ¿Qué hace el símbolo "." en una expresión regular?
 A) Marca el final de la cadena
 B) Coincide con cualquier carácter (excepto salto de línea)
 C) Representa un punto literal
 D) Separa patrones

**22.** ¿Qué hace el símbolo "^" en una expresión regular?
 A) Marca el inicio de la cadena
 B) Marca el final de la cadena
 C) Representa elevación
 D) Niega el patrón

**23.** ¿Qué hace el símbolo "$" en una expresión regular?
 A) Marca el inicio de la cadena
 B) Marca el final de la cadena
 C) Representa variables
 D) Multiplica el patrón

**24.** ¿Qué significa "+" en una expresión regular?
 A) Suma
 B) Una o más repeticiones del elemento anterior
 C) Exactamente dos repeticiones
 D) Cero repeticiones

**25.** ¿Qué significa "*" en una expresiones regular?
 A) Cero o más repeticiones del elemento anterior
 B) Una o más repeticiones
 C) Multiplicación
 D) Fin de patrón

**26.** ¿Qué significa "?" en una expresión regular?
 A) Cero o una repetición (opcional)
 B) Una o más repeticiones
 C) Pregunta al usuario
 D) Cualquier carácter

**27.** ¿Qué significa "[A-Za-z0-9]" en una expresión regular?
 A) Cualquier carácter
 B) Solo números
 C) Letras mayúsculas, minúsculas y dígitos
 D) Cualquier símbolo especial

**28.** ¿Qué significa "\d" en una expresión regular?
 A) Cualquier carácter
 B) Espacios en blanco
 C) Dígitos (0-9)
 D) Letras

**29.** ¿Qué significa "\w" en una expresión regular?
 A) Espacios en blanco
 B) Caracteres de palabra (letras, dígitos, subrayado)
 C) Cualquier carácter especial
 D) Solo letras

**30.** ¿Qué significa "\s" en una expresión regular?
 A) Caracteres especiales
 B) Espacios en blanco
 C) Dígitos
 D) Sustantivos

**31.** ¿Qué significa "{2,5}" en una expresión regular?
 A) Entre 2 y 5 repeticiones
 B) Exactamente 2 repeticiones
 C) 5 repeticiones
 D) Ninguno de los anteriores

**32.** Para encontrar patrones que comiencen con "#" seguido de palabra, ¿cuál sería la expresión?
 A) #word
 B) #\w+
 C) #.*
 D) #[a-z]

---

## 4. Librería re - Funciones Básicas

**33.** ¿Cuál es el comando correcto para buscar un patrón al inicio de una cadena?
 A) re.search()
 B) re.match()
 C) re.findall()
 D) re.finditer()

**34.** ¿Cuál es la función para encontrar la primera aparición de un patrón en cualquier posición?
 A) re.match()
 B) re.search()
 C) re.findall()
 D) re.compile()

**35.** ¿Qué función devuelve una lista con TODAS las apariciones del patrón?
 A) re.match()
 B) re.search()
 C) re.findall()
 D) re.sub()

**36.** ¿Cuál es la función para reemplazar todas las apariciones de un patrón?
 A) re.match()
 B) re.findall()
 C) re.sub()
 D) re.replace()

**37.** ¿Cuál es la función para dividir una cadena usando un patrón como delimitador?
 A) re.split()
 B) re.divide()
 C) re.cut()
 D) re.slice()

**38.** ¿Qué devuelve re.match() si NO hay coincidencia?
 A) False
 B) ""
 C) None
 D) Error

**39.** ¿Cuál es el beneficio de usar re.compile()?
 A) Compila el código Python
 B) Reutilizar el patrón compilado múltiples veces
 C) Aumenta la velocidad automáticamente
 D) Convierte regex a re

**40.** Si quiero extraer emails de un texto, ¿cuál es la función más adecuada?
 A) re.match()
 B) re.search()
 C) re.findall()
 D) re.compile()

---

## 5. Expresiones Regulares - Casos Prácticos

**41.** Para validar un email simple, ¿cuál sería el patrón aproximado?
 A) \w+@\w+
 B) [A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}
 C) @
 D) [a-z]@[a-z]

**42.** Para extraer números de teléfono en formato "123-456-7890", ¿cuál sería el patrón?
 A) \d+
 B) \d{3}-\d{3}-\d{4}
 C) [0-9]
 D) \d-\d-\d

**43.** Para encontrar URLs que comiencen con "http" o "https", ¿cuál sería el patrón?
 A) http
 B) https?
 C) http.*
 D) http|https

**44.** Para extraer hashtags (#palabra), ¿cuál es el patrón?
 A) #
 B) #\w+
 C) #.*
 D) #[a-z]

**45.** Para eliminar múltiples espacios en blanco, ¿qué función se usa?
 A) re.match(r' {2,}', ' ', texto)
 B) re.sub(r' {2,}', ' ', texto)
 C) re.findall(r' ', texto)
 D) re.split(r' ', texto)

**46.** Para extraer fechas en formato "DD-MM-YYYY", ¿cuál sería el patrón?
 A) \d{2}-\d{2}-\d{4}
 B) \d+-\d+-\d+
 C) [0-9]{2}-[0-9]{2}-[0-9]{4}
 D) Las opciones A y C son correctas

---

## 6. Librería regex vs re

**47.** ¿Cuál es la principal limitación de "re" que "regex" soluciona?
 A) re es más lento
 B) re no puede compilar patrones
 C) regex permite lookbehind de longitud variable
 D) re no funciona con Unicode

**48.** ¿Cuál es el comando para instalar regex?
 A) pip install re
 B) pip install regex
 C) python -m install regex
 D) apt-get install regex

**49.** ¿Qué es un "lookbehind"?
 A) Mirar hacia adelante en el texto
 B) Mirar hacia atrás en el texto sin incluir en coincidencia
 C) Buscar en archivos anteriores
 D) Revisar la sintaxis

**50.** ¿Cuál es un caso donde regex es preferible a re?
 A) Buscar números simples
 B) Validar emails básicos
 C) Detectar emojis con propiedades Unicode específicas
 D) Partir strings por separador

**51.** Si necesito trabajar con emojis, ¿cuál librería es más recomendable?
 A) re
 B) regex
 C) nltk
 D) spacy

**52.** ¿Qué soporta regex que re no soporta fácilmente?
 A) Patrones simples
 B) Expresiones recursivas
 C) División de textos
 D) Compilación de patrones

---

## 7. NLTK - Tokenización

**53.** ¿Cuál es el comando para instalar NLTK?
 A) pip install nltk
 B) pip install natural-language-toolkit
 C) npm install nltk
 D) apt-get install nltk

**54.** ¿Cuál es la función de NLTK para descargar recursos?
 A) nltk.install()
 B) nltk.download()
 C) nltk.get()
 D) nltk.fetch()

**55.** ¿Cuál es la función más común de NLTK para tokenizar texto?
 A) nltk.tokenize()
 B) nltk.word_tokenize()
 C) nltk.split()
 D) nltk.segment()

**56.** Si ejecuto `nltk.download('punkt')`, ¿qué estoy descargando?
 A) Un diccionario completo
 B) Modelos de tokenización
 C) Todas las stopwords
 D) Un modelo de sentimientos

**57.** En NLTK, si tokenizo "¡Hola! ¿Cómo estás?", ¿la puntuación aparecerá como tokens separados?
 A) No, se elimina automáticamente
 B) Sí, como tokens separados
 C) Solo algunos signos
 D) Depende del idioma

**58.** ¿Cuál es una limitación de NLTK para idiomas no ingleses?
 A) No puede tokenizar
 B) El soporte no es tan avanzado como para inglés
 C) No tiene diccionarios
 D) Es completamente incompatible

---

## 8. NLTK - POS Tagging y Lematización

**59.** ¿Qué significa POS tagging?
 A) Posición de la oración
 B) Part of Speech tagging (etiquetado de categorías gramaticales)
 C) Procesamiento de oraciones
 D) Puntuación original de sentencias

**60.** La función para POS tagging en NLTK es:
 A) nltk.tag()
 B) nltk.pos_tag()
 C) nltk.grammar_tag()
 D) nltk.label()

**61.** En NLTK, "NNP" típicamente significa:
 A) Sustantivo común
 B) Nombre propio
 C) Negación
 D) Número

**62.** ¿Cuál es la diferencia entre stemming y lematización?
 A) No hay diferencia
 B) Stemming corta palabras sin diccionario, lematización usa diccionarios (WordNet)
 C) Lematización es más rápida
 D) Stemming usa diccionarios

**63.** El PorterStemmer en NLTK es para:
 A) Español
 B) Francés
 C) Inglés
 D) Todos los idiomas

**64.** Para lematización en inglés en NLTK se usa:
 A) PorterStemmer
 B) WordNetLemmatizer
 C) Lemmatizer
 D) LemmatizerEn

**65.** Si lematizo "playing", "played", "plays" en inglés, ¿cuál será el resultado?
 A) Todos se convierten a "play"
 B) Todos se convierten a "plai"
 C) Se mantienen igual
 D) Se convierten a "player"

---

## 9. NLTK - Stopwords y análisis

**66.** ¿Qué es una stopword en NLTK?
 A) Palabra que aparece primero
 B) Palabra incorrectamente escrita
 C) Palabra frecuente sin significado sustancial
 D) Palabra que termina una oración

**67.** Para obtener stopwords en inglés con NLTK:
 A) nltk.stopwords()
 B) nltk.stopwords.words('english')
 C) nltk.stop_words('english')
 D) nltk.get_stopwords()

**68.** ¿Qué debe descargarse para usar stopwords en NLTK?
 A) 'tokenizers'
 B) 'stopwords'
 C) 'corpus'
 D) 'punkt'

---
## 10. spaCy - Instalación y Modelos

**69.** ¿Cuál es el comando para instalar spaCy?
 A) pip install spacy-nlp
 B) pip install spacy
 C) npm install spacy
 D) apt-get install spacy

**70.** Para descargar el modelo en español de spaCy:
 A) python -m spacy download spanish
 B) python -m spacy download es
 C) python -m spacy download es_core_news_sm
 D) spacy.download('es')

**71.** ¿Cuál es el modelo más pequeño de spaCy para español?
 A) es_core_news_lg
 B) es_core_news_md
 C) es_core_news_sm
 D) es_small

**72.** Las ventajas de spaCy frente a NLTK son:
 A) Mejor rendimiento
 B) Modelos más rápidos y optimizados
 C) Mejor para producción
 D) Todas las anteriores

**73.** ¿Qué lenguajes soporta spaCy?
 A) Solo inglés
 B) Inglés y español
 C) Múltiples idiomas (inglés, español, alemán, francés, etc.)
 D) Solo idiomas europeos

---

## 11. spaCy - Pipeline Básico

**74.** Para cargar un modelo en spaCy:
 A) nlp = spacy.create('es_core_news_sm')
 B) nlp = spacy.load('es_core_news_sm')
 C) nlp = spacy.import('es_core_news_sm')
 D) nlp = spacy.open('es_core_news_sm')

**75.** Después de nlp(texto), ¿qué objeto se retorna?
 A) String
 B) List
 C) Doc
 D) Token

**76.** El atributo `token.pos_` en spaCy devuelve:
 A) La posición del token
 B) La categoría gramatical general
 C) La etiqueta específica
 D) Si es stopword

**77.** El atributo `token.lemma_` devuelve:
 A) La palabra original
 B) La forma lematizada
 C) La raíz de la palabra
 D) El significado

**78.** El atributo `token.is_stop` indica:
 A) Si es la última palabra
 B) Si es una stopword
 C) Si está al inicio
 D) Si es un signo de puntuación

**79.** El atributo `token.is_punct` indica:
 A) Si es una stopword
 B) Si es un número
 C) Si es un signo de puntuación
 D) Si está al final

---

## 12. spaCy - Análisis Avanzado

**80.** El reconocimiento de entidades (NER) en spaCy identifica:
 A) Solo nombres de personas
 B) Nombres, lugares, organizaciones, fechas, cantidades, etc.
 C) Solo ubicaciones
 D) Solo números

**81.** El atributo para acceder a las entidades en un Doc de spaCy es:
 A) doc.tokens
 B) doc.entities
 C) doc.ents
 D) doc.named_entities

**82.** El atributo `ent.label_` devuelve:
 A) El texto de la entidad
 B) La categoría de la entidad (PER, LOC, ORG, etc.)
 C) La posición de la entidad
 D) El número de caracteres

**83.** Una limitación de los modelos NER de spaCy es:
 A) No funcionan
 B) Pueden fallar en contextos desconocidos
 C) Solo funcionan en inglés
 D) Son lentísimos

**84.** Para mejorar la precisión del NER en un contexto específico:
 A) Usar otro modelo
 B) Fine-tuning del modelo
 C) Cambiar de librería
 D) No es posible

**85.** El atributo `token.dep_` devuelve:
 A) Las palabras anteriores
 B) La relación sintáctica (sujeto, objeto, etc.)
 C) El documento
 D) Las palabras siguientes

---

## 13. spaCy - Optimización

**86.** Para procesamiento de grandes volúmenes, ¿cuál es la forma recomendada?
 A) Bucle for con nlp(texto)
 B) Usar nlp.pipe()
 C) Usar nlp.batch()
 D) No hay optimización

**87.** ¿Qué hace nlp.pipe() que lo hace más eficiente?
 A) Compila los patrones
 B) Aplica optimizaciones internas al procesar multiple textos
 C) Aumenta la memoria
 D) Solo funciona en GPU

**88.** Para desactivar componentes innecesarios del pipeline en spaCy:
 A) nlp.disable()
 B) with nlp.disable_pipes("tagger", "parser"):
 C) nlp.remove_pipes()
 D) No es posible

**89.** Si solo necesito tokenización en spaCy, ¿qué componentes puedo desactivar?
 A) Tokenizador
 B) Tagger, parser, NER
 C) Solo NER
 D) No se puede

**90.** ¿Cuál es un modelo de spaCy que usa transformers?
 A) es_core_news_sm
 B) es_core_web_md
 C) Modelos con sufijo "-trf"
 D) Solo existen los tres modelos estándar

---

## 14. NLTK vs spaCy

**91.** NLTK es mejor cuando:
 A) Trabajas en producción con mucho volumen
 B) Necesitas documentación académica y corpus clásicos
 C) Necesitas máximo rendimiento
 D) Solo trabajas en inglés

**92.** spaCy es mejor cuando:
 A) Estás aprendiendo NLP
 B) Necesitas máximo rendimiento en producción
 C) Solo tienes datos en inglés
 D) No necesitas modelos preentrenados

**93.** ¿Cuál librería tiene mejor soporte para español?
 A) NLTK
 B) spaCy tiene soporte mejor y más directo
 C) Ambas igual
 D) Ninguna

**94.** ¿Puede usarse NLTK y spaCy juntos?
 A) No, son incompatibles
 B) Sí, se pueden combinar
 C) Solo en inglés
 D) No tiene sentido

---

## 15. Pandas/Polars con Minería de Texto

**95.** Para aplicar una función a cada elemento de una columna de texto en Pandas:
 A) df['columna'].apply(función)
 B) df['columna'].map(función)
 C) df['columna'].transform(función)
 D) Todas las anteriores

**96.** En Polars, para aplicar una función a cada elemento:
 A) df['columna'].apply(función)
 B) df.with_columns(pl.col('columna').map_elements(función))
 C) df['columna'].transform(función)
 D) df.map(función)

**97.** Para tokenizar una columna de texto en Pandas:
 A) df['text'].apply(nltk.word_tokenize)
 B) df['text'].str.split()
 C) df['text'].apply(lambda x: nltk.word_tokenize(x))
 D) Todas son válidas

**98.** En Polars, ¿cuál es el tipos de dato para listas?
 A) List
 B) Array
 C) pl.List()
 D) pl.Sequence

**99.** Si almaceno tokens en una columna de Polars como lista:
 A) df['tokens'] = [['hola', 'mundo']]
 B) df.with_columns(pl.col('text').map_elements(..., return_dtype=pl.List(pl.Utf8)))
 C) df['tokens'] = pl.List(...)
 D) No es posible

**100.** Para integrar spaCy con Pandas/Polars:
 A) Función apply con nlp(texto)
 B) map_elements con nlp(texto)
 C) Crear columnas con atributos del Doc
 D) Todas las anteriores

---

## SOLUCIONARIO

### Sección 1-2: Aspectos Básicos y Codificación
1. **B** - Minería de texto extrae información y patrones
2. **C** - Requieren procesamiento lingüístico especial
3. **B** - Token es unidad pequeña del texto
4. **B** - Tokenizar es dividir en unidades
5. **C** - Stopwords no aportan significado sustancial
6. **B** - Normalización aplica estándares
7. **C** - Recolección es el primer paso
8. **C** - Después de normalizar, solo 1 versión

9. **B** - American Standard Code for Information Interchange
10. **C** - ASCII estándar usa 7 bits
11. **B** - 128 caracteres (2^7)
12. **B** - No puede representar caracteres especiales
13. **C** - Código único para cada carácter de idiomas conocidos
14. **A** - Unicode Transformation Format - 8 bits
15. **D** - Entre 1 y 4 bytes (variable)
16. **B** - Los 128 primeros coinciden con ASCII
17. **C** - UTF-8 es por defecto
18. **B** - encoding="utf-8" en open()
19. **B** - Mostrará caracteres incorrectos
20. **B** - langdetect detecta idioma

### Sección 3-4: Expresiones Regulares Básicas
21. **B** - Coincide con cualquier carácter
22. **A** - Marca el inicio de cadena
23. **B** - Marca el final de cadena
24. **B** - Una o más repeticiones
25. **A** - Cero o más repeticiones
26. **A** - Cero o una repetición (opcional)
27. **C** - Letras mayúsculas, minúsculas y dígitos
28. **C** - Dígitos (0-9)
29. **B** - Caracteres de palabra (letras, dígitos, subrayado)
30. **B** - Espacios en blanco
31. **A** - Entre 2 y 5 repeticiones
32. **B** - #\w+ para hashtags

### Sección 5-6: Librería re
33. **B** - re.match() busca al inicio
34. **B** - re.search() encontrá primera aparición
35. **C** - re.findall() devuelve lista
36. **C** - re.sub() reemplaza
37. **A** - re.split() divide
38. **C** - None si no hay coincidencia
39. **B** - Reutilizar patrón compilado
40. **C** - re.findall() para múltiples emails

### Sección 7: Casos Prácticos Regex
41. **B** - [A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}
42. **B** - \d{3}-\d{3}-\d{4}
43. **D** - http|https
44. **B** - #\w+
45. **B** - re.sub(r' {2,}', ' ', texto)
46. **D** - Las opciones A y C son correctas

### Sección 8: regex vs re
47. **C** - Lookbehind de longitud variable
48. **B** - pip install regex
49. **B** - Mirar hacia atrás sin incluir
50. **C** - Detectar propiedades Unicode y emojis
51. **B** - regex
52. **B** - Expresiones recursivas

### Sección 9-10: NLTK
53. **A** - pip install nltk
54. **B** - nltk.download()
55. **B** - nltk.word_tokenize()
56. **B** - Modelos de tokenización
57. **B** - Sí, como tokens separados
58. **B** - El soporte no es tan avanzado
59. **B** - Part of Speech tagging
60. **B** - nltk.pos_tag()
61. **B** - Nombre propio
62. **B** - Stemming corta sin diccionario, lematización usa diccionarios
63. **C** - Inglés
64. **B** - WordNetLemmatizer
65. **A** - Todos se convierten a "play"

66. **C** - Palabra frecuente sin significado
67. **B** - nltk.stopwords.words('english')
68. **B** - 'stopwords' debe descargarse

### Sección 11-12: spaCy
69. **B** - pip install spacy
70. **C** - python -m spacy download es_core_news_sm
71. **C** - es_core_news_sm
72. **D** - Todas las anteriores
73. **C** - Múltiples idiomas

74. **B** - nlp = spacy.load('es_core_news_sm')
75. **C** - Doc
76. **B** - Categoría gramatical general
77. **B** - Forma lematizada
78. **B** - Si es una stopword
79. **C** - Si es un signo de puntuación

80. **B** - Nombres, lugares, organizaciones, fechas, cantidades
81. **C** - doc.ents
82. **B** - Categoría de la entidad
83. **B** - Pueden fallar en contextos desconocidos
84. **B** - Fine-tuning del modelo
85. **B** - Relación sintáctica (sujeto, objeto, etc.)

### Sección 13-14: Optimización y Comparación
86. **B** - Usar nlp.pipe()
87. **B** - Aplica optimizaciones internas
88. **B** - with nlp.disable_pipes("tagger", "parser"):
89. **B** - Tagger, parser, NER
90. **C** - Modelos con sufijo "-trf"

91. **B** - Necesitas documentación académica
92. **B** - Necesitas máximo rendimiento en producción
93. **B** - spaCy tiene soporte mejor
94. **B** - Sí, se pueden combinar

### Sección 15: Integración con DataFrames
95. **D** - Todas las anteriores
96. **B** - df.with_columns(pl.col('columna').map_elements(función))
97. **D** - Todas son válidas
98. **C** - pl.List()
99. **B** - df.with_columns(pl.col('text').map_elements(..., return_dtype=pl.List(pl.Utf8)))
100. **D** - Todas las anteriores

---

## RESUMEN DE RESPUESTAS RÁPIDO

| Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta |
|----------|-----------|----------|-----------|----------|-----------|
| 1 | B | 35 | C | 69 | B |
| 2 | C | 36 | C | 70 | C |
| 3 | B | 37 | A | 71 | C |
| 4 | B | 38 | C | 72 | D |
| 5 | C | 39 | B | 73 | C |
| 6 | B | 40 | C | 74 | B |
| 7 | C | 41 | B | 75 | C |
| 8 | C | 42 | B | 76 | B |
| 9 | B | 43 | D | 77 | B |
| 10 | C | 44 | B | 78 | B |
| 11 | B | 45 | B | 79 | C |
| 12 | B | 46 | D | 80 | B |
| 13 | C | 47 | C | 81 | C |
| 14 | A | 48 | B | 82 | B |
| 15 | D | 49 | B | 83 | B |
| 16 | B | 50 | C | 84 | B |
| 17 | C | 51 | B | 85 | B |
| 18 | B | 52 | B | 86 | B |
| 19 | B | 53 | A | 87 | B |
| 20 | B | 54 | B | 88 | B |
| 21 | B | 55 | B | 89 | B |
| 22 | A | 56 | B | 90 | C |
| 23 | B | 57 | B | 91 | B |
| 24 | B | 58 | B | 92 | B |
| 25 | A | 59 | B | 93 | B |
| 26 | A | 60 | B | 94 | B |
| 27 | C | 61 | B | 95 | D |
| 28 | C | 62 | B | 96 | B |
| 29 | B | 63 | C | 97 | D |
| 30 | B | 64 | B | 98 | C |
| 31 | A | 65 | A | 99 | B |
| 32 | B | 66 | C | 100 | D |
| 33 | B | 67 | B |  |  |
| 34 | B | 68 | B |  |  |

---

## TÉRMINOS CLAVE POR SECCIÓN

| Sección | Conceptos |
|---------|-----------|
| **Básicos** | Minería de texto, tokenización, normalización, stopwords, pipeline |
| **Codificación** | ASCII, Unicode, UTF-8, encoding, caracteres especiales |
| **Regex Básico** | ^, $, ., *, +, ?, \d, \w, \s, [], {n,m} |
| **Librería re** | match(), search(), findall(), sub(), split(), compile() |
| **Casos Prácticos** | Emails, teléfonos, URLs, hashtags, fechas, números |
| **regex vs re** | Lookbehind variable, Unicode avanzado, recursividad, emojis |
| **NLTK** | word_tokenize, pos_tag, WordNetLemmatizer, stopwords |
| **spaCy** | load(), Doc, token.pos_, token.lemma_, NER, ents, nlp.pipe() |
| **Comparación** | NLTK (académico), spaCy (producción), soporte de idiomas |
| **DataFrames** | apply(), map_elements(), integración con minería de texto |

---

**Total de preguntas: 100**  
**Dificultad:** Media-Alta  
**Enfoque:** Práctico (expresiones regulares, NLTK, spaCy)  
**Tiempo estimado:** 100-130 minutos  

Este test es ideal para:
✅ Autoevaluación antes de examen  
✅ Preparación práctica de minería de texto  
✅ Comprensión de NLTK vs spaCy  
✅ Dominio de expresiones regulares  
✅ Integración con Pandas/Polars
