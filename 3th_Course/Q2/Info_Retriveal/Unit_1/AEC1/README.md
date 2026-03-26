# AEC1 - Análisis de Sentimiento y Tendencias en Redes Sociales

![image.png](attachment:23514a5f-0acd-4aeb-921a-558d6cb0b1f3:image.png)

## Introducción

En este proyecto he desarrollado un flujo completo de extracción, limpieza y análisis de datos aplicado a tweets relacionados con Bitcoin. La idea es construir un pipeline reutilizable que me permita trabajar con este tipo de datos de forma consistente y replicable en otros escenarios similares.

El núcleo del proyecto es la clase DataExtractor, donde concentro toda la lógica: desde la carga de datos hasta el análisis final. Esto me permite no depender del notebook como tal y reutilizar directamente el código en otros contextos, como el dashboard que incluyo en el proyecto. En cierto modo, he intentado separar claramente la lógica de datos de la parte de visualización, algo que considero clave y que resultó ser uno de mis principales problemas en la asignatura de Inteligencia Artificial a la hora de mantener el código limpio y escalable.

## Dataset

He utilizado el dataset de tweets sobre Bitcoin disponible en Kaggle, en formato CSV. Me parece que tiene suficiente volumen como para que aparezcan patrones reales, tanto en hashtags como en comportamiento de usuarios.

No incluyo el dataset en el repositorio por tamaño y licencia, así que hay que descargarlo manualmente y colocarlo en la carpeta del proyecto. Aun así, el código está preparado para funcionar directamente una vez se añade el fichero, sin necesidad de configuraciones adicionales.

---

## Desarrollo del proyecto

La primera decisión importante que seguí fue la carga de datos. En lugar de leer el CSV directamente, utilizo pandas.read_csv con chunksize, lo que me permite trabajar de forma más facil si el dataset crece o hay limitaciones de memoria. Es una decisión sencilla, pero bastante más realista que asumir que todo cabe en RAM.

El preprocesado del texto es probablemente la parte más importante del proyecto. Convierto todo a minúsculas, elimino URLs y menciones, y limpio emojis y símbolos usando categorías Unicode. Mantengo el carácter # porque es esencial para el análisis, ya que es precisamente el elemento que quiero estudiar. Después normalizo los espacios para dejar el texto consistente y evitar problemas en pasos posteriores.

Ejemplo:

- Original: "Check out #Bitcoin at [https://bitcoin.org](https://bitcoin.org/) 🚀 @user"
- Limpio: "check out #bitcoin"

A partir de ahí, extraigo hashtags con expresiones regulares y elimino duplicados dentro del mismo tweet para no sesgar las frecuencias. Esto evita que un único tweet tenga demasiado peso en el análisis simplemente por repetir un mismo hashtag varias veces.

Con los datos ya preparados, calculo frecuencias globales, por usuario y por fecha. Esto permite ver tanto qué hashtags dominan la conversación como cómo evolucionan en el tiempo y quiénes son los usuarios más activos.

Además, incluyo una métrica simple pero bastante útil: el porcentaje de uso de hashtags que proviene del top 1% de usuarios. No es un detector de bots como tal, pero sirve como señal bastante clara de actividad anómala o automatizada, especialmente cuando hay una concentración muy alta en pocos perfiles.

---

## Implementación

Toda la lógica está encapsulada en la clase DataExtractor, que actúa como una especie de “API sencilla” digamos. Incluye métodos para cargar datos, limpiar texto, extraer hashtags y generar métricas.

He intentado que sea independiente del entorno en el que se ejecute, lo que me ha permitido reutilizarla directamente en el dashboard sin cambios relevantes. Esto también facilita que el código sea más mantenible y fácil de ampliar en caso de querer añadir nuevas funcionalidades en el futuro.

---

## Ejecución

Para ejecutar el proyecto:

```bash
python -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib seaborn wordcloud
```

Pasos:

1. Descargar el dataset desde Kaggle
2. Colocarlo en la carpeta AEC1/
3. Ejecutar el notebook AEC1_DataExtractor.ipynb

---

## Visualización y dashboard

Al final del notebook genero visualizaciones como el top de hashtags, la evolución temporal y nubes de palabras, que permiten interpretar los datos de forma bastante directa y detectar patrones sin necesidad de profundizar en tablas.

Además como añadido a la práctica, he decidido crear un pequeño dashboard en Streamlit (muy sencillo es solo para visualizar) donde se puede subir el dataset y explorar los resultados de forma interactiva. Con esto no solo facilito a mi profesor la corrección, sino que también demuestro que la lógica está bien desacoplada y preparada para integrarse en otras herramientas.

---

## Referencias

- 42 AI Bootcamp (Organización orientada a IA dentro de 42 Paris creada por estudiantes):
    
    https://42-ai.github.io/
    
    https://github.com/42-AI
    
- Kaggle dataset:
    
    https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets
    
- Pandas documentation:
    
    https://pandas.pydata.org/docs/user_guide/index.html
    
- Matplotlib documentation:
    
    https://matplotlib.org/stable/users/index.html
    
- Seaborn tutorial:
    
    https://seaborn.pydata.org/tutorial.html
    
- WordCloud documentation:
    
    https://amueller.github.io/word_cloud/
    
- Regex tester:
    
    https://regex101.com/
    
- Unicode standard (TR44):
    
    https://unicode.org/reports/tr44/