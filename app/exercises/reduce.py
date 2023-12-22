import functools

numbers = [1, 2, 3, 4, 5]

result = functools.reduce(lambda counter, item: counter + item, numbers)
print(f"El resultado de sumar todos los números del arreglo es: {result}")
print("=" * 20)

words = ["www", "google", "com"]
link_page = functools.reduce(lambda accumulator_word, word: f"{accumulator_word}.{word}", words)
print(link_page)
