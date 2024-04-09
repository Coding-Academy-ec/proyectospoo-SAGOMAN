class Equipo:
    def __init__(self, id, nombre, objetivo, jefe):
        self.id = id
        self.nombre = nombre
        self.objetivo = objetivo
        self.jefe = jefe

    def __str__(self):
        return f" Id: {self.id} , \nEquipo: {self.nombre} , Objetivo: {self.objetivo} , Jefe: {self.jefe}"