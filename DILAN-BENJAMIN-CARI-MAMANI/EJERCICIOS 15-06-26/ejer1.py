n = int(input("Ingrese el valor de n: "))

suma = 0
i = 1

while i <= n:
    suma = suma + (i / (i ** 2))
    i = i + 1

print("La suma es:", suma)