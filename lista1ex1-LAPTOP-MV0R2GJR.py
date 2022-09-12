from sys import float_repr_style


print("Bem Vindo!")
distancia = float(input("Digite a distância em km entre o ponta inicial e final:"))
tempo = float(input("Digite o tempo gasto no percurso em horas:"))
velocidadeMedia = distancia/tempo
print("A velocidade média é:",velocidadeMedia," km/h")
if velocidadeMedia > 100:
    print("Você atingiu o limite de velocidade, portanto será multado em R$100.000.000.000,25")
else:
    print("Parabéns, continue assim. Dirigir na velocidade correta salva vidas!")





