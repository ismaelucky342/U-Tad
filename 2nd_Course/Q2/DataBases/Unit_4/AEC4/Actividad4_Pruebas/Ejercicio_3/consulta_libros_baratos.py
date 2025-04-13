from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

cursor.execute("SELECT titulo_libro, precio FROM libros WHERE precio < 20.00")
resultados = cursor.fetchall()

print("Libros con precio menor a 20.00:")
for titulo, precio in resultados:
    print(f"{titulo} - ${precio}")

cursor.close()
conn.close()