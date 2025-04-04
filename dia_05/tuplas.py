# %%

dados_teo = [32, 1, "casado", "dev golang"]
dados_teo

# %%

dados_teo.append("3241.43")
dados_teo

# %%

tupla_teo = (32, 1, "Casado", "dev goLang", ["maria", "antonia"])

print(type(tupla_teo))
print(tupla_teo)

# %% Só consigo mudar a lista na tupla

tupla_teo[-1].append("ana")
print(tupla_teo)