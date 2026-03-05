import json

def listar_empanadas():

    try:
        with open("empanadas.json", "r") as archivo:
            empanadas = json.load(archivo)

        print("\n===== LISTA DE EMPANADAS =====\n")

        for nombre, datos in empanadas.items():

            print("Nombre:", nombre)
            print("Ingredientes:", ", ".join(datos["ingredientes"]))
            print("Disponibilidad:", datos["disponibilidad"])
            print("Sabor:", datos["sabor"])
            print("-" * 30)

    except FileNotFoundError:
        print("No existe el archivo de empanadas.")