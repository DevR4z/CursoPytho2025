
texto = """Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)
valor_item = 0

if opcao == "1":
    valor_item = 1.50
elif opcao == "2":
    valor_item = 2.50


if valor_item == 0:
    print("Entre com a opção correta (1 ou 2), por favor.")

# Passo 2 - Quantas garrafas

else:
    texto2 = "Quantas garrafas você deseja? "
    quantidade = int(input(texto2))

    conta = valor_item * quantidade

    if conta > 0:
        print("Sua conta deu: R$",conta)
    else:print("Que pena, volte sempre!")