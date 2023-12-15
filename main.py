from persona import Persona


def print_text(name):
    print(f'Hola, {name}')


if __name__ == '__main__':

    persona = Persona()
    persona.nombre = "Ricardo"
    persona.edad = 29
    # print(vars(persona)) ---> Imprime el objeto creado.
    print_text(f"La persona ingresada se llama: {persona.nombre} y tiene {persona.edad} años.")