# BIBLIOTECAS
import os
from fpdf import FPDF

projeto = input("Digite a descrição do projeto")
horas_estimadas = input("Digite o total de horas estimadas")
valor_hora = input("Digite o valor da hora trabalhada")
prazo = input("Digite o prazo estimado para conclusão")
cliente = input("Digite o nome do Cliente")
autor = "Marcello Queiroz"

valor_total = str(int(horas_estimadas)*int(valor_hora))

pdf = FPDF()
pdf.add_page()
pdf.set_author(autor)
pdf.set_font("Arial")

file_path = 'c:\\Users\\marce\\OneDrive\\Documentos\\GitRepositorios\\Portfolio_Python\\Orçamento_pdf\\template.png'
pdf.image(file_path, x=0, y=0)

pdf.text(115,145,projeto)
pdf.text(115,160,horas_estimadas)
pdf.text(115,190,prazo)
pdf.text(115,205,valor_total)

pdf.output(f"Orçamento {cliente}.pdf")
print("Orçamento gerado com sucesso!")