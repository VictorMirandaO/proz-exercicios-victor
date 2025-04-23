import math

print("Seja bem-vindo a Calculadora, aqui você pode fazer operações matemáticas básicas")
print("Operações disponíveis: +, -, *, /, **, raiz")

sinal = input("Digite o sinal da operação: ")
if sinal == 'raiz':
    primeiro_numero = int(input("Digite o número da raiz: "))

elif sinal == '**':
    primeiro_numero = int(input('''O primeiro número será base.
        Digite o primeiro número: '''))
else:
    primeiro_numero = int(input("Digite o primeiro número: "))

if sinal == 'raiz':
    print(f"O resultado da raiz é: {math.sqrt(primeiro_numero)}")
    exit( )


if sinal == '**':
    segundo_numero = int(input('''O segundo número será o expoente
    Digite o segundo número: '''))
else:
    segundo_numero = int(input("Digite o segundo número: "))

if sinal not in ['+', '-', '*', '/', '**', 'raiz']:
    print("Operação inválida")
    exit( )




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

def raiz(primeiro_numero, segundo_numero):
    return primeiro_numero ** (1/segundo_numero)

if segundo_numero == 0:
    print(f"Não é possível realizar {sinal} por zero")  
    exit( )

elif primeiro_numero == 0 and segundo_numero < 0:
    print(f"Não é possível realizar {sinal} por zero por um número negativo")
    exit( )

elif primeiro_numero < 0 and segundo_numero < 0:
    print(f"Não é possível realizar {sinal} por dois números negativos")
    exit( )

elif primeiro_numero < 0 and segundo_numero == 0:
    print(f"Não é possível realizar {sinal} por um número negativo e zero")
    exit( )
elif sinal == 'raiz' and segundo_numero == 0:
    print("Não é possível fazer raiz de zero")
    exit( ) 

elif sinal == 'raiz' and primeiro_numero < 0:
    print("Não é possível fazer raiz de um número negativo")
    exit( )
elif sinal == 'raiz' and segundo_numero < 0:
    print("Não é possível fazer raiz por um número negativo")
    exit( )

elif sinal == 'raiz' and primeiro_numero == 0:
    print("Não é possível fazer raiz de zero")
    exit( )



if sinal == '+':
    print(f"O resultado da soma é: {soma(primeiro_numero, segundo_numero)}")
elif sinal == '-':
    print(f"O resultado da subtração é: {subtracao(primeiro_numero, segundo_numero)}")
elif sinal == '*':
    print(f"O resultado da multiplicação é: {multiplicacao(primeiro_numero, segundo_numero)}")
elif sinal == '/':
    print( f"O resultado da divisão é: {divisao(primeiro_numero, segundo_numero)}")
elif sinal == '**':
    print(f"O resultado da potenciação é: {potenciacao(primeiro_numero, segundo_numero)}")

print("Obrigado por usar a calculadora!")
