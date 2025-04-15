import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="cine_db"
)
cursor = conn.cursor()

# Mostrar tablas disponibles
def mostrar_tablas():
    cursor.execute("SHOW TABLES")
    for (tabla,) in cursor.fetchall():
        print("→", tabla)

# Mostrar columnas de una tabla
def estructura_tabla(nombre):
    cursor.execute(f"DESCRIBE {nombre}")
    for columna in cursor.fetchall():
        print(columna)

# Mostrar índices
def mostrar_indices(nombre):
    cursor.execute(f"SHOW INDEX FROM {nombre}")
    for indice in cursor.fetchall():
        print(indice)

# Menu
def menu():
    while True:
        print("\n--- Explorador MySQL ---")
        print("1. Ver tablas")
        print("2. Ver estructura de tabla")
        print("3. Ver índices")
        print("4. Salir")
        opc = input("Elige: ")
        if opc == "1":
            mostrar_tablas()
        elif opc == "2":
            tabla = input("Nombre de la tabla: ")
            estructura_tabla(tabla)
        elif opc == "3":
            tabla = input("Nombre de la tabla: ")
            mostrar_indices(tabla)
        elif opc == "4":
            break

menu()
cursor.close()
conn.close()
