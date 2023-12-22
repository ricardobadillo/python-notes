print("\nList comprehension:\n")

numbers = [element for element in range(1, 11)]
print(numbers)

print("=" * 20)

even_numbers = [element for element in range(1, 11) if element % 2 == 0]
print(even_numbers)

print("=" * 20)

odd_numbers = [element for element in range(1, 11) if element % 2 == 1]
print(odd_numbers)

print("\nDictionary comprehension:\n")

number_dictionary = {element: element * 5 for element in range(1, 11)}
print(number_dictionary)

print("=" * 20)

properties = ["nombre", "apellido", "edad"]
values = ["Ricardo", "Badillo", 30]

my_data = {properties[element]: values[element] for element in range(0, 3)}
print(my_data)

print("=" * 20)

merge_array = zip(properties, values)
print(list(merge_array))  # Output: [('nombre', 'Ricardo'), ('apellido', 'Badillo'), ('edad', 30)].

data_dictionary = {p: v for (p, v) in zip(properties, values)}
print(data_dictionary)  # Output: {'nombre': 'Ricardo', 'apellido': 'Badillo', 'edad': 30}.

print("=" * 20)

# Método inexacto utilizado solo para practicar.

names = ["Ricardo", "Carlos", "Vicente", "Carla", "Andreína", "María", "Carlos", "David", "Ricardo"]

mens_names = {element: names[element] for element in range(0, len(names)) if names[element][-1] != "a"}
print(mens_names)
