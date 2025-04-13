from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

autor = input("Introduce el apellido del autor: ")

query = """
SELECT titulo_libro FROM libros
JOIN autores ON libros.autor_id = autores.autor_id
WHERE apellido_autor = %s
"""

cursor.execute(query, (autor,))
resultados = cursor.fetchall()

print("Libros del autor:")
for libro in resultados:
    print("-", libro[0])

cursor.close()
conn.close()