# Unidad 1. El ecosistema Python.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Instalación De Python](#2-instalación-de-python)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Instalación de Python en Windows](#22-instalación-de-python-en-windows)
  - [2.3 Instalación de Python en Linux](#23-instalación-de-python-en-linux)
  - [2.4 Instalación de Python en macOS](#24-instalación-de-python-en-macos)
- [3. Entornos (Ide) De Programación: Jupyter, Pycharm, Vscode](#3-entornos-ide-de-programación-jupyter-pycharm-vscode)
  - [3.1 Introducción](#31-introducción)
  - [3.2 El lenguaje de programación Python](#32-el-lenguaje-de-programación-python)
  - [3.3 Jupyter](#33-jupyter)
  - [3.4 PyCharm](#34-pycharm)
  - [3.5 Visual Studio Code (VSCode)](#35-visual-studio-code-vscode)
- [4. El Lenguaje Python: Sintaxis Y Estructuras Básicas](#4-el-lenguaje-python-sintaxis-y-estructuras-básicas)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Sintaxis básicas en Python](#42-sintaxis-básicas-en-python)
  - [4.3 Tipos de datos en Python](#43-tipos-de-datos-en-python)
  - [4.4 Estructuras de datos habituales en Python](#44-estructuras-de-datos-habituales-en-python)
  - [4.5 Estructuras de control de flujo de ejecución](#45-estructuras-de-control-de-flujo-de-ejecución)
  - [4.6 Funciones](#46-funciones)
  - [4.7 Programación orientada a objetos](#47-programación-orientada-a-objetos)
  - [4.8 Manejo de excepciones](#48-manejo-de-excepciones)
  - [4.9 Enlaces de interés](#49-enlaces-de-interés)
- [5. Librerías Python: Instalación, Mantenimiento Y Creación De Paquetes Propios](#5-librerías-python-instalación-mantenimiento-y-creación-de-paquetes-propios)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Instalación de librerías con pip](#52-instalación-de-librerías-con-pip)
  - [5.3 Instalación de librerías desde repositorios externos](#53-instalación-de-librerías-desde-repositorios-externos)
  - [5.4 Mantenimiento y actualización de librerías](#54-mantenimiento-y-actualización-de-librerías)
  - [5.5 Entornos virtuales](#55-entornos-virtuales)
  - [5.6 Creación de paquetes propios y publicación en PyPl](#56-creación-de-paquetes-propios-y-publicación-en-pypl)
- [6. Introducción A Formatos De Datos: Csv, Json, Parquet, Avro](#6-introducción-a-formatos-de-datos-csv-json-parquet-avro)
  - [6.1 Introducción](#61-introducción)
  - [6.2 Tipos de datos](#62-tipos-de-datos)
  - [6.3 CSV (Comma-Separated Values)](#63-csv-comma-separated-values)
  - [6.4 JSON (JavaScript Object Notation)](#64-json-javascript-object-notation)
  - [6.5 Parquet](#65-parquet)
  - [6.6 Avro](#66-avro)
  - [6.7 Enlaces de interés](#67-enlaces-de-interés)
- [7. Manipulación Y Análisis De Datos Con Pandas Y Polars](#7-manipulación-y-análisis-de-datos-con-pandas-y-polars)
  - [7.1 Introducción](#71-introducción)
  - [7.2 Carga e inspección de datos](#72-carga-e-inspección-de-datos)
  - [7.3 Selección, filtrado y creación](#73-selección-filtrado-y-creación)
  - [7.4 Agrupación, ordenación y unión](#74-agrupación-ordenación-y-unión)
  - [7.5 Enlaces de interés](#75-enlaces-de-interés)
- [8. Conclusiones](#8-conclusiones)
  - [8.1 Conclusiones de la unidad](#81-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad didáctica, se explorará el ecosistema Python, proporcionando una comprensión de sus componentes más relevantes y su aplicación en el análisis de datos. Python es un lenguaje de programación versátil y ampliamente utilizado en diversas áreas, incluyendo la ciencia de datos, el aprendizaje automático y el desarrollo web.

A continuación, se presentarán los fundamentos del lenguaje Python, abordando su sintaxis básica y sus estructuras de datos principales. También se discutirá la instalación y el mantenimiento de librerías en Python, enfatizando su importancia en la expansión de sus capacidades y en la realización de tareas específicas. Además, introduciremos los formatos de datos más comunes, como CSV, JSON, Parquet y Avro, que son fundamentales para el manejo de datos.

Finalmente, exploraremos cómo utilizar las librerías Pandas y Polars para la manipulación y análisis de datos, herramientas esenciales en la ciencia de datos que permiten realizar operaciones complejas de manera eficiente y efectiva.



- **Instalación de Python**  
  Antes de instalar cualquier IDE o herramienta adicional, es fundamental tener Python instalado en el sistema. A continuación, veremos los pasos instalar Python en Windows, macOS y Linux.
- **Entornos (IDE) de Programación: Jupyter, Pycharm, VsCode**  
  En este apartado vamos a conocer los IDEs más utilizados cuando se quiere programar en Python. Un IDE es una herramienta que facilita la escritura, ejecución y depuración de código, ofreciendo funcionalidades que mejoran la productividad del desarrollador.
- **El lenguaje Python: Sintaxis y Estructuras básicas**  
  En este apartado, introduciremos los elementos esenciales del lenguaje Python, incluyendo su sintaxis básica, tipos de datos fundamentales y estructuras de control de flujo. Aprenderemos a escribir y ejecutar scripts simples, realizar operaciones aritméticas y lógicas, y manipular datos utilizando listas, tuplas, diccionarios y estructuras similares.
- **Librerías Python: Instalación, mantenimiento y creación de paquetes propios**  
  Este apartado introduce a los estudiantes a la gestión de paquetes en Python, aprenderemos a instalar y mantener librerías utilizando el gestor de paquetes pip, a crear entornos virtuales para aislar dependencias y a crear nuestros propios paquetes, incluyendo cómo publicarlos en el repositorio oficial de Python, PyPI.
- **Introducción a formatos de datos: CSV, JSON, PARQUET, AVRO**  
  En este apartado, exploraremos los formatos de datos más utilizados: CSV, JSON, Parquet y Avro, y aprenderemos cómo trabajar con ellos en Python.
- **Manipulación y Análisis de datos con Pandas y Polars**  
  En este apartado, exploraremos cómo utilizar ambas librerías para manipular y analizar datos de manera efectiva.



#### Objetivos



En esta unidad se plantean los siguientes objetivos:



1. Comprender el ecosistema Python y su relevancia en la ciencia de datos.
2. Familiarizarse con los entornos de desarrollo integrados para Python y seleccionar el más adecuado según sus necesidades.
3. Entender la sintaxis básica de Python y las estructuras de datos fundamentales.
4. Instalar y mantener librerías en Python de manera eficiente.
5. Conocer y manejar diferentes formatos de datos como CSV, JSON, Parquet y Avro.
6. Utilizar las librerías Pandas y Polars para manipular y analizar datos.



## 2. Instalación De Python



### 2.1 Introducción



![image](assets/cm5xt2du500583571wvmro0rl-stock-image.jpg)



Antes de instalar cualquier IDE o herramienta adicional, es fundamental tener Python instalado en el sistema. A continuación, veremos los pasos instalar Python en Windows, macOS y Linux.



### 2.2 Instalación de Python en Windows



1. Entrar en la página web del siguiente enlace: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. En el apartado “Stable Releases”, hacer click en “Download Windows installer” de la versión correspondiente y acorde a tu sistema operativo. Para este curso utilizaremos la última versión estable de Python 3.11.9, para Windows 64-bit: [https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)
3. ![image](assets/cm5xt6ghx009g3571syxr93id-step3-Imagen1.jpg)
   Ejecuta el instalador y En la primera pantalla, marcar la opción "Add Python 3.x to PATH" para añadir Python al PATH del sistema y facilitar su uso desde la línea de comandos.
4. Hacer click en “install now” y seguir las instrucciones.
5. Verifica la instalación ejecutando el siguiente comando en la terminal (CMD): python --version (o python3 --version)



### 2.3 Instalación de Python en Linux



Python viene preinstalado en gran parte de las distribuciones de Linux. Sin embargo, puede ser necesario instalar una versión más reciente o específica.



1. Actualizar los repositorios: sudo apt update.
2. Instalar Python 3: sudo apt install python3.
3. Instalar pip para gestionar paquetes: sudo apt install python3-pip.
4. Verificar la instalación: python3 –version.



### 2.4 Instalación de Python en macOS



1. Entrar en la página web del siguiente enlace: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. En el apartado “Stable Releases”, hacer click en “Download macOS installer” de la versión correspondiente y acorde a tu sistema operativo. Para este curso utilizaremos la última versión estable de Python 3.11.9: [https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg](https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg)
3. Ejecuta el instalador y seguir las instrucciones.
4. Verifica la instalación ejecutando el siguiente comando en la terminal (CMD): python3 --version



## 3. Entornos (Ide) De Programación: Jupyter, Pycharm, Vscode



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



En este apartado vamos a conocer los IDEs más utilizados cuando se quiere programar en Python. Un IDE es una herramienta que facilita la escritura, ejecución y depuración de código, ofreciendo funcionalidades que mejoran la productividad del desarrollador.



### 3.2 El lenguaje de programación Python



Python es un lenguaje de programación de alto nivel, interpretado y de propósito general, creado por Guido van Rossum y lanzado por primera vez en 1991. Se caracteriza por su sintaxis clara y legible, lo que facilita el aprendizaje y la escritura de código eficiente. Entre los paradigmas que soporta Python encontramos el orientado a objetos, funcional y procedimental.

Desde su creación, Python se ha consolidado como una herramienta fundamental en diversos campos como la ciencia de datos, la inteligencia artificial, la bioinformática y el desarrollo web. La elección de un lenguaje de programación para una solución particular a menudo se basa en la comunidad de desarrollo que lo respalda, y Python destaca en este aspecto debido a su vasta y activa comunidad.

Estudiar y utilizar Python es crucial, especialmente en áreas de análisis de datos, debido a la gran cantidad de bibliotecas y frameworks disponibles que abordan problemas específicos en diversas disciplinas científicas. Por ejemplo, en el ámbito de la ciencia de datos, bibliotecas como pandas, NumPy, SciPy y scikit-learn han hecho de Python el lenguaje preferido para el análisis y modelado de datos, facilitando a los investigadores y profesionales el desarrollo de soluciones eficientes y escalables.

La abundancia de bibliotecas especializadas en Python no solo facilita el acceso a herramientas avanzadas y métodos estadísticos, sino que también permite a los investigadores aprovechar las contribuciones y el conocimiento acumulado de la comunidad. Esto optimiza la calidad y la relevancia de sus trabajos en contextos científicos específicos.

Comparado con R, Python ofrece una mayor versatilidad y una integración más fluida con otras tecnologías y aplicaciones de software, lo que lo convierte en una opción más adecuada para proyectos que requieren un enfoque multidisciplinario. Además, la creciente popularidad de Python, como se ilustra en la gráfica adjunta de popularidad, demuestra su preferencia en la industria y la academia, impulsando el estudio y uso de Python, así como el desarrollo continuo de sus dependencias y paquetes asociados.

Todo ello ha hecho que Python se convierta en uno de los lenguajes populares de 2024, siguiendo la tendencia de los últimos años.



![image](assets/cm5xtj1fp00gm357112bia5um-Imagen2.jpg)



### 3.3 Jupyter



Dentro del ecosistema Jupyter, trabajaremos con JupyterLab es el entorno de desarrollo interactivo de última generación, diseñado para mejorar y ampliar las capacidades de Jupyter Notebook. Nos proporciona una interfaz más flexible y potente que permite trabajar con cuadernos (notebooks), editores de texto, terminales y otras herramientas en una sola aplicación unificada.

Para instalar JupyterLab, utilizaremos el gestor de paquetes pip, que se incluye con la instalación de Python.

1. **Abrir la terminal o CMD**
2. **Ejecutar:** Windows & Mac: pip install jupyterlab Linux: pip3 install jupyterlab
3. **Verifica la instalación inicializando jupyter ejecutando en la terminal**: jupyter lab

Entre sus características principales encontramos:

1. **Celdas interactivas**: permite ejecutar código en bloques denominados celdas.
2. **Visualización integrada**: soporta la integración de gráficos y visualizaciones directamente en el cuaderno.
3. **Compatibilidad con múltiples lenguajes**: aunque está diseñado para Python, Jupyter soporta otros lenguajes a través de kernels.



### 3.4 PyCharm



PyCharm es un IDE centrado para el desarrollo en Python. Ha sido creado por JetBrains, misma compañía que el famoso IntelliJ. Ofrece herramientas avanzadas para escribir, depurar y probar código, y es ampliamente utilizado tanto en la industria como en el ámbito académico.

PyCharm dispone de dos versiones: Community (gratuita) y Professional (de pago). En este curso utilizaremos la versión Community. Para instalar:

1. Accede a [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
2. ![image](assets/cm5xtm8im00hq35710woz0ki6-step2-Imagen3.jpg)
   Hacer click en descargar la edición Community
3. Seguir las instrucciones de instalación. En caso de que lo pregunte, marcar la opción “Update PATH variable”.



Entre sus características principales encontramos:

1. **Autocompletado inteligente**: Sugerencias de código basadas en el contexto.
2. **Depurador gráfico**: Herramientas para inspeccionar variables y flujos de ejecución.
3. **Integración con sistemas de control de versiones**: Soporte para Git, SVN, entre otros.



### 3.5 Visual Studio Code (VSCode)



VS Code es un IDE que ha sido desarrollado por Microsoft. Se ha vuelto muy popular por su flexibilidad y amplia gama de extensiones, así como cierto carácter open-source. Aunque no es un IDE exclusivo para Python, se puede configurar para ofrecer una experiencia completa de desarrollo en este lenguaje.

VSCode es gratuito y se puede descargar desde el sitio oficial:

1. Accede a [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Hacer click en descargar
3. Seguir las instrucciones de instalación.

A continuación, deberemos instalar ciertas extensiones para habilitar Python y Jupyter.

1. ![image](assets/cm5xtr7h300kl3571q1j8mkcy-step1-Imagen4.png)
   Abrir VSCode y navegar a la sección de extensiones.
2. ![image](assets/cm5xtr7h300kl3571q1j8mkcy-step2-Imagen5.jpg)
   Buscar “Python” e instalar “Python” y “Python debugger”
3. ![image](assets/cm5xtr7h300kl3571q1j8mkcy-step3-Imagen6.jpg)
   Buscar “Jupyter” e instalar “Jupyter”.
4. Reiniciar VSCode si es necesario.



Entre sus características principales encontramos:

1. **Extensibilidad:** gran cantidad de extensiones disponibles para personalizar y ampliar funcionalidades.
2. **Terminal integrada:** acceso rápido a la línea de comandos desde el editor.
3. **Depuración y pruebas:** herramientas para depurar código y ejecutar pruebas unitarias.



![image](assets/cm5xtvxgt00na3571e934o8bq-Imagen7.png)



Por facilidad de integración y opciones que no requieren pago adicional, en este curso utilizaremos VSCode.



## 4. El Lenguaje Python: Sintaxis Y Estructuras Básicas



### 4.1 Introducción



![image](assets/cm5xtxrgo00p5357184ym5736-stock-image.jpg)



La programación básica en Python es fundamental para desarrollar aplicaciones en diversos campos como la ciencia de datos, el aprendizaje automático y el desarrollo web. En este apartado, introduciremos los elementos esenciales del lenguaje Python, incluyendo su sintaxis básica, tipos de datos fundamentales y estructuras de control de flujo. Aprenderemos a escribir y ejecutar scripts simples, realizar operaciones aritméticas y lógicas, y manipular datos utilizando listas, tuplas, diccionarios y estructuras similares.



### 4.2 Sintaxis básicas en Python



La sintaxis básica en Python es sencilla y legible, lo que facilita su aprendizaje y uso. Las instrucciones fundamentales incluyen la asignación de variables, las operaciones aritméticas básicas y la capacidad de imprimir resultados en la consola.

Otro recurso muy útil es la capacidad de comentar código, que se realiza con el símbolo #.

Un ejemplo de estas tareas es el siguiente:



```ini
# Asignación de variables
x = 10
y = 5

# Operaciones aritméticas básicas
suma = x + y
resta = x - y
producto = x * y
cociente = x / y

# Imprimir resultados
print(suma)       # Output: 15
print(resta)      # Output: 5
print(producto)   # Output: 50
print(cociente)   # Output: 2.0
```



Para ejecutar el siguiente código en VSCode, se deben seguir los siguientes pasos:

1. Con el IDE abierto, navegar por las siguientes opciones en el apartado File: File > New File > Jupyter Notebook
2. En el archivo abierto, hacemos click en la celda que aparece vacía y pegamos el código.
3. ![image](assets/cm5xu0s6t00sh3571v7bwh60v-step3-INSD_BAIN_U1_Imagen8.jpg)
   Hacemos click en el botón de ejecutar o bien por atajos (Ctrl + Shift en Windows). Al ejecutar el código, los resultados aparecerán en la consola o directamente debajo de la celda.
4. Finalmente, podemos guardar el archivo con Ctrl + S e incluso guardarlo en un repositorio de Git.



### 4.3 Tipos de datos en Python



Los tipos de datos básicos en Python son similares a los de otros lenguajes de programación y son fundamentales para manejar información. Estos incluyen:



- **Datos de tipo numéricos**  
  1. **Enteros (int):** números sin parte decimal, por ejemplo, 42.
  2. **Flotantes (float):** números con parte decimal, por ejemplo, 3.14.
- **Datos de tipo cadena de texto (str)**  
  Representan secuencias de caracteres, por ejemplo, "Hola, mundo".
- **Datos de tipo lógico (bool)**  
  Representan valores de verdad, True o False.



Un ejemplo de cuál es la nomenclatura que estos siguen en Python es el siguiente:



```ini
# Números
numero_entero = 42
numero_flotante = 3.14

# Cadenas de texto
texto = "Hola, mundo"

# Valores lógicos
logico = True

# Imprimir valores
print(numero_entero)    # Output: 42
print(numero_flotante)  # Output: 3.14
print(texto)            # Output: Hola, mundo
print(logico)           # Output: True
```



### 4.4 Estructuras de datos habituales en Python



Python ofrece diversas estructuras de datos que permiten almacenar y manipular colecciones de elementos de manera eficiente. Las más habituales son: Listas (List), Tuplas (Tuple), Conjuntos (Set) y Diccionarios (Dictionary).



#### Listas (List)



Una lista (list) es una colección que se caracteriza por ser ordenada y mutable, que puede contener elementos de diferentes tipos, tales como strings, números e incluso objetos o estructuras de datos como diccionarios. Se puede acceder a un elemento de la lista indicándolo entre corchetes. Es importante recordar que la numeración de las listas comienza en 0, es decir, el primer elemento se accedería con: mi_lista[0].

Un ejemplo básico de esta estructura es el siguiente.



```markdown
# Definición de una lista

lista = [1, 2, 3, 4, 5]

 

# Acceso a elementos

print(lista[0])    # Output: 1

 

# Modificación de elementos

lista[1] = 10

 

# Añadir elementos

lista.append(6)

 

# Recorrer una lista

for elemento in lista:

   print(elemento)
```



Esto nos devuelve por pantalla lo siguiente.



```ini
1

1

10

3

4

5

6
```



#### Tuplas (Tuple)



Las tuplas (tuple) se diferencian de las listas en que son inmutables, es decir, una vez creadas no se pueden modificar.

Mientras que las listas las definimos mediante corchetes [], las tuplas las definimos entre paréntesis ().



```ruby
# Definición de una tupla

tupla = (1, 2, 3)

 

# Acceso a elementos

print(tupla[0])    # Output: 1

 

# Las siguientes operaciones no son válidas y generarían un error

# tupla[1] = 10

# tupla.append(4)
```



#### Conjuntos (Set)



Un conjuntos o set, es una colección desordenada (a diferencia de las listas, las cuales eran ordenadas) de elementos únicos, útiles para operaciones de conjunto como unión e intersección.

La forma de definir un conjunto es entre llaves {}.



```markdown
# Definición de un conjunto

conjunto_1 = {1, 2, 3, 3}

 

# Los elementos duplicados se eliminan

print(conjunto_1)    # Output: {1, 2, 3}

 

# Añadir elementos

conjunto_1.add(4)

 

# Operaciones de conjunto

conjunto_2 = {3, 4, 5}

union = conjunto_1.union(conjunto_2)

print(union)

interseccion = conjunto_1.intersection(conjunto_2)

print(interseccion)
```



Como resultado, obtenemos lo siguiente



```css
{1, 2, 3}

{1, 2, 3, 4, 5}

{3, 4}
```



#### Diccionarios



A una colección donde existen pares de clave-valor y siendo las claves únicas, se le conoce como diccionario. Los diccionarios son mutables, es decir, se pueden añadir o eliminar claves, valores e incluso modificarlos. Como valores de las claves, también podemos encontrar otros objetos.

Su sintaxis es la siguiente, {‘key’:’value’}



```python
# Definición de un diccionario

diccionario = {'nombre': 'Ana', 'edad': 28}

 

# Acceso a valores

print(diccionario['nombre'])    # Output: Ana

 

# Modificación de valores

diccionario['edad'] = 29

 

# Añadir nuevos pares clave-valor

diccionario['ciudad'] = 'Madrid'

 

# Recorrer un diccionario

for clave, valor in diccionario.items():

   print(f"{clave}: {valor}")
```



### 4.5 Estructuras de control de flujo de ejecución



Para controlar el flujo, encontramos estructuras similares a las presentes en otros lenguajes. Concretamente, podemos encontrar las siguientes implementadas de forma nativa:

- Estructuras condicionales
- Estructuras de tipo bucle



#### Estructuras condicionales



La sintaxis de**las estructuras condicionales** en Python utiliza la palabra clave if, seguida opcionalmente por elif (else if) y else.



```python
# Estructuras condicionales

x = 7

 

if x > 5:

   print("x es mayor que 5")

else:

   print("x es menor o igual a 5")
```



#### Estructuras de tipo bucle



Las  **estructuras de tipo bucle** se dividen en dos tipos: los bucles “for” y los “while”.

En el caso de “for” se utiliza para iterar sobre una secuencia, como por ejemplo una lista o tupla. La sintaxis de los bucles “for”es la siguiente.



```python
# Bucle For

for i in [1, 2, 3, 4, 5]:

   print(i)

 

# Utilizar la función range()

for i in range(1, 6):

   print(i)
```



En el caso de un bucle “while”, el bloque de código se repite mientras la condición sea verdadera. La sintaxis de los bucles “while” es la siguiente.



```haskell
# Bucle While

contador = 1

 

while contador <= 5:

   print(contador)

   contador += 1
```



### 4.6 Funciones



Una función de Python es un bloque de código reutilizable que permite realizar tareas específicas. Su sintaxis es similar a otros lenguajes de programación. Al igual que en estos lenguajes, las funciones en Python pueden aceptar argumentos, ejecutar operaciones y devolver resultados. Para definirlas se utiliza la palabra “def”, seguidas del nombre de la función y paréntesis que pueden contener parámetros

Por ejemplo, una función que suma dos números se define de la siguiente manera:



```yaml
# Definición de una función
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamada a la función
print(sumar(5, 10))    # Output: 15
```



Las funciones pueden tener parámetros opcionales, valores por defecto y pueden devolver múltiples valores.



```ini
# Función con parámetros por defecto
def saludar(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}!"

print(saludar("Carlos"))                # Output: Hola, Carlos!
print(saludar("Ana", "Buenos días"))    # Output: Buenos días, Ana!
```



### 4.7 Programación orientada a objetos



La programación orientada a objetos (POO) es un paradigma que organiza el diseño de software alrededor de objetos, que pueden contener datos y código para manipular esos datos. Python soporta plenamente la POO, permitiendo crear clases, instanciar objetos.

Una clase se entiende como una plantilla donde se definen las propiedades y comportamientos (atributos y métodos) que tendrán los objetos creados a partir de ella.

Por otro lado, un objeto sería una instancia de la clase creada, es decir, una entidad que posee los atributos y métodos definidos en la clase.



![image](assets/cm5xukvxs015k3571tn93cg2a-Imagen10.png)



Para definir una clase en Python, se hará mediante el uso de la clave class:



```python
# Definición de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
```



El método _ init _ es el constructor de la clase y se ejecuta al crear un nuevo objeto.

El uso de self se hace para referenciar a la instancia actual de la clase. Además, se utiliza para acceder a los atributos y métodos.

Para crear un objeto (instancia de una clase), simplemente llamamos a la clase como si fuera una función:



```ini
# Crear instancias de la clase Persona (objeto)
persona1 = Persona("Ana", 30)
persona2 = Persona("Luis", 25)

# Acceder a atributos y métodos
print(persona1.nombre)  # Output: Ana
persona2.saludar()      # Output: Hola, me llamo Luis y tengo 25 años.
```



### 4.8 Manejo de excepciones



El manejo de excepciones es esencial para crear programas robustos que puedan manejar errores y situaciones inesperadas sin interrumpir la ejecución del programa.

En Python existen múltiples tipos de excepciones tales como “ValueError”, “ZeroDivisionError” entre otras. Sin embargo, la manera más genérica de definir excepciones es la siguiente:



```python
# Código que puede generar una excepción
try:
    numero = int(input("Introduce un número entero: "))
    resultado = 10 / numero
except Exception as e:
    print("Ha ocurrido un error:", e)
finally:
    print("Fin del programa.")
```



### 4.9 Enlaces de interés



Por supuesto, abarcar todo el contenido del lenguaje de programación de Python no es el objetivo de este apartado ni unidad. Sin embargo, sí es importante tener claros los conceptos definidos.

Para poder consultar de forma más exhaustiva el amplio abanico de funcionalidades que vienen implementadas de forma nativa en Python, se proporcionan los siguientes enlaces.

Para consultar todo el listado de funciones y diferentes métodos de interacción con las estructuras de control se aconseja revisar las siguientes hojas de código de referencia:

- [https://www.pythoncheatsheet.org/](https://www.pythoncheatsheet.org/)
- [https://www.datacamp.com/cheat-sheet/category/python](https://www.datacamp.com/cheat-sheet/category/python)

De igual modo, se recomienda revisarse en profundidad la documentación oficial de Python

- [https://docs.python.org/es/3/tutorial/index.html](https://docs.python.org/es/3/tutorial/index.html)



## 5. Librerías Python: Instalación, Mantenimiento Y Creación De Paquetes Propios



### 5.1 Introducción



![image](assets/cm5xut0l401br3571i09twl57-stock-image.jpg)



La instalación de librerías, también conocidos como paquetes, en Python es un aspecto fundamental que permite a los usuarios extender las capacidades básicas del lenguaje para aplicaciones industriales y científicas.

Este apartado introduce a los estudiantes a la gestión de paquetes en Python, aprenderemos a instalar y mantener librerías utilizando el gestor de paquetes pip, a crear entornos virtuales para aislar dependencias y a crear nuestros propios paquetes, incluyendo cómo publicarlos en el repositorio oficial de Python, PyPI.

Comprender estos conceptos permitirá a los estudiantes gestionar eficientemente sus entornos de trabajo y aprovechar al máximo las herramientas disponibles en Python para realizar análisis de datos complejos y desarrollar soluciones robustas.



### 5.2 Instalación de librerías con pip



A la hora de trabajar con Python es necesario comprender cómo se maneja el versionado de las librerías.

La mayoría de los paquetes de código que posee el lenguaje, y a los que se le da un soporte continuo, se encuentran en el repositorio PyPi ([https://pypi.org/](https://pypi.org/))

El gestor de paquetes pip es la herramienta estándar para instalar y gestionar librerías en Python. Viene incluido con las versiones modernas de Python y permite instalar paquetes desde el Python Package Index (PyPI).

Para instalar una librería, se utiliza el comando pip install seguido del nombre del paquete. Esto descargará e instalará automáticamente la última versión disponible del paquete desde PyPI:



```ini
pip install nombre_de_la_libreria
```



Por ejemplo, para instalar la librería “requests” que utilizaremos para hacer llamadas HTTP, se haría mediante:



```ini
pip install requests
```



Al ejecutar este comando, pip buscará la librería requests en PyPI, descargará el paquete y lo instalará en tu entorno de Python. Una vez completado, podrás importar y utilizar requests en tus scripts

Para poder importar la biblioteca de código, una vez instalado, se debe ejecutar la siguiente instrucción:



```python
import setuptools # Para importar todo el paquete
from setuptools import setup, find_packages # Para importar solo las funciones necesarias
```



A veces es necesario instalar una versión específica de una librería, ya sea por compatibilidad o por requisitos del proyecto. Puedes especificar la versión exacta utilizando == seguido del número de versión.



```ini
pip install nombre_de_la_libreria==versión
```



Dado que los paquetes siguen un versionado semántico, si queremos instalar una versión específica de numpy sería:



```bat
pip install numpy==2.1.3
```



Cuando se trata de proyectos con múltiples dependencias, es común listar todas las librerías y sus versiones en un archivo requirements.txt. Esto facilita la instalación de todas las dependencias de una sola vez, asegurando que todos los colaboradores utilicen las mismas versiones.

Un ejemplo de archivo sería:



```ini
numpy==2.1.3 # Instalará version específica
polars>=1.16.0 # Instalará la versión definida o una superior en caso de haberla
requests
```



Para instalar estos paquetes simplemente deberemos navegar en el terminal hasta el directorio donde se encuentre el archivo y ejecutar:



```bat
pip install -r requirements.txt
```



### 5.3 Instalación de librerías desde repositorios externos



Además de instalar paquetes desde PyPI, pip permite instalar librerías directamente desde repositorios como GitHub. Esto es útil cuando necesitas una versión específica o en desarrollo de una librería que aún no ha sido publicada en PyPI.

Puedes instalar una librería directamente desde un repositorio utilizando la sintaxis git+URL:



```dockerfile
pip install git+https://github.com/usuario/repositorio.git
```



Por ejemplo, para instalar requests:



```dockerfile
pip install git+https://github.com/psf/requests.git
```



Puedes especificar una rama, etiqueta o incluso un commit específico añadiendo @ seguido de la referencia:



```dockerfile
pip install git+https://github.com/usuario/repositorio.git@rama
```



### 5.4 Mantenimiento y actualización de librerías



Aunque es muy habitual fijar versiones de los paquetes con los que trabajamos, es importante mantener las librerías actualizadas para beneficiarse de las últimas funcionalidades, mejoras de rendimiento y parches de seguridad.

Sin embargo, para conocer qué librerías deberemos actualizar en nuestro entorno virtual, lo primero que debemos conocer es cómo listar los paquetes instalados.

Para ello haremos uso del parámetro --list.



```bat
pip list
```



Un ejemplo de output sería:



```ini
Package                       Version
----------------------------- --------------
aiohttp                       3.8.5
aiosignal                     1.3.1
alembic                       1.13.3
annotated-types               0.7.0
```



El siguiente paso en el mantenimiento de un paquete sería actualizarla. Para actualizar un paquete a su versión más reciente, se utiliza el parámetro --upgrade:



```ini
pip install --upgrade nombre_de_la_libreria
```



Por ejemplo, para actualizar Polars sería:



```bat
pip install --upgrade polars
```



Por último, debemos conocer cómo desinstalar paquetes que no deseamos tener o no utilizamos para evitar conflictos, puedes desinstalarla con el siguiente comando:



```ini
pip uninstall nombre_de_la_libreria
```



Para desinstalar Polars sería:



```ini
pip uninstall polars
```



### 5.5 Entornos virtuales



Los entornos virtuales son espacios aislados que permiten gestionar las dependencias de proyectos de forma independiente. Esto evita conflictos entre librerías y versiones, especialmente cuando trabajas en múltiples proyectos con requisitos diferentes

Para crear entornos virtuales de manera sencilla podrás utilizar el módulo venv.

El siguiente comando creará un entorno virtual en el directorio donde estemos ubicados:



```bat
python -m venv nombre_entorno # Para Windows
python3 -m venv nombre_entorno # Para macOS o Linux
```



Una vez tenemos el entorno creado, deberemos activarlo para comenzar a utilizar los paquetes instalados en el mismo, o instalar nuevos paquetes en él de manera aislada.

Para activarlo, deberemos ejecutar el siguiente comando:



```bat
nombre_entorno\Scripts\activate # Para Windows
source nombre_entorno /bin/activate # Para macOS o Linux
```



Una vez hemos terminado de trabajar con el entorno virtual, deberemos desactivarlo para volver a nuestra línea de comandos normal.

Para ello ejecutaremos el siguiente comando:



```ini
deactivate
```



![image](assets/cm5y1bbml01hb3571jw5iullp-Imagen11.png)



En el siguiente video veremos una breve explicación de su importancia:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651977_1/scormcontent/assets/INSD_BAIN_U1_Video1.mp4?v=1)



### 5.6 Creación de paquetes propios y publicación en PyPl



Crear y publicar tus propios paquetes permite compartir tu trabajo con la comunidad y facilitar su instalación y uso mediante pip.



#### Estructura y código básico de un paquete



Para crear un paquete, debes organizar tu proyecto siguiendo una estructura específica.



![image](assets/cm5y4c7b6004b3570pdae6j3d-Imagen12.jpg)



Cada uno de estos directorios o archivos tiene una función:

- mi_paquete/: directorio raíz del proyecto.
- README.md: documento con descripción del paquete, instrucciones de instalación y uso.
- setup.py: script de configuración que define cómo se empaqueta y distribuye el paquete.
- mi_paquete/: carpeta que contiene el código del paquete.
- **init**.py: archivo que indica a Python que este directorio debe ser tratado como un paquete.
- modulo.py: archivo(s) con el código fuente del paquete.

Por ejemplo, podríamos encontrar el siguiente contenido en los archivos:



```python
# modulo.py
def saludar(nombre):
    return f"¡Hola, {nombre}!"
# __init__.py
from .modulo import saludar

__all__ = ['saludar']
```



#### Configuración para empaquetar



De cara a definir las instrucciones para empaquetar y distribuir tu librería, debemos definir el archivo pyproject.toml. El archivo pyproject.toml contiene la configuración necesaria para empaquetar e instalar tu librería. Utiliza setuptools para definir las propiedades de tu paquete.

Un ejemplo de archivo sería:



```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mi_paquete"
version = "0.1.0"
description = "Una descripción breve de tu paquete"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Nombre del autor", email = "autor.email@example.com"}
]
homepage = "https://github.com/tu_usuario/mi_paquete"
dependencies = []
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]
```



Cada uno de estos parámetros tiene una función:

- **name**: nombre del paquete tal como aparecerá en PyPI.
- **version**: número de versión siguiendo el esquema semántico (mayor.menor.parche).
- **author**: información de contacto.
- **description**: descripción breve del paquete.
- **homepage**: URL del proyecto, como el repositorio en GitHub.
- **dependencies**: lista de paquetes a incluir; find_packages() detecta automáticamente los paquetes en el directorio.
- **classifiers**: metadatos que ayudan a los usuarios a encontrar tu paquete.
- **Requires-python**: versiones de Python soportadas.

Como ejemplo de cómo se visualiza todo esto en PyPi, se puede consultar cualquier página de un paquete, como Polars: [https://pypi.org/project/polars/](https://pypi.org/project/polars/).



#### Preparación de archivos y subir a PyPi



Antes de subir el paquete, necesitamos generar los archivos de distribución. Para ello deberemos instalar:



```bat
pip install setuptools twine wheel build
```



Una vez instalados, deberemos navegar al directorio donde se encuentre nuestro pyproject.toml y ejecutar el siguiente comando:



```bat
python -m build # En caso de error, probar a usar python3 para macOS o Linux
```



Finalmente, antes de poder subir el paquete a los repositorios de PyPi, deberemos crear una cuenta y una API key en PyPI [https://pypi.org/](https://pypi.org/) o para test (recomendado en este curso) [https://test.pypi.org/](https://test.pypi.org/), [https://test.pypi.org/manage/account/token/](https://test.pypi.org/manage/account/token/).

Tras ello, deberemos ejecutar el siguiente comando para subir todos los paquetes en el directorio dist, creado por el paso anterior.



```bat
twine upload --repository testpypi dist/* -u __token__ -p <api_key>
```



Para probar si el paquete se ha subido correctamente a testpypi, podemos instalarlo de la siguiente manera:



```ini
pip install -i https://test.pypi.org/simple/ mi_paquete
```



A continuación, veremos el proceso completo de generar un paquete, subirlo a Test PyPi y descargarlo en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651977_1/scormcontent/assets/INSD_BAIN_U1_Video2.mp4?v=1)



#### Enlaces de interés



Para poder consultar de forma más exhaustiva el proceso de gestión de paquetes y de su publicación tenemos diversas fuentes:



> Guía oficial de gestión de paquetes
>
> [Link](https://packaging.python.org/en/latest/tutorials/installing-packages/)

> Guía oficial de empaquetado en Python
>
> [Link](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

> Documentación de setuptools
>
> [Link](https://setuptools.pypa.io/en/latest/)

> Documentación de twine
>
> [Link](https://twine.readthedocs.io/en/latest/)



## 6. Introducción A Formatos De Datos: Csv, Json, Parquet, Avro



### 6.1 Introducción



![image](assets/cm5y7dyhn00cq3570gco3t57c-stock-image.jpg)



La programación básica en Python constituye el fundamento sobre el cual se construyen aplicaciones de uso industrial y científico. En el análisis y manipulación de datos, es común trabajar con diferentes formatos de archivos que almacenan información de manera estructurada. Cada formato posee características, ventajas y casos de uso propias. En este apartado, exploraremos los formatos de datos más utilizados: CSV, JSON, Parquet y Avro, y aprenderemos cómo trabajar con ellos en Python.



### 6.2 Tipos de datos



En el análisis de datos, es fundamental identificar el tipo de datos con el que se está trabajando para seleccionar las herramientas y métodos más adecuados. Existen tres tipos de datos:



![image](assets/cm5y7gmn500eu3570dxvkif2c-Imagen13.png)

- **Datos estructurados**  
  Se organizan en formatos rígidos como tablas con filas y columnas, facilitando su almacenamiento y consulta.
- **Datos Semi-estructurados**  
  Poseen una organización parcial mediante etiquetas o esquemas flexibles, lo que permite una mayor adaptabilidad al integrar información diversa.
- **Datos no estructurados**  
  No siguen un esquema predefinido y abarcan una amplia variedad de formatos, lo que los hace más complejos de gestionar, pero altamente versátiles para capturar información rica y detallada.



En el video a continuación, entenderemos estas clasificaciones con mayor detalle:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651977_1/scormcontent/assets/INSD_BAIN_U1_Video3.mp4?v=1)



### 6.3 CSV (Comma-Separated Values)



El formato CSV se caracteriza por su simplicidad. Además, es ampliamente utilizado para almacenar datos tabulares en texto plano. En un archivo CSV, cada línea representa un registro, y los campos están separados por comas (u otro delimitador). Es compatible con la mayoría de las aplicaciones y lenguajes de programación.

Es un formato de datos estructurados que almacena información en tablas con filas y columnas, utilizando comas como delimitadores.

Un ejemplo de CSV podría ser:



```csv
"id","firstname","lastname","email"
"1","Kerry","O'Connell","Kerry16@gmail.com"
"2","Ethel","Miller","Ethel14@hotmail.com"
"3","Willie","Barton","Willie.Barton@gmail.com"
"4","Ellis","Lowe","Ellis.Lowe@gmail.com"
"5","Raymond","Miller","Raymond.Miller@gmail.com"
"6","Ellen","Thompson","Ellen92@hotmail.com"
"7","Joe","Rice","Joe55@gmail.com"
"8","Nathaniel","Legros","Nathaniel40@hotmail.com"
"9","Maxine","Schinner","Maxine93@hotmail.com"
"10","Tim","Jacobson","Tim92@hotmail.com"
```



Para trabajar con CSV utilizaremos Pandas o Polars y el concepto de dataframes, que se explicará en detalle en el siguiente apartado de esta unidad.

Antes de nada, debemos asegurar que tenemos instalados los paquetes. Como recomendación, se deberán instalar en un entorno virtual:



```bat
pip -m venv data-types # En Windows
pip3 -m venv data-types # En macOS y Linux
data-types/Source/activate # En Windows
source data-types/bin/activate # En macOS y Linux
pip install pandas polars # En Windows
pip3 install pandas polars # En macOS y Linux
```



Una vez instaladas en nuestro entorno virtual, podremos importarlas y utilizarlas para leer un csv gracias a la función .read_csv():



```python
# Lectura con pandas
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

df
```



```python
# Lectura con polars
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')

df
```



Como output tenemos un dataframe que se puede visualizar en un archivo de tipo .ipynb de la siguiente forma:



![image](assets/cm5y7rl2900m33570utcx101m-carousel1-Imagen14.jpg)

![image](assets/cm5y7rl2900m33570utcx101m-carousel2-Imagen15.jpg)



De igual modo, para escribir un csv, haremos uso del dataframe:



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

# Escritura
df.to_csv('datos_salida_pandas.csv')
```



```python
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')

# Escritura
df.write_csv('datos_salida_polars.csv')
```



Para CSV, hay numerosas opciones tales como elegir el delimitador, encoding e incluso índices que se pueden excluir cuando trabajamos con Pandas o Polars.

Adicionalmente, se puede trabajar con archivos CSV mediante el módulo CSV de python. Sin embargo, no es tan utilizado y puede llegar a tener cierta complejidad.



### 6.4 JSON (JavaScript Object Notation)



En el caso de JSON se trata de un formato ligero de intercambio de datos, fácilmente legible y de escribir. Es ideal para representar estructuras de datos complejas y anidadas, como objetos y arrays.

Representa datos semi-estructurados mediante una estructura de pares clave-valor, permitiendo una mayor flexibilidad en la organización de la información.

Un ejemplo de JSON:



```json
[
    {
        "id": 1,
        "firstname": "Julio",
        "lastname": "Pfannerstill",
        "email": "Julio.Pfannerstill39@hotmail.com"
    },
    {
        "id": 2,
        "firstname": "Suzanne",
        "lastname": "Murphy",
        "email": "Suzanne.Murphy22@hotmail.com"
    }
]
```



Al igual que con CSV, utilizaremos tanto Pandas como Polars para trabajar con este tipo de archivos:



```ruby
import pandas as pd

# Lectura
df = pd.read_json('data.json')

# Escritura
df.to_json('datos_salida_pandas.json')
```



```python
import polars as pl

# Lectura
df = pl.read_json('data.json')

# Escritura
df.write_json('datos_salida_polars.json')
```



De forma adicional, podemos trabajar directamente con el módulo json de python:



```python
# Uso de módulo JSON
import json

# Lectura
with open('datos.json') as f:
    data = json.load(f)
    print(data)

# Escritura
with open('datos_salida.json', 'w') as f:
    json.dump(data, f)
```



### 6.5 Parquet



Parquet es un formato de almacenamiento basado en columnas, diseñado para el procesamiento eficiente de grandes conjuntos de datos. Es especialmente útil en entornos de Big Data y cuando se trabaja con sistemas distribuidos como Hadoop o Spark.

Soporta compresión y codificación eficientes, lo que reduce el espacio de almacenamiento y mejora el rendimiento de lectura. Esto lo hace idóneo cuando trabajamos en entornos de Big Data.

Además, tanto Parquet como Avro, forman parte del ecosistema de Apache facilitando su integración y compartiendo beneficios con otras tecnologías como Kafka, Hive o Spark.

Para generar archivos Parquet de manera visual para ejemplos, utilizaremos: [https://konbert.com/generator/parquet](https://konbert.com/generator/parquet)

Para trabajar con ellos, en caso de utilizar Pandas, deberemos instalar el paquete pyarrow mediante:



```bat
pip install pyarrow
```



Una vez instalada la dependencia, podemos trabajar con estos archivos de la siguiente manera:



```ruby
import pandas as pd

# Lectura
df = pd.read_parquet('datos.parquet')

# Escritura
df.to_parquet('datos_salida_pandas.parquet')
```



```python
import polars as pl

# Lectura
df = pl.read_parquet('datos.parquet')

# Escritura
df.write_parquet('datos_salida_polars.parquet')
```



### 6.6 Avro



Avro es un sistema de serialización de datos que utiliza esquemas definidos en JSON para representar estructuras de datos complejas en formato binario. Es ampliamente utilizado en sistemas de Big Data y streaming, como Apache Kafka. Avro facilita la interoperabilidad entre diferentes sistemas y lenguajes de programación.

Se considera semi-estructurado debido a su capacidad de incluir un esquema que define la estructura de los datos, facilitando la serialización y deserialización eficiente

Un ejemplo de esquema podría ser:



```dart
schema = {
    'doc': 'documento Avro',
    'name': 'Usuario',
    'namespace': 'ejemplo.avro',
    'type': 'record',
    'fields': [
        {'name': 'name', 'type': 'string'},
        {'name': 'age', 'type': 'int'},
        {'name': 'city', 'type': 'string'},
    ],
}
```



Al igual que Parquet, forma parte del ecosistema de Apache facilitando su integración y compartiendo beneficios con otras tecnologías como Kafka.

Para generar archivos Avro de manera visual para ejemplos, utilizaremos: [https://konbert.com/generator/avro](https://konbert.com/generator/avro)

De igual forma que con Parquet, para tratar Avro con Pandas, debemos instalar el paquete fastavro:

pip install fastavro

Una vez instalada la dependencia, podemos trabajar con estos archivos de la siguiente manera:



```python
import fastavro
import pandas as pd

# Lectura
with open('datos.avro', 'rb') as f:
    avro_reader = fastavro.reader(f)
    schema = avro_reader.writer_schema
    df_avro = pd.DataFrame(avro_reader)

# Escritura
with open('datos_salida_pandas.avro', 'wb') as f:
    data = df_avro.to_dict('records')
    fastavro.writer(f, schema, data)
```



```python
import polars as pl

# Lectura
df = pl.read_avro('datos.avro')

# Escritura
df.write_avro('datos_salida_polars.avro')
```



A modo resumen, según el caso de uso será necesario utilizar un tipo de archivo u otro:



![image](assets/cm5y82t9y00su3570qgacpr6q-Imagen16.png)



A continuación, podremos ver un video donde comparamos los diferentes formatos:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651977_1/scormcontent/assets/INSD_BAIN_U1_Video4.mp4?v=1)



### 6.7 Enlaces de interés



> Trabajar con CSV mediante módulo nativo de Python
>
> [Link](https://docs.python.org/3/library/csv.html)

> Trabajar con JSON mediante módulo nativo de Python
>
> [Link](https://docs.python.org/3/library/json.html)

> Parquet VS Avro
>
> [Link](https://airbyte.com/data-engineering-resources/parquet-vs-avro)



## 7. Manipulación Y Análisis De Datos Con Pandas Y Polars



### 7.1 Introducción



![image](assets/cm5y89e8y00vv3570v8g9qbb9-stock-image.jpg)



La manipulación y análisis de datos son componentes centrales en la ciencia e ingeniería de datos. Python ofrece poderosas librerías para estas tareas, siendo Pandas la más popular y ampliamente utilizada. Polars es una librería más reciente que ofrece rendimiento mejorado y eficiencia en memoria debido a su implementación con Rust. Además, Polars está empezando a ofrecer posibilidad de procesamiento paralelizable.

En este apartado, exploraremos cómo utilizar ambas librerías para manipular y analizar datos de manera efectiva.

El elemento principal en ambas librerías es el de DataFrame. Este se trata de una estructura bidimensional (tabular) con columnas de diferentes tipos, similar a una hoja de cálculo o una tabla SQL.



### 7.2 Carga e inspección de datos



La primera etapa en el análisis de datos es la carga de estos desde diversas fuentes tales como CSV, JSON, Parquet o Avro. En este caso, veremos cómo leer archivos CSV.

Como hemos visto en el apartado anterior, la manera de cargar datos desde un CSV es simple.



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')
```



```ini
import polars as pl

# Lecturadf = pl.read_csv('datos.csv')
```



Adicionalmente, podemos obtener cierta información de nuestro DataFrame, por ejemplo, podemos extraer las N primeras filas:



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

print(df.head(10)) # Por defecto las 5 primeras
```



```python
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')

print(df.head(10)) # Por defecto las 5 primeras
```



![image](assets/cm5y8cwc200xz3570ssk6hklf-carousel1-Imagen17.jpg)

![image](assets/cm5y8cwc200xz3570ssk6hklf-carousel2-Imagen18.jpg)



Como podemos ver, visualmente podemos observar ciertas diferencias en la información que nos proporciona cada librería. En el caso de Polars directamente podemos observar el tamaño del output, 5 filas y 4 columnas, además del tipo de dato de cada columna.

Adicionalmente, podemos obtener más información que nos ayudarán a describir nuestro DataFrame de la siguiente manera:



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')


print(df.info()) # Información del DataFrame
print(df.describe(include='all')) # Información descriptiva
```



```ruby
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')
print(f'df types: {df.dtypes}') # Información del DataFrame

print(f'df size: {df.shape}') # Información del DataFrame
print(df.describe()) # Información descriptiva
```



![image](assets/cm5y8f4to00zh35702789dnxd-carousel1-Imagen19.jpg)

![image](assets/cm5y8f4to00zh35702789dnxd-carousel2-Imagen20.jpg)



Sin embargo, en este caso, es Pandas quien proporciona más información sobre nuestros datos de manera sencilla. Obtener la misma información con Polars requerirá mayor complejidad.



### 7.3 Selección, filtrado y creación



La capacidad de seleccionar y filtrar es fundamental en el análisis e ingeniería de datos. En este caso, ambos paquetes ofrecen una solución ligeramente diferente.



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

columna_firstname = df['firstname']
print(columna_firstname)

columnas_multiples = df[['firstname', 'lastname']]
print(columnas_multiples)
```



```python
# Lectura
df = pl.read_csv('datos.csv')

columna_firstname = df.select('firstname')
print(columna_firstname)


columnas_multiples = df.select(['firstname', 'lastname'])
print(columnas_multiples)
```



![image](assets/cm5y8hktz011r3570y5e1eo3f-carousel1-Imagen21.jpg)

![image](assets/cm5y8hktz011r3570y5e1eo3f-carousel2-Imagen22.jpg)



Para filtrar, la sintaxis es sencilla, simplemente deberemos extender la utilizada previamente para seleccionar columnas. Por ejemplo, en Pandas bastará con igualar el valor de la columna y en Polars deberemos usar el método “filter”de la siguiente manera:



```python
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

columna_filtrada = df[df['firstname'] == 'Kerry' ]
print(columna_filtrada)

# Output
id firstname   lastname              email
0   1     Kerry  O'Connell  Kerry16@gmail.com
```



```python
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')

columna_filtrada = df.filter(pl.col('firstname') == "Kerry")
print(columna_filtrada)

# Output
```



![image](assets/cm5zp7ber004o356x0smgq9ei-Imagen1.png)



También podemos crear nuevas columnas a la vez que las completamos con valores:



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

df['full_name'] = df['firstname'] + df['lastname']
df['full_name']

# Output
0     KerryO'Connell
1        EthelMiller
2       WillieBarton
3          EllisLowe
4      RaymondMiller
5      EllenThompson
6            JoeRice
7    NathanielLegros
8     MaxineSchinner
9        TimJacobson
```



```python
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')

df = df.with_columns((pl.col('firstname')+pl.col('lastname')).alias('full_name'))
df.select('full_name')

# Output
full_name
str
"KerryO'Connell"
"EthelMiller"
"WillieBarton"
"EllisLowe"
"RaymondMiller"
"EllenThompson"
"JoeRice"
"NathanielLegros"
"MaxineSchinner"
"TimJacobson
```



Para modificar columnas podemos operar sobre ella misma de la siguiente forma:



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

df['full_name'] = df['firstname'] + df['lastname']
df['full_name'] = df['full_name']+df['email']
df['full_name']

# Output
0           KerryO'ConnellKerry16@gmail.com
1            EthelMillerEthel14@hotmail.com
2       WillieBartonWillie.Barton@gmail.com
3             EllisLoweEllis.Lowe@gmail.com
4     RaymondMillerRaymond.Miller@gmail.com
5          EllenThompsonEllen92@hotmail.com
6                    JoeRiceJoe55@gmail.com
7    NathanielLegrosNathaniel40@hotmail.com
8        MaxineSchinnerMaxine93@hotmail.com
9              TimJacobsonTim92@hotmail.com
```



```python
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')

df = df.with_columns((pl.col('firstname')+pl.col('lastname')).alias('full_name'))
df = df.with_columns((pl.col('full_name')+pl.col('email')).alias('full_name'))
df.select('full_name')

# Output
full_name
str
"KerryO'ConnellKerry16@gmail.co…
"EthelMillerEthel14@hotmail.com"
"WillieBartonWillie.Barton@gmai…
"EllisLoweEllis.Lowe@gmail.com"
"RaymondMillerRaymond.Miller@gm…
"EllenThompsonEllen92@hotmail.c…
"JoeRiceJoe55@gmail.com"
"NathanielLegrosNathaniel40@hot…
"MaxineSchinnerMaxine93@hotmail…
"TimJacobsonTim92@hotmail.com"
```



### 7.4 Agrupación, ordenación y unión



En todo tratamiento de datos será necesaria la agrupación según nos interese, al igual que ordenación e incluso combinar esos datos con otros mediante técnicas de unión similares a los JOIN de SQL.

Para agrupar, podemos referirnos a los clásicos groupby también existentes en SQL:



```python
import pandas as pd
import random

# Lectura
df = pd.read_csv('datos.csv')

random_age = [random.randrange(25,28,1) for x in range(len(df))]

df['age'] = random_age
agrupado_edad = df.groupby('age')['firstname'].apply(list)
print(agrupado_edad)

# Output
age
25              [Ethel, Ellen, Tim]
26       [Kerry, Nathaniel, Maxine]
27    [Willie, Ellis, Raymond, Joe]
Name: firstname, dtype: object
```



```python
import polars as pl
import random

# Lectura
df = pl.read_csv('datos.csv')

random_age = [random.randrange(25,28,1) for x in range(df.height)]

df = df.with_columns(pl.Series(name='age', values=random_age))
agrupado_edad = df.group_by('age').agg(pl.col('firstname'))
print(agrupado_edad)

# Output
```



![image](assets/cm5zphb1b00jn356xgwodx48v-Imagen2.jpg)



El caso de ordenar columnas es algo más sencillo:



```ruby
import pandas as pd

# Lectura
df = pd.read_csv('datos.csv')

df_ordenado = df.sort_values(by='firstname', ascending=True)
df_ordenado

# Output
```



![image](assets/cm5zpiyf000kq356x06uahrza-Imagen3.jpg)



```python
import polars as pl

# Lectura
df = pl.read_csv('datos.csv')

df_ordenado = df.sort('firstname',descending=False)
df_ordenado

 # Output
```



![image](assets/cm5zpkera00mf356x2bugxsas-Imagen4.jpg)



Finalmente tenemos las operaciones de unión mediante concatenación o join:



```r
# Concatenar verticalmente
import pandas as pd

df_1 = pd.read_csv('datos.csv')
df_2 = pd.read_csv('datos.csv')

df_concatenado = pd.concat([df_1,df_2])
df_concatenado

# Unión de dos dataframes utilizando una clave

df_unido = pd.merge(df_1, df_2, on='id', how='inner')
df_unido
```



```r
# Concatenar verticalmente
import polars as pl

df_1 = pl.read_csv('datos.csv')
df_2 = pl.read_csv('datos.csv')

df_concatenado = pl.concat([df_1,df_2])
df_concatenado

# Unión de dos dataframes utilizando una clave

df_unido = df_1.join(df_2, on='id', how='inner')
df_unido
```



Cómo se puede observar, en cuanto a sintaxis ambos paquetes tienen operaciones parecidas y diferentes. Algunas con mejor legibilidad que otras, pero por lo general es una sintaxis similar.

En cuanto a características más relevantes, en Polars los DataFrames son inmutables, haciendo que cada operación genere uno nuevo. Además, Polars se caracteriza por un mejor rendimiento y manejo más eficiente de la memoria que se hace más evidente con grandes volúmenes.

Por otro lado, Pandas es el estándar en la industria y tiene muchos más años y comunidad por detrás, lo que lo convierte en una solución más fiable para proyectos en producción.

La decisión de utilizar uno u otro dependerá del caso de uso, pero en última instancia del desarrollador.

Para ayudar con la toma de esta decisión, veamos un breve video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651977_1/scormcontent/assets/INSD_BAIN_U1_Video5.mp4?v=1)



### 7.5 Enlaces de interés



> Documentación de Polars
>
> [Link](https://docs.pola.rs/)

> Documentación de Pandas
>
> [Link](https://pandas.pydata.org/docs/index.html)

> Polars cheat-sheet
>
> [Link](https://franzdiebold.github.io/polars-cheat-sheet/Polars_cheat_sheet.pdf)

> Pandas cheat-sheet
>
> [Link](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)



## 8. Conclusiones



### 8.1 Conclusiones de la unidad



En esta unidad didáctica, hemos explorado de manera profunda el ecosistema Python y las herramientas que lo componen para la ciencia de datos. Comenzamos por familiarizarnos con Python y configurando los entornos de desarrollo integrados más populares, como JupyterLab, PyCharm y Visual Studio Code, comprendiendo sus características distintivas y cómo pueden optimizar nuestro flujo de trabajo como desarrolladores y analistas de datos.

Nos sumergimos en los fundamentos del lenguaje Python, explorando su sintaxis básica y las estructuras de datos esenciales como listas, tuplas, diccionarios y conjuntos. Estas bases son imprescindibles para cualquier tarea de programación y sientan los cimientos para abordar desafíos más complejos en el futuro.

La gestión de librerías o paquetes es un aspecto crítico en el desarrollo en Python. Aprendimos a instalar, actualizar y desinstalar librerías utilizando pip, el gestor de paquetes estándar de Python. Además, comprendimos la importancia de los entornos virtuales para aislar las dependencias de cada proyecto, evitando conflictos y garantizando la reproducibilidad de nuestros entornos de desarrollo. Un aspecto destacado fue la creación y publicación de nuestros propios paquetes en PyPI, lo que nos abre las puertas para contribuir activamente a la comunidad de Python y compartir nuestras soluciones con otros profesionales además de crear soluciones internas adaptadas a nuestras necesidades y reutilizables por nuestro equipo.

Exploramos los formatos de datos más comunes en el ámbito de la ciencia de datos: CSV, JSON, Parquet y Avro. Entendimos las características particulares de cada uno, sus ventajas y casos de uso. Saber cómo trabajar con estos formatos es esencial para importar, exportar y transformar datos en diversos proyectos, y nos permite adaptarnos a las necesidades específicas de cada situación.



Nota Final: Se anima a los estudiantes a continuar explorando el ecosistema Python y enfrentarse a proyectos personales. La tecnología evoluciona rápidamente y es necesario estar atentos a las nuevas actualizaciones y librerías.
