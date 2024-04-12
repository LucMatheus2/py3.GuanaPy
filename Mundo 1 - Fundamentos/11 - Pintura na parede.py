# Algoritmo : Calcula a quantidade de tinta necessária para a área de uma parede.
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19

# Entrada de dados
alturaDaParede = float(input("Qual a altura da parede em metros :"))
larguraDaParede = float(input("Qual a largura da parede em metros :"))

# Processamento
areaDaParede = alturaDaParede * larguraDaParede
quantidadeDeTintaNecessaria = areaDaParede/2 # <- Cada litro de tinta suporta até 2m²

# Saída de dados
print("A área da parede é de {:.1f} m² quantidade de tinta necessária é de {:.1f} litros".format(areaDaParede,quantidadeDeTintaNecessaria))