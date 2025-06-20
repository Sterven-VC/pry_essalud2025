from .entities.Actividad import Actividad
from flask import flash

class ModelActividad:

    @classmethod
    def register_actividad(cls, db, actividad):
        try:
            cursor = db.cursor()
            sql = """ """
        