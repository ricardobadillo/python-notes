# Pares de llave / valor.
# Arreglos asociativos (hash maps).
# Son demasiado rápidos para búsquedas.

empty = {}  # Diccionario vacío.

print("")

print(type(empty))  # Output: Retorna el tipo de estructura de datos: 'dict'.
print(type(empty) is dict)  # Output: True.

print("=" * 20)

diccionario = {
    "nombre": "Ricardo",
    "apellido": "Badillo",
    "edad": 29
}

print("" * 20)

print(diccionario)
print(diccionario.get("nombre"))  # Output: "Ricardo".
print(diccionario.get("salario"))  # Output: None. No existe la propiedad "salario".
print("nombre" in diccionario)  # Output: True.

print("=" * 20)

diccionario["edad"] = 30  # Editar una propiedad.
diccionario["salario"] = 1000  # Crear nueva propiedad.
print(diccionario)

print("=" * 20)

diccionario.pop("salario")  # Eliminar una propiedad.
# del diccionario["salario"] # Eliminar una propiedad.
print(list(diccionario.keys()))  # Imprimir las llaves del diccionario.
print(list(diccionario.values()))  # Imprimir los valores del diccionario.

print("=" * 20)

for key, value in diccionario.items():
    print(f"{key}: {value}")

print("=" * 20)

print(diccionario.clear())  # Limpiar el diccionario.

