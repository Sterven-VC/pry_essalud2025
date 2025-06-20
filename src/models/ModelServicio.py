from .entities.Servicio import Servicio
from flask import flash

class ModelServicio:

    @classmethod
    def create_servicio(cls, db, nombre, departamento_id):
        try:
            cursor = db.cursor()
            sql = 'INSERT INTO servicio (nombre, departamento_id) VALUES (%s, %s)'
            cursor.execute(sql, (nombre, departamento_id))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al registrar el servicio ' + str(ex))
            return False
        
    @classmethod
    def get_all_servicios(cls, db):
        try:
            cursor = db.cursor()
            sql = 'SELECT * FROM servicio'
            cursor.execute(sql)
            results = cursor.fetchall()
            servicios = []
            for row in results:
                servicio = Servicio(row[0], row[1], row[2])
                servicios.append(servicio)
            cursor.close()
            return servicios
        except Exception as ex:
            flash ('Error al listar servicios ' + str(ex))

    @classmethod
    def get_servicio_by_id(cls,db,id):
        try:
            cursor = db.cursor()
            sql = 'SELECT * FROM servicio WHERE id = %s'
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row:
                return Servicio(row[0], row[1], row[2])
            else:
                return None
        except Exception as ex:
            flash ('Error al obtener el servicio '+ str(ex))
            return None

    @classmethod
    def update_servicio(cls, db, servicio):
        try:
            cursor = db.cursor()
            sql = 'UPDATE servicio SET departamento_id=%s, nombre=%s WHERE id=%s'
            cursor.execute(sql, (servicio.nombre, servicio.departamento_id, servicio.id))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash ('Error al actualizar el servicio '+ str(ex))
            return False
        
    @classmethod
    def delete_servicio (cl, db, id):
        try:
            cursor = db.cursor()
            sql = 'DELETE FROM servicio where id = %s'
            cursor.execute(sql, (id,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash ('Error al borrar el servicio ' + str(ex))
            return False




