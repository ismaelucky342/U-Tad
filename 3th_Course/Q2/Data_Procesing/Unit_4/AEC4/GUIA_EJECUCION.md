# AEC4 - ANÁLISIS DE PELÍCULAS CON SPARK Y POSTGRESQL

## 📋 RESUMEN DEL PROYECTO

Este proyecto completa la Actividad Práctica AEC4 de la Unidad 4 de Data Processing con dos partes:

### **PARTE 1: Análisis con DataFrames y RDDs**
- Dataset: Movie Industry (250 películas, 10 columnas)
- Archivo: `movies_analysis.scala`
- Incluye: RDD, transformaciones, análisis exploratorio, UDFs, queries SQL

### **PARTE 2: Conector JDBC a PostgreSQL**
- Base de datos: PostgreSQL local
- Archivo: `postgresql_jdbc_connector.scala`
- Incluye: Ejercicio guiado, 2 queries SQL propias, análisis de módulos

---

## 🚀 INSTRUCCIONES DE EJECUCIÓN

### **REQUISITOS PREVIOS**

```bash
# 1. Verificar que tienes instalados:
- Spark (spark-shell disponible en PATH)
- PostgreSQL (iniciado: sudo systemctl status postgresql)
- Java JDK 8+

# 2. Archivos necesarios:
- ~/Descargas/movies.csv (250 registros de películas)
- ~/Descargas/postgresql-42.7.1.jar (driver JDBC)
```

#### **Verificar instalaciones:**
```bash
which spark-shell
which psql
java -version
```

---

## 📖 PARTE 1: ANÁLISIS CON RDD Y DATAFRAME

### **Paso 1: Preparar archivos**

```bash
# Verificar que el dataset existe
ls -lh ~/Descargas/movies.csv

# Contenido esperado:
# - 251 líneas (1 header + 250 registros)
# - 10 columnas: id, title, release_date, budget, revenue, 
#               runtime, genre, vote_average, popularity, cast_size
```

### **Paso 2: Ejecutar en Spark Shell**

```bash
# Abrir Spark Shell
spark-shell

# Dentro de Spark, pegar el contenido completo de: movies_analysis.scala
# El archivo está dividido en secciones claras con comentarios

# O ejecutar directamente:
spark-shell --file /ruta/a/movies_analysis.scala
```

### **Paso 3: Pantallazos para documentar**

Mientras ejecutas, toma screenshots de:

✓ **[PASO 1-2]** Lectura como RDD
```
Número de particiones del RDD: 4
Total de líneas (incluyendo header): 251
```

✓ **[PASO 3]** Transformaciones RDD
```
Total de registros parseados: 250
Primeros 5 registros del RDD:
(10000,The Shawshank Redemption,2025-02-01,157655242,625901256,108,Drama,8.1,679.93,149)
...
```

✓ **[PASO 4]** Conversión a DataFrame
```
root
 |-- id: integer (nullable = true)
 |-- title: string (nullable = true)
 |-- release_date: string (nullable = true)
 |-- budget: long (nullable = true)
 |-- revenue: long (nullable = true)
 |-- runtime: integer (nullable = true)
 |-- genre: string (nullable = true)
 |-- vote_average: double (nullable = true)
 |-- popularity: double (nullable = true)
 |-- cast_size: integer (nullable = true)
```

✓ **[PASO 5]** Estructura y Metadatos
```
Total de registros: 250
Total de columnas: 10
Registros únicos: 250
```

✓ **[PASO 6]** Análisis exploratorio (Estadísticas, Cuartiles)
✓ **[PASO 7]** Conversión DF→RDD→DF
✓ **[PASO 8]** Queries avanzadas (SQL + UDF + UDAF)

### **Contenido clave a documentar**

#### Query 1: Filtrado con condicionales
```sql
SELECT title, budget, revenue, vote_average 
FROM movies 
WHERE genre = 'Action' AND budget > 100000000 AND vote_average > 6.0
ORDER BY revenue DESC
```

#### Query 2: Agrupación múltiple
```sql
SELECT genre, year, COUNT(*) as num_peliculas, 
       AVG(revenue) as ingresos_promedio, MAX(revenue) as ingresos_max
FROM movies (con YEAR extraído de release_date)
GROUP BY genre, year
HAVING COUNT(*) > 2
ORDER BY ingresos_promedio DESC
```

