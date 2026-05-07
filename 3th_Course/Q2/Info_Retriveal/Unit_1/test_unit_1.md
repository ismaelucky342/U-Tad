# Test: Ecosistema de Python

## 1. Instalación y IDEs

**1.** ¿Cuál es la versión actual recomendada de Python?
- [ ] A) 2.7
- [ ] B) 3.9
- [ ] C) 3.11.9
- [ ] D) 3.10

**2.** Al instalar Python, ¿qué opción es importante marcar?
- [ ] A) Add Python 3.x to PATH
- [ ] B) Crear acceso directo
- [ ] C) Instalar compilador
- [ ] D) Todas las anteriores

**3.** ¿Cuál es el comando para verificar la versión de Python instalada?
- [ ] A) python --check
- [ ] B) python3 --version
- [ ] C) python -v
- [ ] D) python --info

**4.** ¿Qué es un entorno virtual?
- [ ] A) Un servidor remoto
- [ ] B) Un aislamiento de dependencias del proyecto
- [ ] C) Una máquina virtual
- [ ] D) Un repositorio de código

**5.** ¿Cuál es el módulo de Python para crear entornos virtuales?
- [ ] A) virtualenv
- [ ] B) venv
- [ ] C) env
- [ ] D) python-env

**6.** En Windows, ¿cuál es el comando para crear un entorno virtual?
- [ ] A) python -m venv nombre_entorno
- [ ] B) python --create-env nombre_entorno
- [ ] C) venv crear nombre_entorno
- [ ] D) python -env nombre_entorno

**7.** En Windows, ¿cuál es el comando para activar un entorno virtual?
- [ ] A) source nombre_entorno/bin/activate
- [ ] B) nombre_entorno\Scripts\activate
- [ ] C) activate nombre_entorno
- [ ] D) . nombre_entorno/bin/activate

**8.** ¿Cuál es el comando para desactivar un entorno virtual?
- [ ] A) deactivate
- [ ] B) exit
- [ ] C) python -m venv --deactivate
- [ ] D) source deactivate

**9.** ¿Qué es pip?
- [ ] A) Un IDE
- [ ] B) Un gestor de paquetes
- [ ] C) Un sistema operativo
- [ ] D) Un servidor web

**10.** ¿Cuál es el comando para instalar una librería con pip?
- [ ] A) pip add nombre_libreria
- [ ] B) pip install nombre_libreria
- [ ] C) pip import nombre_libreria
- [ ] D) pip load nombre_libreria

**11.** ¿Cómo instalar una versión específica de una librería?
- [ ] A) pip install nombre_libreria:version
- [ ] B) pip install nombre_libreria@version
- [ ] C) pip install nombre_libreria==version
- [ ] D) pip install nombre_libreria-version

**12.** ¿Para qué sirve requirements.txt?
- [ ] A) Documentar el proyecto
- [ ] B) Listar las dependencias del proyecto
- [ ] C) Almacenar variables de entorno
- [ ] D) Configurar el servidor

**13.** ¿Cuál es el comando para instalar dependencias desde requirements.txt?
- [ ] A) pip -r requirements.txt
- [ ] B) pip install -r requirements.txt
- [ ] C) pip load requirements.txt
- [ ] D) pip install requirements.txt

**14.** ¿Qué comando muestra todos los paquetes instalados?
- [ ] A) pip show
- [ ] B) pip list
- [ ] C) pip display
- [ ] D) pip packages

**15.** ¿Cómo actualizar un paquete con pip?
- [ ] A) pip update nombre_libreria
- [ ] B) pip install --upgrade nombre_libreria
- [ ] C) pip upgrade nombre_libreria
- [ ] D) pip refresh nombre_libreria

**16.** ¿Cuál es el comando para desinstalar un paquete?
- [ ] A) pip remove nombre_libreria
- [ ] B) pip uninstall nombre_libreria
- [ ] C) pip delete nombre_libreria
- [ ] D) pip erase nombre_libreria

**17.** PyCharm viene en dos versiones, ¿cuáles son?
- [ ] A) Free y Enterprise
- [ ] B) Community y Professional
- [ ] C) Basic y Advanced
- [ ] D) Standard y Premium

