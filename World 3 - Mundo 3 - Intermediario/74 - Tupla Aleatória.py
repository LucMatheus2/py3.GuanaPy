'''
Exercicios de tuplas aleatórias

@author Lucas Matheus Costa <teclucas.costa@hotmail.com>
@since 18/07/2021
'''
#Importar pacotes
from random import randint

#Definindo a tupla aleatória
tuplaAleatoria = (
    randint(0,50),
    randint(0,50),
    randint(0,50),
    randint(0,50)
)
#Organizando uma nova tupla pra ajudar
tuplaNova = sorted(tuplaAleatoria)

#Saída de informações
print("A tupla é a {}".format(tuplaAleatoria))
print("O menor valor é: {}".format(tuplaNova[0]))
print("O maior valor é: {}".format(tuplaNova[len(tuplaNova)-1]))