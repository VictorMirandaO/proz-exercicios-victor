# jogo de perguntas e respostas
print("Jogo em desenvolvimento, ainda estou estruturando o codigo")

print("Realize o cadastro;")
while True:
    nome = input("Digite seu nome ou usuario: ").strip()

    nome_formatado = nome.replace(" ", "")

    if nome_formatado.isalnum() and any(c.isalpha() for c in nome_formatado):
        break
    else:
        print("Nome inválido! Deve conter pelo menos uma letra, pode ter números e espaços, mas sem símbolos.")


while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade <= 0 or idade > 100:
            print("Por favor, digite uma idade válida.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número válido.")

print(" ")
print("As dificuldades disponíveis são:")
print('''
1 - Muito fácil
2 - Fácil
2 - Médio
3 - Difícil
4 - Muito difícil
5 - Insano
6 - Impossível''')
print(" ")

dificuldade = int(input("Por favor, digite a dificuldade do jogo (apenas o número): "))
print(" ")
print("As categorias disponíveis são:")
print('''
    1 - Tecnologia  
    3 - Youtubers e Influencers  
    3 - Geografia  
    4 - Matemática  
    5 - Filmes e Séries 
    6 - História  
    7 - Língua Portuguesa  
    8 - Cultura Pop  
    9 - Espaço e Astronomia  
    10 - Personalidades Famosas  
    11 - Transporte e Automóveis  
    12 - Ciências  
    13 - Esportes  
    14 - Curiosidades Gerais  
    15 - Música  
    16 - Jogos  
    17 - Animes e Desenhos''')
print(" ")

categoria = input("Por favor, digite a categoria do jogo (apenas os números): ")
print("Atente-se a categoria escolhida, pois as perguntas serão baseadas na mesma.")

print(" ")
print(" ")
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
