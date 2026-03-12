# Unidad 1 — El ecosistema Python (Mega‑temario)

> Asignatura: **Búsqueda y Análisis de la Información**
>
> Este documento es intencionalmente largo. La idea es que tengas un **temario autosuficiente** con teoría + ejemplos + ejercicios.

---

## Checklist global (TO‑DO) — Unidad 1

Marca a medida que avances:

### Introducción y objetivos
- [ ] Entender el objetivo de la unidad (ecosistema Python)
- [ ] Entender qué es “reproducibilidad” en proyectos
- [ ] Definir tu stack mínimo: terminal + VSCode + venv + pip

### Instalación de Python
- [ ] Instalar Python en Windows
- [ ] Instalar Python en Linux
- [ ] Instalar Python en macOS
- [ ] Verificar `python`/`python3`/`pip` y el ejecutable real
- [ ] Entender PATH y “múltiples Python”

### Herramientas
- [ ] Jupyter: cuándo usarlo y cómo evitar “estado oculto”
- [ ] PyCharm: concepto de proyecto e intérprete
- [ ] VSCode: intérprete/venv, depuración y notebooks

### Python lenguaje
- [ ] Sintaxis básica y estilo (PEP 8)
- [ ] Tipos, mutabilidad, copias
- [ ] Estructuras de datos (list/tuple/dict/set)
- [ ] Control de flujo (if/for/while/match)
- [ ] Funciones (firmas, docstrings, *args/**kwargs)
- [ ] POO (clases, composición, dataclasses)
- [ ] Excepciones (raise, chaining, custom)

### Paquetes y entornos
- [ ] `pip` (instalar, freeze, requirements)
- [ ] Instalar desde git/local
- [ ] Actualizar dependencias y entender compatibilidad
- [ ] `venv` y aislamiento real
- [ ] Concepto de paquete propio y PyPI

### Datos
- [ ] CSV (delimitadores, encoding, quoting)
- [ ] JSON (objetos, arrays, JSONL)
- [ ] Parquet (columnar, compresión)
- [ ] Avro (esquema, evolución)

### Pandas
- [ ] Cargar/inspeccionar
- [ ] Filtrar/seleccionar
- [ ] Crear columnas
- [ ] GroupBy/merge

### Práctica
- [ ] Completar biblioteca de ejercicios
- [ ] Completar mini‑proyecto IR

---

## Índice
- 0. Introducción y objetivos
- 1. Instalación y configuración
  - 1.1 Windows
  - 1.2 Linux
  - 1.3 macOS
  - 1.4 Troubleshooting (PATH, versiones, pip)
- 2. Herramientas (Jupyter, PyCharm, VSCode)
  - 2.1 Qué usar según la tarea
  - 2.2 Configuración mínima en VSCode
    - 2.3 Jupyter en profundidad (kernels, buenas prácticas)
    - 2.4 PyCharm (proyecto, venv, debugging)
    - 2.5 Flujo recomendado para la asignatura
- 3. Python (de básico a muy práctico)
  - 3.1 Sintaxis, scripts, módulos
  - 3.2 Tipos y mutabilidad
  - 3.3 Estructuras de datos y patrones comunes
  - 3.4 Control de flujo
  - 3.5 Funciones
  - 3.6 POO
  - 3.7 Excepciones
    - 3.8 IO (ficheros) y `pathlib`
    - 3.9 Módulos clave (collections, re, json, csv)
    - 3.10 Debugging y logging
- 4. Paquetes, pip y entornos
  - 4.1 pip (instalar, freeze, reproducibilidad)
  - 4.2 venv (aislamiento real)
  - 4.3 Publicación (visión de alto nivel)
    - 4.4 Reproducibilidad real (requirements, rangos, locks)
- 5. Formatos de datos
  - 5.1 CSV
  - 5.2 JSON (y JSONL)
  - 5.3 Parquet
  - 5.4 Avro
    - 5.5 Cómo elegir formato (reglas prácticas)
- 6. Pandas
  - 6.1 Carga e inspección
  - 6.2 Limpieza y transformación
  - 6.3 GroupBy, merge, pivot
    - 6.4 Tipos, missing values y datetime
    - 6.5 Rendimiento (apply vs vectorización)
- 7. Biblioteca de ejercicios (por carpetas)
- 8. Mini‑proyecto: mini buscador (IR)
- 9. Enlaces y recursos

---

## Temario oficial (punto por punto) + TO‑DO

Esta sección replica el temario “tal cual” y te sirve como lista de control.

### Bloque A — Introducción
- [ ] Introducción y objetivos
- [ ] Introducción (por qué Python en IR)

### Bloque B — Instalación
- [ ] Instalación de Python en Windows
- [ ] Instalación de Python en Linux
- [ ] Instalación de Python en macOS

### Bloque C — Herramientas
- [ ] El lenguaje de programación Python (visión general)
- [ ] Jupyter
- [ ] PyCharm
- [ ] Visual Studio Code (VSCode)

### Bloque D — Fundamentos del lenguaje
- [ ] Sintaxis básicas en Python
- [ ] Tipos de datos en Python
- [ ] Estructuras de datos habituales en Python
- [ ] Estructuras de control de flujo de ejecución
- [ ] Funciones
- [ ] Programación orientada a objetos
- [ ] Manejo de excepciones
- [ ] Enlaces de interés

### Bloque E — Librerías, pip y entornos
- [ ] Instalación de librerías con pip
- [ ] Instalación de librerías desde repositorios externos
- [ ] Mantenimiento y actualización de librerías
- [ ] Entornos virtuales
- [ ] Creación de paquetes propios y publicación en PyPI

### Bloque F — Formatos de datos
- [ ] Tipos de datos (fila vs columna)
- [ ] CSV (Comma‑Separated Values)
- [ ] JSON (JavaScript Object Notation)
- [ ] Parquet
- [ ] Avro
- [ ] Enlaces de interés

### Bloque G — Pandas
- [ ] Carga e inspección de datos
- [ ] Selección, filtrado y creación
- [ ] Agrupación, ordenación y unión
- [ ] Enlaces de interés

### Bloque H — Cierre
- [ ] Conclusiones de la unidad

Sugerencia: completa los ejercicios de la sección 7 en paralelo.

## 0. Introducción y objetivos

Python es el “lenguaje pegamento” del análisis de información: te permite desde procesar ficheros y APIs (JSON/CSV) hasta montar pipelines de limpieza y análisis (Pandas), y más adelante en la asignatura, implementar estructuras típicas de IR (índices invertidos, scoring, ranking).

### Qué vas a dominar aquí (en términos de competencias)
- Montar un entorno reproducible (que *mañana* funcione igual que hoy).
- Escribir código Python limpio, debuggable, y con manejo de errores.
- Trabajar con datos reales (sucios, incompletos) sin romper el flujo.

### Qué significa “ecosistema” en Python
Cuando alguien dice “ecosistema Python” normalmente se refiere a:
- **Intérprete** (CPython) y su versión.
- **Librería estándar** (json, csv, pathlib, collections, re...).
- **Gestor de paquetes** (`pip`) y repositorio (PyPI).
- **Entornos** (venv/conda) para aislar dependencias.
- **Herramientas** (VSCode/Jupyter) para desarrollar y analizar.

En esta asignatura lo importante es que seas capaz de:
- instalar y aislar dependencias;
- leer y transformar datos;
- escribir código modular para algoritmos de IR.

### TO‑DO de la sección
- [ ] Entender por qué reproducibilidad = “no perder semanas”
- [ ] Identificar tus herramientas: VSCode + venv + pip

---

## 1. Instalación y configuración

### 1.1 Instalación en Windows

**Opciones típicas:**
- Instalador oficial de python.org
- Microsoft Store (menos recomendable para proyectos serios)

**Pasos (recomendado):**
1. Descarga desde https://www.python.org/downloads/windows/
2. Ejecuta el instalador
3. Marca **Add Python to PATH**
4. Instala

**Verificación:**
```bash
python --version
pip --version
```

**Errores clásicos y solución rápida:**
- “python no se reconoce como un comando”: el PATH no apunta a la instalación.
- “pip no existe”: el instalador no agregó pip o estás llamando al Python equivocado.

**Tip práctico:**
En Windows a veces conviene usar:
```bash
py -V
py -m pip --version
py -m pip install requests
```
El launcher `py` te reduce el caos de versiones.

**TO‑DO Windows:**
- [ ] Instalar y verificar Python
- [ ] Entender diferencia `python` vs `py`

#### Windows: “recetas” rápidas
1) Mostrar dónde está Python:
```bash
where python
python -c "import sys; print(sys.executable)"
```

2) Usar pip del intérprete correcto:
```bash
python -m pip install -U pip
python -m pip install pandas
```

3) Si `pip` da problemas, reinstala/actualiza:
```bash
python -m ensurepip --upgrade
python -m pip install -U pip
```

---

### 1.2 Instalación en Linux

En Linux suele venir `python3` ya instalado, pero necesitas también `pip` y `venv`.

Debian/Ubuntu:
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
pip3 --version
```

**TO‑DO Linux:**
- [ ] Verificar `python3` y `pip3`
- [ ] Instalar `python3-venv`

#### Linux: notas prácticas
- En Debian/Ubuntu, evita instalar paquetes con `sudo pip` (mezcla sistema con proyecto).
- En general: *venv siempre*.

Mostrar rutas:
```bash
which python3
python3 -c "import sys; print(sys.executable)"
```

---

### 1.3 Instalación en macOS

Recomendado: Homebrew.
```bash
brew install python
python3 --version
pip3 --version
```

**TO‑DO macOS:**
- [ ] Instalar Python con brew
- [ ] Verificar versión y pip

#### macOS: notas prácticas
- `python` del sistema puede no ser el que quieres: usa `python3`.
- Homebrew suele instalar en `/opt/homebrew/...` (Apple Silicon) o `/usr/local/...` (Intel).

---

### 1.4 Troubleshooting (PATH, versiones, pip)

#### 1.4.1 `python` vs `python3`
- En Linux/macOS suele ser `python3`.
- En Windows suele ser `python` o `py`.

#### 1.4.2 ¿Qué Python se está ejecutando?
Para evitar confusiones, imprime el ejecutable:
```python
import sys
print(sys.executable)
print(sys.version)
```

#### 1.4.3 `pip` correcto
**Regla de oro:** usa `python -m pip` para instalar en el intérprete correcto.
```bash
python3 -m pip install pandas
python3 -m pip list
```

#### 1.4.4 Múltiples versiones de Python
En proyectos reales, podrás necesitar Python 3.10 en un proyecto y 3.12 en otro.
- Linux/macOS: `pyenv` (concepto)
- Windows: `py` launcher + instalaciones múltiples

**TO‑DO troubleshooting:**
- [ ] Saber encontrar `sys.executable`
- [ ] Instalar con `python -m pip`

#### 1.4.5 Errores típicos (y cómo pensar)
1) “Funciona en terminal pero no en VSCode”
- Causa típica: VSCode está usando otro intérprete.
- Solución: seleccionar intérprete del `.venv` y reiniciar terminal integrada.

2) “Instalo pandas pero luego import falla”
- Causa típica: instalaste en un Python distinto.
- Solución: `python -m pip install ...` + `python -c "import pandas; print(pandas.__version__)"`

3) “Tengo 2 pythons”
- Es normal. Lo importante es ser explícito.

---

## 2. Herramientas (Jupyter, PyCharm, VSCode)

### 2.1 ¿Qué usar según la tarea?
- **Jupyter**: exploración, prototipado, explicación paso a paso.
- **VSCode**: scripts, proyectos, control de versiones, debugging, refactor.
- **PyCharm**: IDE pesado, muy bueno para proyectos grandes (si te gusta JetBrains).

### 2.2 Jupyter (Notebook / Lab)

**Qué es:** un documento que mezcla texto (Markdown) + celdas de código ejecutables.

**Ventajas reales:**
- Perfecto para análisis de datos incremental.
- Permite ver resultados inmediatamente.

**Peligros reales:**
- “Estado oculto”: una celda puede depender de otra ejecutada antes.
- Difícil de testear y modularizar.

**Buenas prácticas:**
- Re-ejecuta “Restart kernel & Run all” para validar.
- Evita copiar/pegar código: convierte en funciones.

### 2.3 Jupyter en profundidad (kernels, buenas prácticas)

#### 2.3.1 Kernel
El *kernel* es el proceso Python que ejecuta tus celdas. Problema típico: tienes varios entornos y el notebook ejecuta el kernel equivocado.

Checklist:
- [ ] Saber identificar el kernel activo
- [ ] Cambiar kernel al venv correcto

#### 2.3.2 Patrones recomendados en notebooks
- Arranca con una celda de imports y configuración.
- Escribe funciones en celdas (no bloques enormes sueltos).
- Evita estados globales opacos.

Ejemplo (estructura mínima):
```python
from pathlib import Path
import pandas as pd

DATA = Path("datasets") / "ventas.csv"
df = pd.read_csv(DATA)
df.head()
```

### 2.4 PyCharm (proyecto, venv, debugging)

Puntos clave:
- En PyCharm, el proyecto está asociado a un intérprete (idealmente el `.venv`).
- Depurar en PyCharm suele ser muy cómodo si vienes de IDEs clásicos.

Checklist:
- [ ] Crear proyecto y asignar intérprete `.venv`
- [ ] Ejecutar un script con breakpoints

### 2.5 Flujo recomendado para la asignatura

1) Crea un venv por unidad/proyecto.
2) Escribe ejercicios en `.py` (más fácil de versionar y testear).
3) Usa notebooks sólo cuando necesites exploración.

---

## 2.6 VSCode: depuración y calidad

Checklist:
- [ ] Saber poner breakpoints
- [ ] Saber inspeccionar variables
- [ ] Saber ejecutar un archivo con el intérprete del venv

Debugging mínimo:
- un script con `if __name__ == "__main__":`
- configura el intérprete
- ejecuta con Debug

### 2.3 VSCode (configuración mínima)

Extensiones recomendadas:
- Python
- Pylance
- Jupyter (si vas a usar notebooks)

Conceptos:
- Linter/formatter (ej. `ruff`/`black`)
- Debugger
- Selección de intérprete (tu venv)

**TO‑DO herramientas:**
- [ ] Tener VSCode con Python + Pylance
- [ ] Saber seleccionar tu entorno virtual

---

## 3. Python (de básico a muy práctico)

### 3.1 Sintaxis, scripts y módulos

**Script:** archivo `.py` ejecutable.
```bash
python3 mi_script.py
```

**Módulo:** un `.py` importable.

**Paquete:** carpeta con `__init__.py` (en Python clásico) o paquete namespace.

Ejemplo rápido:
```python
# archivo: utils.py

def normalize(text: str) -> str:
    return text.strip().lower()
```

```python
# archivo: main.py
from utils import normalize

print(normalize("  Hola  "))
```

**TO‑DO:**
- [ ] Entender `if __name__ == "__main__":`
- [ ] Saber separar en módulos

#### 3.1.1 Patrón `__main__` (por qué existe)

Cuando importas un módulo, Python ejecuta su “top level” una vez. Para que un archivo se pueda **importar** sin ejecutar la parte de “programa principal”, se usa:
```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```
Esto te permite:
- reusar funciones desde otros módulos;
- testear;
- evitar side-effects al importar.

---

### 3.2 Tipos de datos y mutabilidad

#### 3.2.1 Tipos básicos
- `int`, `float`, `bool`, `str`
- `None` (`NoneType`)

#### 3.2.2 Mutabilidad
- Inmutables: `int`, `float`, `bool`, `str`, `tuple`
- Mutables: `list`, `dict`, `set`

Ejemplo: aliasing (error típico)
```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]  (porque b y a apuntan al mismo objeto)
```

Copia superficial vs profunda:
```python
import copy

x = [[1], [2]]
y = x.copy()          # superficial
z = copy.deepcopy(x)  # profunda

x[0].append(99)
print(y)  # también cambia
print(z)  # no cambia
```

**TO‑DO:**
- [ ] Saber cuándo necesitas `copy.deepcopy`
- [ ] Entender aliasing

#### 3.2.3 Igualdad vs identidad
- `==` compara valores
- `is` compara identidad (mismo objeto)

Ejemplo:
```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False
```

---

### 3.3 Estructuras de datos y patrones

#### 3.3.1 Listas
- Ordenadas, mutables.
- Muy usadas para secuencias.

Patrones:
- Slicing: `lst[a:b:c]`
- Comprensiones: `[f(x) for x in xs if cond]`

Ejemplo:
```python
nums = [1, 2, 3, 4, 5]
pares_cuadrado = [n*n for n in nums if n % 2 == 0]
```

#### 3.3.2 Tuplas
- Inmutables.
- Ideales para claves compuestas.

```python
coord = (40.4168, -3.7038)
```

#### 3.3.3 Diccionarios
- Clave->valor.
- Base de muchos algoritmos IR (índice invertido clásico).

```python
freq = {}
for token in ["a", "b", "a"]:
    freq[token] = freq.get(token, 0) + 1
```

#### 3.3.4 Sets
- Unicidad.
- Intersecciones rápidas (búsqueda booleana, IR):

```python
docs_a = {1, 2, 3}
docs_b = {2, 3, 4}
print(docs_a & docs_b)  # {2, 3}
```

**TO‑DO:**
- [ ] Dominar `.get` en dict
- [ ] Saber cuándo usar set vs list

#### 3.3.5 `collections` (cuando crezcas)
En proyectos reales, `collections.Counter` y `defaultdict` son oro:
```python
from collections import Counter, defaultdict

tokens = ["a", "b", "a"]
print(Counter(tokens))

index = defaultdict(set)
index["python"].add(1)
```

---

### 3.4 Control de flujo

#### 3.4.1 `if/elif/else`
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

#### 3.4.2 `for`
```python
for i, value in enumerate(["a", "b"]):
    print(i, value)
```

#### 3.4.3 `while`
```python
n = 3
while n > 0:
    n -= 1
```

#### 3.4.4 `match` (Python 3.10+)
Útil para patrones simples:
```python
match status:
    case 200:
        msg = "OK"
    case 404:
        msg = "Not found"
    case _:
        msg = "Other"
```

**TO‑DO:**
- [ ] Saber usar `enumerate`
- [ ] Entender `match` (si tu versión lo permite)

#### 3.4.5 Comprensiones y control de flujo declarativo
Mucho código Python “idiomático” usa comprensiones:
```python
lineas = ["a", "", "b", "  "]
no_vacias = [ln.strip() for ln in lineas if ln.strip()]
```

---

### 3.5 Funciones (muy a fondo)

#### 3.5.1 Firma y docstring
```python
def tokenize(text: str, *, lowercase: bool = True) -> list[str]:
    """Convierte texto en tokens separando por espacios.

    Args:
        text: texto de entrada
        lowercase: si True, pasa a minúsculas

    Returns:
        Lista de tokens
    """
    if lowercase:
        text = text.lower()
    return text.split()
```

#### 3.5.2 `*args` y `**kwargs`
```python
def log(*values, sep=" "):
    print(sep.join(str(v) for v in values))

log("IR", "con", "Python")
```

#### 3.5.3 Scope
- Local
- Enclosing
- Global
- Built‑in

**TO‑DO:**
- [ ] Definir funciones con parámetros keyword-only (`*`)
- [ ] Saber leer y escribir docstrings

#### 3.5.4 Errores típicos con parámetros mutables
Nunca uses un mutable como default:
```python
def bad(acc=[]):
    acc.append(1)
    return acc
```
Esto “comparte” la lista entre llamadas.

Patrón correcto:
```python
def good(acc=None):
    if acc is None:
        acc = []
    acc.append(1)
    return acc
```

---

### 3.6 Programación Orientada a Objetos

#### 3.6.1 Qué problema resuelve
- Encapsular estado + comportamiento
- Modelar entidades (Documento, Colección, Tokenizador)

Ejemplo: documento y normalización
```python
class Document:
    def __init__(self, doc_id: int, text: str):
        self.doc_id = doc_id
        self.text = text

    def normalized(self) -> str:
        return " ".join(self.text.lower().split())
```

#### 3.6.2 `@dataclass`
Simplifica clases de datos.
```python
from dataclasses import dataclass

@dataclass
class Posting:
    doc_id: int
    tf: int
```

**TO‑DO:**
- [ ] Crear una clase simple con métodos
- [ ] Usar `@dataclass` para estructuras

#### 3.6.3 Composición vs herencia
En IR, suele ser mejor **composición**:
- `InvertedIndex` *tiene un* `Tokenizer`
- `Tokenizer` *tiene una* estrategia de normalización

Evita herencia si no hay una jerarquía clara.

---

### 3.7 Excepciones

#### 3.7.1 Estructura
```python
try:
    x = int(value)
except ValueError as e:
    raise ValueError("value debe ser un entero") from e
```

#### 3.7.2 Custom exceptions
```python
class ParseError(Exception):
    pass
```

**TO‑DO:**
- [ ] Manejar errores sin “silenciar” excepciones importantes

#### 3.7.3 `try/except/else/finally`
`else` corre si no hubo excepción; `finally` siempre.
```python
try:
    value = int("123")
except ValueError:
    value = 0
else:
    value += 1
finally:
    pass
```

---

## 3.8 IO (ficheros) y `pathlib`

Checklist:
- [ ] Abrir ficheros con `with open(...)`
- [ ] Usar `Path` para rutas robustas

Lectura segura:
```python
from pathlib import Path

path = Path("datasets") / "ventas.csv"
with path.open(encoding="utf-8") as f:
    text = f.read()
```

## 3.9 Módulos clave (collections, re, json, csv)

### `re` (expresiones regulares) para normalización
Ejemplo: sustituir no-letras por espacio.
```python
import re

clean = re.sub(r"[^\w]+", " ", "Hola, mundo!!!")
```

## 3.10 Debugging y logging

Checklist:
- [ ] Saber usar `print` estratégicamente (al inicio)
- [ ] Saber usar `logging` (cuando crezca)

Logging mínimo:
```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Cargando datos...")
```

---

## 4. Paquetes, `pip` y entornos

### TO‑DO de la sección
- [ ] Instalar paquetes en el intérprete correcto (`python -m pip`)
- [ ] Exportar dependencias (`pip freeze`)
- [ ] Reinstalar dependencias (`pip install -r requirements.txt`)
- [ ] Instalar desde git/local
- [ ] Entender por qué un venv evita conflictos

### 4.1 Instalar con pip (bien)

**Regla de oro:** usa el pip del intérprete.
```bash
python3 -m pip install pandas
python3 -m pip freeze > requirements.txt
```

#### 4.1.1 Versionado (por qué importa)
- `pandas==2.2.0` fija versión exacta.
- `pandas>=2.2,<3` permite rango.

#### 4.1.2 Comandos de diagnóstico
```bash
python3 -m pip list
python3 -m pip show pandas
python3 -m pip check
```

#### 4.1.3 Instalar desde repositorios externos
Git:
```bash
python3 -m pip install git+https://github.com/usuario/repo.git
```
Editable (para desarrollo):
```bash
python3 -m pip install -e ./mi_paquete
```

#### 4.1.4 Mantenimiento y actualización de librerías

Comandos útiles:
```bash
python3 -m pip list --outdated
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pandas
python3 -m pip uninstall pandas
```

Reglas prácticas:
- Actualiza de 1 en 1 (o en pequeños lotes) para poder diagnosticar.
- Si algo rompe: revisa el changelog y prueba fijar versión.
- Evita “mezclar” instalaciones del sistema con el venv.

Higiene de dependencias:
- `pip check` detecta incompatibilidades.
- `pip freeze` captura el estado exacto del entorno.

#### 4.1.5 Caché de pip (por qué a veces “va raro”)

Pip cachea descargas. Si notas comportamiento extraño (raro, pero pasa), puedes inspeccionar/limpiar:
```bash
python3 -m pip cache dir
python3 -m pip cache purge
```

### 4.2 Entornos virtuales (venv)

Crear (desde la carpeta del proyecto):
```bash
python3 -m venv .venv
```
Activar:
```bash
source .venv/bin/activate
```

**TO‑DO entornos:**
- [ ] Crear `.venv`
- [ ] Instalar dependencias dentro del `.venv`

#### 4.2.1 Señales de que estás dentro del venv
```bash
python3 -c "import sys; print(sys.executable)"
python3 -c "import sys; print(sys.prefix)"
```

#### 4.2.2 Regla de oro
Nunca instales dependencias “del proyecto” en el Python del sistema.

### 4.3 Paquetes propios y PyPI (visión rápida)
- Estructura moderna: `pyproject.toml`
- Publicación: `build` + `twine`

Conceptos útiles (alto nivel):
- **Módulo**: un `.py`
- **Paquete**: carpeta importable
- **Distribución**: lo que subes a PyPI

---

### 4.4 Reproducibilidad real (requirements)

Flujo mínimo recomendado:
1. Crear venv.
2. Instalar dependencias.
3. Congelar:
```bash
python3 -m pip freeze > requirements.txt
```
4. Reprobar en limpio:
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip check
```

---

## 5. Formatos de datos

### TO‑DO de la sección
- [ ] Leer y escribir CSV con `csv`
- [ ] Leer JSON con `json.load`
- [ ] Leer JSONL línea a línea
- [ ] Entender Parquet vs CSV
- [ ] Entender el rol del esquema en Avro

### 5.1 CSV

**Problemas reales de CSV:**
- Separador distinto (`,` vs `;`)
- Encoding (`utf-8`, `latin-1`)
- Comillas y escapes

Lectura robusta con `csv`:
```python
import csv

with open("datasets/ventas.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
```

Escritura recomendada:
```python
import csv

rows = [
    {"id": 1, "ciudad": "Madrid", "ventas": 700},
    {"id": 2, "ciudad": "Sevilla", "ventas": 250},
]

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "ciudad", "ventas"])
    writer.writeheader()
    writer.writerows(rows)
```

Truco para separador `;`:
```python
reader = csv.DictReader(f, delimiter=';')
```

### 5.2 JSON (y JSON Lines)

**JSON normal:** un objeto/array completo.

**JSONL:** una línea = un JSON (perfecto para logs/eventos, streaming).

Ejemplo JSONL:
```python
import json

items = [{"id": 1}, {"id": 2}]
with open("out.jsonl", "w", encoding="utf-8") as f:
    for obj in items:
        f.write(json.dumps(obj) + "\n")
```

Lectura JSON “clásico”:
```python
import json

with open("datasets/users.json", encoding="utf-8") as f:
    payload = json.load(f)
users = payload["users"]
```

### 5.3 Parquet

Parquet es columnar: ideal para analítica.

Con Pandas:
```python
import pandas as pd

df = pd.DataFrame({"id": [1, 2], "text": ["hola", "mundo"]})
df.to_parquet("out.parquet", index=False)
```

Notas:
- Parquet necesita engine (normalmente `pyarrow`).
- Ideal si el dataset crece y haces analítica.

### 5.4 Avro

Conceptos:
- Esquema explícito
- Evolución de esquema

Nota: Avro es típico en pipelines de eventos. En esta unidad basta con entender el concepto.

---

### 5.5 Cómo elegir formato (reglas prácticas)
- CSV: simple, universal, pero sin tipos.
- JSON: jerárquico, perfecto para APIs.
- JSONL: streaming y colecciones de documentos.
- Parquet: analítica y eficiencia.
- Avro: esquema + evolución.

---

## 6. Pandas

### TO‑DO de la sección
- [ ] Inspección (shape/head/info/describe)
- [ ] Limpieza (missing, dtypes)
- [ ] Transformación (nuevas columnas)
- [ ] GroupBy/agg
- [ ] Merge/concat
- [ ] Exportación

### 6.1 Carga e inspección
```python
import pandas as pd

df = pd.read_csv("datasets/ventas.csv")
print(df.head())
print(df.info())
```

Inspección rápida:
```python
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isna().sum())
```

### 6.2 Selección y filtrado
```python
solo_madrid = df[df["ciudad"] == "Madrid"]
```

Filtro compuesto:
```python
mask = (df["ciudad"] == "Madrid") & (df["ventas"] >= 600)
print(df[mask])
```

### 6.3 GroupBy
```python
ventas_por_ciudad = df.groupby("ciudad")["ventas"].sum().reset_index()
```

Agregaciones múltiples:
```python
resumen = df.groupby("ciudad").agg(
    total=("ventas", "sum"),
    media=("ventas", "mean"),
    n=("ventas", "count"),
).reset_index()
print(resumen)
```

---

### 6.4 Tipos, missing values y datetime

Conversión robusta:
```python
import pandas as pd

df["ventas"] = pd.to_numeric(df["ventas"], errors="coerce").fillna(0)
```

---

### 6.5 Rendimiento

Preferir vectorización:
```python
df["ventas_x2"] = df["ventas"] * 2
```

---

## 7. Biblioteca de ejercicios

Carpetas (hazlos en orden):
- [Ejercicios/00_setup/README.md](Ejercicios/00_setup/README.md)
- [Ejercicios/01_python_basics/README.md](Ejercicios/01_python_basics/README.md)
- [Ejercicios/02_data_structures/README.md](Ejercicios/02_data_structures/README.md)
- [Ejercicios/03_control_flow_functions/README.md](Ejercicios/03_control_flow_functions/README.md)
- [Ejercicios/04_oop_exceptions/README.md](Ejercicios/04_oop_exceptions/README.md)
- [Ejercicios/05_packages_venv/README.md](Ejercicios/05_packages_venv/README.md)
- [Ejercicios/06_formats_csv_json/README.md](Ejercicios/06_formats_csv_json/README.md)
- [Ejercicios/07_parquet_avro/README.md](Ejercicios/07_parquet_avro/README.md)
- [Ejercicios/08_pandas/README.md](Ejercicios/08_pandas/README.md)
- [Ejercicios/09_mini_proyecto_ir/README.md](Ejercicios/09_mini_proyecto_ir/README.md)

En cada carpeta tienes un README con ejercicios + uno o más ficheros `.py` con TODOs.

---

## 8. Mini‑proyecto IR: mini buscador

Objetivo: construir un mini buscador que:
- Indexe documentos (strings)
- Cree un índice invertido `token -> {doc_id: tf}`
- Permita consultas AND/OR
- (Opcional) scoring simple por TF‑IDF

### Checklist paso a paso
- [ ] Cargar docs desde [datasets/docs.jsonl](datasets/docs.jsonl)
- [ ] Implementar `normalize` + `tokenize`
- [ ] Construir índice invertido (sets)
- [ ] Implementar AND/OR
- [ ] (Opcional) TF y posting list con `{doc_id: tf}`
- [ ] (Opcional) ranking simple

Archivo base:
- [Ejercicios/09_mini_proyecto_ir/09_mini_search.py](Ejercicios/09_mini_proyecto_ir/09_mini_search.py)

---

## 9. Enlaces y recursos
- Documentación Python: https://docs.python.org/3/
- PEP 8 (estilo): https://peps.python.org/pep-0008/
- Pandas: https://pandas.pydata.org/