**18.** ¿Quién desarrolló PyCharm?
- [ ] A) Google
- [ ] B) Facebook
- [ ] C) JetBrains
- [ ] D) Microsoft

**19.** ¿Cuál es la ventaja principal de VSCode para Python?
- [ ] A) Viene con Python incluido
- [ ] B) Es completamente gratuito y extensible
- [ ] C) No necesita configuración
- [ ] D) Solo funciona en Windows

**20.** ¿Cuál es el comando para iniciar JupyterLab?
- [ ] A) jupyter start
- [ ] B) jupyter notebook
- [ ] C) jupyter lab
- [ ] D) jupyter run

---

## 2. Sintaxis Básica

**21.** En Python, ¿cuál es el símbolo para comentarios?
- [ ] A) //
- [ ] B) --
- [ ] C) #
- [ ] D) /* */

**22.** ¿Cuál es el resultado de 10 + 5?
- [ ] A) 15
- [ ] B) 105
- [ ] C) 10
- [ ] D) 5

**23.** ¿Cuál es el operador para división entera en Python?
- [ ] A) /
- [ ] B) //
- [ ] C) \
- [ ] D) div

**24.** ¿Qué tipo de dato es 42?
- [ ] A) float
- [ ] B) string
- [ ] C) int
- [ ] D) bool

**25.** ¿Qué tipo de dato es 3.14?
- [ ] A) int
- [ ] B) float
- [ ] C) string
- [ ] D) complex

**26.** ¿Cuál es el primer índice de una lista en Python?
- [ ] A) 0
- [ ] B) 1
- [ ] C) -1
- [ ] D) Depende de la lista

**27.** ¿Qué son las listas en Python?
- [ ] A) Inmutables y desordenadas
- [ ] B) Mutables y desordenadas
- [ ] C) Mutables y ordenadas
- [ ] D) Inmutables y ordenadas

**28.** Si tengo lista = [1, 2, 3], ¿qué valor tiene lista[2]?
- [ ] A) 1
- [ ] B) 2
- [ ] C) 3
- [ ] D) Error

**29.** ¿Qué son las tuplas?
- [ ] A) Listas modificables
- [ ] B) Variables compartidas
- [ ] C) Colecciones inmutables
- [ ] D) Funciones reutilizables

**30.** ¿Cuál es el símbolo para definir un conjunto (set)?
- [ ] A) []
- [ ] B) ()
- [ ] C) {}
- [ ] D) <>

**31.** Si conjunto = {1, 2, 3, 3}, ¿cuántos elementos tiene?
- [ ] A) 4
- [ ] B) 5
- [ ] C) 3
- [ ] D) 2

**32.** ¿Cuál es el método para añadir un elemento a una lista?
- [ ] A) list.add()
- [ ] B) list.push()
- [ ] C) list.append()
- [ ] D) list.insert()

**33.** ¿Cuál es el método para añadir un elemento a un conjunto?
- [ ] A) set.append()
- [ ] B) set.insert()
- [ ] C) set.add()
- [ ] D) set.push()

**34.** ¿Qué es un diccionario en Python?
- [ ] A) Una lista de palabras
- [ ] B) Una estructura que almacena pares clave-valor
- [ ] C) Un tipo de comentario
- [ ] D) Una función especial

**35.** Si d = {'nombre': 'Ana'}, ¿qué devuelve d['nombre']?
- [ ] A) 'Ana' con tipo int
- [ ] B) 'Ana' con tipo str
- [ ] C) Error
- [ ] D) None

**36.** ¿Cuál es la sintaxis para acceder a un valor en un diccionario?
- [ ] A) diccionario.clave
- [ ] B) diccionario[clave]
- [ ] C) diccionario->clave
- [ ] D) diccionario::clave

---

## 3. Control de Flujo

**37.** ¿Cuál es la palabra clave para condicionales en Python?
- [ ] A) if
- [ ] B) when
- [ ] C) switch
- [ ] D) condition

**38.** ¿Qué significa elif?
- [ ] A) else
- [ ] B) else if
- [ ] C) else if-else
- [ ] D) elif function

