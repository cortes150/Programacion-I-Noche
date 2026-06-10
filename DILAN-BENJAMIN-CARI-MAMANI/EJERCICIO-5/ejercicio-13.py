suma = 0
contador = 0

print(" FERIA DE CIENCIAS ")

while True:
    puntaje = float(input("Puntaje del proyecto: "))
    
    if puntaje < 0:
        break
    
    suma = suma + puntaje
    contador = contador + 1

if contador > 0:
    promedio = suma / contador
    print(f"Promedio de puntajes: {promedio}")
else:
    print("No se ingresaron puntajes")