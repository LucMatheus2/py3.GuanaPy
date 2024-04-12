# Algoritmo : Bonificaçãp salaria de 15%
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19

# Constantes
bonificacaoDeSalario = 15 #<- Esse valor deve variar de 0 á 100

# Entrada de dados
salario = float(input("Digite o salário do funcionário (em R$) :"))

# Processamento
salario = salario + (salario*(bonificacaoDeSalario/100))

# Saida de dados
print("O Novo salário do funcionário é R$ {:.2f} \033[m".format(salario))