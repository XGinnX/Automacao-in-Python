# Criando desafio de automação em Python

# Site Mockup -> https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Step 1: Acessar o site da empresa
import pyautogui as pya
import pandas as pd
import numpy as np
import openpyxl as op
import time

pya.PAUSE = 0.5

# pya.click -> clicar em algum lugar da tela
# pya.write -> escrever algum texto
# pya.press -> pressionar 1 tecla do teclado
# pya.hotkey("ctrl","v") -> Combinas teclas

url="https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir Navegador 
pya.press("win")
pya.write("chrome")
pya.press("enter")

# Acessar o Navegador
pya.press("tab")
pya.press("enter")

# Acessa o site
pya.write(url)
pya.press("enter")

time.sleep(3) # Recurso dá uma pausa maior - 3 segundos

# Step 2: Fazer o Login
pya.click(x=714, y=465)
pya.write("email.teste@gmail.com")
pya.press("tab")
pya.write("testeSenha")

# Por meio do TAB
pya.press("tab")
pya.press("enter")
time.sleep(5)

#Utilizando o click
#pya.click(x=952, y=680)
#time.sleep(5) # Tempo de Transição de tela

# Step 3: Importar a base de dados 
tabela = pd.read_csv("produtos.csv")

print(tabela)
# Step 4: Cadastrar 1 Produto
for linha in tabela.index:
  # clicar no campo de código
    pya.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pya.write(str(codigo))
    # passar para o proximo campo
    pya.press("tab")
    # preencher o campo
    pya.write(str(tabela.loc[linha, "marca"]))
    pya.press("tab")
    pya.write(str(tabela.loc[linha, "tipo"]))
    pya.press("tab")
    pya.write(str(tabela.loc[linha, "categoria"]))
    pya.press("tab")
    pya.write(str(tabela.loc[linha, "preco_unitario"]))
    pya.press("tab")
    pya.write(str(tabela.loc[linha, "custo"]))
    pya.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pya.write(str(tabela.loc[linha, "obs"]))
    pya.press("tab")
    pya.press("enter") # cadastra o produto (botao enviar)
    
    pya.scroll(5000)

# Step 5: Repetir o Processo de Cadastro até acabar