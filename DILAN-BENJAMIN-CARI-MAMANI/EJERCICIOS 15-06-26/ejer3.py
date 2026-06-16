n = int(input("Ingrese la cantidad de términos: "))

t = 1
impar = 1

for i in range(n):
    print(t ,end = ",")

    t = t + impar
    impar = impar + 2