import pymysql
from config import config

# Obtiene la configuración actual de la aplicación (development en este caso)
current_config = config['development']()

def get_connection():
    connection = pymysql.connect(
        host=current_config.MYSQL_HOST,
        user=current_config.MYSQL_USER,
        password=current_config.MYSQL_PASSWORD,
        database=current_config.MYSQL_DB,
        charset='utf8mb4',
        autocommit=True
    )
    return connection

def reconnect_db(connection):
    try:
        # Intenta reconectar si la conexión está inactiva o perdida
        connection.ping(reconnect=True)
    except pymysql.MySQLError as e:
        print(f"Error al reconectar: {e}")