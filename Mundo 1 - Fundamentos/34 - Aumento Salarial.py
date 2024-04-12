# Algoritmo : Aumento salarial
# Versão 1.1
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19

# Entrada de dados
salarioReal = float(input("Digite o salario do funcionário :"))

# Processamento
if (salarioReal > 1250):
    percentualDeAumento = 10
else:
    percentualDeAumento = 15

salarioAumentada = salarioReal + (salarioReal*(percentualDeAumento/100))

# Saída de dados
print("O Novo Salário é de R$ {:.2f}".format(salarioAumentada))