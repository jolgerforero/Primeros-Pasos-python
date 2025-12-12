
def pedir_numero():
    while True:
        try:
            numero = int(input("Digite un número (0 para finalizar): "))
            return numero
        except ValueError:
            print("Entrada incorrecta. Ingrese un valor numérico, Por favor. ")

def Corroborar_paridad(num):

    if num % 2 == 0:
        print(f"El número {num} es PAR.")
    else:
        print(f"El número {num} es IMPAR.")

def main():
    num = 1

    while num != 0:
        num = pedir_numero()
        
        if num != 0:
            Corroborar_paridad(num)
        
    print("\nFinalizó el programa.")

if __name__ == "__main__":
    main()
