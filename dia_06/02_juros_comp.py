# %%
def j_c(aporte:int, taxa:float, anos:int)->float:
    """
    j_c serve para calcular o retorno financeiro a partir de um aporte. Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para calculo do valor a ser retornado

aporte:
    um número inteiro que represente um valor em R$

taxa:
    um número float entre 0 e 1 que represente o valor da taxa de juros

anos:
    um número inteiro >= 1 que representa o tempo que o inverstimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos

# %%
j_c(anos=4, aporte=1000, taxa=0.13)