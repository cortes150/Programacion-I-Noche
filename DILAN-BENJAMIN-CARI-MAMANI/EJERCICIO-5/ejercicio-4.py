cafes = 0
print("CAFETERIA")
Compro_Respuesta = input("¿Compró café?: ")
while Compro_Respuesta != "salir":

    if Compro_Respuesta == "si":
        cafes =  cafes + 1

    elif Compro_Respuesta == "no":
        print("No compró café")

    Compro_Respuesta = input("¿Compró café?: ")

print(f"En la jornada se vendió {cafes} cafés")


