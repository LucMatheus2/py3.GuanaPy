'''
# Algoritmo : Conversor de temperatura
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''

#Entrada de dados
grausEmCelsius = float(input("\033[34mInforme a temperatura em celsius(ºC) :"))

#Processamento
grausEmFahrenheit = ((9*grausEmCelsius)/5)+32

#Saída de dados
print("A Temperatura em fahrenheit é {:.1f} ºF".format(grausEmFahrenheit))