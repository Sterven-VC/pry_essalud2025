from .entities.JuntaDirectiva import JuntaDirectiva
from flask import flash

class ModelJuntaDirectiva:
    @classmethod
    def register_JuntaDirectiva(cls, db, junta_directiva):
        try:
            cursor = db.cursor()
            
            # Desactivar cualquier junta directiva activa existente
            sql_disable_current = "UPDATE junta_directiva SET vigencia = FALSE WHERE vigencia = TRUE"
            cursor.execute(sql_disable_current)

            # Verificar si ya existe una junta directiva en el mismo rango de fechas
            sql_check = """SELECT COUNT(*) FROM junta_directiva 
                           WHERE (fecha_inicio <= %s AND fecha_fin >= %s)
                           OR (fecha_inicio <= %s AND fecha_fin >= %s)"""
            cursor.execute(sql_check, (junta_directiva.fecha_fin, junta_directiva.fecha_inicio, junta_directiva.fecha_inicio, junta_directiva.fecha_fin))
            if cursor.fetchone()[0] > 0:
                flash("ERROR REGISTER: YA EXISTE UNA JUNTA DIRECTIVA EN EL MISMO RANGO DE FECHAS")
                return False
            
            sql = """INSERT INTO junta_directiva (nombre, fecha_inicio, fecha_fin, miembro1, cargo1, miembro2, cargo2, miembro3, cargo3, miembro4, cargo4, miembro5, cargo5, miembro6, cargo6, miembro7, cargo7, miembro8, cargo8, vigencia)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (junta_directiva.nombre, junta_directiva.fecha_inicio, junta_directiva.fecha_fin, junta_directiva.miembro1, junta_directiva.cargo1, junta_directiva.miembro2, junta_directiva.cargo2, junta_directiva.miembro3, junta_directiva.cargo3, junta_directiva.miembro4, junta_directiva.cargo4, junta_directiva.miembro5, junta_directiva.cargo5, junta_directiva.miembro6, junta_directiva.cargo6, junta_directiva.miembro7, junta_directiva.cargo7, junta_directiva.miembro8, junta_directiva.cargo8, junta_directiva.vigencia)
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash(f"ERROR REGISTER: NO SE PERMITEN DIRECTIVOS CON EL MISMO NOMBRE {str(ex)}")
            return False


    @classmethod
    def get_all_juntas_directivas(cls, db):
        try:
            cursor = db.cursor()
            sql = """
            SELECT * 
            FROM junta_directiva
            ORDER BY vigencia DESC, fecha_inicio DESC
             """
            cursor.execute(sql)
            results = cursor.fetchall()
            juntas_directivas = []
            for row in results:
                junta_directiva = JuntaDirectiva(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20])
                juntas_directivas.append(junta_directiva)
            cursor.close()
            return juntas_directivas
        except Exception as ex:
            flash("ERROR LISTAR: " + str(ex))
            return [] 

    @classmethod
    def get_junta_directiva_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM junta_directiva WHERE id = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row:
                junta_directiva = JuntaDirectiva(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20])
                return junta_directiva
            return None
        except Exception as ex:
            flash("ERROR OBTENER ID: " + str(ex))
            return None

    @classmethod
    def update_junta_directiva(cls, db, junta_directiva):
        try:
            cursor = db.cursor()

            # Desactivar cualquier junta directiva activa existente si la nueva es activa
            if junta_directiva.vigencia:
                sql_disable_current = "UPDATE junta_directiva SET vigencia = FALSE WHERE vigencia = TRUE AND id != %s"
                cursor.execute(sql_disable_current, (junta_directiva.id,))
            
            sql = """UPDATE junta_directiva SET nombre = %s, fecha_inicio = %s, fecha_fin = %s, miembro1 = %s, cargo1 = %s, miembro2 = %s, cargo2 = %s, miembro3 = %s, cargo3 = %s, miembro4 = %s, cargo4 = %s, miembro5 = %s, cargo5 = %s, miembro6 = %s, cargo6 = %s, miembro7 = %s, cargo7 = %s, miembro8 = %s, cargo8 = %s, vigencia = %s
                     WHERE id = %s"""
            cursor.execute(sql, (junta_directiva.nombre, junta_directiva.fecha_inicio, junta_directiva.fecha_fin, junta_directiva.miembro1, junta_directiva.cargo1, junta_directiva.miembro2, junta_directiva.cargo2, junta_directiva.miembro3, junta_directiva.cargo3, junta_directiva.miembro4, junta_directiva.cargo4, junta_directiva.miembro5, junta_directiva.cargo5, junta_directiva.miembro6, junta_directiva.cargo6, junta_directiva.miembro7, junta_directiva.cargo7, junta_directiva.miembro8, junta_directiva.cargo8, junta_directiva.vigencia, junta_directiva.id))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR ACTUALIZAR: VALORES DUPLICADOS CON REGISTROS ANTERIORES")
            return False


    @classmethod
    def delete_junta_directiva(cls, db, id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM junta_directiva WHERE id = %s"
            cursor.execute(sql, (id,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR BORRAR: " + str(ex))
            return False


    @classmethod
    def get_junta_directiva_vigente(cls, db):
        cursor = db.cursor()
        sql = "SELECT * FROM junta_directiva WHERE vigencia = 1 LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        if result:
            return JuntaDirectiva(*result)
        return None