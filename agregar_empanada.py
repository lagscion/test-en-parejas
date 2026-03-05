from gestion_empanadas import cargar_info, guardar_info
# Función para agregar una empanada

def agregar_empanada():
    empanadas = cargar_info()

    nombre = input("Nombre de la empanada: ")
    ingredientes = input("Ingredientes separados por coma: ").split(",")
    disponibilidad = input("Disponible (si/no): ").lower() == "si"
    sabor = input("Sabor: ")

    empanadas[nombre] = {
        "ingredientes": ingredientes,
        "disponibilidad": disponibilidad,
        "sabor": sabor
    }

    guardar_info(empanadas)

#__________________________________________________________________