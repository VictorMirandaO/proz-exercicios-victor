# jogo de perguntas e respostas
print("em desenvolvimento")

print("Realize o cadastro")
nome = input("Por favor, digite seu nome ou usuario: ")
idade = int(input("Por favor, digite sua idade: "))
print("As dificuldades disponíveis são:")
print("1 - Muito fácil")
print("2 - Fácil")
print("2 - Médio")
print("3 - Difícil")
print("4 - Muito difícil")
print("5 - Insano")
print("6 - Impossível")
print(" ")

dificuldade = input("Por favor, digite a dificuldade do jogo (apenas o número): ")
print(" ")
print("Por favor, escolha a categoria do jogo:")
print("Atente-se a categoria escolhida, pois as perguntas serão baseadas na mesma.")

categoria = input("Por favor, digite a categoria do jogo (te): ")
print(" ")

print(f"Olá {nome}, seja bem vindo ao jogo de perguntas e respostas!")
print(f"Confira se suas informações estão corretas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Dificuldade: {dificuldade}")
print(" ")

print("Suas informações estão corretas?")
print("1 - Sim")
print("2 - Não")
opcao = int(input("Digite o número correspondente a sua resposta: "))

if opcao == 1:
    print("Ótimo! Vamos começar.")
    print(" ")
elif opcao == 2:
    print("Por favor, corrija suas informações.")
    print(" ")
    nome = input("Por favor, digite seu nome ou usuario: ")
    idade = int(input("Por favor, digite sua idade: "))
    dificuldade = input("Por favor, digite a dificuldade do jogo (facil, medio, dificil): ")
    print(" ")
    print(f"Olá {nome}, seja bem vindo ao jogo de perguntas e respostas!")

print(" ")

print("Vamos começar!")
print("As perguntas serão em base a sua idade e a dificuldade escolhida.")
print(" ")
print("Regras:")
print("1 - Responda as perguntas corretamente.")
print("2 - Cada pergunta correta vale 1 ponto.")
print("3 - O jogo possui 10 perguntas.")
print("4 - Boa sorte!")
print(" ")

print("Perguntas:")

if dificuldade == "facil":
    perguntas = {
        "Quem é o presidente do Brasil?": "jair bolsonaro",
        "Qual é a capital do Brasil?": "brasilia",
        "Qual é a capital de São Paulo?": "sao paulo",
        "Qual é a capital do Rio de Janeiro?": "rio de janeiro",
        "Qual é a capital de Minas Gerais?": "belo horizonte",
    }
elif dificuldade == "medio":
    perguntas = {
        "Quem é o presidente do Brasil?": "jair bolsonaro",
        "Qual é a capital do Brasil?": "brasilia",
        "Qual é a capital de São Paulo?": "sao paulo",
        "Qual é a capital do Rio de Janeiro?": "rio de janeiro",
        "Qual é a capital de Minas Gerais?": "belo horizonte",
        "Qual é a capital do Ceará?": "fortaleza",
        "Qual é a capital do Pará?": "belem",
        "Qual é a capital do Paraná?": "curitiba",
    }
elif dificuldade == "dificil":
    perguntas = {
        "Quem é o presidente do Brasil?": "jair bolsonaro",
        "Qual é a capital do Brasil?": "brasilia",
        "Qual é a capital de São Paulo?": "sao paulo",
        "Qual é a capital do Rio de Janeiro?": "rio de janeiro",
        "Qual é a capital de Minas Gerais?": "belo horizonte",
        "Qual é a capital do Ceará?": "fortaleza",
        "Qual é a capital do Pará?": "belem",
        "Qual é a capital do Paraná?": "curitiba",
        "Qual é a capital do Amazonas?": "manaus",
        "Qual é a capital do Acre?": "rio branco",
    }

pontos = 0

for pergunta, resposta in perguntas.items():
    print(pergunta)
    resposta_usuario = input("Digite sua resposta: ").lower()
    if resposta_usuario == resposta:
        print("Resposta correta!")
        pontos += 1
    else:
        print(f"Resposta incorreta! A resposta correta é {resposta}.")
        
print(" ")
print(f"Você acertou {pontos} perguntas.")
if pontos == 10:
    print("Parabéns, você acertou todas as perguntas!")
else:
    print("Que pena, tente novamente.")

print(" ")

print("Obrigado por jogar!")
print("Fim do jogo.")
print(" ")
print("Desenvolvido por: Victor Miranda")
