# %%

nome = "Rafael"

for letra in nome:
    print(letra)

# %%
num = 2
max_num = 100

for i in range(1, max_num+1):
    print(num, "x", i, "=", num *i)

# %%
# Quais numeros são divisiveis por 4
# no intervalo [4-100]
for i in range(4, 101):
    if i % 4 == 0:
        print(i)