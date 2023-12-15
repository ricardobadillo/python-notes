import entry_point_main

print(f"La variable __name__ del archivo entry_point_main está configurada como: {__name__}")

# Caso en el que este archivo es ejecutado desde la terminal.
if __name__ == "__main__":
    print("Archivo #2 ejecutado como archivo principal.")

else:
    print("Archivo #2 ha sido importado")

