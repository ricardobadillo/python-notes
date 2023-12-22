# Las tuplas son inmutables.
# Estructura de datos de solo lectura.
# Son más rápidas que las listas.
# Son útiles para datos constantes.
# Son una estructura de datos de tipo secuencial.

numbers = (1, 2, 3, 4, 5)
books = ("Rayuela", "La resistencia", "Ensayo sobre la ceguera", "Rayuela")

print(books[1])

print(type(numbers))  # Output: "tuple".
print(type(numbers) is tuple)  # Output: True.

print("=" * 20)

# numbers.append(6) ❌
# numbers[0] = 0 ❌

print(numbers.index(3))  # Output: 2. El número 3 está en la posición 2.
print(books.count("Rayuela"))  # Output: 2.

print("=" * 20)

numbers = list(numbers)  # Convertir una tupla en una lista.
print(type(numbers))

print("=" * 20)

for book in books:
    print(book)