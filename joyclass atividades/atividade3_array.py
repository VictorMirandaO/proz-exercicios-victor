lista_produtos = ["máscaras faciais", "batons", "esmaltes", "perfumes", "loções", "xampus", "sabonetes", "deliniadores"]

lista_produtos[1] = "rímel"
lista_produtos[4] = "cremes hidratantes"
lista_produtos.pop()

lista_produtos.append("protetor solar")
lista_produtos.append("óleo mixelar")

print("Nova lista de produtos:")
for produto in lista_produtos:
    print(produto)