from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

libro = input("Título del libro a eliminar: ")

cursor.execute("DELETE FROM libros WHERE titulo_libro = %s", (libro,))
conn.commit()

if cursor.rowcount > 0:
    print("Libro eliminado correctamente.")
else:
    print("Libro no encontrado.")

cursor.close()
conn.close()