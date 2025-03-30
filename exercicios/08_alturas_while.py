soma = 0
count = 4

while count > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    count -= 1

print("Soma das alturas:",round(soma,2))