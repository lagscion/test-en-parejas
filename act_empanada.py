from gestion_empanadas import cargar_info, guardar_info
# Funcion para modificar información de la empanada.
def actualizar_empanada():
    empanadas = cargar_info()

    nombre = input("Nombre de la empanada a actualizar: ")

    if nombre in empanadas:

        ingredientes = input("Nuevos ingredientes (separados por coma): ").split(",")
        disponibilidad = input("Disponible (si/no): ").lower() == "si"
        sabor = input("Nuevo sabor: ")

        empanadas[nombre] = {
            "ingredientes": ingredientes,
            "disponibilidad": disponibilidad,
            "sabor": sabor
        }

        guardar_info(empanadas)
        print("Empanada actualizada correctamente.")

    else:
        print("La empanada no existe en el inventario.")
#_____________________________________________________________________________________________