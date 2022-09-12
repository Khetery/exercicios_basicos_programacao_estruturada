print("Bem Vindo!")
base = float(input("Informe a base do triângulo:"))
altura = float(input("Informe a altura do triângulo:"))
area = (base*altura)/2
if base <=0:
    print("erro, digite um número real!")
if altura <=0:
    print("erro, digite um número real!")
else:
    print("A área é:",area)