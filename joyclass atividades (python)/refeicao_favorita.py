almoco_favorito = "lasanha"
almoco_preco = 20.00

bebida_favorita = "cocacola"
bebida_preco = 5.00


total = almoco_preco + bebida_preco
print(f"O total da refeição é de R${total:.2f}.")

sobremesa_favorita = "pudim"
sobremesa_preco = 10.00

convidados = 5

novo_total = (almoco_preco * 5) + (bebida_preco * 3) + (sobremesa_preco * 2)
print(f"O total da refeição para 5 pessoas é de R${novo_total:.2f}.")


valor_por_pessoa = novo_total / convidados
print(f"Cada convidado deve pagar R${valor_por_pessoa:.2f}.")

orcamento = 18
bom_amigo = True

if(orcamento >= valor_por_pessoa):
    print("O valor está dentro do orçamento.")
elif(bom_amigo == True):
    print("Tenho um amigo que pode me ajudar.")
else:
    print("Pedir ajuda a outro amigo.")