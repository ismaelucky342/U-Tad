import mysql.connector
import random
from faker import Faker

fake = Faker()
generos = ["Ficción", "No Ficción", "Ciencia", "Historia", "Fantasía", "Terror", "Biografía"]

conn = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="Unidad4"
)

cursor = conn.cursor()

for i in range(1, 2001):
    titulo = fake.sentence(nb_words=4)
    autor = fake.name()
    año = random.randint(1950, 2025)
    genero = random.choice(generos)
    cursor.execute("""
        INSERT INTO libros (id_libro, titulo, autor, año_publicacion, genero)
        VALUES (%s, %s, %s, %s, %s)
    """, (i, titulo, autor, año, genero))

conn.commit()
cursor.close()
conn.close()