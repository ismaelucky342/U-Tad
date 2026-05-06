#!/usr/bin/env python3
"""
Generador de logs web artificiales para pruebas de Spark Streaming
Genera logs en formato Apache/Nginx
"""

import random
import time
from datetime import datetime, timedelta
import socket
import os
import sys

class LogGenerator:
    """Generador de logs web realistas"""
    
    def __init__(self):
        self.ips = [
            "192.168.1.100", "192.168.1.101", "192.168.1.102",
            "192.168.1.103", "192.168.1.104",
            "203.0.113.50", "203.0.113.51", "203.0.113.52",
            "203.0.113.53", "203.0.113.54",
            "198.51.100.20", "198.51.100.21", "198.51.100.22",
            "198.51.100.23", "198.51.100.24"
        ]
        
        self.users = ["admin", "user1", "user2", "user3", "user4", "guest", "-"]
        
        self.paths = [
            "/index.html", "/dashboard", "/api/login", "/api/users",
            "/products", "/checkout", "/cart", "/logout", "/profile",
            "/admin", "/settings", "/about", "/contact", "/api/data",
            "/images/logo.png", "/css/style.css", "/js/app.js",
            "/search", "/results", "/invoice", "/reports"
        ]
        
        self.methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"]
        self.status_codes = [100, 200, 201, 204, 301, 302, 304, 400, 401, 403, 404, 500, 502, 503]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Chrome/91.0.4472.124",
            "Firefox/89.0",
            "Safari/14.1.1",
            "curl/7.68.0",
            "Apache-HttpClient/4.5.13"
        ]
        
    def get_timestamp(self):
        """Retorna timestamp en formato Apache log"""
        return datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0200")
    
    def generate_log_line(self, request_id=None):
        """
        Genera una línea de log en formato Apache/Nginx
        
        Formato: IP - USER [timestamp] "METHOD PATH PROTOCOL" STATUS SIZE "REFERER" "USER-AGENT"
        """
        ip = random.choice(self.ips)
        user = random.choice(self.users)
        timestamp = self.get_timestamp()
        method = random.choice(self.methods)
        path = random.choice(self.paths)
        protocol = "HTTP/1.1"
        
        # Status 200 es más común (70% de probabilidad)
        if random.random() < 0.75:
            status = 200
            size = random.randint(500, 5000)
        elif random.random() < 0.70:
            status = 404
            size = 0
        elif random.random() < 0.80:
            status = 500
            size = 0
        else:
            status = random.choice(self.status_codes)
            size = random.randint(100, 2000) if status in [200, 201] else 0
        
        referer = "-" if random.random() < 0.3 else f"https://example.com{random.choice(self.paths)}"
        user_agent = random.choice(self.user_agents)
        
        log_line = f'{ip} - {user} [{timestamp}] "{method} {path} {protocol}" {status} {size} "{referer}" "{user_agent}"'
        return log_line
    
    def generate_to_file(self, filename, count, batch_delay=0.5):
        """
        Genera logs a un archivo en modo batch
        Simula llegada de logs a lo largo del tiempo
        """
        print(f"\n{'='*80}")
        print(f"GENERADOR DE LOGS WEB")
        print(f"{'='*80}")
        print(f"Generando {count} líneas de log...")
        print(f"Archivo: {filename}\n")
        
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else ".", exist_ok=True)
            
            with open(filename, 'w') as f:
                for i in range(count):
                    log_line = self.generate_log_line(i)
                    f.write(log_line + '\n')
                    
                    if (i + 1) % 10 == 0:
                        print(f"  [{i+1:3d}/{count}] Generados...")
                        time.sleep(batch_delay / 10)  # Pequeña pausa
            
            print(f"\n✓ Archivo '{filename}' generado exitosamente")
            print(f"  Total de líneas: {count}")
            print(f"  Tamaño aproximado: {os.path.getsize(filename) / 1024:.1f} KB\n")
            
        except Exception as e:
            print(f"✗ Error generando archivo: {e}\n")
            sys.exit(1)
    
    def stream_to_socket(self, host="localhost", port=9999, count=None, interval=0.5):
        """
        Envía logs a un socket TCP en tiempo real
        Útil para Spark Streaming desde socket
        """
        print(f"\n{'='*80}")
        print(f"STREAMING DE LOGS A SOCKET")
        print(f"{'='*80}")
        print(f"Host: {host}:{port}")
        print(f"Conectando...")
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            print(f"✓ Conectado a {host}:{port}\n")
            
            sent_count = 0
            try:
                while True:
                    if count and sent_count >= count:
                        print(f"\n✓ Se enviaron {sent_count} mensajes")
                        break
                    
                    log_line = self.generate_log_line()
                    
                    try:
                        s.send((log_line + '\n').encode('utf-8'))
                        sent_count += 1
                        
                        if sent_count % 10 == 0:
                            print(f"[{sent_count:4d}] Enviados...")
                        
                        time.sleep(interval)
                        
                    except BrokenPipeError:
                        print(f"\n✗ Conexión perdida después de {sent_count} mensajes")
                        break
                    except Exception as e:
                        print(f"✗ Error enviando: {e}")
                        break
                        
            except KeyboardInterrupt:
                print(f"\n\n✓ Interrupción del usuario")
                print(f"  Mensajes enviados: {sent_count}")
                
        except ConnectionRefusedError:
            print(f"\n✗ No se pudo conectar a {host}:{port}")
            print(f"  Asegúrate de que Spark Streaming esté escuchando en ese puerto")
            sys.exit(1)
        except Exception as e:
            print(f"✗ Error: {e}\n")
            sys.exit(1)
        finally:
            try:
                s.close()
            except:
                pass
    
    def stream_to_directory(self, directory="logs_input", interval=0.5, logs_per_batch=10):
        """
        Genera batchs de logs y los guarda en un directorio
        Spark Streaming vigila este directorio
        """
        print(f"\n{'='*80}")
        print(f"GENERADOR DE LOGS POR LOTES")
        print(f"{'='*80}")
        print(f"Directorio: {directory}")
        print(f"Logs por lote: {logs_per_batch}")
        print(f"Intervalo entre lotes: {interval}s\n")
        
        os.makedirs(directory, exist_ok=True)
        batch_num = 0
        total_logs = 0
        
        try:
            while True:
                batch_num += 1
                filename = f"{directory}/batch_{batch_num:03d}.log"
                
                with open(filename, 'w') as f:
                    for _ in range(logs_per_batch):
                        log_line = self.generate_log_line()
                        f.write(log_line + '\n')
                        total_logs += 1
                
                print(f"[{batch_num:3d}] Lote generado: {filename} ({total_logs} total)")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print(f"\n\n✓ Interrupción del usuario")
            print(f"  Lotes generados: {batch_num}")
            print(f"  Total de logs: {total_logs}")

