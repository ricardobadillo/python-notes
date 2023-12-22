def sumar(number):
    return number + 5


def suma_acumulada(number):
    return sumar(number) + number


print(suma_acumulada(5))

print("=" * 20)

# Map

numbers = [1, 2, 3, 4, 5]

duplicate_numbers = list(map(lambda num: num * 2, numbers))
print(duplicate_numbers)

print("=" * 20)

animal = ["Perro", "Gato", "Loro", "Pájaro", "Tigre"]

animals = list(map(lambda a: a + "s", animal))
print(animals)

# Map con dos arreglos.

zeros = [0, 0, 0, 0, 0]
identity = [1, 1, 1, 1, 1]

identity_array = list(map(lambda x, y: x + y, zeros, identity))
print(identity_array)

