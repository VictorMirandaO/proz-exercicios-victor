# verificar número
def mostrar_numero():
    numero_valido = False

    print("Escreva um número menor ou igual a 100.")
    
    while(numero_valido == False):
        try:
            num = int(input("Digite um número: "))

            if num > 100:
                print("O número precisa ser menor ou igual a 100.")

            elif num <= 0:
                print("O número precisa ser maior que 0.")

            else:
                print("Boa! Você digitou o número:", num)
                numero_valido = True
        except:
            print("Digite um número válido. Por favor, apenas inteiros.")

mostrar_numero()