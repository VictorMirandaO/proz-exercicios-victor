print("Seja bem-vindo ao verificador de quantidade de pessoas no IBGE.")

#var
contador = 1
qtd_diaria = int(input("Insira a quantidade de pessoas entrevistadas no dia: "))

print(f"A quantidade de pessoas entrevistadas neste dia é de {qtd_diaria} pessoas.")

while contador <= qtd_diaria:
    print("Você entrevistou a pessoa de codigo: 00",contador)
    contador = contador + 1

print("Fim da entrevista.")

