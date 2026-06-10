suma = 0
contador = 0

print("Promediador de Produccion")

litros = int(input("Ingrese cantidad de litros vendidos hoy: "))
while litros != 0:

    suma = suma + litros
    contador = contador + 1
    litros = int(input("Ingrese cantidad de litros vendidos hoy: "))

print(F"El promedio de ventas en estos {contador} dias es de {suma/contador}")