**39.** ¿Cuál es la sintaxis correcta para un bucle for?
- [ ] A) for (i = 0; i < 10; i++)
- [ ] B) for i in range(10):
- [ ] C) for i from 0 to 10
- [ ] D) for(i; 0; 10)

**40.** ¿Qué valores produce range(1, 4)?
- [ ] A) 1, 2, 3, 4
- [ ] B) 0, 1, 2, 3
- [ ] C) 1, 2, 3
- [ ] D) 1, 4

**41.** ¿Cuándo termina un bucle while?
- [ ] A) Siempre después de 10 iteraciones
- [ ] B) Cuando se cumple la condición
- [ ] C) Cuando la condición es falsa o hay break
- [ ] D) Nunca

**42.** ¿Cuál es la diferencia entre for y while?
- [ ] A) No hay diferencia
- [ ] B) for itera sobre secuencias, while repite mientras condición sea verdadera
- [ ] C) while es más rápido
- [ ] D) for es para strings, while para números

---

## 4. Funciones

**43.** ¿Cuál es la palabra clave para definir una función?
- [ ] A) function
- [ ] B) func
- [ ] C) def
- [ ] D) define

**44.** ¿Cuál es la palabra clave para retornar valores?
- [ ] A) give
- [ ] B) return
- [ ] C) exit
- [ ] D) output

**45.** ¿Qué es un parámetro con valor por defecto?
- [ ] A) Parámetro que no se usa
- [ ] B) Parámetro opcional con valor asignado
- [ ] C) Parámetro obligatorio
- [ ] D) Parámetro booleano

**46.** ¿Puede una función retornar múltiples valores?
- [ ] A) No, solo uno
- [ ] B) Sí, mediante tuplas
- [ ] C) Solo si es recursiva
- [ ] D) Solo si es asincrónica

---

## 5. Programación Orientada a Objetos

**47.** ¿Qué es una clase?
- [ ] A) Un tipo de función
- [ ] B) Uma plantilla para crear objetos
- [ ] C) Una variable global
- [ ] D) Un módulo

**48.** ¿Qué es un objeto?
- [ ] A) Una función
- [ ] B) Una instancia de una clase
- [ ] C) Un diccionario
- [ ] D) Una lista

**49.** ¿Cuál es el método constructor en Python?
- [ ] A) constructor()
- [ ] B) __init__()
- [ ] C) create()
- [ ] D) init()

**50.** ¿Qué representa self en POO?
- [ ] A) La clase
- [ ] B) La instancia actual del objeto
- [ ] C) Una variable global
- [ ] D) Un método estático

---

## 6. Manejo de Excepciones

**51.** ¿Cuál es la palabra clave para manejar excepciones?
- [ ] A) catch
- [ ] B) handle
- [ ] C) try
- [ ] D) error

**52.** ¿En qué bloque va el código que puede fallar?
- [ ] A) except
- [ ] B) finally
- [ ] C) try
- [ ] D) handle

**53.** ¿Cuándo se ejecuta el bloque finally?
- [ ] A) Solo si hay error
- [ ] B) Solo si no hay error
- [ ] C) Siempre
- [ ] D) Nunca

**54.** ¿Qué excepción se lanza al dividir por cero?
- [ ] A) ValueError
- [ ] B) TypeError
- [ ] C) ZeroDivisionError
- [ ] D) ArithmeticError

---

## 7. Formatos de Datos

**55.** ¿CSV es un formato?
- [ ] A) Estructurado
- [ ] B) Semi-estructurado
- [ ] C) No estructurado
- [ ] D) Binario

**56.** ¿Qué significa CSV?
- [ ] A) Comma-Separated Values
- [ ] B) Comma-Structured Vector
- [ ] C) Common Separated Values
- [ ] D) Comma-Series Values

**57.** ¿Cuáles son los tipos de formatos de datos?
- [ ] A) Solo estructurados y no estructurados
- [ ] B) Estructurados, semi-estructurados y no estructurados
- [ ] C) Estructurados y comprimidos
- [ ] D) Locales y remotos

**58.** ¿CSV es un formato?
- [ ] A) Semi-estructurado
- [ ] B) Estructurado
- [ ] C) No estructurado
- [ ] D) Propietario

