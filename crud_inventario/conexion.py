import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='inventario_db'
    )
