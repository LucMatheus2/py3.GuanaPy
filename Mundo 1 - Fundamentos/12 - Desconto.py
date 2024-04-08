'''
# Algoritmo : Desconto de 5% sobre o produto
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''
#Constantes
percentualDeDesconto = 5 #<- Esse valor deve variar de 0 á 100

#Entrada de dados
precoDoProduto = float(input("Digite o preço de um produto (em R$) :"))

#Processamento
precoDoProduto = precoDoProduto - (precoDoProduto*(percentualDeDesconto/100))

#Saida de dados
print("O Novo preço do produto é R$ {:.2f}".format(precoDoProduto))