ronda = 1
usuarioGana = 0
pcGana = 0


print("PIEDRA, PAPEL O TIJERA")
print()

while ronda <= 5:
    print("--- RONDA", ronda, "---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    
    usuario = int(input("Elige (1-3): "))
    
    if ronda % 3 == 1:
        pc = 1 
    elif ronda % 3 == 2:
        pc = 2 
    else:
        pc = 3 
    
    if pc == 1:
        print("PC eligió: Piedra")
    elif pc == 2:
        print("PC eligió: Papel")
    else:
        print("PC eligió: Tijera")
    

    if usuario == pc:
        print("Empate")
    elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
        print("Gana Usuario")
        usuarioGana = usuarioGana + 1
    else:
        print("Gana PC")
        pcGana = pcGana + 1
    
    ronda = ronda + 1

print("RESULTADO FINAL")
print(f"Victorias del usuario: {usuarioGana}")
print(f"Victorias de la PC: {pcGana}")

if usuarioGana > pcGana:
    print("Ganaste")
elif pcGana > usuarioGana:
    print("Perdiste")
else:
    print("Empate")