# Test Unidad 4: Modelización y Análisis en Minería de Texto con Python

## 1. Descubrimiento de Tópicos - LDA

**1.** ¿Qué significa LDA?
- [ ] A) Linear Discriminant Analysis
- [ ] B) Latent Dirichlet Allocation
- [ ] C) Large Data Architecture
- [ ] D) Learning Distribution Algorithm

**2.** ¿Cuál es el objetivo principal del LDA?
- [ ] A) Clasificar documentos por autor
- [ ] B) Descubrir automáticamente temas latentes en documentos
- [ ] C) Traducir textos
- [ ] D) Comprimir archivos

**3.** ¿Qué es un "tópico" en LDA?
- [ ] A) Un título de un documento
- [ ] B) Una distribución de palabras
- [ ] C) Un párrafo importante
- [ ] D) Un número

**4.** ¿En qué se fundamenta matemáticamente LDA?
- [ ] A) En regresión lineal
- [ ] B) En tree-based models
- [ ] C) En distribuciones Dirichlet
- [ ] D) En redes neuronales

**5.** ¿Qué es un hiperparámetro α en LDA?
- [ ] A) El número de palabras
- [ ] B) Controla la concentración de tópicos en documentos
- [ ] C) El número de iteraciones
- [ ] D) Un error de ejecución

**6.** ¿Qué es un hiperparámetro β (eta) en LDA?
- [ ] A) El número de documentos
- [ ] B) Controla la distribución de palabras dentro de tópicos
- [ ] C) La velocidad de aprendizaje
- [ ] D) Un tipo de datos

**7.** ¿Qué librería se utiliza típicamente para implementar LDA en Python?
- [ ] A) nltk
- [ ] B) gensim
- [ ] C) sklearn
- [ ] D) spacy

**8.** ¿Cómo se instala Gensim?
- [ ] A) pip install topic-modeling
- [ ] B) pip install gensim
- [ ] C) pip install lda
- [ ] D) pip install text-mining

**9.** En el preprocesamiento para LDA, ¿qué es esencial hacer?
- [ ] A) Nada especial
- [ ] B) Tokenizar, eliminar stopwords, lematizar
- [ ] C) Solo tokenizar
- [ ] D) Convertir a minúsculas solamente

**10.** ¿Qué es bag-of-words (BoW)?
- [ ] A) Una bolsa de códigos
- [ ] B) Representación de documento como vector de frecuencias de palabras
- [ ] C) Un tipo de almacenamiento
- [ ] D) Un protocolo

---

## 2. Implementación de LDA con Gensim

**11.** ¿Qué es un Diccionario en Gensim?
- [ ] A) Un archivo de palabras
- [ ] B) Una estructura que asigna IDs únicos a cada palabra
- [ ] C) Un tipo de base de datos
- [ ] D) Un archivo de configuración

**12.** ¿Cómo se crea un Dictionary en Gensim?
- [ ] A) dictionary = Dictionary()
- [ ] B) dictionary = corpora.Dictionary(documents)
- [ ] C) dictionary = gensim.create_dict()
- [ ] D) dictionary = make_dictionary()

**13.** ¿Qué método convierte un documento a bag-of-words?
- [ ] A) document.to_bow()
- [ ] B) dictionary.doc2bow(document)
- [ ] C) bow(document)
- [ ] D) document.as_bow()

**14.** ¿Cuál es el formato de salida de doc2bow?
- [ ] A) Un diccionario
- [ ] B) Una lista de (word_id, frequency)
- [ ] C) Un documento
- [ ] D) Una matriz

**15.** ¿Qué es LdaModel en Gensim?
- [ ] A) Un tipo de base de datos
- [ ] B) El modelo entrenado de LDA
- [ ] C) Una función de Pandas
- [ ] D) Un archivo comprimido

**16.** ¿Cuál es un parámetro importante en LdaModel?
- [ ] A) num_topics
- [ ] B) passes
- [ ] C) per_word_topics
- [ ] D) Todos

**17.** ¿Qué hace el parámetro num_topics?
- [ ] A) Define el número de documentos
- [ ] B) Define cuántos tópicos se desea extraer
- [ ] C) Define el número de palabras
- [ ] D) Define las iteraciones

**18.** ¿Qué hace el parámetro passes?
- [ ] A) El número de tópicos
- [ ] B) El número de iteraciones sobre el corpus
- [ ] C) El número de documentos
- [ ] D) La velocidad de entrenamiento

