fiebre = 0

print(" HOSPITAL ")

while True:
    temperatura = float(input("Temperatura del paciente: "))
    
    if temperatura == 0:
        break
    
    if temperatura > 37.5:
        fiebre = fiebre + 1

print(f"Pacientes con fiebre: {fiebre}")