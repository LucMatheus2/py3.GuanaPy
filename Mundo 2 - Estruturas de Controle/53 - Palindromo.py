'''
# Algoritmo : É um palindromo?
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20
'''
#Entrada de dados
frase = input("Digite uma frase : ")

#Lógica de 'Igualizar'
frase = frase.lower()
frase = frase.replace(" ","")

#Comparar
fraseI = ""
for i in range(len(frase)-1,-1,-1):
    fraseI += frase[i]

#Saída de dados
if (frase == fraseI):
    print("Olha, a frase é um palindromo, então não faz diferença se inverter")
else:
    print("A Frase não é palindromo, então ela é diferente") 