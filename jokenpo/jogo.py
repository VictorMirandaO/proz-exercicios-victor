
import random
opcoes = ["pedra", "papel", "tesoura"]
jogadas = 3
continuar = True


print('''
Seja bem vindo ao Jokenpo!
Tente ganhar do computador.

''')

while continuar:

    jogada_bot = random.choice(opcoes).lower()
    jogada_usuario = input("Escoha sua jogada entre 'pedra', 'papel' ou 'tesoura': ").lower()


    if jogada_usuario not in opcoes:
        print("Entrada invalida, jogo encerrado.")
        continuar = False



    elif jogada_bot == jogada_usuario:
        print(f"Você escolheu {jogada_usuario} e deu empate!")
    elif jogada_bot == "pedra" and jogada_usuario == "papel":
        print(f"Você escolheu {jogada_usuario} e o computador {jogada_bot}. Parabéns, você ganhou!")

    elif jogada_bot == "papel" and jogada_usuario == "tesoura":
        print(f"Você escolheu {jogada_usuario} e o computador {jogada_bot}. Parabéns, você ganhou!")

    elif jogada_bot == "tesoura" and jogada_usuario == "pedra":
        print(f"Você escolheu {jogada_usuario} e o computador {jogada_bot}. Parabéns, você ganhou!")

    else:
        print(f"Você escolheu {jogada_usuario} e o computador {jogada_bot}. Você perdeu, boa sorte na proxima.")
        continuar = input("Deseja continuar? (sim/não): ").lower()
        if continuar == "sim" or continuar == "s":
            continuar = True
        else:
            continuar = False

