# %%
def par_impar(numero:int):
    if numero % 2 == 0:
        print("É par!")
    else:
        print("É impar!")

numero = int(input("Entre com um número: "))

par_impar(numero)