**19.** ¿Cómo se obtienen los tópicos después del entrenamiento?
- [ ] A) lda_model.topics()
- [ ] B) lda_model.show_topics()
- [ ] C) lda_model.get_topics()
- [ ] D) lda_model.topics_list()

**20.** ¿Cómo se obtiene la distribución de tópicos para un documento?
- [ ] A) lda_model.document_topics(doc)
- [ ] B) lda_model.get_document_topics(doc_bow)
- [ ] C) doc.get_topics()
- [ ] D) lda_model.doc_topics()

---

## 3. Evaluación de LDA

**21.** ¿Qué es perplexity en LDA?
- [ ] A) Un error de programación
- [ ] B) Una métrica de la capacidad predictiva del modelo
- [ ] C) Una estructura de datos
- [ ] D) Un tipo de tópico

**22.** ¿Qué es topic coherence?
- [ ] B) Una métrica que evalúa consistencia de palabras en tópicos
- [ ] A) Un tipo de error
- [ ] C) Un compilador
- [ ] D) Un algoritmo

**23.** ¿Cuál es la librería para calcular coherencia?
- [ ] A) sklearn.metrics
- [ ] B) gensim.models.CoherenceModel
- [ ] C) nltk.coherence
- [ ] D) scipy

**24.** ¿Un score alto de coherencia qué indica?
- [ ] A) Un modelo malo
- [ ] B) Un modelo con tópicos bien definidos
- [ ] C) Más documentos
- [ ] D) Error en el cálculo

**25.** ¿Cómo se mejora la calidad de LDA?
- [ ] A) No se puede mejorar
- [ ] B) Experimentar con num_topics, passes, alpha y beta
- [ ] C) Solo cambiar el idioma
- [ ] D) Aumentar datos aleatoriamente

---

## 4. Análisis de Sentimiento - Conceptos

**26.** ¿Qué es análisis de sentimiento?
- [ ] A) Detectar emociones en texto
- [ ] B) Determinar si un texto es positivo, negativo o neutral
- [ ] C) Contar palabras
- [ ] D) Traducir textos

**27.** ¿Cuáles son los tres sentimientos básicos?
- [ ] A) Bueno, malo, indiferente
- [ ] B) Feliz, triste, asustado
- [ ] C) Positivo, negativo, neutral
- [ ] D) Amor, odio, miedo

**28.** ¿Qué es polaridad en análisis de sentimiento?
- [ ] A) Un tipo de imán
- [ ] B) Una medida de si el sentimiento es positivo o negativo
- [ ] C) Un idioma
- [ ] D) Un algoritmo

**29.** ¿Qué es subjetividad en análisis de sentimiento?
- [ ] A) Algo mal escrito
- [ ] B) Una medida de si el texto expresa opinión vs hecho
- [ ] C) Un tipo de error
- [ ] D) Un formato

**30.** ¿Cuáles son los dos enfoques principales?
- [ ] A) Machine Learning y Deep Learning solo
- [ ] B) Basado en diccionarios léxicos y modelos estadísticos
- [ ] C) SQL y NoSQL
- [ ] D) Hadoop y Spark

---

## 5. TextBlob para Análisis de Sentimiento

**31.** ¿Qué es TextBlob?
- [ ] A) Un tipo de base de datos
- [ ] B) Una librería de Python para tareas NLP simples
- [ ] C) Un navegador web
- [ ] D) Un servidor

**32.** ¿Cómo se instala TextBlob?
- [ ] A) pip install text-blob
- [ ] B) pip install textblob
- [ ] C) pip install blob
- [ ] D) pip install sentiment

**33.** ¿Cómo se crea un objeto TextBlob?
- [ ] A) blob = TextBlob(texto)
- [ ] B) blob = text_blob(texto)
- [ ] C) blob = Blob(texto)
- [ ] D) blob = create_blob(texto)

**34.** ¿Cuál es el método para obtener el sentimiento en TextBlob?
- [ ] A) blob.sentiment()
- [ ] B) blob.analyze()
- [ ] C) blob.sentiment (atributo)
- [ ] D) blob.analyze_sentiment()

**35.** ¿Qué retorna blob.sentiment?
- [ ] A) Una cadena
- [ ] B) Un número
- [ ] C) Una tupla (polaridad, subjetividad)
- [ ] D) Un diccionario

