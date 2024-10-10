import pyautogui
import time
import pandas as pd

LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 0.5   

# Passo 1: entrar no sistema da empresa
pyautogui.click(x=113, y=1031)
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=210, y=61)

# Passo 2: fazer login (qlq e-mail e senha).

pyautogui.write(LINK)
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)

# colocando e-mail
pyautogui.click(x=716, y=372)
pyautogui.write("lele@gmail.com")
# colocando senha
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("enter")

# apenas remover a notificação do google de alerta de senha.
time.sleep(1)
pyautogui.click(x=972, y=372)

# Passo 3: Importar a base de dados.
tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto.
# Passo 5: Repetir o processo de cadastro até acabar os produtos.
time.sleep(0.5)
pyautogui.click(x=677, y=256)


for linha in tabela.index:
    #selecionar o primeiro campo a cada loop
    pyautogui.click(x=677, y=256)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #clicar no botão enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


