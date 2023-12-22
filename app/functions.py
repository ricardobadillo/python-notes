# Suma de los números considerando un número inicial y uno final.
def sum_first_final(first, final):
    suma = 0

    for i in range(first, final + 1):
        suma += i

    return suma


print(sum_first_final(3, 5))


# Suma de tres números.
def sum_tern(a=3, b=5, c=7):
    return a + b + c


print(sum_tern(10, 10, 10))
# print(sum_tern(b=10))