**36.** ¿Cuál es el rango típico de polaridad en TextBlob?
- [ ] A) 0-100
- [ ] B) 0-1
- [ ] C) -1 a 1
- [ ] D) -100 a 100

**37.** ¿Qué valor de polaridad indica sentimiento positivo?
- [ ] A) Menores a 0
- [ ] B) Iguales a 0
- [ ] C) Mayores a 0
- [ ] D) Iguales a 1

**38.** ¿Cómo se obtienen las oraciones de un TextBlob?
- [ ] A) blob.sentences
- [ ] B) blob.get_sentences()
- [ ] C) blob.sentences (atributo)
- [ ] D) split_sentences(blob)

**39.** ¿Cómo se obtienen palabras clave de TextBlob?
- [ ] A) blob.keywords
- [ ] B) blob.noun_phrases
- [ ] C) blob.important_words()
- [ ] D) blob.get_keywords()

**40.** ¿TextBlob puede hacer traducción?
- [ ] A) No
- [ ] B) Sí con blob.translate()
- [ ] C) Solo a inglés
- [ ] D) Con Google API

---

## 6. spaCy para Análisis de Sentimiento

**41.** ¿Qué es spaCy?
- [ ] A) Un espacio en blanco
- [ ] B) Una librería de NLP moderna y rápida
- [ ] C) Un protocolo de red
- [ ] D) Una base de datos

**42.** ¿Cómo se instala spaCy?
- [ ] A) pip install spacy
- [ ] B) pip install space
- [ ] C) pip install nlp-space
- [ ] D) pip install lang

**43.** ¿Cuál es la ventaja de spaCy sobre TextBlob?
- [ ] A) No tiene ventajas
- [ ] B) Es más rápido y tiene modelos más potentes
- [ ] C) Solo funciona en Linux
- [ ] D) Usa menos memoria

**44.** ¿Cómo se carga un modelo en spaCy?
- [ ] A) nlp = spacy.load('es_core_news_sm')
- [ ] B) nlp = spacy_model('es_core_news_sm')
- [ ] C) nlp = load_model('es_core_news_sm')
- [ ] D) nlp = init_spacy('es_core_news_sm')

**45.** ¿Qué es un Doc en spaCy?
- [ ] A) Un documento de texto
- [ ] B) Un objeto procesado que contiene tokens y anotaciones
- [ ] C) Una estructura de datos
- [ ] D) Un archivo

**46.** ¿Cómo se procesa texto con spaCy?
- [ ] A) doc = nlp.process(texto)
- [ ] B) doc = nlp(texto)
- [ ] C) doc = spacy.parse(texto)
- [ ] D) doc = process_text(texto)

**47.** ¿Qué es un Token en spaCy?
- [ ] A) Un símbolo especial
- [ ] B) Una palabra proceada con información lingüística
- [ ] C) Un tipo de archivo
- [ ] D) Un código de autenticación

**48.** ¿Cómo se obtienen tokens de un Doc?
- [ ] A) doc.tokens
- [ ] B) doc[i] para cada posición
- [ ] C) Ambas
- [ ] D) for token in doc

**49.** ¿Qué información contiene cada Token?
- [ ] A) Solo la palabra
- [ ] B) POS, lemma, entity, dependencies
- [ ] C) Solo lema
- [ ] D) Solo tipo de entidad

**50.** ¿Para análisis de sentimiento, qué usa spaCy típicamente?
- [ ] A) Modelos propios de sentimiento
- [ ] B) Texblob integrado
- [ ] C) Se requiere integrar con otra librería o modelo entrenado
- [ ] D) No puede faire análisis de sentimiento

---

## 7. Parsing de Documentos

**51.** ¿Qué es parsing en minería de texto?
- [ ] A) Eliminar palabras comunes
- [ ] B) Analizar la estructura gramatical de un texto
- [ ] C) Traducir documentos
- [ ] D) Contar palabras

**52.** ¿Qué es POS tagging?
- [ ] A) Etiquetar mensajes de correo
- [ ] B) Anotar cada palabra con su parte del discurso
- [ ] C) Crear publicaciones
- [ ] D) Un tipo de archivo

**53.** ¿Cuál es un ejemplo de etiqueta POS?
- [ ] A) NOUN, VERB, ADJ, ADV
- [ ] B) .txt, .pdf, .doc
- [ ] C) positivo, negativo
- [ ] D) HTML, JSON

