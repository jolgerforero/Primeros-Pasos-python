def es_positivo(numero):
    return numero > 0

def es_negativo(numero):
    return numero < 0

def es_cero_neutro(numero):
    return numero == 0

def identificar_signo():
    try:
        entrada = input("Por favor, introduce un número: ")
        numero = float(entrada)

        if es_positivo(numero):
            print(f"El número {numero} es POSITIVO.")
        elif es_negativo(numero):
            print(f"El número {numero} es NEGATIVO.")
        elif es_cero_neutro(numero):
            print(f"El número {numero} es NEUTRO (Cero).")
        
    except ValueError:
        print("Introduce un número real, porfavor.")

if __name__ == "__main__":
    identificar_signo()