**59.** El formato JSON es:
- [ ] A) Estructurado
- [ ] B) Semi-estructurado
- [ ] C) No estructurado
- [ ] D) Propietario

**60.** ¿Cuál es una ventaja de JSON frente a CSV?
- [ ] A) Ocupa menos espacio
- [ ] B) Es más rápido
- [ ] C) Puede representar estructuras complejas y anidadas
- [ ] D) Es más antiguo

**61.** ¿Qué formato es ideal para Big Data?
- [ ] A) CSV
- [ ] B) JSON
- [ ] C) Parquet
- [ ] D) XML

**62.** ¿A qué ecosistema pertenecen Parquet y Avro?
- [ ] A) Microsoft
- [ ] B) Google Cloud
- [ ] C) Apache
- [ ] D) Amazon

**63.** ¿Cuál es una ventaja de Parquet?
- [ ] A) Almacenamiento basado en columnas
- [ ] B) Compresión eficiente
- [ ] C) Mejora el rendimiento de lectura
- [ ] D) Todas las anteriores

**64.** ¿Para qué se utiliza Avro?
- [ ] A) Almacenamiento de imágenes
- [ ] B) Serialización de datos y streaming
- [ ] C) Análisis de datos
- [ ] D) Compresión de archivos

**65.** Para trabajar con Parquet en Pandas, ¿qué paquete debo instalar?
- [ ] A) pandas-parquet
- [ ] B) pyarrow
- [ ] C) parquet-py
- [ ] D) arrow

**66.** Para trabajar con Avro en Pandas, ¿qué paquete debo instalar?
- [ ] A) pandas-avro
- [ ] B) fastavro
- [ ] C) avro-py
- [ ] D) avro-tools

---

## 8. Pandas - Carga e Inspección

**67.** ¿Qué es un DataFrame?
- [ ] A) Un archivo
- [ ] B) Una estructura bidimensional similar a una tabla
- [ ] C) Un tipo de dato primitivo
- [ ] D) Un módulo de Python

**68.** ¿Cuál es el comando para leer un archivo CSV con Pandas?
- [ ] A) pd.load_csv()
- [ ] B) pd.read_csv()
- [ ] C) pd.import_csv()
- [ ] D) pd.open_csv()

**69.** ¿Cuál es el comando para guardar un DataFrame a CSV?
- [ ] A) df.save_csv()
- [ ] B) df.to_csv()
- [ ] C) df.write_csv()
- [ ] D) df.export_csv()

**70.** ¿Qué método muestra las primeras 5 filas de un DataFrame?
- [ ] A) df.first()
- [ ] B) df.top()
- [ ] C) df.head()
- [ ] D) df.display()

**71.** ¿Cuál es el comando para obtener información del DataFrame?
- [ ] A) df.summary()
- [ ] B) df.info()
- [ ] C) df.describe()
- [ ] D) df.stats()

**72.** ¿Qué método devuelve estadísticas descriptivas?
- [ ] A) df.summary()
- [ ] B) df.stats()
- [ ] C) df.describe()
- [ ] D) df.summary_statistics()

---

## 9. Pandas - Selección y Filtrado

**73.** ¿Cómo se selecciona una columna en Pandas?
- [ ] A) df.select('columna')
- [ ] B) df['columna']
- [ ] C) df.get('columna')
- [ ] D) df.columna()

**74.** Si quiero filtrar `df` donde 'edad' > 25, ¿cuál es la sintaxis correcta?
- [ ] A) df.filter(df['edad'] > 25)
- [ ] B) df[df['edad'] > 25]
- [ ] C) df.where(edad > 25)
- [ ] D) df.select(edad > 25)

**75.** ¿Cómo se seleccionan múltiples columnas en Pandas?
- [ ] A) df.select(['col1', 'col2'])
- [ ] B) df[['col1', 'col2']]
- [ ] C) df.get('col1', 'col2')
- [ ] D) df.columns(['col1', 'col2'])

**76.** Si quiero crear una nueva columna `df['full_name']` concatenando 'firstname' y 'lastname', ¿cuál es la sintaxis?
- [ ] A) df['full_name'] = df['firstname'] + df['lastname']
- [ ] B) df.with_columns('full_name', df['firstname'] + df['lastname'])
- [ ] C) df['full_name'] = concat(df['firstname'], df['lastname'])
- [ ] D) df['full_name'] = merge(df['firstname'], df['lastname'])