**54.** ¿Qué es lematización?
- [ ] A) Contar palabras
- [ ] B) Reducir palabras a su forma base/lema
- [ ] C) Eliminar duplicados
- [ ] D) Traducir

**55.** ¿Cuál es la diferencia entre lematización y stemming?
- [ ] A) No hay diferencia
- [ ] B) Lematización usa diccionario; stemming usa reglas
- [ ] C) Stemming es más antiguo
- [ ] D) Lematización requiere más recursos

**56.** ¿Qué es Named Entity Recognition (NER)?
- [ ] A) Reconocer redes
- [ ] B) Identificar entidades como nombres, lugares, organismos
- [ ] C) Reconocer emociones
- [ ] D) Un tipo de algoritmo

**57.** ¿Cómo se obtienen entidades en spaCy?
- [ ] A) doc.entities
- [ ] B) doc.ents
- [ ] C) doc.named_entities()
- [ ] D) doc.get_entities()

**58.** ¿Qué es dependency parsing?
- [ ] A) Analizar dependencias del sistema
- [ ] B) Analizar relaciones gramaticales entre palabras
- [ ] C) Eliminar dependencias
- [ ] D) Crear dependencias

**59.** ¿Cómo se accede a las dependencias en spaCy?
- [ ] A) token.dep_
- [ ] B) token.dependency
- [ ] C) token.get_dependency()
- [ ] D) doc.dependencies

**60.** ¿Qué librería es buena para parsing tradicional?
- [ ] A) regex
- [ ] B) NLTK
- [ ] C) spaCy
- [ ] D) Ambas B y C

---

## 8. Resumen Automático de Textos

**61.** ¿Qué es resumen automático de textos?
- [ ] A) Escribir un nuevo documento
- [ ] B) Producir una versión condensada manteniendo ideas principales
- [ ] C) Eliminar palabras
- [ ] D) Traducir

**62.** ¿Cuáles son los dos tipos de resumen?
- [ ] A) Largo y corto
- [ ] B) Extractivo (selecciona frases existentes) y Abstractivo (genera nuevas)
- [ ] C) Inglés y español
- [ ] D) Positivo y negativo

**63.** ¿Cuál es un enfoque extractivo para resumen?
- [ ] A) Usar redes neuronales
- [ ] B) Seleccionar frases basándose en frecuencia de palabras
- [ ] C) Crear síntesis
- [ ] D) Traducir

**64.** ¿Qué librería puede hacer resumen abstractivo básico?
- [ ] A) gensim
- [ ] B) transformers (con modelos pre-entrenados)
- [ ] C) NLTK
- [ ] D) requests

**65.** ¿Cuál es una métrica para evaluar resúmenes?
- [ ] A) BLEU
- [ ] B) ROUGE
- [ ] C) F1-score
- [ ] D) Ambas B y C

**66.** ¿Qué es ROUGE en summarization?
- [ ] A) Un color
- [ ] B) Una métrica que compara resúmenes contra referencias
- [ ] C) Un algoritmo
- [ ] D) Un tipo de archivo

**67.** ¿Cuál es una limitación del resumen extractivo?
- [ ] A) Requiere entrenamiento
- [ ] B) No genera frases cohesivas, solo selecciona
- [ ] C) Es muy lento
- [ ] D) Requiere GPU

**68.** ¿Resumir un documento típicamente produce qué porcentaje?
- [ ] A) 10%
- [ ] B) 50%
- [ ] C) 30-40%
- [ ] D) 90%

**69.** ¿Es posible resumir con spaCy?
- [ ] A) No
- [ ] B) Sí, usando text rank u otros algoritmos
- [ ] C) Solo con modelos especiales
- [ ] D) Requiere API externa

**70.** ¿Cuál es la ventaja del resumen automático?
- [ ] A) No tiene ventajas
- [ ] B) Ahorra tiempo en procesar documentos largos
- [ ] C) Reemplaza lectores humanos
- [ ] D) Siempre es correcto

---

## 9. Pipelines Integrados

**71.** ¿Qué es un pipeline en minería de texto?
- [ ] A) Un tubo
- [ ] B) Una secuencia de pasos de procesamiento
- [ ] C) Una base de datos
- [ ] D) Un servidor

**72.** ¿En qué orden se aplican típicamente las etapas?
- [ ] A) Cualquier orden
- [ ] B) Recolección → Limpieza → Preprocesamiento → Análisis
- [ ] C) Análisis → Limpieza
- [ ] D) Solo limpieza

