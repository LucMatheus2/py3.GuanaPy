'''
# Algoritmo : É uma casa de cambio
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''
cotacaoUSD = 4 #Considerando a cotação US$ 1,00 = R$ 4,00
valorNaCarteira = float(input("\033[32mQuanto é o valor em reais na sua carteira: "))
#Saída de dados
print("Você tem US$ {:.2f}".format(valorNaCarteira/cotacaoUSD))