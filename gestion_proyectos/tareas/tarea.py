class Tarea:
    def __init__(self, nombre, descripcion,fecha_inicio, fecha_limite, id_proyecto):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_limite = fecha_limite
        self.id_proyecto = id_proyecto
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nDescripción: {self.descripcion}\nFecha límite: {self.fecha_limite}, Proyecto: {self.id_proyecto}"