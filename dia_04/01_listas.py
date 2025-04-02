# %%
# Uma maneira de definir listas
idades = [28,42,43,35,39,28,38]

print(idades)

# %%

teo = ["Téo", "Calvo", 32, 1, "Casado", 2342.98]
print(teo)

# %%

type(teo)

# %%
# idade
print(teo[2])

# %%

print("Soma idades:", sum(idades))

print("Qtde idades:", len(idades))

print("Média idades:", round(sum(idades)/ len(idades), 1))

print("Menor idade:", min(idades))

print("Maior idade:", max(idades))

# %%

teo = ["Téo Calvo", 
       32,
       True,
       "Casado",
       ["estagiario", "ds jr", "ds pl", "ds sr", "head"],
       [1500, 4000, 4550, 6500, 10000],
       ["Ana", "Maria", "Claudia"]]

print("Tamanho de téo:", len(teo))

# %%

teo[-1][-1]

# %%

# Primeiros 4 elementos
teo[0:4]

# %%

teo[4][3:5]

# %%

teo[4][-2:]

# %%

teo[:4]

# teo [ start : stop ]

# %%

salarios = teo[5]
salarios[::2]

# teo [ start : stop : step ]