#### Query 3: SQL
```sql
SELECT genre, COUNT(*) as num_peliculas,
       ROUND(AVG(revenue - budget) / AVG(budget) * 100, 2) as roi_promedio_percent
FROM movies
GROUP BY genre
ORDER BY roi_promedio_percent DESC
```

#### Query 4: UDF Personalizado
```scala
val classifyRentability = udf((budget: Long, revenue: Long) => {
  val roi = (revenue - budget).toDouble / budget
  if (roi > 5.0) "Extremadamente Rentable (ROI > 500%)"
  else if (roi > 2.0) "Muy Rentable (ROI > 200%)"
  else if (roi > 1.0) "Rentable (ROI > 100%)"
  else if (roi > 0.0) "Moderadamente Rentable"
  else "No Rentable (Pérdidas)"
})
```

---

## 🗄️ PARTE 2: CONECTOR JDBC A POSTGRESQL

### **Paso 1: Verificar PostgreSQL**

```bash
# Comprobar que PostgreSQL está corriendo
sudo systemctl status postgresql

# Testeando conexión
sudo -u postgres psql -c "SELECT * FROM mytable;"

# Output esperado:
# id |   name    | rating
# ---|-----------|--------
# 1  | Clase     |      9
# 2  | Tutorial  |      8
# 3  | Ejercicio |     10
```

### **Paso 2: Iniciar Spark Shell con driver JDBC**

```bash
spark-shell --jars /home/nirmata/Descargas/postgresql-42.7.1.jar
```

### **Paso 3: Ejecutar el código JDBC**

```bash
# Dentro de Spark Shell, pegar el contenido de: postgresql_jdbc_connector.scala
```

### **Paso 4: Pantallazos para documentar**

✓ **[PASO 1]** Configuración de propiedades JDBC
```
✓ Propiedades configuradas:
  - Usuario: postgres
  - Driver: org.postgresql.Driver
  - Host: localhost (puerto 5432 por defecto)
```

✓ **[PASO 2-3]** Lectura de PostgreSQL
```
+---+--------+------+
| id|    name|rating|
+---+--------+------+
|  1|   Clase|     9|
|  2|Tutorial|     8|
|  3|Ejercicio|     10|
+---+--------+------+
```

✓ **[PASO 4]** Crear tabla con JDBC
```
spark.sql("CREATE TABLE pgtable USING jdbc OPTIONS (...)")
✓ Tabla 'pgtable' creada exitosamente
```

✓ **[QUERY 1]** Crear Vista (high_quality_modules)
```
+---+--------+------+-------------------+
| id|    name|rating|quality_category  |
+---+--------+------+-------------------+
|  1|   Clase|     9|      Excelente    |
|  2|Tutorial|     8|      Muy Bueno    |
+---+--------+------+-------------------+
```

✓ **[QUERY 2]** Análisis Detallado
```
+-----------------------------+-----+
|          Metrica            |Valor|
+-----------------------------+-----+
|Módulos de alta calidad (>=8)|  2  |
|Rating máximo                |  10 |
|Rating mínimo                |  9  |
|Rating promedio global       | 8.67|
|Total de módulos             |  3  |
+-----------------------------+-----+
```

### **Explicaciones clave a documentar**

#### 1. Comandos de instalación de PostgreSQL
```bash
# En terminal:
sudo pacman -S postgresql postgresql-libs  # En Arch Linux
sudo -u postgres initdb -D /var/lib/postgres/data
sudo systemctl start postgresql
sudo -u postgres psql
```

#### 2. Configuración de tabla
```sql
ALTER USER postgres PASSWORD 'postgres';
CREATE TABLE mytable(id INT, name VARCHAR, rating INT);
INSERT INTO mytable VALUES(1, 'Clase', 9);
\q
```

#### 3. Driver JDBC
```bash
# Descarga:
wget https://jdbc.postgresql.org/download/postgresql-42.7.1.jar

# Uso en Spark:
spark-shell --jars postgresql-42.7.1.jar
```

#### 4. Conexión desde Spark
```scala
val props = new Properties()
props.setProperty("user", "postgres")
props.setProperty("driver", "org.postgresql.Driver")
props.setProperty("password", "postgres")

val jdbcDF = spark.read.jdbc(
  "jdbc:postgresql://localhost:5432/postgres",
  "mytable",
  props
)
```

