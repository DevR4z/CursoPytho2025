# %%
import random

def get_input():
    while True:
        try:
           num_usuario = int(input("Entre com um número: "))
        except ValueError as error:
            print("Valor invalido!")
            continue

        if 1 <= num_usuario <= 15:
            return num_usuario
        
        print("O valor deve ser entre 1 e 15")

def check_numbers(num_sorteio, num_usuario):
    if num_sorteio == num_usuario:
        print("Parabéns!")
        return True
    elif num_usuario > num_sorteio:
        print("Número muito alto. Tente um número menor!")
        return False
    else:
        print("Número muito baixo. Tente um número maior!")
        return False

num_sorteio = random.randint(1,15)

for i in range(3):

    num_usuario = get_input()
    
    if check_numbers(num_sorteio=num_sorteio, num_usuario=num_usuario):
        break

else:
    print("suas tentativas acabaram!")