**73.** ¿Cómo se integra LDA con análisis de sentimiento?
- [ ] A) No es posible
- [ ] B) Se pueden combinar: primero LDA para tópicos, luego sentimiento por tópico
- [ ] C) Solo secuencialmente
- [ ] D) Requieren API diferentes

**74.** ¿Qué es una buena práctica en pipelines?
- [ ] A) Hacer todo en una línea
- [ ] B) Modularizar: funciones reutilizables y componentes independientes
- [ ] C) No documentar
- [ ] D) No testear

**75.** ¿Cómo se valida un pipeline completo?
- [ ] A) No se valida
- [ ] B) Pruebas manuales, métricas, reporte de resultados
- [ ] C) Solo con datos de prueba
- [ ] D) Nunca

---

## 10. Aplicaciones Prácticas

**76.** ¿Para qué se usa análisis de sentimiento en marketing?
- [ ] A) Crear anuncios
- [ ] B) Entender la reputación y aceptación de productos
- [ ] C) Traducir contenido
- [ ] D) Aumentar precios

**77.** ¿Para qué se usa LDA en periodismo?
- [ ] A) Escribir artículos
- [ ] B) Descubrir temas principales en grandes colecciones de noticias
- [ ] C) Vender periódicos
- [ ] D) Publicidad

**78.** ¿Qué aplicación tiene parsing en búsqueda?
- [ ] A) Crear un buscador
- [ ] B) Entender estructura de preguntas para mejorar búsquedas
- [ ] C) Contar búsquedas
- [ ] D) Filtrar usuarios

**79.** ¿Cómo se usa resumen en gestión documental?
- [ ] A) Para eliminar documentos
- [ ] B) Para crear índices y resúmenes de grandes corpus
- [ ] C) For archiving
- [ ] D) No tiene uso

**80.** ¿Cuál es el beneficio de combinar múltiples técnicas?
- [ ] A) Se ejecuta más lento
- [ ] B) Se obtiene análisis más rico y múltiples perspectivas
- [ ] C) Ocupa más memoria
- [ ] D) No hay beneficio

---

## SOLUCIONARIO

| Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta |
|----------|-----------|----------|-----------|----------|-----------|
| 1 | B | 28 | B | 55 | B |
| 2 | B | 29 | B | 56 | B |
| 3 | B | 30 | B | 57 | B |
| 4 | C | 31 | B | 58 | B |
| 5 | B | 32 | B | 59 | A |
| 6 | B | 33 | A | 60 | D |
| 7 | B | 34 | C | 61 | B |
| 8 | B | 35 | C | 62 | B |
| 9 | B | 36 | C | 63 | B |
| 10 | B | 37 | C | 64 | B |
| 11 | B | 38 | C | 65 | D |
| 12 | B | 39 | B | 66 | B |
| 13 | B | 40 | B | 67 | B |
| 14 | B | 41 | B | 68 | C |
| 15 | B | 42 | A | 69 | B |
| 16 | D | 43 | B | 70 | B |
| 17 | B | 44 | A | 71 | B |
| 18 | B | 45 | B | 72 | B |
| 19 | B | 46 | B | 73 | B |
| 20 | B | 47 | B | 74 | B |
| 21 | B | 48 | D | 75 | B |
| 22 | B | 49 | B | 76 | B |
| 23 | B | 50 | C | 77 | B |
| 24 | B | 51 | B | 78 | B |
| 25 | B | 52 | B | 79 | B |
| 26 | B | 53 | A | 80 | B |
| 27 | C | 54 | B |

---

## Preguntas Adicionales (81-100)

**81.** ¿Cuál es la importancia de la calidad de datos en LDA?
- [ ] A) No es importante
- [ ] B) LDA es muy sensible al ruido y datos de baja calidad
- [ ] C) Solo afecta la velocidad
- [ ] D) Afecta solo la presentación

**82.** ¿Qué es stop words removal?
- [ ] A) Eliminar todos los signos
- [ ] B) Eliminar palabras frecuentes sin significado temático
- [ ] C) Eliminar números
- [ ] D) Eliminar tildes

**83.** ¿Para qué se usan librerías como VADER?
- [ ] A) Web scraping
- [ ] B) Análisis de sentimiento específico para redes sociales
- [ ] C) Traducción
- [ ] D) Compresión

