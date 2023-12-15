edad = int(input("\nIngresa tu edad: "))

# Si se ejecuta la excepción, el programa se detiene.
try:
    if edad < 18:
        raise Exception("No se permiten menores de edad.")
except Exception as error:
    print(f"Ha ocurrido un error el cual está descrito por: {error}")
else:
    print("Pase adelante.")
print("Bloque que se ejecuta indiferentemente que ocurra. 😊")
