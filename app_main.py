import os 
from gestion_ventas import ingresar_ventas


def limpiar_pantalla():
    """Limpia la pantalla de la consola.
    Compatible con Windows, Unix/Linux y Mac."""
    
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/Mac
        os.system('clear')
        
def menu():
    """Muestra el menú principal y maneja las opciones del usuario."""
    while True:
        limpiar_pantalla()
        print("\n====== Menú principal======")
        print("1. Ingresar ventas")
        print("2. Analizar ventas (requiere archivo CSV)")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_ventas()
        elif opcion == "2":
            pass
        elif opcion == "3":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Por favor, intente nuevamente.")
        input("Presione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de ventas.")
    menu()