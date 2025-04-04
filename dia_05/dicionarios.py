# %%

lista = [2, 13, "Rafael", ["ds", "de", "da"], True]

lista[2]
      
# %%
# Dicionarios são pares de chave/valor

dados_rafael = {
    "sobrenome":"Abranches",
    "nome":"Rafael",
    "filhos":False,
    "formacao":["estatistica", "bigdata datascience"],
    "cargos":[
        {"nome": "ds jr.", "empresa": "tapps" },
        {"nome": "ds pl.", "empresa": "sas" },
        {"nome": "ds sr.", "empresa": "boticario" },
        {"nome": "ds espec.", "empresa": "via varejo" },
        ]
}

# %%
print(dados_rafael)
print(dados_rafael["formacao"][-1])
print(dados_rafael["cargos"][-1]["empresa"])

# %%
dados_rafael["estado civil"] = "casado"

# %%
print("Chaves:", dados_rafael.keys())
print("Valores:", dados_rafael.values())
print("Items:", dados_rafael.items())

# %%
for i in dados_rafael:
    print(i, "->", dados_rafael[i])

# %%
for items in dados_rafael.items():
    print(items)

# %%
for [chave, valor] in dados_rafael.items():
    print(chave, "->", valor)