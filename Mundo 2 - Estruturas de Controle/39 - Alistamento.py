# Algoritmo : Alistamento Militar
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19

# Importação de pacotes
from datetime import date

# Entrada De Dados
anoDeNascimento = int(input("Qual o ano do seu nascimento? : "))

# Processamento
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento

# Saida de dados
if (idade < 18):
    print("Você é ainda muito novo(a) para se alistar, espere mais {} anos".format(18-idade))
elif (idade == 18):
    print("Esse ano você deve se alistar, apresente-se na junta militar do seu municipio")
else:
    print("Já passou da hora de se alistar, você deveria ter se apresentado na junta militar há {} anos, Apresente-se lá imediatamente!".format(idade-18))

print("(C) 2019-20 - Luk")
