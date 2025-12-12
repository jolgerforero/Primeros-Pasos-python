def pedir_numeros():
    while True:
        try:
            cantidad = int(input("Digite la cantidad de números para sumar: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Digitela nuevamente.")
                continue
            return cantidad
        except ValueError:
            print("Entrada incorrecta. Ingrese un número entero positivo valido, Por favor.")

def solicitar_datos_suma(suma, indice):
    while True:
        try:
            prompt = f"Digite el Número {indice}: "
            numero = int(input(prompt))
            
            return suma + numero
        except ValueError:
            print("Entrada incorrecta. Por favor, ingrese un número valido.")

def main():

    cantidad_a_sumar = pedir_numeros()
    suma = 0
    
    if cantidad_a_sumar > 0:
        for i in range(cantidad_a_sumar):
            suma = solicitar_datos_suma(suma, i + 1)
        
        print(f"\nEl acumulado total es: {suma}")
    else:
        print("\nNo se ingresaron números para sumar. El resultado es 0.")

if __name__ == "__main__":
    main()
