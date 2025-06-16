import pymysql

# Configuración de conexión
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_cutest'

)

def get_connection():
    return connection
