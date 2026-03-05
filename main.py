from agregar_empanada import agregar_empanada
from  act_empanada import actualizar_empanada
from listar import listar_empanadas
def mostrar_menu():
    print("\n" + "="*40)
    print("        SISTEMA DE EMPANADAS")
    print("="*40)
    print("1. 🥟 Listar empanadas")
    print("2. ➕ Agregar empanada")
    print("3. ✏️  Editar empanada")
    print("4. ❌ Eliminar empanada")
    print("5. 🚪 Salir")
    print("="*40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_empanadas()
        elif opcion == "2":
            agregar_empanada()
        elif opcion == "3":
            actualizar_empanada()
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")    

if __name__ == "__main__":
    main()