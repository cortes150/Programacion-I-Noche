contador = 0

print(" RESTAURANTE ")

while True:
    plato = input("Plato vendido: ")
    
    if plato == "cerrar":
        break
    
    contador = contador + 1

print(f"Platos registrados: {contador}")