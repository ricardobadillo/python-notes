text = "Hola, soy un texto"

print("")

print("Hola" in text)  # Output: True. "Hola" está en la cadena.

print("=" * 20)

name = "Ricardo"
print(len(name))  # Output: 7.
print(name.upper())  # Output: RICARDO.
print(name.lower())  # Output: ricardo.
print(name.isupper())  # Output: False.
print(name.islower())  # Output: False.

print("=" * 20)

print(f"La letra 'o' aparece {name.count("o")} vez")  # Output: 1. La letra "o" solo aparece una vez.

print(text.replace("Hola", "Chao"))

print("=" * 20)

print(name[len(name) - 1])  # Output: o. Última letra de la palabra.
print(name[-1])  # Output: o. Última letra de la palabra.

print("=" * 20)

print(text[0:4])  # Output: "Hola".
print(text[:4])  # Output: "Hola". (Inicia por defecto en 0).
print(text[6:])  # Output: "soy un texto".
