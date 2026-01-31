# Parte Teórica - Sistemas Distribuidos (Unidad 6) — Resumen corto

## Cambio de Chip: Dev vs Ops

- **Objetivo**: Integrar servicios Cloud DENTRO del código.
- **Herramienta principal**: **SDK** (Software Development Kit).
  - En Python: **Boto3**.

---

## Boto3 y Credenciales

- No se hardcodean credenciales en el código.
- **Orden de búsqueda** de credenciales por el SDK:
  1. **Variables de entorno** (`AWS_ACCESS_KEY_ID`...).
  2. Archivos locales (`~/.aws/credentials`).
  3. **Roles IAM** (si ejecutas dentro de EC2/Lambda). *Best Practice*.

---

## Servicios desde el Código

### 1. RDS (Bases de datos)
- Para el programador es casi igual a una BBDD local.
- **Endpoint**: Usas DNS de AWS, no IP.
- **Security Groups**: El firewall debe permitir tu IP o el SG de tu app.
- **Serverless (Lambda) + RDS**:
  - Cuidado con abrir/cerrar conexiones en cada petición (satura la BBDD).
  - Solución: Usar **RDS Proxy** o inicializar fuera del handler.

### 2. Lambda (Serverless)
- Ejecución por eventos. Pagas por milisegundos.
- **Handler**: Función de entrada (`def lambda_handler(event, context):`).
- **Objetos clave**:
  - `event`: DATOS (body HTTP, nombre de archivo subido, etc).
  - `context`: INFO ejecución (ram restante, timeout).
- **Cold Start vs Warm Start**:
  - Código **fuera** del handler: Se ejecuta 1 vez (inicialización). Eje: Conectar a BBDD aquí.
  - Código **dentro** del handler: Se ejecuta en cada petición.

### 3. S3 (Almacenamiento de Objetos)
- No es un sistema de archivos normal.
- **Inmutable**: No puedes añadir texto al final de un archivo. Tienes que resubirlo entero.
- **Estructura**: `Bucket` (contenedor único mundial) -> `Key` (ruta/nombre).
- **Operaciones Boto3**:
  - `put_object`: Subir bytes.
  - `upload_file`: Subir fichero de disco (gestiona multipart auto).
  - `generate_presigned_url`: Dar acceso temporal a un archivo privado.

---

## Chuleta de Código (Python)

```python
import boto3
import os

# Cliente
s3 = boto3.client('s3')

# Lambda Handler tipico
def lambda_handler(event, context):
    # Acceder a variables de entorno (Config)
    tabla = os.environ['NOMBRE_TABLA']
    
    # Leer evento
    usuario = event.get('user_id')
    
    return {"status": 200}
```
