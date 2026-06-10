tiempos = []

print("Registrador de tiempos")
tiempo = int(input("Ingrese su tiempo: "))

while tiempo != 0:
    tiempos.append(tiempo)
    tiempo = int(input("Ingrese su tiempo: "))
print(f"El menor tiempo fue {min(tiempos)} seg")