import mysql.connector
import time

# Conexión
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="tienda_online"
)
cursor = conn.cursor()

# 1. Insertar producto
def insertar_producto(nombre, precio, stock):
    sql = "INSERT INTO PRODUCTOS (nombre, precio, stock) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, precio, stock))
    conn.commit()

# 2. Buscar por nombre exacto
def buscar_por_nombre(nombre):
    sql = "SELECT * FROM PRODUCTOS WHERE nombre = %s"
    cursor.execute(sql, (nombre,))
    for row in cursor.fetchall():
        print(row)

# 3. Buscar por nombre parcial
def buscar_por_nombre_parcial(texto):
    sql = "SELECT * FROM PRODUCTOS WHERE nombre LIKE %s"
    cursor.execute(sql, ('%' + texto + '%',))
    for row in cursor.fetchall():
        print(row)

# 4. Listar ordenados por precio
def listar_productos_ordenados():
    cursor.execute("SELECT * FROM PRODUCTOS ORDER BY precio ASC")
    for row in cursor.fetchall():
        print(row)

# 5. Comparar tiempo con y sin índice
def comparar_tiempos():
    start = time.time()
    buscar_por_nombre("Teclado")
    end = time.time()
    print("Tiempo de búsqueda:", end - start)

# Menú
def menu():
    while True:
        print("\n1. Insertar producto")
        print("2. Buscar producto exacto")
        print("3. Buscar producto parcial")
        print("4. Listar productos por precio")
        print("5. Salir")
        opc = input("Elige: ")
        if opc == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            insertar_producto(nombre, precio, stock)
        elif opc == "2":
            nombre = input("Nombre exacto: ")
            buscar_por_nombre(nombre)
        elif opc == "3":
            texto = input("Texto parcial: ")
            buscar_por_nombre_parcial(texto)
        elif opc == "4":
            listar_productos_ordenados()
        elif opc == "5":
            break

menu()
cursor.close()
conn.close()
# Cerrar la conexión
conn.close()