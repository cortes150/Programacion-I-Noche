n = int(input("Número límite: "))

i = 1
suma = 0

while i <= n:
    print(i)
    suma = suma + i
    i = i + 1

print()
print(f"Suma total: {suma}")