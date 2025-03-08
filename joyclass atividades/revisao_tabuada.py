print("Seja bem-vindo a tabuada.")
numero = int(input("Digite um número para ver a tabuada: "))
print(" ")
print("Usando o for:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# utilizando a função

def tabuada(numero):
    for i in range(1, 11):
        res = str(numero) + " x " + str(i) + " = " + str(numero * i)

        print(res)

print(" ")
print("Usando a função:")
tabuada(numero)

# utilizando o while

print(" ")
print("Usando o while na funçao:")
def tabuada_while(numero):
    i = 1
    while i <= 10:
        res = str(numero) + " x " + str(i) + " = " + str(numero * i)
        print(res)
        i += 1

tabuada_while(numero)

# utilizando o while fora da função

print(" ")

print("Usando o while fora da função:")
i = 1
while i <= 10:
    res = str(numero) + " x " + str(i) + " = " + str(numero * i)
    print(res)
    i += 1
