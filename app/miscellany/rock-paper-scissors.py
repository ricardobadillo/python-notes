import random

options = ["piedra", "papel", "tijera"]


def rules_game(user_option, computer_option):

    if user_option == computer_option:
        # print("Empate")
        return 0, 0

    elif user_option == "piedra":
        if computer_option == "tijera":
            # print("Has ganado")
            return 1, 0

        elif computer_option == "papel":
            # print("Has perdido")
            return 0, 1

    elif user_option == "papel":
        if computer_option == "piedra":
            # print("Has ganado")
            return 1, 0

        elif computer_option == "tijera":
            # print("Has perdido")
            return 0, 1

    elif user_option == "tijera":
        if computer_option == "papel":
            # print("Has ganado")
            return 1, 0

        elif computer_option == "piedra":
            # print("Has perdido")
            return 0, 1
    return None


def choise_option():
    option = input("Elige una opción: ").lower()

    if option not in options:
        return None

    else:
        return option


def determinate_winner(user_points, computer_points):

    if computer_points == 2:
        return "Has perdido la partida"

    elif user_points == 2:
        return "Has ganado la partida"

    else:
        return None


if __name__ == '__main__':

    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        user_option_result = choise_option()

        if user_option_result is None:
            print("Opción inválida. Inténtelo de nuevo")
        else:
            print(f"\nRound #{rounds}")
            print("=" * 25)
            computer_option_result = random.choice(options)
            print(f"Opción de la máquina: {computer_option_result}. Opción del usuario: {user_option_result}")

            values = rules_game(user_option_result, computer_option_result)

            user_wins = user_wins + values[0]
            computer_wins = computer_wins + values[1]
            print("=" * 20)
            print(f"Usuario: {user_wins} - Computadora: {computer_wins}")
            print("=" * 20)
            rounds += 1

            final = determinate_winner(user_points=user_wins, computer_points=computer_wins)

            if final:
                print(final)
                print("=" * 20)
                break

