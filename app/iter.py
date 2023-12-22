from functools import partial
from random import randint

vowels = ["a", "e", "i", "o", "u"]

vowels_iter = iter(vowels)

print(next(vowels_iter))  # Output: "a".
print(next(vowels_iter))  # Output: "e".

# Ejemplo: Juego de la ruleta rusa.

pull_trigger = partial(randint, 1, 6)

print("=" * 20)
print("Empieza el juego de la ruleta rusa")
print("=" * 20)

# El ciclo funciona hasta que el número aleatorio sea 6.
for i in iter(pull_trigger, 6):
    print(f"Sigues vivo. Ha sido seleccionado el {i}")

print("Has muerto. Juego terminado.")
