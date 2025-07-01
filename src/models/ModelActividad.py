from .entities.Actividad import Actividad
from flask import flash

class ModelActividad:

    # Registrar una nueva actividad
    @classmethod
    def register_actividad(cls, db, actividad):
        try:
            cursor = db.cursor()
            sql = 'INSERT INTO actividad (nombre, servicio_id, departamento_id, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(sql, (actividad.nombre, actividad.servicio_id, actividad.departamento_id, actividad.hora_inicio, actividad.hora_fin))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al registrar la actividad: ' + str(ex))
            return False
    
    # Obtener todas las actividades
    @classmethod
    def get_all_actividades(cls, db):
        try:
            cursor = db.cursor()
            sql = 'SELECT * FROM actividad'
            cursor.execute(sql)
            results = cursor.fetchall()
            actividades = []
            for row in results:
                actividad = Actividad(row[0], row[1], row[2], row[3], row[4], row[5])
                actividades.append(actividad)
            cursor.close()
            return actividades
        except Exception as ex:
            flash('Error al listar las actividades: ' + str(ex))
            return []

    # Obtener una actividad por su ID
    @classmethod
    def get_actividad_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            sql = 'SELECT * FROM actividad WHERE id = %s'
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row:
                return Actividad(row[0], row[1], row[2], row[3], row[4], row[5])
            else:
                return None
        except Exception as ex:
            flash('Error al obtener la actividad: ' + str(ex))
            return None

    # Actualizar una actividad existente
    @classmethod
    def update_actividad(cls, db, actividad):
        try:
            cursor = db.cursor()
            sql = 'UPDATE actividad SET nombre = %s, servicio_id = %s, departamento_id = %s, hora_inicio = %s, hora_fin = %s WHERE id = %s'
            cursor.execute(sql, (actividad.nombre, actividad.servicio_id, actividad.departamento_id, actividad.hora_inicio, actividad.hora_fin, actividad.id))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al actualizar la actividad: ' + str(ex))
            return False

    # Eliminar una actividad
    @classmethod
    def delete_actividad(cls, db, id):
        try:
            cursor = db.cursor()
            sql = 'DELETE FROM actividad WHERE id = %s'
            cursor.execute(sql, (id,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al eliminar la actividad: ' + str(ex))
            return False

    # Obtener actividades por servicio
    @classmethod
    def get_actividades_by_servicio(cls, db, servicio_id):
        try:
            cursor = db.cursor()
            sql = 'SELECT id, nombre, servicio_id, departamento_id, hora_inicio, hora_fin FROM actividad WHERE servicio_id = %s'
            cursor.execute(sql, (servicio_id,))
            results = cursor.fetchall()
            actividades = []
            for row in results:
                actividad = Actividad(row[0], row[1], row[2], row[3], row[4], row[5])
                actividades.append(actividad)
            cursor.close()
            return actividades
        except Exception as ex:
            from flask import flash
            flash('Error al obtener actividades por servicio: ' + str(ex))
            return []
