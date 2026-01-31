# Unidad 6. Programación de Aplicaciones en Cloud/AWS

## 1. Introducción y objetivos

Estás en la recta final. En la Unidad 5 aprendimos *qué* es la nube y *qué* servicios ofrece a nivel de infraestructura. En esta unidad, cambiamos el chip: dejaremos de pensar como administradores de sistemas para pensar como **desarrolladores de software**.

El objetivo principal es aprender a **integrar servicios Cloud dentro del código de nuestras aplicaciones**. Ya no se trata solo de crear una máquina virtual, sino de que tu código Python, Java o Node.js hable nativamente con bases de datos gestionadas, ejecute funciones sin servidor y almacene archivos de forma programática.

### Objetivos específicos:
1.  Entender cómo conectar una aplicación a **RDS** (Base de datos relacional).
2.  Desarrollar funciones **Serverless** con **AWS Lambda**.
3.  Integrar almacenamiento de objetos **S3** utilizando el SDK (Software Development Kit).
4.  Manejar credenciales y configuración de forma segura (variables de entorno).

---

## 2. Introducción: El SDK de AWS

Para que tu código interactúe con AWS, no usamos la consola web. Usamos un **SDK** (Software Development Kit).
En el ecosistema de **Python** (que usaremos en los ejemplos), la librería estándar se llama **Boto3**.

### ¿Qué permite hacer Boto3?
Permite controlar CUALQUIER servicio de AWS desde tu script Python.
- Subir un archivo a S3.
- Encender una máquina EC2.
- Invocar una función Lambda.
- Leer un registro de una base de datos DynamoDB.

**Instalación típica:**
```bash
pip install boto3
```

**Configuración de credenciales:**
El SDK busca automáticamente credenciales en:
1.  Variables de entorno (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).
2.  Archivos de configuración locales (`~/.aws/credentials`).
3.  Roles de IAM (si el código se ejecuta dentro de, por ejemplo, una Lambda o EC2). **Esta es la forma recomendada en producción**.

---

## 3. RDS: Bases de datos como servicio (Relational Database Service)

Desde la perspectiva del programador, RDS es **casi indistingible** de una base de datos local. No necesitas aprender una API especial de AWS para hacer consultas SQL. Sigues usando tus drivers de siempre (`psycopg2` para PostgreSQL, `mysql-connector` para MySQL, etc.).

### Diferencias clave para el desarrollador:

1.  **El Endpoint:** En lugar de conectar a `localhost` o `127.0.0.1`, conectarás a una URL DNS proporcionada por AWS (ej: `mydb.c12345.us-east-1.rds.amazonaws.com`).
2.  **Seguridad:** Debes asegurarte de que el **Security Group** de la base de datos permita el tráfico entrante desde tu IP (si desarrollas en local) o desde el Security Group de tu aplicación (si está en EC2/Lambda).
3.  **Gestión de Conexiones:** En entornos Serverless (como Lambda), abrir y cerrar conexiones a la base de datos en cada ejecución es muy costoso y puede saturar la base de datos. Se recomienda usar **RDS Proxy** o gestionar el pool de conexiones cuidadosamente.

### Ejemplo de conexión (Python + PostgreSQL)

```python
import psycopg2
import os

# NUNCA hardcodees credenciales en el código. Usa variables de entorno.
db_host = os.environ.get("DB_HOST")  # Endpoint de RDS
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")

def get_connection():
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass,
            port=5432
        )
        return conn
    except Exception as e:
        print(f"Error conectando a RDS: {e}")
        return None
```

---

## 4. Lambda: Computación Serverless

AWS Lambda permite ejecutar código sin aprovisionar ni administrar servidores. Pagas solo por el tiempo de cómputo que consumes (milisegundos).

### Conceptos de Programación en Lambda

1.  **El Handler (Manejador):** Es la función de entrada. AWS necesita saber qué función ejecutar cuando ocurre el evento. Por defecto suele ser `lambda_function.lambda_handler`.
2.  **El objeto `event`:** Contiene los datos que dispararon la función. Si es una API REST, contiene el body del HTTP request. Si es un cron, contiene la hora. Si es S3, contiene el nombre del archivo subido.
3.  **El objeto `context`:** Información sobre el entorno de ejecución (cuánta memoria queda, ID de la petición, tiempo restante antes del timeout).
4.  **Cold Start vs Warm Start:**
    *   El código fuera del `handler` se ejecuta solo una vez cuando AWS arranca el contenedor (inicialización).
    *   El código dentro del `handler` se ejecuta en cada petición.
    *   *Tip:* Inicializa conexiones a BBDD o clientes SDK **fuera** del handler para reutilizarlos.

### Estructura base

```python
import json

# Inicialización (se ejecuta una vez por "Cold Start")
print("Inicializando función...")

def lambda_handler(event, context):
    # Lógica por petición (se ejecuta siempre)
    print("Evento recibido:", json.dumps(event))
    
    nombre = event.get('nombre', 'Mundo')
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Hola, {nombre}!')
    }
```

---

