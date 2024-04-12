# Entrada dos numeros
valor1 = input("Digite um número natural : ")
valor2 = input("Digite outro número natural : ")
valor3 = input("Digite mais um número natural : ")
valor4 = input("Digite o último número natural : ")

# Convertendo os valores
valor1 = int(valor1)
valor2 = int(valor2)
valor3 = int(valor3)
valor4 = int(valor4)

# Criando a tupla
tuplaDeValores = (valor1,valor2,valor3,valor4)

# Registrando ocorrências
numerosDeOcorrenciasDoNumeroNove = tuplaDeValores.count(9)
indiceDeAparicaoDoNumeroTres = tuplaDeValores.index(3)

# Imprimindo dados de saída
print("O número nove(9) aparece {} vezes".format(numerosDeOcorrenciasDoNumeroNove))
print("O número três(3) aparece na {}ª posição".format(indiceDeAparicaoDoNumeroTres+1))
print("Os números pares na tupla são : ",end="[")
for num in tuplaDeValores:
    if num%2==0:
        print(num,end=',')
print('...]')
