# Algoritmo : Sorteio de alunos
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19

# Bibliotecas
from random import choice

# Entrada de dados
aluno01 = input("Digite o nome do 1º Aluno :")
aluno02 = input("Digite o nome do 2º Aluno :")
aluno03 = input("Digite o nome do 3º Aluno :")
aluno04 = input("Digite o nome do 4º Aluno :")

listaDeAlunos = [aluno01,aluno02,aluno03,aluno04]

# Processamento
escolhido = choice(listaDeAlunos)

# Saida de dados
print("O aluno escolhido foi o(a) {}".format(escolhido))