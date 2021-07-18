'''
# Algoritmo : Cadastro de nome e sobrenome
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''

#Entrada de dados
nomeCompleto = input("Digite o seu nome completo : ")

#Processamento
nomeCompleto = nomeCompleto.split()

#Isso não precisa, só que acho que ficar melhor de entender o código assim
primeiroNome = nomeCompleto[0]
ultimoNome = nomeCompleto[len(nomeCompleto)-1]

#Saída de dados
print("O nome para cadastro é : {} {}".format(primeiroNome,ultimoNome))
