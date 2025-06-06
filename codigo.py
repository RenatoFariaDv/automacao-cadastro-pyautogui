import pyautogui
import time

# PYAUTOGUI >> FAZER AUTOMAÇÕES COM PYTHON
# pyautogui.click >> clicar em algum lugar
# pyautogui.press >> apertar uma tecla
# pyautogui.write >> escrever um texto
# time.sleep >> faz a automação esperar o tempo que você determinar

# PASSO 1 ENTRAR NO SITE DA EMPRESA

# ABRIR O CHROME

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)


# DIGITAR O NOME DO SITE

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") 
time.sleep(2)
pyautogui.press('enter')



# PASSO 2 FAZER LOGIN

pyautogui.click(x=605, y=468)
pyautogui.write("renato.py@gmail.com")
pyautogui.press("tab")
pyautogui.write("249836")
pyautogui.press("tab")
pyautogui.press("enter")

# PASSO 3 IMPORTAR A BASE DE DADOS

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# PASSO 4 REPETIR PARA TODOS OS PRODUTOS
     

for linha in tabela.index: 

    pyautogui.click(x=614, y=318)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)


    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)
    





    

    






