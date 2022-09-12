print("Bem Vindo!")
nota1 = float(input("Digite uma nota:"))
nota2 = float(input("Digite outra nota:"))
media = (nota1+nota2)/2
if media >= 7:
    print("Parabéns, Você foi aprovado!")
else:
    print("Exame!")
    exame = float(input("Digite a nota do exame:"))
    if (((exame+media)/2) >= 5):
        print('Aprovado...')
    else:
        print('Reprovado...')