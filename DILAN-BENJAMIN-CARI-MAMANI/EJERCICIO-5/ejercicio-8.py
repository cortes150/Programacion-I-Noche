Contador = 0 
cancion = input("registre la cancion: ")
while cancion != "fin":
    Contador += 1
    cancion = input("registre la cancion: ")
print(f"Registraste {Contador} canciones en total")
