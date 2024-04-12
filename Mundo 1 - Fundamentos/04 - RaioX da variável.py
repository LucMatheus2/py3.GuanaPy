# Algoritmo : Mostra os detalhes de uma variável
# Autor: Lucas Matheus Costa
# Belém: ???/2017

# Separar informações
print("="*30)

#Entrada de dados
texto = input("\033[35mDigite um texto qualquer :")

#Saída de dados
print("="*30)
print("Mensagem : {}".format(texto))
print("="*30)
print("Classe: {}".format(type(texto)))
print("Ele é um número? : {}".format(texto.isnumeric()))
print("Ele é um texto? : {}".format(texto.isalpha()))
print("Ele é texto e número ao mesmo tempo : {}".format(texto.isalnum()))
print("Ele pode ser impresso?: {}".format(texto.isprintable()))
print("Ele está em maiúsculo? : {}".format(texto.isupper()))
print("Ele está capitalizado? : {}".format(texto.istitle()))
