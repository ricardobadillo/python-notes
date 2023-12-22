try:
    division = 0 / 0
    print(division)
except ZeroDivisionError as error:
    print(f"Ha ocurrido un error el cual está descrito por: {error}.")
else:
    print("Bloque que se ejecuta si no hay error")
finally:
    print("Bloque que se ejecuta indiferentemente que ocurra. 😊")
    print("=" * 20)

try:
    assert 1 == 1, "Condición falsa"
except AssertionError as error:
    print(f"Ha ocurrido un error el cual está descrito por: {error}.")
else:
    print("Bloque que se ejecuta si no hay error")
finally:
    print("Bloque que se ejecuta indiferentemente que ocurra. 😊")
    print("=" * 20)

