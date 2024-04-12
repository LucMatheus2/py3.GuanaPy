# Exercicios de tuplas agora trabalhando com a tabela do brasileirão
# 
# @author Lucas Matheus Costa <teclucas.costa@hotmail.com>
# @since 18/07/2021


#Colocando a tabela do Brasileirão
tabelaDoBrasileirao = ('Palmeiras','Atlético-MG','Fortaleza','Bragantino','Athletico-PR','Ceará SC','Bahia','Fluminense','Flamengo','Santos','Atlético-GO','Corinthians','Juventude','São Paulo','Internacional','América-MG','Cuiabá','Sport Recife','Grêmio','Chapecoense')
tam = len(tabelaDoBrasileirao) # <- Variável de controle 

#Imprimindo os primeiros colocados
print("===OS PRIMEIROS COLOCADOS SÃO ===")
for times in range(0, 5):
    print("{}ª Posição - {}".format(times+1,tabelaDoBrasileirao[times]))

#Imprimindo os últimos colocados
print("=== OS LANTERNAS SÃO ===")
gatilhoLanterna = tam - 5
for times in range(gatilhoLanterna,tam):
   print("{}ª Posição - {}".format(times+1,tabelaDoBrasileirao[times]))

#Imprimindo os times em ordem alfabética
print("=== OS TIMES EM ORDEM ALFABÉTICA SÃO ===")
timesEmOrdemAlfabetica = sorted(tabelaDoBrasileirao)
for time in timesEmOrdemAlfabetica:
    print("- {}".format(time))

#Colocando a chapecoense
print("="*30)
print("A Chapecoense está na {}ª posição".format(tabelaDoBrasileirao.index('Chapecoense')+1))