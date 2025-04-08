# %%
import requests # Para realizar req na web
import json # Para tratar listas/dicionarios para arquivos json
from tqdm import tqdm
import pandas as pd

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
    "19060100",
    "58038200",
]
url = "https://viacep.com.br/ws/{cep}/json/"
dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i)) # requisição
    if resposta.status_code == 200: # Verifica se foi OK a requisição
        dados.append(resposta.json()) # Adiciona o cep em dados
dados

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %%
print(dados)

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)