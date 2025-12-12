def obtener_mes(numero_mes):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo",
        "Junio", "Julio", "Agosto", "Septiembre",
        "Octubre", "Noviembre", "Diciembre"]
    if 1 <= numero_mes <= 12:
        return meses[numero_mes - 1]
    else:
        return "Entrada incorrecta. Ingresa un numero valido, porfavor."
numero_mes = int(input("Introduce un numero del 1 al 12: "))
print(obtener_mes(numero_mes))