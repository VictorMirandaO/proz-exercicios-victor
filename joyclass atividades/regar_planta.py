print("Hoje é seguda-feira, e precisamos regar todas as plantas.")
print("Vamos pedir ajuda ao robô.")

plantas_seg = ["tomate", "batata", "cenoura", "tomate", "batata", "cenoura"]

print("")
print(f"As plantas que precisam ser regadas são: {plantas_seg}.")

for i, planta in enumerate(plantas_seg):
    mensagem =  f"Robô, por favor. regue a planta {i+1}, que é de {planta}."
    print(mensagem)

print("Todas as plantas foram regadas.")


# Nessa leva somente temos batatas e tomates. Porém as batatas já foram regadas ontem.
# Então, precisamos regar somente os tomates.
print(" ")
print("Hoje é terça-feira, e precisamos regar todas as plantas.")
print("Vamos pedir ajuda ao robô.")

plantas_ter = ["tomate", "batata", "tomate", "batata", "tomate", "batata"]

print("")
plantas_para_regar = [planta for planta in plantas_ter if planta != "batata"]
print(f'''As plantas que precisam ser regadas são: {plantas_para_regar}.
Pois, batatas já foram regadas ontem.''')



while "batata" in plantas_ter:
    plantas_ter.remove("batata")

for i, planta1 in enumerate(plantas_ter):
    mensagem1 =  f"Robô, por favor. regue a planta {i+1}, que é de {planta1}."
    print(mensagem1)
