
frases = {}


while True:
    frase = input("Entre com a frase: ")
    if frase == "":
        break

    if frase not in frases:
            frases[frase] = 1
    else:
         frases[frase] += 1

items = list(frases.items())
items.sort(key=lambda x: x[-1], reverse=True) #True or None

for i, j in items:
     print(i, "->", j)