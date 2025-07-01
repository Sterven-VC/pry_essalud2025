from .entities.AsignacionDoctorActividad import AsignacionDoctorActividad
from flask import flash

class ModelAsignacionDoctorActividad:
    @classmethod
    def asignar_doctor(cls, db, asignacion):
        try:
            cursor = db.cursor()
            sql = 'INSERT INTO asignacion_doctor_actividad (doctor_id, actividad_id, fecha) VALUES (%s, %s, %s)'
            cursor.execute(sql, (asignacion.doctor_id, asignacion.actividad_id, asignacion.fecha))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al asignar doctorssds: ' + str(ex))
            return False

    @classmethod
    def obtener_asignaciones_mes(cls, db, mes, anio):
        try:
            cursor = db.cursor()
            sql = '''SELECT * FROM asignacion_doctor_actividad WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s'''
            cursor.execute(sql, (mes, anio))
            results = cursor.fetchall()
            asignaciones = [AsignacionDoctorActividad(row[0], row[1], row[2], row[3]) for row in results]
            cursor.close()
            return asignaciones
        except Exception as ex:
            flash('Error al obtener asignaciones: ' + str(ex))
            return []

    @classmethod
    def get_asignaciones_by_mes(cls, db, mes, anio):
        return cls.obtener_asignaciones_mes(db, mes, anio)

    @classmethod
    def contar_doctores_en_actividad_dia(cls, db, actividad_id, fecha):
        try:
            cursor = db.cursor()
            sql = 'SELECT COUNT(*) FROM asignacion_doctor_actividad WHERE actividad_id = %s AND fecha = %s'
            cursor.execute(sql, (actividad_id, fecha))
            count = cursor.fetchone()[0]
            cursor.close()
            return count
        except Exception as ex:
            flash('Error al contar doctores: ' + str(ex))
            return 0

    @classmethod
    def quitar_doctor(cls, db, actividad_id, doctor_id, fecha):
        try:
            cursor = db.cursor()
            sql = 'DELETE FROM asignacion_doctor_actividad WHERE actividad_id = %s AND doctor_id = %s AND fecha = %s'
            cursor.execute(sql, (actividad_id, doctor_id, fecha))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al quitar doctor: ' + str(ex))
            return False

    @classmethod
    def count_doctores_por_actividad_dia(cls, db, actividad_id, fecha):
        # Alias para compatibilidad con el backend
        return cls.contar_doctores_en_actividad_dia(db, actividad_id, fecha)
