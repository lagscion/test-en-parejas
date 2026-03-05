import json
# Inventario de las empanadas

def cargar_info(inv_emp = "empanadas.json"):
    try:
        with open(inv_emp, "r")as invn:
            return json.load(invn)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def guardar_info(info, inv_emp = "inventario.json"):
    try:
        with open(inv_emp, "w") as invn:
            json.dump(info, invn)
    except Exception as ex:
        print("Error al guardar el archivo.", ex)
#__________________________________________________________