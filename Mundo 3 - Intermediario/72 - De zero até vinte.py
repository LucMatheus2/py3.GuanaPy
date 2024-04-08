'''
Exercicios de tuplas que vão de zero até vinte

@author Lucas Matheus Costa <teclucas.costa@hotmail.com>
@since 18/07/2021
'''

#Definindo a tupla
tuplaDeNumerais = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

#Colocando o número escolhido
numeroEscolhido = input("Digite um número natural entre 0 e 20 : ")
valido = True

#Fazendo a conversão e o processamento
numeroEscolhido = int(numeroEscolhido)
numeroEscolhido = abs(numeroEscolhido)

#Gatilho - fazendo a checagem do numero
if (numeroEscolhido > len(tuplaDeNumerais)):
    valido = False
    numeroEscolhido = 0

numeroEscolhido = tuplaDeNumerais[numeroEscolhido]

#Imprimindo o número
if (valido == False):
    print("Você digitou um valor incorreto")
else:
    print("Você digitou o número {}".format(numeroEscolhido))
