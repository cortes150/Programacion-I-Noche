palabra_secreta = "java"
intentos = 0
print(" ")
print("JUEGO DE ADIVINA LA PALABRAAA")
print(" ")

intento = input("Adivina la Palabra: ")


while intento != "java":
    intentos += 1
    intento = input("Adivina la Palabra: ")
    
print("CORRRREEEEEEECCTTOOOOOO")
print(F"Te tomo {intentos} intentos lograrlo")