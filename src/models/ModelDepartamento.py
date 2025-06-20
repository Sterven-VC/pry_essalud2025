from .entities.Departamento import Departamento
from flask import flash

class ModelDepartamento:

    @classmethod
    def create_departamento(cls, db, nombre):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO departamento (nombre) VALUES (%s)"
            cursor.execute(sql, (nombre,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash ('Error al registar departamento ' + str(ex))
            return False
    
    @classmethod
    def get_all_departamentos (cls, db):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM departamento"
            cursor.execute(sql)
            results = cursor.fetchall()
            departamentos = []
            for row in results:
                departamento = Departamento(row[0], row[1])
                departamentos.append(departamento)
            cursor.close()
            return departamentos
        except Exception as ex:
            flash ('Error al listar departamentos ' + str(ex))
            return[]

    @classmethod
    def get_departamento_by_id (cls, db, id):
        try:
            cursor= db.cursor()
            sql = "SELECT * FROM departamento WHERE id = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row:
                return Departamento(row[0], row[1])
            else:
                return None
        except Exception as ex:
            flash ('Error al obtener el departamento ' + str(ex))
            return None
        
    @classmethod
    def update_departamento (cls, db, departamento):
        try:
            cursor = db.cursor()
            sql = 'UPDATE departamento SET nombre = %s WHERE id = %s'
            cursor.execute(sql, (departamento.nombre, departamento.id))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash ('Error al actualizar departamento ' + str(ex))
            return False

    @classmethod
    def delete_departamento (cls, db, id):
        try:
            cursor = db.cursor()
            sql = 'DELETE FROM departamento WHERE id = %s'
            cursor.execute(sql, (id,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash ('Error al eliminar ' + str(ex))
            return False

    