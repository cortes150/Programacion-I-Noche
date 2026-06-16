n = int(input("Ingrese la cantidad de términos: "))

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)