print("Seja bem-vindo ao verificador de nome e idade.")

nome = input("Digite seu nome: ").strip()

if not nome.replace(" ", "").isalpha():
    print("Por favor, digite um nome válido.")
    exit()

nascimento = input("Digite o ano do seu nascimento: ")
ano_atual = 2025

if nascimento.isnumeric():
    nascimento = int(nascimento)
    if 1922 <= nascimento <= ano_atual:
        idade = ano_atual - nascimento
        print(f"Olá, {nome}! Você tem {idade} anos.")
    else:
        print("Por favor, digite um ano de nascimento válido.")
else:
    print("Por favor, digite um ano de nascimento válido.")