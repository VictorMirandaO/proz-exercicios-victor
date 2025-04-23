
# var
import random
alvo = random.randint(0, 100)
numero_tentativas = 5

print('''
Seja bem vindo ao jogo de adivinhação!
Seu objetivo é acertar o número de 0 a 100. Boa sorte!

''')


while numero_tentativas > 0:
    try:
        chute = int(input("Por favor, digite um número: "))

        if chute == alvo:
            print("Resposta correta, parabéns você acertou!")
            break
        elif chute > alvo:
            print(f"Que pena, tente um valor mais baixo que {chute}!")
        else:
            print(f"Que pena, tente um valor mais alto que {chute}!")
            
        
        numero_tentativas -=1
        mostrar_tentativas = numero_tentativas
        if numero_tentativas > 0:
            print(f"Restam {numero_tentativas} tentativas.")

        
            

    except ValueError:
        print("Valor digitado invalido! Por favor, digite um número inteiro de 0 a 100.")

if numero_tentativas == 0:
    print(f"Que pena, as suas tentativas acabaram :( O numero era o {alvo}")