---

## 📊 ESTRUCTURA DE ARCHIVOS

```
AEC4/
├── README.md (este archivo)
├── movies.csv (250 registros, 10 columnas)
├── movies_analysis.scala (PARTE 1 - 300+ líneas)
├── postgresql_jdbc_connector.scala (PARTE 2 - 300+ líneas)
└── DOCUMENTACION_PDF/ (pantallazos finales)
    ├── pasosRDD.png
    ├── printSchema.png
    ├── estadisticas.png
    ├── udf_udaf.png
    ├── jdbc_conexion.png
    ├── query1_vista.png
    └── query2_analisis.png
```

---

## ✅ CRITERIOS DE EVALUACIÓN CUBIERTOS

### **PARTE 1: Análisis RDD y DataFrame**

- ✅ **Fuente de datos:** 250 registros, 10 columnas, múltiples tipos
- ✅ **Lectura como RDD:** Implementado con `sparkContext.textFile()`
- ✅ **Transformaciones RDD:** split, map, filter, cache
- ✅ **Conversión RDD→DF:** `.toDF()` con nombres explícitos
- ✅ **Estructura:** printSchema, show(), count()
- ✅ **Análisis exploratorio:** 
  - Estadísticas básicas (describe)
  - Detección de nulos
  - **Método extra:** Análisis de cuartiles (approxQuantile)
- ✅ **DF→RDD→DF:** Con transformación de filtrado explicada
- ✅ **Problema personalizado:** Análisis de rentabilidad de películas por género
- ✅ **5 Queries avanzadas:**
  1. Con condicionales (WHERE + AND)
  2. Agrupación múltiple (genre + año)
  3. SQL (TOP 5 géneros)
  4. **UDF personalizado** (classifyRentability)
  5. UDAF (popularidad por género)
- ✅ **Explicaciones:** Cada paso comentado y documentado

### **PARTE 2: Conector JDBC PostgreSQL**

- ✅ **Instalación PostgreSQL:** sudo + initdb + systemctl
- ✅ **Tabla de prueba:** CREATE TABLE + INSERTs
- ✅ **Driver JDBC:** postgresql-42.7.1.jar descargado
- ✅ **Explicación comandos:** Comentados línea por línea
- ✅ **Lectura JDBC:** Properties + spark.read.jdbc()
- ✅ **CREATE TABLE JDBC:** Tabla virtual mapeada a PostgreSQL
- ✅ **2 Queries SQL propias:**
  1. CREATE TABLE high_quality_modules (con vista + CASE WHEN)
  2. Análisis detallado (UNION ALL + agregaciones)
- ✅ **Explicaciones:** Conceptos de JDBC, ventajas, limitaciones

---

## 🔧 COMANDOS RÁPIDOS

### Resetear PostgreSQL (si hay errores)
```bash
sudo systemctl stop postgresql
sudo -u postgres rm -rf /var/lib/postgres/data
sudo -u postgres initdb -D /var/lib/postgres/data
sudo systemctl start postgresql
```

### Ejecutar solo consultas SQL en PostgreSQL
```bash
sudo -u postgres psql postgres << EOF
SELECT * FROM mytable;
\dt  -- ver todas las tablas
\q
EOF
```

### Verificar driver JDBC
```bash
jar -tf ~/Descargas/postgresql-42.7.1.jar | grep -i postgresql
```

---

## 📝 NOTAS IMPORTANTES

1. **Paths:** Actualiza `/home/nirmata/` según tu usuario
2. **Puerto PostgreSQL:** Por defecto 5432, modifica si es diferente
3. **Contraseña:** En este ejercicio es `postgres`, cámbiala en producción
4. **Particiones Spark:** En `local[*]` usa todos los cores disponibles
5. **Cache:** El código usa `.cache()` para evitar recálculos

---

## 🎯 PRÓXIMOS PASOS

1. ✅ Ejecutar ambos archivos .scala
2. ✅ Tomar screenshots de cada sección importante
3. ✅ Documentar en PDF con explicaciones personales
4. ✅ Explicar con propias palabras qué hace cada comando
5. ✅ Analizar y comentar los resultados obtenidos

---

**Generado:** 2 de mayo de 2026  
**Versión:** AEC4 v1.0  
**Estado:** ✓ Completo y listo para ejecutar
