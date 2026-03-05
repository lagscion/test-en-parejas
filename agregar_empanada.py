from gestion_empanadas import cargar_info, guardar_info
# Función para agregar una empanada

def agregar_empanada(nombre, ingredientes, disponibilidad, sabor):
    empanadas = cargar_info()

    empanadas[nombre] = {
        "ingredientes": ingredientes,
        "disponibilidad": disponibilidad,
        "sabor": sabor
    }

    guardar_info(empanadas)

#__________________________________________________________________