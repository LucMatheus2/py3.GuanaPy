'''
# Algoritmo : Programa de Natação
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Importação de pacotes
from datetime import date

#Entrada de dados
anoDeNascimento = int(input("\033[34mDigite o seu ano de nascimento : "))

#Processamento e Saída
anoAtual = date.today().year
idadeDoCidadão = anoAtual - anoDeNascimento

if(idadeDoCidadão <= 9):
    print("Você entrará na categoria MIRIM")
elif(idadeDoCidadão > 9 and idadeDoCidadão <= 14):
    print("Você entrará na categoria INFANTIL")
elif(idadeDoCidadão > 14 and idadeDoCidadão <= 19):
    print("Você entrará na categoria JUNIOR")
elif (idadeDoCidadão > 19 and idadeDoCidadão <= 25):
    print("Você entrará na categoria SÊNIOR")
elif (idadeDoCidadão > 25):
    print("Você entrará na categoria MESTRE")

print("(c) 2019-20 | Teclucas98")
