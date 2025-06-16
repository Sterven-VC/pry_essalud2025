# models/ModelNoticia.py

from .entities.Noticia import Noticia
from flask import flash

class ModelNoticia:

    @classmethod
    def register_noticia(cls, db, noticia):
        try:
            cursor = db.cursor()
            sql = """INSERT INTO noticia (titulo, fecha_noticia, ruta_foto, description, information) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (noticia.titulo, noticia.fecha_noticia, noticia.ruta_foto, noticia.description, noticia.information))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR DE REGISTER: " + str(ex))
            return False

    @classmethod
    def get_all_noticias(cls, db):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM noticia"
            cursor.execute(sql)
            results = cursor.fetchall()
            noticias = []
            for row in results:
                noticia = Noticia(row[0], row[1], row[2], row[3], row[4], row[5])
                noticias.append(noticia)
            cursor.close()
            return noticias
        except Exception as ex:
            flash("ERROR DE LISTAR: " + str(ex))
            return []

    @classmethod
    def get_noticia_by_id(cls, db, id):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM noticia WHERE id = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row:
                noticia = Noticia(row[0], row[1], row[2], row[3], row[4], row[5])
                return noticia
            return None
        except Exception as ex:
            flash("ERROR: " + str(ex))
            return None

    @classmethod
    def update_noticia(cls, db, noticia):
        try:
            cursor = db.cursor()
            sql = """UPDATE noticia SET titulo = %s, fecha_noticia = %s, ruta_foto = %s, description = %s, information = %s
                     WHERE id = %s"""
            cursor.execute(sql, (noticia.titulo, noticia.fecha_noticia, noticia.ruta_foto, noticia.description, noticia.information, noticia.id))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR DE ACTUALIZAR: " + str(ex))
            return False

    @classmethod
    def delete_noticia(cls, db, id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM noticia WHERE id = %s"
            cursor.execute(sql, (id,))
            db.commit()
            cursor.close()
            return True
        except Exception as ex:
            flash("ERROR DE ELIMINAR: " + str(ex))
            return False
