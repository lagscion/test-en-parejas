from gestion_empanadas import cargar_info, guardar_info
# Función para eliminar una empanada

def eliminar_empanada():
    empanadas = cargar_info()

    nombre = input("Nombre de la empanada a eliminar: ")

    if nombre in empanadas:
        del empanadas[nombre]  # Elimina la empanada del diccionario
        guardar_info(empanadas)  # Guarda el inventario actualizado
        print(f"Empanada '{nombre}' eliminada correctamente.")
    else:
        print("La empanada no existe en el inventario.")
#_______________________________________________________________