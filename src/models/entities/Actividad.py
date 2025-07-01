class Actividad:
    def __init__(self, id, nombre, servicio_id, departamento_id, hora_inicio=None, hora_fin=None):
        self.id = id
        self.nombre = nombre
        self.servicio_id = servicio_id
        self.departamento_id = departamento_id
        self.hora_inicio = hora_inicio  # Nuevo campo hora_inicio
        self.hora_fin = hora_fin  # Nuevo campo hora_fin
