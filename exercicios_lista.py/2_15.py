# %%

lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

num = int(input("Entre com um número: "))

contador = 0
for i in lista:
    if i == num:
        contador += 1

print("Quantidade de", num,":",contador)
