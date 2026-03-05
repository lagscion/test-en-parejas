import json
# Inventario de las empanadas
def cargar_info(archivo = "empanadas.json"):
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def guardar_info(info, archivo = "empanadas.json"):
    with open(archivo, "w") as f:
        json.dump(info, f, indent=4)
#__________________________________________________________