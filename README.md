# Portfolio_Python
Compilation of materials that exemplifies beliefs, skills, qualifications, education, training, and experiences.

# Comandos Básicos


### Bibliotecas úteis ###

    ## yfinance
        pip install yfinance
        Biblioteca do Python que permite a extração de dados financeiros de várias fontes, como Yahoo Finance, de forma rápida e fácil. Com o yfinance, é possível obter informações atualizadas sobre ações, índices, moedas e muito mais, facilitando a análise e tomada de decisão no mercado financeiro.
        
        import yfinance as yf

        Definindo o ticker da ação desejada
            ticker = "AAPL"

            # Obtendo os dados da ação
            data = yf.download(ticker)

            # Exibindo as informações obtidas
            print(data)

        Cálculo de Indicadores
            # Definindo o ticker da ação desejada
            ticker = "AAPL"

            # Obtendo os dados da ação
            data = yf.download(ticker)

            # Calculando a média móvel de 50 dias
            data["MA50"] = data["Close"].rolling(window=50).mean()

            # Exibindo as informações obtidas
            print(data)

        pip install pyautogui

    ## matplotlib

        pip install matplotlib
        Criar gráficos
        import matplotlib as mpl

    ## pyautogui
        pip install pyautogui
            Manipular comandos do teclado e posição do mouse

    ## pyperclip
        Copiar mensagem sem erros de formatação
        puperclip.copy(variavel)

    ## streanlit
        !pip install streamlit
        Biblioteca de dados pra criar aplicativos Web interativos e atualizáveis em tempo real
        https://streamlit.io/

        import streamlit as st

    ## mymodel
        !pip install mymodel
        Gráficos e controle de gráficos

        import mymodel as m

    ## pandas
        !pip install pandas
        A biblioteca do Pandas é uma poderosa ferramenta que permite a manipulação eficiente de bases de dados, incluindo tratamento, limpeza e análise estatística dos mesmos. Além disso, o Pandas possibilita consultas em bancos de dados, visualizações gráficas e integração com outras ferramentas amplamente utilizadas na área de dados.

        import pandas as pd

    ## webbrowser
        Biblioteca já instalada por padrão
        Serve pra acessar endereço web

    ## time
        Biblioteca já instalada por padrão
        Pausar execução por determinado período

    ## openpyxl


    ## plotly express
        import plotly.express as px
        Criar gráficos abançados estilo BI
        
        Criar gráfico
        grafico = px.histogram(dados, x="loja",y="preco",text_auto=True,title="Faturamento",color="forma_pagamento")

        Mostrar gráfico
        grafico.show()

        Exportar pra arquivo HTML
        grafico.write_html("faturamento.html")


    ## nbformat


    ## fpdf
        Gerador de PDF
        pip install fpdf
        import fpdf

    ## NumPy
    ## SciPy
    ## Dask
    ## Seaborn

    ## Bokeh
    ## Altair
        
        
