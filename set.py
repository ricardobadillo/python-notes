# Los conjuntos no aceptan elementos duplicados.
# Son desordenados.
# Aceptan operaciones lógicas.
# De acceso rápido.

# A set se le puede pasar cualquier estructura de datos iterable.
empty_set = set()  # Conjunto vacío.

conjunto = {1, 2, 3, 4, 5}
subconjunto = {6, 7, 8, 9, 10}
conjunto.add(6)
conjunto.remove(6)
conjunto.update(subconjunto)
conjunto.add(1)  # No se inmuta por ser un elemento ya perteneciente al conjunto.

print("")
print(conjunto)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.

conjunto.discard(10)
print(conjunto)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}.

conjunto1 = {5, 6, 7}
conjunto2 = {8, 9, 0}

print("=" * 20)

print(conjunto1 == conjunto2)  # Output: False. Los conjuntos no son iguales.
conjunto.clear()  # Limpiar todos los elementos del conjunto.

print("=" * 20)

# Operaciones entre conjuntos.

first_set = {"Real Madrid", "Barcelona", "Juventus", "PSG", "Liverpool"}
second_set = {"Manchester United", "Bayern Munich", "Milan", "Barcelona", "PSG"}

union = first_set.union(second_set)
# print(first_set | second_set)

soloA = first_set.difference(second_set)
# print(first_set - second_set)

soloB = second_set.difference(first_set)
# print(second_set - first_set)

interseccion = first_set.intersection(second_set)
# print(first_set & second_set)

diferencia_simetrica = first_set.symmetric_difference(second_set)
# print(first_set ^ second_set)

print(f"Los equipos que aparecen en ambos conjuntos son:\n{union}\n")
print(f"Los equipos que aparecen en el primer conjunto y no en el segundo son:\n{soloA}\n")
print(f"Los equipos que aparecen en el segundo conjunto y no en el primero son: \n{soloB}\n")
print(f"Los equipos que aparecen en ambos conjuntos son: \n{interseccion}\n")

print("=" * 20)

# Eliminar los duplicados.
list_with_duplicates = ["Real Madrid", "Barcelona", "PSG", "Manchester City", "Barcelona"]

print(list_with_duplicates)

set_without_duplicates = set(list_with_duplicates)
list_with_duplicates = list(set_without_duplicates)

print(list_with_duplicates)  # Output: El arreglo inicial sin elementos repetidos.
