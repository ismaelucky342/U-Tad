from conexion_db import conectar

conn = conectar()
cursor = conn.cursor()

with open("ejercicio4_3.sql", "r") as f:
    script = f.read()

for statement in script.strip().split(';'):
    if statement.strip():
        cursor.execute(statement)

conn.commit()
cursor.close()
conn.close()
print("Tablas creadas correctamente.")