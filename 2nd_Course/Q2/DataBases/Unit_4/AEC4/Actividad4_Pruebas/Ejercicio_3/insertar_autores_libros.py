from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

# Insertar autores
autores = [
    ("Gabriel", "García Márquez"),
    ("Isabel", "Allende"),
    ("Jorge", "Luis Borges")
]

cursor.executemany("INSERT INTO autores (nombre_autor, apellido_autor) VALUES (%s, %s)", autores)

# Insertar libros
libros = [
    ("Cien años de soledad", "1967-05-30", 18.50, 1),
    ("El amor en los tiempos del cólera", "1985-09-05", 21.00, 1),
    ("La casa de los espíritus", "1982-01-01", 19.90, 2),
    ("Eva Luna", "1987-11-11", 15.00, 2),
    ("Ficciones", "1944-01-01", 22.00, 3),
]

cursor.executemany("INSERT INTO libros (titulo_libro, fecha_publicacion, precio, autor_id) VALUES (%s, %s, %s, %s)", libros)

conn.commit()
cursor.close()
conn.close()
print("Autores y libros insertados correctamente.")