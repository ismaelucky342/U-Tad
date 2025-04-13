import MySQLdb

def conectar():
    return MySQLdb.connect(
        host="localhost",
        user="tu_usuario",
        passwd="tu_contraseña",
        db="biblioteca_db"
    )