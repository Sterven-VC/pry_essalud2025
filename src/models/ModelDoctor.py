from .entities.Doctor import Doctor
from flask import flash

class ModelDoctor:
    
    @classmethod
    def create_doctor(cls, db, doctor):
        try:
            cursor = db.cursor()
            sql = 'INSERT INTO doctor (nombre, id_usuario) VALUES (%s, %s)'
            cursor.execute(sql, (doctor.nombre, doctor.id_usuario))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al registrar el doctor: ' + str(ex))
            return False

    @classmethod
    def get_all_doctores(cls, db):
        try:
            cursor = db.cursor()
            sql = 'SELECT * FROM doctor'
            cursor.execute(sql)
            results = cursor.fetchall()
            doctores = []
            for row in results:
                doctor = Doctor(row[0], row[1], row[2])  # id, nombre, id_usuario
                doctores.append(doctor)
            cursor.close()
            return doctores
        except Exception as ex:
            flash('Error al listar doctores: ' + str(ex))
            return []

    @classmethod
    def get_doctor_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            sql = 'SELECT * FROM doctor WHERE id = %s'
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row:
                return Doctor(row[0], row[1], row[2])
            else:
                return None
        except Exception as ex:
            flash('Error al obtener el doctor: ' + str(ex))
            return None

    @classmethod
    def update_doctor(cls, db, doctor):
        try:
            cursor = db.cursor()
            sql = 'UPDATE doctor SET nombre = %s, id_usuario = %s WHERE id = %s'
            cursor.execute(sql, (doctor.nombre, doctor.id_usuario, doctor.id))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al actualizar el doctor: ' + str(ex))
            return False

    @classmethod
    def delete_doctor(cls, db, id):
        try:
            cursor = db.cursor()
            sql = 'DELETE FROM doctor WHERE id = %s'
            cursor.execute(sql, (id,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash('Error al eliminar el doctor: ' + str(ex))
            return False

    @classmethod
    def get_doctores_by_departamento(cls, db, departamento_id):
        try:
            cursor = db.cursor()
            sql = '''SELECT d.id, d.nombre, d.id_usuario FROM doctor d
                     JOIN user u ON d.id_usuario = u.id
                     WHERE u.departamento_id = %s'''
            cursor.execute(sql, (departamento_id,))
            results = cursor.fetchall()
            from models.entities.Doctor import Doctor
            doctores = [Doctor(row[0], row[1], row[2]) for row in results]
            cursor.close()
            return doctores
        except Exception as ex:
            from flask import flash
            flash('Error al obtener doctores por departamento: ' + str(ex))
            return []

    @classmethod
    def get_doctores_by_usuario(cls, db, id_usuario):
        try:
            cursor = db.cursor()
            sql = 'SELECT id, nombre, id_usuario FROM doctor WHERE id_usuario = %s'
            cursor.execute(sql, (id_usuario,))
            results = cursor.fetchall()
            from models.entities.Doctor import Doctor
            doctores = [Doctor(row[0], row[1], row[2]) for row in results]
            cursor.close()
            return doctores
        except Exception as ex:
            from flask import flash
            flash('Error al obtener doctores por usuario: ' + str(ex))
            return []