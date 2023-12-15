# Es la estructura de datos más utilizada.
# Tienen tamaño dinámico.
# Ordenado y de tipo secuencial.

print("")

number_list = [1, 2, 3, 4, 5]
dos_dos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(number_list[2:3])  # Output: El sub-arreglo [3].
print(dos_dos[2:8:2])  # Output: Elige de dos en dos los números del intervalo [3, 8). [3, 5, 7].

print("=" * 20)

number_list.append(-1)
print(number_list)  # Output: Nuevo arreglo: [1, 2, 3, 4, 5, -1].

print("=" * 20)

number_list.insert(0, 0)  # Coloca el 0 en la posición 0.
number_list.extend([6, 7, 8, 9, 10])

print(number_list)
number_list.sort()
print(number_list)  # Output: [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Ordena la lista.

number_list.remove(-1)
print(number_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("=" * 20)

day_list = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print(day_list)
print("Martes" in day_list)  # Output: True. Martes sí está en el arreglo de días.
print(day_list.index("Jueves"))  # Output: 3. Jueves está ocupando la posición 3 del arreglo.
print(day_list.count("Jueves"))  # Output: 1. El día jueves solo aparece una vez.
