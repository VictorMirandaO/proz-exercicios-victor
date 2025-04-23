# utilizando o for
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)

# while agora
andar = 20
while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1
