# AEC2 - Procesamiento de Datos

## Introduccion

Esta practica ha consistido en un recorrido practico por tres bloques un ejercicio con comandos de HDFS, una representacion manual de MapReduce con registros simulados, y un analisis de un sistema real bajo el teorema CAP. La entrega esta dividida en esos tres bloques para que sea facil de seguir y de presentar como memoria.

En el bloque 1 hago el caso de HDFS con un paso que falla y su correccion. En el bloque 2 muestro el flujo Map y Reduce con diez registros y en el bloque 3 tengo un caso CAP con justificacion tecnica y de negocio. Ademas de este archivo, presento como material adicional un script con mini menu interactivo que ejecuta el bloque de HDFS y sirve como visor de los otros bloques para facilitar el debug.

## Bloque 1 - HDFS

La idea es un caso aplicado a una editorial ficticia, se descarga un libro en local, se crea un directorio en HDFS, se sube el archivo, se inspecciona su contenido y se gestiona su ciclo de vida con renombrado, descarga y borrado.

Incluyo un error intencionado al subir un fichero que no existe para mostrar el tipo de fallo mas comun, explicar por que ocurre y aplicar el procedimiento correcto para solucionarlo.

### Comandos completos (bloque 1)

> Ruta de Hadoop usada en los apuntes: `/home/bigdata/hadoop-3.3.6/`.

```bash
cd /home/bigdata/hadoop-3.3.6/

# Arranque de HDFS
sbin/start-dfs.sh

# Comprobaciones iniciales
bin/hdfs dfs -help
bin/hdfs dfs -ls /

# Crear directorio de trabajo
bin/hdfs dfs -mkdir /ebooks

# Descargar libro en local
mkdir -p /home/bigdata/datos
wget -q https://www.gutenberg.org/cache/epub/11/pg11.txt -O /home/bigdata/datos/alice.txt

# Paso con error intencionado
bin/hdfs dfs -put /home/bigdata/datos/no_existe.txt /ebooks/

# Solucion: subir el archivo correcto
bin/hdfs dfs -put /home/bigdata/datos/alice.txt /ebooks/
bin/hdfs dfs -ls /ebooks
bin/hdfs dfs -head /ebooks/alice.txt
bin/hdfs dfs -tail /ebooks/alice.txt

# Buscar y medir uso de espacio
bin/hdfs dfs -find / -name alice.txt
bin/hdfs dfs -du -h /ebooks
bin/hdfs dfs -count /ebooks

# Renombrar, descargar y borrar
bin/hdfs dfs -mv /ebooks/alice.txt /ebooks/alice_renombrado.txt
bin/hdfs dfs -get /ebooks/alice_renombrado.txt /home/bigdata/datos/alice_descargado.txt
bin/hdfs dfs -rm /ebooks/alice_renombrado.txt

# Parar HDFS
sbin/stop-dfs.sh
```

### Capturas

Ejecutar el script:

```bash
chmod +x run_hdfs_pruebas.sh
./run_hdfs_pruebas.sh
```

## 2) Practica manual de MapReduce

### Escenario real elegido

He elegido el caso de uso de bicicletas compartidas en una gran ciudad. El objetivo es calcular el porcentaje de devoluciones tardias por estacion, un indicador util para detectar puntos con problemas de disponibilidad o funcionamiento.

### Justificacion Big Data

El problema creo que encaja en Big Data por varias razones por un lado el volumen es alto porque hay millones de viajes al mes, cada uno con muchos atributos. La velocidad es elevada porque los eventos se generan en tiempo real desde docks y apps. La variedad aparece en la mezcla de datos de viajes, logs de la aplicacion y variables externas como el clima. La veracidad no es perfecta por fallos de sensores o usuarios, y el valor esta en optimizar la operativa y mejorar la experiencia del usuario.

### Representacion manual de Map y Reduce (10 registros)

#### Registros de entrada (simulados)

Formato: `(viaje_id, estacion, minutos_retraso)`

1. (v001, SOL, 0)
2. (v002, SOL, 7)
3. (v003, ATO, 0)
4. (v004, ATO, 12)
5. (v005, ATO, 4)
6. (v006, GRA, 0)
7. (v007, GRA, 0)
8. (v008, GRA, 9)
9. (v009, SOL, 0)
10. (v010, SOL, 3)

Criterio: se considera tardia si `minutos_retraso > 5`.

#### Fase Map

Emito `(estacion, (tardia, total))` para cada registro.

- v001 -> (SOL, (0, 1))
- v002 -> (SOL, (1, 1))
- v003 -> (ATO, (0, 1))
- v004 -> (ATO, (1, 1))
- v005 -> (ATO, (0, 1))
- v006 -> (GRA, (0, 1))
- v007 -> (GRA, (0, 1))
- v008 -> (GRA, (1, 1))
- v009 -> (SOL, (0, 1))
- v010 -> (SOL, (0, 1))

#### Shuffle/Sort

Agrupo por clave:

- SOL -> (0,1), (1,1), (0,1), (0,1)
- ATO -> (0,1), (1,1), (0,1)
- GRA -> (0,1), (0,1), (1,1)

#### Fase Reduce

Sumo tardias y totales y calculo el porcentaje:

- SOL -> tardias=1, total=4, porcentaje=25%
- ATO -> tardias=1, total=3, porcentaje=33.3%
- GRA -> tardias=1, total=3, porcentaje=33.3%

Resultado final: ATO y GRA presentan mas retraso relativo que SOL.

## 3) Caso CAP

### Sistema distribuido real: Apache Cassandra

He escogido Apache Cassandra porque es una base de datos distribuida muy usada en servicios con mucha carga (telemetria, logs, IoT). Es un ejemplo claro para explicar los compromisos del teorema CAP.

### Analisis CAP

- Tolerancia a particiones (P): si hay cortes de red, el sistema sigue funcionando con los nodos disponibles.
- Disponibilidad (A): prioriza responder peticiones aunque exista particion, devolviendo respuestas locales.
- Consistencia (C): no siempre es estricta; se trabaja con consistencia eventual o configurada por nivel.

### Justificacion tecnica

Cassandra replica datos y permite elegir niveles de consistencia en lectura y escritura. En caso de particion, prefiere seguir aceptando operaciones para no frenar el servicio (A) y tolerar la particion (P), aunque eso implique divergencias temporales entre replicas.

### Justificacion de negocio

En sistemas de monitorizacion y logs es mas importante mantener el servicio activo y no perder datos que bloquear todo por consistencia estricta. La consistencia eventual es suficiente porque se puede reconciliar mas tarde.

## Uso de IA (si aplica)

Para cumplir la norma del enunciado, dejo documentado el uso de IA si se considera:

- **Prompt usado:** "Genera un README para una practica con HDFS, MapReduce manual y un caso CAP; incluye un paso con error y su solucion, y un script de pruebas."
- **Respuesta de la IA (resumen):** propuso una estructura con secciones, un ejemplo HDFS con error de ruta, un flujo MapReduce con 10 registros y un caso CAP con Cassandra.
- **Mi interpretacion personal:** revise la propuesta, ajuste el escenario a mis palabras, seleccione un dataset de dominio publico y redacte la explicacion final con mis propios criterios.

## Referencias

- https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html
- https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSUserGuide.html
- https://www.gutenberg.org/ (libros de dominio publico)
