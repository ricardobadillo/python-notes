# Asignación múltiple.

first_value = input("Ingrese un número: ")
second_value = input("Ingrese otro número: ")

print("=" * 20)

# Asignación múltiple en variables.

first_value, second_value = second_value, first_value

print(f"El primer número es: {first_value}")
print(f"El segundo número es {second_value}")

print("=" * 20)

# Asignación múltiple en listas.

number_list = [5, 10, 15]

a, b, c = number_list

print(f"El valor de a es: {a}")  # 5
print(f"El valor de b es: {b}")  # 10
print(f"El valor de c es: {c}")  # 15

print("=" * 20)

# Asignación múltiple en conjuntos.

fruit_list = {"Durazno", "Manzana", "Pera"}

d, m, p = fruit_list

print(f"El valor de d es: {d}")
print(f"El valor de m es: {m}")
print(f"El valor de p es: {p}")

print("=" * 20)

# Asignación múltiple en tuplas.

book_list = ("Rayuela", "La resistencia")

first_book, second_book = book_list

print(f"El primer libro es: {first_book}")
print(f"El segundo libro es: {second_book}")

print("=" * 20)

# Asignación múltiple en diccionarios.

usuario = {
    "nombre": "Ricardo",
    "apellido": "Badillo"
}

nombre, apellido = usuario.values()

print(f"El nombre de la persona ingresada es: {nombre} {apellido}")

print("=" * 20)

# Asignación múltiple en funciones.


def get_profile():
    name = "Ricardo"
    lastname = "Badillo"
    age = 29

    return name, lastname, age


get_name, get_lastname, get_age = get_profile()

print(f"El nombre obtenido de la función es: {get_name}")
print(f"El apellido obtenido de la función es: {get_lastname}")
print(f"La edad obtenida de la función es: {get_age}")
