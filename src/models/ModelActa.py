from .entities.Acta import Acta
from flask import flash


class ModelActa:
    @classmethod
    def get_vigente_junta_id(cls, db):
        try:
            cursor = db.cursor()
            sql = "SELECT id FROM junta_directiva WHERE vigencia = 1 LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            if result:
                return result[0]  # Retorna el ID de la junta directiva vigente
            else:
                flash("No se encontró ninguna junta directiva vigente.")
                return None
        except Exception as ex:
            flash("ERROR: " + str(ex))
            return None

    @classmethod
    def register_acta(cls, db, acta):
        try:
            cursor = db.cursor()
            # Obtener la junta directiva vigente (vigencia = 1)
            id_junta_vigente = cls.get_vigente_junta_id(db)
            
            if not id_junta_vigente:
                return False

            acta.id_junta_directiva = id_junta_vigente
            
            # Registrar el acta con la junta directiva vigente
            sql = """INSERT INTO acta (nombre, fecha, ruta_pdf, id_junta_directiva, asistencia_1, asistencia_2, asistencia_3, asistencia_4, asistencia_5, asistencia_6, asistencia_7, asistencia_8)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (acta.nombre, acta.fecha, acta.ruta_pdf, acta.id_junta_directiva, acta.asistencia_1, acta.asistencia_2, acta.asistencia_3, acta.asistencia_4, acta.asistencia_5, acta.asistencia_6, acta.asistencia_7, acta.asistencia_8))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR: " + str(ex))
            return False

    @classmethod
    def get_all_actas(cls, db):
        try:
            cursor = db.cursor()
            # Obtener el ID de la junta directiva vigente
            sql_vigente = "SELECT id FROM junta_directiva WHERE vigencia = 1 LIMIT 1"
            cursor.execute(sql_vigente)
            id_junta_vigente = cursor.fetchone()
            
            if not id_junta_vigente:
                flash("No hay una junta directiva vigente.")
                return []

            id_junta_vigente = id_junta_vigente[0]
            
            # Obtener las actas asociadas a la junta directiva vigente
            sql = """
            SELECT id, nombre, fecha, ruta_pdf, id_junta_directiva, asistencia_1, asistencia_2, asistencia_3, asistencia_4, asistencia_5, asistencia_6, asistencia_7, asistencia_8
            FROM acta 
            WHERE id_junta_directiva = %s
            """
            cursor.execute(sql, (id_junta_vigente,))
            results = cursor.fetchall()
            actas = []
            for row in results:
                acta = Acta(row[0], row[1], row[2], row[3], row[4] , row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
                actas.append(acta)
            cursor.close()
            return actas
        except Exception as ex:
            flash("ERROR:  mostrar" + str(ex))
            return []
            
    @classmethod
    def get_acta_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM acta WHERE id = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            cursor.close()
            if row:
                return Acta(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
            else:
                flash("Acta no encontrada.")
                return None
        except Exception as ex:
            flash("ERROR: " + str(ex))
            return None

    @classmethod
    def update_acta(cls, db, acta):
        try:
            cursor = db.cursor()

            # Actualizar el acta con la nueva información
            sql = """UPDATE acta 
                    SET nombre = %s, fecha = %s, ruta_pdf = %s, id_junta_directiva = %s, 
                        asistencia_1 = %s, asistencia_2 = %s, asistencia_3 = %s, 
                        asistencia_4 = %s, asistencia_5 = %s, asistencia_6 = %s, 
                        asistencia_7 = %s, asistencia_8 = %s
                    WHERE id = %s"""
            cursor.execute(sql, (
                acta.nombre, acta.fecha, acta.ruta_pdf, acta.id_junta_directiva,
                acta.asistencia_1, acta.asistencia_2, acta.asistencia_3,
                acta.asistencia_4, acta.asistencia_5, acta.asistencia_6,
                acta.asistencia_7, acta.asistencia_8, acta.id
            ))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR: " + str(ex))
            return False

    @classmethod
    def delete_acta(cls, db, id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM acta WHERE id = %s"
            cursor.execute(sql, (id,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR: " + str(ex))
            return False



#class ModelActa:
    @classmethod
    def get_actas_with_cuorum_status(cls, db):
        try:
            cursor = db.cursor()
            sql = """SELECT id, nombre, fecha, asistencia_1, asistencia_2, asistencia_3, asistencia_4, asistencia_5, asistencia_6, asistencia_7, asistencia_8
                     FROM acta"""
            cursor.execute(sql)
            actas = cursor.fetchall()
            cursor.close()

            # Determinar cuórum
            cuorum_status = []
            for acta in actas:
                asistencia_count = sum([acta[i] for i in range(3, 11)])  # Contar las asistencias
                if asistencia_count > 5:
                    status = "Cuórum"
                else:
                    status = "No cuórum"
                cuorum_status.append({
                    'id': acta[0],
                    'nombre': acta[1],
                    'fecha': acta[2],
                    'asistencia': asistencia_count,
                    'status': status
                })
            return cuorum_status
        except Exception as ex:
            print("ERROR:", ex)
            return []
