def pecasRestantes (total_de_pecas):
    print("Restam", total_de_pecas,"Pecas!")

def turnoDoJogador (pecas, total_de_pecas,limite_de_pecas_por_jogada):
    while (pecas>limite_de_pecas_por_jogada) or (pecas<0):
        print("O Valor máximo de peças por jogada é",limite_de_pecas_por_jogada)
        pecas = int(input("Digite quantas Peças Você Deseja Tirar?"))

    total_de_pecas = (total_de_pecas-pecas)
    print("Você retirou",pecas,"peças.")
    return total_de_pecas

def turnoDoComputador (pecas,total_de_pecas,limite_de_pecas_por_jogada):
    pecas = total_de_pecas%(limite_de_pecas_por_jogada+1)
    total_de_pecas = (total_de_pecas-pecas)
    print("O Seu Oponente Retirou",pecas,"Peças")
    return total_de_pecas
    
print("Bem Vindo ao NIM")
total_de_pecas = 0
limite_de_pecas_por_jogada = 0
pecas = 0

print("Vamos Começar!")
total_de_pecas = int(input("Digite a quantidade de peças="))
limite_de_pecas_por_jogada = int(input("Digite o Limite de Peças por Jogada="))

if (total_de_pecas%(limite_de_pecas_por_jogada+1))== 0:
    print("Você Começa!")

else:
    print("Eu começo!")
    total_de_pecas=(turnoDoComputador(pecas,total_de_pecas,limite_de_pecas_por_jogada))
    pecasRestantes(total_de_pecas)

pecas = int(input("Digite quantas Peças Você Deseja Tirar?:\n"))

while (total_de_pecas>0):
    total_de_pecas=(turnoDoJogador(pecas,total_de_pecas,limite_de_pecas_por_jogada))   
    if total_de_pecas==0:
        print("O Jogo acabou, que pena você perdeu, mais sorte na próxima jogada!")
    else:
        pecasRestantes(total_de_pecas)

        total_de_pecas=(turnoDoComputador(pecas,total_de_pecas,limite_de_pecas_por_jogada))

    if total_de_pecas ==0:
        print("O Jogo acabou, que pena você perdeu, mais sorte na próxima jogada!")
    else:
        pecasRestantes(total_de_pecas)
        pecas = int(input("Digite quantas Peças Você Deseja Tirar?:\n"))


    
    



