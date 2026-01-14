# Mini Twitter - Práctica AWS

Aplicación tipo Twitter usando AWS Lambda, RDS, S3 y API Gateway.

##  Estructura
```
├── lambda/              # 5 funciones Lambda (Node.js)
├── web/                 # Páginas HTML + CSS
├── sql/                 # Scripts de base de datos
├── README.md            # Este archivo
└── VIDEO_SCRIPT.md      # Guión para el video
```

##  Funcionalidades (10 puntos)
-  Base de datos RDS + Lambda básicas (5 pts)
-  Sistema de login (2 pts)
-  Registro de usuarios (1 pt)
-  Búsqueda por usuario (1 pt)
-  Diseño mejorado (1 pt)

## � Guía Rápida de Configuración

### 1. Crear Base de Datos RDS
```bash
# En AWS Console:
# RDS → Create Database → MySQL
# Instance: db.t3.micro
# Public access: Yes (solo testing)
# Initial DB: minitwitter

# Conectar y ejecutar:
mysql -h [ENDPOINT] -u admin -p
source sql/create_tables.sql
source sql/sample_data.sql
```

### 2. Construir y Subir Funciones Lambda
```bash
# Construir paquetes
chmod +x build_lambda_packages.sh
./build_lambda_packages.sh

# Subir cada .zip a AWS Lambda Console
# Configurar variables de entorno:
DB_HOST=[tu-endpoint].rds.amazonaws.com
DB_PORT=3306
DB_USER=admin
DB_PASSWORD=[tu-password]
DB_NAME=minitwitter
```

### 3. Crear API Gateway
```bash
# En AWS Console:
# API Gateway → Create REST API
# Crear 5 recursos con métodos:
# - /twitterPost (POST)
# - /twitterRead (GET)
# - /userLogin (POST)
# - /userRegister (POST)
# - /searchByUser (GET)
# Deploy en stage "prod"
```

### 4. Configurar S3 y Subir Web
```bash
# Crear bucket con static hosting
# Habilitar acceso público
# Subir archivos:
aws s3 sync web/ s3://tu-bucket/

# IMPORTANTE: Editar archivos HTML
# Reemplazar todas las URLs de API:
const API_URL = 'https://[TU-API-GATEWAY].amazonaws.com/prod/[recurso]';
```

## Video de Demostración

Ver guión detallado en `VIDEO_SCRIPT.md`

Debe mostrar:
1. Registro: BD antes/después + código Lambda
2. Login: Página + BD + código + redirección
3. Crear comentario: BD antes/después + S3 antes/después
4. Leer comentarios: Timeline + crear nuevo + actualizar
5. Búsqueda: Query BD + código Lambda + demo web

## Para Entregar

```bash
# Crear ZIP con:
├── lambda/          # 5 carpetas con código
├── web/             # HTML y CSS
├── sql/             # Scripts SQL
├── README.md
└── link_video.txt   # URL del video
```

## Troubleshooting

**Lambda no conecta a RDS**: Verificar Security Group puerto 3306  
**CORS error**: Habilitar CORS en API Gateway y re-deploy  
**403 en S3**: Verificar bucket policy permite acceso público  
**Timeout**: Aumentar timeout de Lambda a 30 segundos

## Limpiar después (evitar costos)
```bash
# Eliminar Lambda functions, API Gateway, vaciar S3, parar RDS
```

---
**Sistemas Distribuidos - Enero 2026**
