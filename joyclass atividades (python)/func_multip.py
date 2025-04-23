print("Revisão de função - multiplicação")

def escrever_multiplicacao (num1, num2):
    multip = num1 * num2
    resultado = str(num1) + " x " + str(num2) + " = " + str(multip)
    return resultado

res = escrever_multiplicacao(2, 3)
print(res)