# Función para agregar una empanada

def agregar_empanada(info, nombre, stock = None):
    if nombre in info:
        print("Este tipo de empanada ya esta en el inventario.")
        return
    
    info[nombre] = {} if stock is None else 0
    print("herramienta agregada exitosamente.")

#__________________________________________________________________