**84.** ¿Qué es un modelo pre-entrenado en NLP?
- [ ] A) Un modelo que aprendiste tú
- [ ] B) Un modelo entrenado con datos masivos y listo para usar
- [ ] C) Un modelo en desarrollo
- [ ] D) No existe

**85.** ¿Cuál es una ventaja de usar modelos pre-entrenados?
- [ ] A) No hay ventajas
- [ ] B) Ahorran tiempo y recursos de entrenamiento
- [ ] C) Son más lentos
- [ ] D) Requieren más datos

**86.** ¿Qué es fine-tuning?
- [ ] A) Afinar un instrumento
- [ ] B) Ajustar un modelo pre-entrenado a tu tarea específica
- [ ] C) Entrenar desde cero
- [ ] D) Eliminar capas

**87.** ¿En qué escenario es útil fine-tuning?
- [ ] A) Siempre
- [ ] B) Cuando tienes datos específicos de dominio limitados
- [ ] C) Nunca
- [ ] D) Solo con imágenes

**88.** ¿Qué es TF-IDF?
- [ ] A) Una unidad de medida
- [ ] B) Una técnica para ponderar palabras por su importancia
- [ ] C) Un tipo de base de datos
- [ ] D) Un protocolo

**89.** ¿Cómo se usa TF-IDF en análisis de sentimiento?
- [ ] A) No se usa
- [ ] B) Para pesar palabras importantes en clasificación
- [ ] C) Para comprimir texto
- [ ] D) Para traducir

**90.** ¿Qué es One-Hot Encoding?
- [ ] A) Cocinar un huevo
- [ ] B) Representar categorías como vectores binarios
- [ ] C) Un tipo de compilador
- [ ] D) Un protocolo

**91.** ¿Cuál es una desventaja de One-Hot Encoding?
- [ ] A) Es muy rápido
- [ ] B) Crea vectores muy grandes para vocabularios grandes
- [ ] C) No tiene desventajas
- [ ] D) Solo funciona en Python

**92.** ¿Qué es embeddings en NLP?
- [ ] A) Texto incrustado en HTML
- [ ] B) Representaciones densas de palabras en espacios vectoriales
- [ ] C) Un tipo de base de datos
- [ ] D) Un archivo comprimido

**93.** ¿Cuál es una ventaja de word embeddings?
- [ ] A) Capturan relaciones semánticas entre palabras
- [ ] B) Son muy pequeños
- [ ] C) Se entrenan rápido
- [ ] D) Todas

**94.** ¿Qué es Word2Vec?
- [ ] A) Un navegador
- [ ] B) Un modelo para generar word embeddings
- [ ] C) Una base de datos
- [ ] D) Un protocolo

**95.** ¿Cuáles son los dos enfoques de Word2Vec?
- [ ] A) Skip-gram y CBOW
- [ ] B) Encoder y Decoder
- [ ] C) RNN y CNN
- [ ] D) Supervised y Unsupervised

**96.** ¿Qué es BLEU score?
- [ ] A) Un color
- [ ] B) Una métrica de evaluación en traducción automática
- [ ] C) Un algoritmo
- [ ] D) Un compilador

**97.** ¿Cómo se evalúa la calidad de un análisis de sentimiento?
- [ ] A) No se evalúa
- [ ] B) Precisión, recall, F1-score, matriz de confusión
- [ ] C) Solo visualmente
- [ ] D) Contando palabras

**98.** ¿Qué es confusion matrix?
- [ ] A) Una matriz confusa
- [ ] B) Uma matriz que muestra TP, TN, FP, FN
- [ ] C) Un algoritmo
- [ ] D) Un tipo de archivo

**99.** ¿Cuál es una buena práctica en minería de texto?
- [ ] A) Usar todo automáticamente sin revisión
- [ ] B) Validar y interpretar resultados manualmente
- [ ] C) Solo confiar en métricas
- [ ] D) No documentar

**100.** ¿Qué es el futuro de la minería de texto?
- [ ] A) Va a desaparecer
- [ ] B) Integración con modelos de lenguaje grandes (LLMs), análisis multimodal, interpretabilidad
- [ ] C) Solo análisis básico
- [ ] D) No hay futuro

---

| 81 | B | 91 | B |
| 82 | B | 92 | B |
| 83 | B | 93 | A |
| 84 | B | 94 | B |
| 85 | B | 95 | A |
| 86 | B | 96 | B |
| 87 | B | 97 | B |
| 88 | B | 98 | B |
| 89 | B | 99 | B |
| 90 | B | 100 | B |
