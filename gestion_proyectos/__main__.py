from gestion_proyectos.equipos.equipo import Equipo
from gestion_proyectos.proyectos.proyecto import Proyecto
from gestion_proyectos.tareas.tarea import Tarea

def main():
    # Creacion de equipos
    # id, nombre, objetivo, jefe
    equipo1 = Equipo("EQ_1", "EQUIPO1", "Analistas ciencia de datos","Isaac Sarango")
    equipo2 = Equipo("EQ_2", "EQUIPO2", "Desarrolladores Web","Antonio Salazar")
    
    # Creacion de proyectos
    # id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin , id_equipo
    proyecto1 = Proyecto("PROY_1", "PROYECTO1", "Proyecto encargado a la realizacion de dashboards estadisticos","2023-01-01", "2024-03-30","EQ_1" ) 
    proyecto2 = Proyecto("PROY_2", "PROYECTO2", "Proyecto en hacer pagina web con contenidos dinamicos","2023-01-01", "2024-03-30","EQ_2" ) 

    # crear tareas
    # nombre, descripcion, fecha_limite, id_proyecto
    tarea1 = Tarea("TAR1","Proceso ETL", "2023-01-10","2024-04-08","PROY_1")
    tarea2 = Tarea("TAR2","Creacion de entorno django", "2023-01-10","2024-04-08","PROY_2")

    # Mostrar detalles de las transacciones
    print("\n****************************************")
    
    print("Proyectos del Equipo 1:")
    print("\n****************EQUIPO1***********************")
    print(equipo1)
    print("\n****************PROYECTO1***********************")
    print(proyecto1)
    print("\n****************TAREA1***********************")
    print("Tarea:", tarea1)

    print("\n****************************************")

    print("\nProyectos del Equipo 2:")
    print("\n****************EQUIPO2***********************")
    print(equipo2)
    print("\n****************PROYECTO2***********************")
    print(proyecto2)
    print("\n****************TAREA2***********************")
    print("Tarea:", tarea2)

if __name__ == "__main__":
    main()