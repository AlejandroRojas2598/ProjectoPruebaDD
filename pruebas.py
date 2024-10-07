import random

numero_aleatorio = random.randint(1, 100)

print("Número aleatorio:", numero_aleatorio)

x = 0
y = 0
contador_ejes = 0

while x < 5 and y < 5:
    print("Coordenadas")
    print(f"X: {x} - Y: {y}")
    print("Norte 1 - Este 2 - Oeste 3 - Sur 4")
    eleccion = input()
    eleccion = int(eleccion)
    if eleccion == 1:
        y = y + 1
    elif eleccion == 2:
        x = x + 1
    elif eleccion == 3:
        x = x - 1
    elif eleccion == 4:
        y = y - 1
    
    contador_ejes = contador_ejes + 1
    
