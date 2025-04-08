# %%
import streamlit as st
import requests
import pandas as pd

st.title("Busca CEP")
url = "https://viacep.com.br/ws/{cep}/json/"

cep = st.text_input("Busque o seu CEP")
if cep != "":
    try:
        resp = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data, hide_index=True)
    except Exception as err:
        st.error("Entre com um cep válido.")