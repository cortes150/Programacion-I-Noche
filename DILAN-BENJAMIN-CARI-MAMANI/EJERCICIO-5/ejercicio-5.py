menores = 0 
adultos = 0 

edad = int(input("Cual es su edad?: "))
while edad > 0:
    
    if edad < 18:
        menores = menores + 1

    elif edad > 18:
        adultos = adultos + 1

    edad = int(input("Cual es su edad?: "))
print(f"la cantidad de menores fue {menores}")
print(f"la cantidad de mayores fue {adultos}")
