# BIBLIOTECAS
import pandas
import openpyxl
import plotly
import nbformat

# Carregando o arquivo
dados = pandas.read_excel("vendas.xlsx")

#Validando carregamento dos dados da planilha

# Verificando as primeiras linha carregadas
print(dados.head)
# Verificando as últimas linha carregadas
print(dados.tail)
# Verificando a quantidade de linhas x colunas
print(dados.shape)
# Verificando informações das colunas
print(dados.info)