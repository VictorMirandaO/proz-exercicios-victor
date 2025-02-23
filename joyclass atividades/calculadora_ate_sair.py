import math

def soma(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtracao(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def multiplicacao(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def divisao(primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero

def potenciacao(primeiro_numero, segundo_numero):
    return primeiro_numero ** segundo_numero

def raiz(primeiro_numero):
    return math.sqrt(primeiro_numero)

def solicitar_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, digite um número válido.")

def solicitar_sinal():
    operacoes_validas = ['+', '-', '*', '/', '**', 'raiz']
    while True:
        sinal = input("Digite o sinal da operação: ")
        if sinal in operacoes_validas:
            return sinal
        else:
            print("Por favor, digite um sinal de operação válido (+, -, *, /, **, raiz).")

continuar = True

while continuar:
    print("Seja bem-vindo a Calculadora, aqui você pode fazer operações matemáticas básicas")
    print("Operações disponíveis: +, -, *, /, **, raiz")
    
    sinal = solicitar_sinal()
    
    if sinal == 'raiz':
        primeiro_numero = solicitar_numero("Digite o número para calcular a raiz: ")
        print(f"O resultado da raiz é: {raiz(primeiro_numero)}")
    else:
        primeiro_numero = solicitar_numero("Digite o primeiro número: ")
        
        if sinal == '**':
            segundo_numero = solicitar_numero("Digite o segundo número (expoente): ")
            print(f"O resultado da potenciação é: {potenciacao(primeiro_numero, segundo_numero)}")
        else:
            segundo_numero = solicitar_numero("Digite o segundo número: ")
            
            if sinal == '+':
                print(f"O resultado da soma é: {soma(primeiro_numero, segundo_numero)}")
            elif sinal == '-':
                print(f"O resultado da subtração é: {subtracao(primeiro_numero, segundo_numero)}")
            elif sinal == '*':
                print(f"O resultado da multiplicação é: {multiplicacao(primeiro_numero, segundo_numero)}")
            elif sinal == '/':
                print(f"O resultado da divisão é: {divisao(primeiro_numero, segundo_numero)}")
    
    continuar = input("Deseja continuar? (sim/não): ").lower()
    if continuar != "sim" and continuar != "s":
        continuar = False

print("Obrigado por usar a calculadora!")

