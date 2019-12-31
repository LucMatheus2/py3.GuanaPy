'''
# Algoritmo : Mostra a altura de alguém em metros e converte para centimetros e milimetros
# Autor: Lucas Matheus Costa
# Belém: ???/2017
'''

#Entrada de dados
altura = float(input("Qual a sua altura (em m) :"))

#Saída de dados
print("="*30)
print("A Sua altura em centimetros é : {} cm".format(altura*100))
print("A Sua altura em milimetros é : {} mm".format(altura*1000))