## 5. S3: Simple Storage Service

S3 es un almacenamiento de objetos (archivos). No es un sistema de archivos tradicional (no puedes hacer "append" a un archivo, tienes que sobrescribirlo entero).

### Conceptos clave para el programador:

*   **Bucket:** El contenedor principal (como una carpeta raíz en la nube). Debe tener un nombre único mundialmente.
*   **Key (Clave):** La ruta completa del archivo dentro del bucket (ej: `imagenes/usuarios/foto1.jpg`).
*   **Clases de almacenamiento:** Puedes subir archivos directamente a capas más baratas (Infrequent Access, Glacier) si no los vas a usar mucho.

### Operaciones comunes con Boto3

*   `put_object`: Subir datos (bytes o string).
*   `upload_file`: Subir un archivo desde disco local (gestiona multipart upload automáticamente para archivos grandes).
*   `get_object`: Descargar/Leer datos.
*   `generate_presigned_url`: Crear una URL temporal para que un usuario pueda descargar un archivo privado sin tener credenciales de AWS (muy útil para webs).

---

## 6. Demo 1: Calculadora Serverless (Lambda)

Vamos a simular una backend de una calculadora que recibe dos números y una operación.

**Escenario:**
Una aplicación frontend envía un JSON a nuestra Lambda:
```json
{
  "num1": 10,
  "num2": 5,
  "operacion": "suma"
}
```

**Código de la Lambda (`lambda_function.py`):**

```python
import json

def lambda_handler(event, context):
    # 1. Extraer datos del evento
    # Nota: Si viene de API Gateway, los datos pueden estar en event['body']
    try:
        n1 = float(event.get('num1'))
        n2 = float(event.get('num2'))
        op = event.get('operacion')
    except (ValueError, TypeError):
        return {
            'statusCode': 400,
            'body': json.dumps("Error: Datos de entrada inválidos")
        }

    resultado = 0
    
    # 2. Lógica de negocio
    if op == 'suma':
        resultado = n1 + n2
    elif op == 'resta':
        resultado = n1 - n2
    elif op == 'multiplicacion':
        resultado = n1 * n2
    elif op == 'division':
        if n2 == 0:
            return {'statusCode': 400, 'body': "Error: División por cero"}
        resultado = n1 / n2
    else:
        return {'statusCode': 400, 'body': "Error: Operación no soportada"}

    # 3. Retornar respuesta
    response = {
        'operacion': op,
        'resultado': resultado
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
```

**Prueba:**
En la consola de AWS Lambda, creamos un "Test Event" con el JSON de ejemplo y verificamos la salida.

---

## 7. Demo 2: Gestor de Archivos en S3

Script local en Python para subir facturas a un bucket de S3 automáticamente.

**Requisitos:**
- `pip install boto3`
- Credenciales configuradas (`aws configure` o variables de entorno).

**Código (`gestor_s3.py`):**

```python
import boto3
import os

# Crear cliente de S3
s3 = boto3.client('s3')

BUCKET_NAME = 'mi-bucket-universidad-demo-2024' # Cambiar por uno vuestro único

def crear_bucket_si_no_existe():
    """Crea el bucket si no existe (us-east-1)"""
    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket {BUCKET_NAME} asegurado.")
    except Exception as e:
        # Puede fallar si ya existe y no es nuestro, o por permisos
        print(f"Nota sobre bucket: {e}")

def subir_archivo(nombre_archivo_local, nombre_en_s3):
    try:
        print(f"Subiendo {nombre_archivo_local}...")
        s3.upload_file(nombre_archivo_local, BUCKET_NAME, nombre_en_s3)
        print("Subida exitosa.")
    except Exception as e:
        print(f"Error subiendo: {e}")

def listar_archivos():
    print(f"\nContenido del bucket {BUCKET_NAME}:")
    try:
        respuesta = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in respuesta:
            for obj in respuesta['Contents']:
                print(f" - {obj['Key']} (Tamaño: {obj['Size']} bytes)")
        else:
            print(" - Bucket vacío.")
    except Exception as e:
        print(f"Error listando: {e}")

# Ejecución de prueba
if __name__ == '__main__':
    # 1. Crear un archivo de prueba local
    with open("prueba.txt", "w") as f:
        f.write("Este es el contenido de mi factura o log.")

    # 2. Operaciones
    crear_bucket_si_no_existe()
    subir_archivo("prueba.txt", "carpeta-facturas/2024/factura_001.txt")
    listar_archivos()
    
    # Limpieza local
    os.remove("prueba.txt")
```

### Conclusión de la Unidad
Al finalizar estas demos, habrás tocado los tres pilares del desarrollo moderno en Cloud:
1.  **Cómputo (Lambda):** Lógica de negocio pura, sin servidores.
2.  **Datos Estructurados (RDS):** Persistencia relacional clásica pero gestionada.
3.  **Datos No Estructurados (S3):** Almacenamiento infinito para archivos.

Estos componentes son los "Legos" con los que se construyen arquitecturas complejas como Netflix o Airbnb.