**77.** ¿Cómo se modifica un valor en una columna de Pandas?
- [ ] A) df['columna'][índice] = nuevo_valor
- [ ] B) df.set_value(índice, 'columna', nuevo_valor)
- [ ] C) df.loc[índice, 'columna'] = nuevo_valor
- [ ] D) Todas las anteriores

---

## 10. Pandas - Agrupación y Ordenación

**78.** ¿Cuál es el método para agrupar datos por una columna?
- [ ] A) df.group()
- [ ] B) df.groupby()
- [ ] C) df.aggregate()
- [ ] D) df.cluster()

**79.** Si quiero agrupar por 'edad' y contar ocurrencias, ¿cuál es la sintaxis?
- [ ] A) df.groupby('edad').count()
- [ ] B) df.groupby('edad').size()
- [ ] C) df.groupby('edad').sum()
- [ ] D) df.groupby('edad').agg('count')

**80.** ¿Cuál es el método para ordenar un DataFrame?
- [ ] A) df.sort()
- [ ] B) df.sort_values()
- [ ] C) df.order()
- [ ] D) df.arrange()

**81.** Para ordenar de forma descendente, ¿cuál es el parámetro?
- [ ] A) order='DESC'
- [ ] B) ascending=False
- [ ] C) descending=True
- [ ] D) sort='descend'

**82.** ¿Cómo se concatenan dos DataFrames verticalmente?
- [ ] A) df1.concat(df2)
- [ ] B) pd.merge(df1, df2)
- [ ] C) pd.concat([df1, df2])
- [ ] D) df1.append(df2)

**83.** ¿Cuál es la diferencia entre concat y merge?
- [ ] A) concat une verticalmente, merge une horizontalmente por clave
- [ ] B) merge es más rápido
- [ ] C) concat solo funciona con 2 dataframes
- [ ] D) No hay diferencia

---

## 11. Polars - Lectura y Operaciones

**84.** ¿Cuál es el comando para leer un CSV con Polars?
- [ ] A) pl.load_csv()
- [ ] B) pl.read_csv()
- [ ] C) pl.import_csv()
- [ ] D) pl.open_csv()

**85.** ¿Cómo se selecciona una columna en Polars?
- [ ] A) df['columna']
- [ ] B) df.select('columna')
- [ ] C) df.get('columna')
- [ ] D) df.columna

**86.** ¿Cómo se crea una nueva columna en Polars?
- [ ] A) df['columna'] = valor
- [ ] B) df.with_columns((pl.col('col1') + pl.col('col2')).alias('nueva'))
- [ ] C) df.add_column('columna', valor)
- [ ] D) df.create_column('columna', valor)

**87.** ¿Cómo se filtra en Polars?
- [ ] A) df[df['edad'] > 25]
- [ ] B) df.filter(pl.col('edad') > 25)
- [ ] C) df.where(edad > 25)
- [ ] D) df.select(edad > 25)

**88.** ¿Cómo se agrupa en Polars?
- [ ] A) df.group()
- [ ] B) df.groupby()
- [ ] C) df.group_by()
- [ ] D) df.aggregate()

**89.** ¿Cómo se ordena en Polars?
- [ ] A) df.sort()
- [ ] B) df.sort_values()
- [ ] C) df.sort('columna', descending=False)
- [ ] D) df.order()

**90.** ¿Cuál es la principal ventaja de Polars sobre Pandas?
- [ ] A) Mejor legibilidad
- [ ] B) Mejor rendimiento y eficiencia en memoria
- [ ] C) Viene incluido en Python
- [ ] D) Es más antiguo

**91.** ¿Cuál es una característica de los DataFrames en Polars?
- [ ] A) Son mutables
- [ ] B) Cada operación genera un nuevo DataFrame
- [ ] C) Solo aceptan datos numéricos
- [ ] D) No permiten operaciones encadenadas

