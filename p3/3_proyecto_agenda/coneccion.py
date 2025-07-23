import mysql.connector

# Conexión al servidor MariaDB
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    port=3306
)

cursor = conexion.cursor()

cursor.close()
conexion.close()