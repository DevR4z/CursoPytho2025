# %%
def soma(i:float, j:float):
    return i + j

def media(i:float, j:float):
    return soma(i,j) / 2

i = float(input("Entre com o primeiro valor: "))
j = float(input("Entre com o valor de "))

print("Média", media(i,j))