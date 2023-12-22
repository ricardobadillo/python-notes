# Los números primos menores a 100.
def eratostenes():
    primo = []
    no_primo = []

    for i in range(2, 101):

        if i not in no_primo:
            primo.append(i)

            for j in range(i * i, 101, i):
                no_primo.append(j)

    return primo
