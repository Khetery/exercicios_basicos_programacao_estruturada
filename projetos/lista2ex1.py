CAPACIDADE = 300
idade = int(input("Quantos anos você tem?"))
pessoas = 0


while idade != 0 and pessoas <CAPACIDADE:
    if idade <18:
        print("Entrada Proibida!")
    else:
        pessoas +=1
        print("O números de pessoas na casa é: ", pessoas)
    idade = int(input("Quantos anos você tem?"))
