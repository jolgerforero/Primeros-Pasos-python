def mostrar_menu():
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")

def procesar_opcion(letra):
    letra = letra.upper() 

    if letra == 'A':
        print("\n--> Procesando: Actualizando Sistema...")
    elif letra == 'E':
        print("\n--> Procesando: Eliminando Catálogo...")
    elif letra == 'C':
        print("\n--> Procesando: Creando Productos...")
    elif letra == 'S':
        print("\n--> Finalizó con éxito.")
        return True  
    else:
        print("\nSigue dentro del proceso del DO WHILE. Opción no válida. Intente de nuevo.")

    return False

def main():
    salir = False
    
    while True:
        mostrar_menu()
        
        try:
            letra = str(input("Ingrese su opción: "))
        except EOFError:
            print("\nError de lectura de entrada. Saliendo...")
            break
        
        salir = procesar_opcion(letra)
        
        if salir:
            break
            
    print("EL DO-WHILE ha finalizado.")

if __name__ == "__main__":
    main()
