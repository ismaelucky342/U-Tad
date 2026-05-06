#!/usr/bin/env python3
"""
EJERCICIO 2 - SPARK STREAMING: Análisis de Logs Web en Tiempo Real
Variante 3: Análisis de logs web
- Lee datos desde fichero o socket
- Extrae IP y usuario
- Cuenta accesos por ventana de tiempo
- Identifica usuarios más activos
- Análisis adicional: códigos HTTP, rutas, anomalías
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, regexp_extract, count, desc, when
)
import sys

class WebLogAnalyzer:
    """Analizador de logs web con Spark Streaming"""
    
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("WebLogAnalysis") \
            .master("local[*]") \
            .config("spark.sql.shuffle.partitions", 4) \
            .getOrCreate()
        self.spark.sparkContext.setLogLevel("ERROR")
    
    def _parse_logs(self, logs_df):
        """
        Parsea líneas de log - Formato Apache/Nginx:
        IP - USER [timestamp] "METHOD PATH PROTOCOL" STATUS SIZE "REFERER" "USER-AGENT"
        """
        return logs_df.select(
            regexp_extract(col("log_line"), r'^(\S+)', 1).alias("ip"),
            regexp_extract(col("log_line"), r'- (\S+)', 1).alias("user"),
            regexp_extract(col("log_line"), r'"(\S+)', 1).alias("method"),
            regexp_extract(col("log_line"), r'"\S+\s(\S+)', 1).alias("path"),
            regexp_extract(col("log_line"), r'" (\d+)', 1).alias("status_code"),
            col("log_line")
        ).filter(col("ip") != "")
    
    def analyze_from_directory(self, log_directory="logs_input"):
        """Análisis desde directorio vigilado"""
        
        print("\n" + "="*80)
        print("SPARK STREAMING - ANÁLISIS DE LOGS WEB (Variante 3)")
        print("="*80)
        print(f"\nDirectorio: {log_directory}")
        print("Esperando nuevos archivos de log...\n")
        
        try:
            # Leer logs del directorio
            logs_df = self.spark.readStream \
                .format("text") \
                .option("maxFileAge", "10m") \
                .load(log_directory) \
                .withColumnRenamed("value", "log_line")
            
            # Parsear logs
            parsed = self._parse_logs(logs_df)
            
            # Análisis 1: Top IPs
            print("[ 1/6 ] IPs más activas...")
            ips_query = parsed \
                .groupBy("ip").agg(count("*").alias("accesos")) \
                .orderBy(desc("accesos")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 10) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            # Análisis 2: Top Usuarios
            print("[ 2/6 ] Usuarios más activos...")
            users_query = parsed \
                .filter(col("user") != "-") \
                .groupBy("user").agg(count("*").alias("accesos")) \
                .orderBy(desc("accesos")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 10) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            # Análisis 3: Códigos HTTP (Adicional)
            print("[ 3/6 ] Distribución de códigos HTTP...")
            status_query = parsed \
                .groupBy("status_code").agg(count("*").alias("cantidad")) \
                .orderBy(desc("cantidad")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 10) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            # Análisis 4: Métodos HTTP (Adicional)
            print("[ 4/6 ] Métodos HTTP más utilizados...")
            methods_query = parsed \
                .filter(col("method") != "") \
                .groupBy("method").agg(count("*").alias("cantidad")) \
                .orderBy(desc("cantidad")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 10) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            # Análisis 5: Rutas más visitadas (Adicional)
            print("[ 5/6 ] Rutas más visitadas...")
            paths_query = parsed \
                .filter(col("path") != "") \
                .groupBy("path").agg(count("*").alias("accesos")) \
                .orderBy(desc("accesos")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 8) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            # Análisis 6: Detección de anomalías (Adicional)
            print("[ 6/6 ] Detección de anomalías...\n")
            anomaly_query = parsed \
                .filter(col("status_code").isin("400", "401", "403", "404", "500", "502", "503")) \
                .groupBy("ip").agg(count("*").alias("errores")) \
                .filter(col("errores") > 2) \
                .orderBy(desc("errores")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 5) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            self.spark.streams.awaitAnyTermination()
            
        except Exception as e:
            print(f"✓ Error: {e}")
            sys.exit(1)
        finally:
            self.spark.stop()
    
    def analyze_from_socket(self, host="localhost", port=9999):
        """Análisis desde socket TCP"""
        
        print("\n" + "="*80)
        print("SPARK STREAMING - ANÁLISIS DE LOGS WEB (Variante 3)")
        print("="*80)
        print(f"\nSocket: {host}:{port}")
        print("Esperando logs desde socket...\n")
        
        try:
            logs_df = self.spark.readStream \
                .format("socket") \
                .option("host", host) \
                .option("port", port) \
                .load() \
                .withColumnRenamed("value", "log_line")
            
            parsed = self._parse_logs(logs_df)
            
            # Análisis 1: Top IPs
            ips_query = parsed \
                .groupBy("ip").agg(count("*").alias("accesos")) \
                .orderBy(desc("accesos")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 10) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            # Análisis 2: Top Usuarios
            users_query = parsed \
                .filter(col("user") != "-") \
                .groupBy("user").agg(count("*").alias("accesos")) \
                .orderBy(desc("accesos")) \
                .writeStream \
                .outputMode("complete") \
                .format("console") \
                .option("numRows", 10) \
                .trigger(processingTime="5 seconds") \
                .start()
            
            self.spark.streams.awaitAnyTermination()
        
        except Exception as e:
            print(f"✓ Error: {e}")
            sys.exit(1)
        finally:
            self.spark.stop()


def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Analizador de logs web con Spark Streaming"
    )
    
    parser.add_argument('--directory', '-d', default='logs_input',
                        help='Directorio de logs (default: logs_input)')
    parser.add_argument('--socket', '-s',
                        help='Conexión socket (formato: host:puerto)')
    
    args = parser.parse_args()
    analyzer = WebLogAnalyzer()
    
    if args.socket:
        try:
            host, port = args.socket.split(':')
            port = int(port)
            analyzer.analyze_from_socket(host, port)
        except ValueError:
            print(f"✓ Error formato socket inválido: {args.socket}")
            sys.exit(1)
    else:
        analyzer.analyze_from_directory(args.directory)


if __name__ == "__main__":
    main()
