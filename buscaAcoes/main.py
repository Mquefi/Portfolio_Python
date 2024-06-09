'''
    EXEMPLO

    Rotina pra automatizar a busca de dados de ações em um site financeiro, análise e envio de e-mail pra um determinado destino.


'''
# Bibliotecas
import yfinance
import matplotlib
import pyautogui
import pyperclip
import webbrowser
import time

# Solicitação da Ação e busca da informação no banco de dados do site
ticker = input("Digite o código da ação desejada: ")
dados = yfinance.Ticker(ticker).history(start="2024-01-01", end="2024-06-01")
fechamento = dados.Close


# VARIÁVEIS
valor_max = round(fechamento.max(),2)
valor_min = round(fechamento.min(),2)
valor_medio = round(fechamento.mean(),2)

#utiliza o f antes do texto pra poder incluir entre {} a variável, concatenando
destinatario = "mquefi@gmail.com"
assunto = f"Análise das ações {ticker}"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}

Cotação máxima: R$ {valor_max}
Cotação mínima: R$ {valor_min}
Valor médio: R$ {valor_medio}

Qualquer dúvida, estou a disposição!

Att,

Seu nome, cargo, setor
"""

# Abrir o navegador e e-mail
webbrowser.open("www.gmail.com")
time.sleep(3)

# Clicar em novo e-mail
pyautogui.PAUSE = 3
pyautogui.click(x=-1855, y=214)

# digitar o e-mail do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

#Inserir Assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

#Inserir mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")
fechamento.plot()

#Enviar, após mapeado a localização do botão na tela
pyautogui.click(x=-615, y=1005)

#Fechar a janela de e-mail
pyautogui.click("alt","f4")

#Mensagem de sucesso
print("Email enviado com sucesso")
