contador = 0

print(" BIBLIOTECA ")

while True:
    paginas = int(input("Páginas del libro: "))
    
    if paginas == 0:
        break
    
    if paginas > 300:
        contador = contador + 1

print("Libros con más de 300 páginas:", contador)