import sys

collections = {"Listas": list(), "Tuplas": tuple(), "Diccionarios": dict(), "Conjuntos": set()}

for name, value in collections.items():
    print(f"{name} tienen un peso de: {sys.getsizeof(value)} bytes")

