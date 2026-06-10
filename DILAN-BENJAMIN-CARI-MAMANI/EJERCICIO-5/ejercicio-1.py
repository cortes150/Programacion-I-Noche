total = 0

print("Sumas de Supermercado")
print("Ingresa montos")

while True:
    print(f"\n Total actual: Bs {total}")
    monto_text = input("Montos a sumar: ")
    
    monto = float(monto_text)
    
    if monto == 0:
        print(f"Total final: Bs {total}")
        break  
    else:
        total = total + monto
        print(f"Agregado: Bs {monto}")