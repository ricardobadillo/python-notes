# Algunos de los módulos nativos más utilizados en Python.

import math
import random
import re

random_number = random.randint(0, 100)
print(f"El número aleatorio escogido fue: {random_number}")

print("=" * 20)

identity = math.pow(math.sin(random_number), 2) + math.pow(math.cos(random_number), 2)
print(f"Identidad matemática: {int(identity)}")

print("=" * 20)

texto = "Hola. Este es un texto de prueba con el único propósito de quitar los números que aparezcan en este. Tales números no deben estar escritos en letras sino en números, como por ejemplo: 15. Otro ejemplo puede ser 13."

print(re.findall("[0-9]+", texto))
