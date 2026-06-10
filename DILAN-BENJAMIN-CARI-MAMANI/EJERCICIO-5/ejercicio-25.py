suma = 0
contador = 0
max_nota = -1
min_nota = 11
aprobados = 0
reprobados = 0

while True:
    nombre = input("Nombre del estudiante : ")
    
    if nombre == "fin":
        break
    
    nota = float(input("Nota: "))
    
    suma = suma + nota
    contador = contador + 1
    
    if nota > max_nota:
        max_nota = nota
    
    if nota < min_nota:
        min_nota = nota
    
    if nota >= 6:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

if contador > 0:
    promedio = suma / contador
    print()
    print(" RESULTADOS ")
    print("Promedio general:", promedio)
    print("Nota más alta:", max_nota)
    print("Nota más baja:", min_nota)
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)
else:
    print("No se ingresaron notas")
