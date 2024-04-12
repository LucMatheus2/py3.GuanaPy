# Algoritmo : O seu nome tem silva?
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19

# Entrada de dados
nome = input("Digite o seu nome completo :").strip()

# Processamento
nome = nome.title()
isSilva = 'Silva' in nome

# Saida de dados
print("O seu nome tem 'Silva'?: {}".format(isSilva))