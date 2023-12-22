print("")

# Números impares del 1 al 10.
for numero in range(1, 10, 2):
    print(numero)

print("=" * 20)

colores = [
    {"spanish": "azul", "english": "blue"},
    {"spanish": "verde", "english": "green"},
    {"spanish": "rojo", "english": "red"},
    {"spanish": "amarillo", "english": "yellow"},
    {"spanish": "negro", "english": "black"}
]

for color in colores:
    print(color["spanish"])

# For anidados.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("=" * 20)

for fila in matriz:
    print(fila)

    for celda in fila:
        print(celda)
