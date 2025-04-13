from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

libro = input("Título del libro a actualizar: ")
nuevo_precio = float(input("Nuevo precio: "))

cursor.execute("UPDATE libros SET precio = %s WHERE titulo_libro = %s", (nuevo_precio, libro))
conn.commit()

if cursor.rowcount > 0:
    print("Precio actualizado correctamente.")
else:
    print("Libro no encontrado.")

cursor.close()
conn.close()