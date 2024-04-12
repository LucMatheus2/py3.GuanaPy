# Algoritmo : Aluguel de Carro?
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19

# Entrada de dados
quilometragem = float(input('Quantos quilometros dura a sua viagem? :'))

# Processamento
if quilometragem>200:
    taxa = 0.45
else:
    taxa = 0.50

# Saída
print("O Preço da passagem é R$ {:.2f}".format(quilometragem*taxa))