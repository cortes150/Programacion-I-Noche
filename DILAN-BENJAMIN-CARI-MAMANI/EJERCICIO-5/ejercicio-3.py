print("PUNTAJES DE COMPETENCIA")
print("Ingresa tu puntaje:")

puntajes = []

while True:
    puntaje = int(input("Puntaje obtenido: "))
    
    if puntaje == -1:
        print(f"El puntaje más alto es: {max(puntajes)}")
        break 
    else:
        puntajes.append(puntaje)