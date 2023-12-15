print(f"La variable __name__ está configurada como: {__name__}")

# Caso en el que este archivo es ejecutado desde la terminal.
if __name__ == "__main__":
    print("Ejecutado como archivo principal.")

else:
    print("Ejemplo importado.")

