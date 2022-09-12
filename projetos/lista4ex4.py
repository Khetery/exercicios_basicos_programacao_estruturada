gastoTotal = 0

for mes in range(12):
    gastoMensal = float(input("Informe o gasto no mês"))
    if(gastoMensal<0):
        mes-=1
        print("informe um valor válido para esse mês")
    else:
        gastoTotal+=gastoMensal
        print("Total acumulado: ",gastoTotal)

if(gastoTotal == 0):
    print("O gasto foi de 0, ou seja, gasto nulo")
elif gastoTotal < 300:
    print("O gasto foi de ",gastoTotal," este gasto foi moderado.")
else:
    print("O gasto foi de ",gastoTotal, " e este gasto foi excessivo.")