def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generador de logs web para pruebas de Spark Streaming",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  # Generar archivo con 100 logs
  python3 generate_logs.py --file logs.txt --count 100
  
  # Generar logs continuamente a socket (requiere Spark escuchando)
  python3 generate_logs.py --socket --count 50
  
  # Generar lotes de logs en directorio
  python3 generate_logs.py --directory logs_input --batch
        """
    )
    
    parser.add_argument('--file', '-f', default='access_logs.txt',
                        help='Nombre del archivo de salida (default: access_logs.txt)')
    
    parser.add_argument('--count', '-c', type=int, default=100,
                        help='Número de logs a generar (default: 100)')
    
    parser.add_argument('--socket', '-s', action='store_true',
                        help='Enviar logs a socket TCP en lugar de archivo')
    
    parser.add_argument('--host', default='localhost',
                        help='Host para conexión socket (default: localhost)')
    
    parser.add_argument('--port', '-p', type=int, default=9999,
                        help='Puerto para conexión socket (default: 9999)')
    
    parser.add_argument('--directory', '-d', default='logs_input',
                        help='Directorio para guardar lotes (default: logs_input)')
    
    parser.add_argument('--batch', '-b', action='store_true',
                        help='Generar lotes en directorio en lugar de archivo único')
    
    parser.add_argument('--interval', '-i', type=float, default=0.5,
                        help='Intervalo entre logs o lotes en segundos (default: 0.5)')
    
    args = parser.parse_args()
    
    generator = LogGenerator()
    
    if args.socket:
        generator.stream_to_socket(
            host=args.host,
            port=args.port,
            count=args.count,
            interval=args.interval
        )
    elif args.batch:
        generator.stream_to_directory(
            directory=args.directory,
            interval=args.interval,
            logs_per_batch=10
        )
    else:
        generator.generate_to_file(
            filename=args.file,
            count=args.count,
            batch_delay=args.interval
        )

if __name__ == "__main__":
    main()
