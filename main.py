# Passo a passo do projeto
# Importando bibliotecas necessarias para o projeto
import pyautogui
import time
import pandas

# Funçoes do pyautogui
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> apertar 1 tecla
    # pyautogui.click -> clicar em algum lugar da tela
    # pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empresa 
# abrir o navegador (chrome)
time.sleep(2)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(5) 
pyautogui.press("enter")
time.sleep(3)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
pyautogui.click(x=688, y=352)
time.sleep(3)
pyautogui.write("renangemi@icloud.com")
time.sleep(3)
pyautogui.press("tab")
time.sleep(3)
pyautogui.write('renan99')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)

# Passo 3: Importar a base de dados 
dados=pandas.read_csv('produtos.csv')

# Passo 4: Cadastrar o produto
for item in dados.index:
    #codigo
    pyautogui.click(x=676, y=257)
    codigo=str(dados.loc[item,'codigo'])
    pyautogui.write(codigo)

    #marca
    pyautogui.press('tab')
    marca=str(dados.loc[item,'marca'])
    pyautogui.write(marca)

    #tipo
    pyautogui.press('tab')
    tipo=str(dados.loc[item,'tipo'])
    pyautogui.write(tipo)

    #categoria
    pyautogui.press('tab')
    categoria=str(dados.loc[item,'categoria'])
    pyautogui.write(categoria)

    #preco_unitario
    pyautogui.press('tab')
    preco=str(dados.loc[item,'preco_unitario'])
    pyautogui.write(preco)

    #custo
    pyautogui.press('tab')
    custo=str(dados.loc[item,'custo'])
    pyautogui.write(custo)

    #obs
    pyautogui.press('tab')
    obs=str(dados.loc[item,'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    #clicar no botao de enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(2000)

# Passo 5: Repetir o processo até terminar a tabela (for)