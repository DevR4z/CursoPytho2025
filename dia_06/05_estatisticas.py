# %%
def soma(a:float, b:float, *args):
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args):
    return soma(a, b, *args) / (len(args)+2)

a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))
c = float(input("Entre com o terceiro valor: "))
d = float(input("Entre com o quarto valor: "))

print("Média", media(a,b,c,d))