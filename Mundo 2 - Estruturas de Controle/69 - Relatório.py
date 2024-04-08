#Bibliotecas Importadas
import os

#Varíaveis
idadeDoUsuario = 0
sexoDoUsuario = "m"

quantidadeDePessoasMaioresDeIdade = 0
quantidadeDeHomens = 0
quantidadeDeMulheresMenoresDeVinteAnos = 0
totalDePessoas = 0
opcaoDoUsuario = ""

while True:
    print("===PESQUISA=== | Espaço Amostral : {}".format(totalDePessoas))
    idadeDoUsuario = int(input("Qual a idade do usuário : "))
    while True:
        sexoDoUsuario = input("Qual o sexo do usuário(M/F) : ")
        sexoDoUsuario = sexoDoUsuario.lower()
        if (sexoDoUsuario == "m" or sexoDoUsuario == "f"):
            break
    #Contando pessoas maiores de idade
    if (idadeDoUsuario >= 18):
        quantidadeDePessoasMaioresDeIdade+=1
    #Contando a quantidade de homens
    if (sexoDoUsuario == "m"):
        quantidadeDeHomens+=1
    #Contando a quantidade de mulheres menores de vinte anos
    if (sexoDoUsuario == "f") and (idadeDoUsuario < 20):
        quantidadeDeMulheresMenoresDeVinteAnos+=1
    totalDePessoas+=1
    opcaoDoUsuario = input("Você quer continuar (S/N) : ")
    opcaoDoUsuario = opcaoDoUsuario.lower()
    os.system("clear")
    if (opcaoDoUsuario == "n"):
        break
print("==FIM DA PESQUISA ===")
print(f"Total de Entrevistados {totalDePessoas} pessoas")
print("-------------------------------------------------")
print(f"Qtde de Maiores de Idade = {quantidadeDePessoasMaioresDeIdade} pessoas | Correspondendo a {(quantidadeDePessoasMaioresDeIdade/totalDePessoas)*100:.2f} % do espaço amostral")
print(f"Qtde de Homens = {quantidadeDeHomens} | Correspondendo á {(quantidadeDeHomens/totalDePessoas)*100:.2f} % do espaço amostral")
print(f"Qtde de Mulheres com menos de 20 anos = {quantidadeDeMulheresMenoresDeVinteAnos} | Correspondendo á {(quantidadeDeMulheresMenoresDeVinteAnos/totalDePessoas)*100:.2f} % do espaço Amostral")