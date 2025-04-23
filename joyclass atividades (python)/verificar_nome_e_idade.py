print("Seja bem-vindo ao verificador de nome e idade.")

while True:
    nome = input("Digite seu nome: ").strip()
    if nome.replace(" ", "").isalpha():
        break
    print("Por favor, digite um nome válido.")

ano_atual = 2025

while True:
    nascimento = input("Digite o ano do seu nascimento: ")
    if nascimento.isnumeric():
        nascimento = int(nascimento)
        if 1922 <= nascimento <= ano_atual:
            break
    print("Por favor, digite um ano de nascimento válido.")

idade = ano_atual - nascimento
print(f"Olá, {nome}! Você tem {idade} anos.")