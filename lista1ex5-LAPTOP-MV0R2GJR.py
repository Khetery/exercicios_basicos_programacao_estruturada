from re import A


print("Bem Vindo!\n")
print("Conseiderando uma equação do segundo grau no formato: ax^2+bx+c")
a = int(input("Informe o Valor de A:"))
b = int(input("Informe o Valor de B:"))
c = int(input("Informe o Valor de C"))
delta = (b*b)-4*a*c
if delta <0:
    print("Não há raízes reais...")
if delta ==0:
    x = (-b)/(2*a)
    print("O valor da raiz é ",x)
if delta >0:
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    print("Os Resultados são: ",x1, " e ",x2)