**92.** ¿Cómo se guarda un DataFrame en Polars a CSV?
- [ ] A) df.save_csv()
- [ ] B) df.to_csv()
- [ ] C) df.write_csv()
- [ ] D) df.export_csv()

**93.** ¿Cómo se guarda un DataFrame en Polars a Parquet?
- [ ] A) df.save_parquet()
- [ ] B) df.to_parquet()
- [ ] C) df.write_parquet()
- [ ] D) df.export_parquet()

---

## 12. Comparación Pandas vs Polars

**94.** ¿Cuál de estas es una razón para usar Pandas?
- [ ] A) Es más rápido
- [ ] B) Es el estándar en la industria con comunidad establecida
- [ ] C) Tiene mejor sintaxis
- [ ] D) Consume menos memoria

**95.** ¿Cuál de estas es una razón para usar Polars?
- [ ] A) Viene incluido con Python
- [ ] B) Mejor performance con grandes volúmenes de datos
- [ ] C) Es más fácil de aprender
- [ ] D) Tiene más documentación

**96.** En Pandas, ¿qué devuelve `df.groupby('edad')['nombre'].apply(list)`?
- [ ] A) Un diccionario
- [ ] B) Una lista
- [ ] C) Una Series con listas de valores agrupados
- [ ] D) Un DataFrame

**97.** En Polars, para agrupar y obtener listas, ¿cuál es la sintaxis?
- [ ] A) df.groupby('edad').agg(pl.col('nombre'))
- [ ] B) df.groupby('edad')['nombre'].apply(list)
- [ ] C) df.group_by('edad').select(pl.col('nombre'))
- [ ] D) df.groupby('edad').collect()

---

## 13. Operaciones Prácticas

**98.** Si tengo `df = pd.read_csv('datos.csv')` y quiero las primeras 10 filas, ¿qué comando uso?
- [ ] A) df.head()
- [ ] B) df.head(10)
- [ ] C) df.first(10)
- [ ] D) df.limit(10)

**99.** ¿Cuál es el resultado de `'Anna'.upper()`?
- [ ] A) anna
- [ ] B) ANNA
- [ ] C) Anna
- [ ] D) aNA

**100.** Si quiero instalar pandas, polars y jupyter en un requirements.txt, ¿cuál es el formato?
- [ ] A) pandas polars jupyter
- [ ] B) pandas==polars==jupyter
- [ ] C) pandas\npolars\njupyter
- [ ] D) Cada librería en una línea separada

---

## SOLUCIONARIO

| Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta |
|----------|-----------|----------|-----------|----------|-----------|
| 1 | C | 34 | B | 67 | B |
| 2 | A | 35 | B | 68 | B |
| 3 | B | 36 | B | 69 | B |
| 4 | B | 37 | A | 70 | C |
| 5 | B | 38 | B | 71 | B |
| 6 | A | 39 | B | 72 | C |
| 7 | B | 40 | C | 73 | B |
| 8 | A | 41 | C | 74 | B |
| 9 | B | 42 | B | 75 | B |
| 10 | B | 43 | C | 76 | A |
| 11 | C | 44 | B | 77 | D |
| 12 | B | 45 | B | 78 | B |
| 13 | B | 46 | B | 79 | A |
| 14 | B | 47 | B | 80 | B |
| 15 | B | 48 | B | 81 | B |
| 16 | C | 49 | B | 82 | C |
| 17 | B | 50 | B | 83 | A |
| 18 | C | 51 | C | 84 | B |
| 19 | B | 52 | C | 85 | B |
| 20 | C | 53 | C | 86 | B |
| 21 | C | 54 | C | 87 | B |
| 22 | A | 55 | A | 88 | C |
| 23 | B | 56 | A | 89 | C |
| 24 | C | 57 | B | 90 | B |
| 25 | B | 58 | B | 91 | B |
| 26 | A | 59 | B | 92 | C |
| 27 | C | 60 | C | 93 | C |
| 28 | C | 61 | C | 94 | B |
| 29 | C | 62 | C | 95 | B |
| 30 | C | 63 | D | 96 | C |
| 31 | C | 64 | B | 97 | A |
| 32 | C | 65 | B | 98 | B |
| 33 | C | 66 | B | 99 | B |
| | | | | 100 | D |
