counter = -1

# Los números pares del 0 al 20.

while counter < 25:
    counter += 1

    if counter % 2 == 1:
        continue

    if counter > 20:
        break

    print(counter)

