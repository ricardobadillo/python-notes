from exercises.eratostenes import eratostenes
from random import choice

print("")

# Ejemplo: Mi propio Array: Array de números primos.

prime_numbers = eratostenes()


class PrimeArray:
    def __init__(self, capacity, fill_value=None):
        self.items = list()

        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __automatic_fill__(self):
        for i in range(len(self.items)):
            self.items[i] = choice(prime_numbers)

        return self.items


array_prime = PrimeArray(3)
print(array_prime.__automatic_fill__())