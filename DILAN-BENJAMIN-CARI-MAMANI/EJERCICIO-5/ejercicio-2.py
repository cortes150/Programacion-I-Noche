contador = 0

print("CONTADOR DE ESTUDIANTES")
print("Ingresa estudiantes")

while True:

    print(f"\nContador actual: {contador}")
    estudiante = input("Nombre del estudiante:")
    if estudiante == "FIN" or estudiante == "fin":
        print(f"contador final: {contador} estudiantes en total")
        break
    else:
        contador = contador + 1
        print(f"agregado: {estudiante}")

    