intento = 0
while intento <3:
    pin = input("Ingrese su PIN: ")
    if pin == "1234":
        print("PIN correcto. Acceso concedido.")
        break
    intento += 1
    print(f"PIN incorrecto. Intento {intento} de 3.")
else:
    print("Has agotado tus intentos. Acceso bloqueado.")

input = input("preciona enter para continuar")