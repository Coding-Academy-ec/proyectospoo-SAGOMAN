class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin , id_equipo):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.id_equipo = id_equipo
        
    def __str__(self):
        return f" Id: {self.id_proyecto} , \nProyecto: {self.nombre}\nDescripción: {self.descripcion}\nFecha de inicio: {self.fecha_inicio}\nFecha de fin: {self.fecha_fin} \nEquipo: {self.id_equipo}"