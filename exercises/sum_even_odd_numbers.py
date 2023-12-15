# Suma de los primeros 50 números pares e impares.

numero = 0
sumaPares = 0
sumaImpares = 0
listaPares = list()
listaImpares = list()

while numero <= 100:
    if numero % 2 == 0:
        listaPares.append(numero)
        sumaPares += numero
    elif numero % 2 == 1:
        listaImpares.append(numero)
        sumaImpares += numero
    numero += 1

print(f"La suma de los números pares: {listaPares}",)
print(f"es: {sumaPares}.")
print("")
print(f"La suma de los números impares: {listaImpares}")
print(f"es: {sumaImpares}.")
