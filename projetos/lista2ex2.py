matricula = input("Digite o seu R.A:")
while matricula != "0":
    nota1 = int(input("Digite a nota 1: "))
    nota2 = int(input("Digite a nota 2: "))
    media = (nota1+nota2)/2
    print("Média = ",media)
    if media >=5:
        print("APROVADO!")
    else:
        print("REPROVADO!")
    matricula = input("Digite o seu R.A:")