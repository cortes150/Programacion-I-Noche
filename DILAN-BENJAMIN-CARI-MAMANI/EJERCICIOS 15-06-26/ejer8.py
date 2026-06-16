matriz = []

for i in range(2):
    fila = []
    for j in range(2):
        num = int(input(f"Ingrese [{i}][{j}]: "))
        fila.append(num)
    matriz.append(fila)

for i in range(2):
    for j in range(2):
        print(matriz[i][j], end=" ")
    print()