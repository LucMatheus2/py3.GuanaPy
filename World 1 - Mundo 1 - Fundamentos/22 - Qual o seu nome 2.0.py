'''
# Algoritmo : Seu nome dissecado
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''

#Entrada de dados
nome = input("Digite o seu nome completo e aperte ENTER :")

#Processamento
espacos = nome.count(' ')
nomeQuebrado = nome.split()

# Saida de dados
print("O seu nome em MAIUSCULOS É : {}".format(nome.upper()))
print("O seu nome em minusculos é : {}".format(nome.lower()))
print("O seu nome tem um total de {} letras".format(len(nome) - espacos))
print("O primeiro nome tem {} letras".format(len(nomeQuebrado[0])))