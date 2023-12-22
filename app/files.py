# Para abrir y cerrar un archivo.

file = open("./documents/Texto de prueba.txt", mode="r", encoding="utf-8")
print(file.read())
file.close()

print("=" * 20)

# Para abrir un archivo y cerrarlo de manera automática.
with open("./documents/Texto de prueba.txt", encoding="utf-8") as file:
    for line in file:
        print(line)


# Escribir algún texto en un archivo.
nuevo_archivo = open("./documents/Nuevo archivo.txt", mode="w", encoding="utf-8")
nuevo_archivo.write("Hola, esta es la primera línea del archivo. \n")

