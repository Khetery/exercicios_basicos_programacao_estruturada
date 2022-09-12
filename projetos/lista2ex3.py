from xml.dom.minidom import TypeInfo


vendaBalcao = 0
valorBalcao = 0
vendaTelefone = 0 
valorTelefone = 0

while (1):
    aux = int(input("Selecione a opção desejada: \n 1. Venda por Balcão. \n 2. Venda por Telefone \n 3. Totalização"))
    if(aux == 1):
        vv = int(input("Informe o valor da venda"))
        while vv < 0:
            vv = int(input("Informe um valor de venda válido"))
        vendaBalcao+=1
        valorBalcao+=vv 
    elif(aux == 2):
        vv = int(input("Informe o valor da venda"))
        while vv < 0:
            vv = int(input("Informe um valor de venda válido"))
        vendaTelefone+=1
        valorTelefone+=vv        
    elif(aux == 3):
        desejo = int(input("Selecione a opção desejada: \n 1. Total Balcão. \n 2. Total Telefone \n 3. Total geral"))
        if(desejo == 1):
            print("Foram realizadas ", vendaBalcao , " vendas no balcão, totalizando ", valorBalcao, " reais.")
        if(desejo == 2):
            print("Foram realizadas ", vendaTelefone, " vendas no telefone, totalizando ", valorTelefone, " reais.")
        if(desejo == 3):
            print("Foram realizadas ", vendaBalcao+vendaTelefone , " vendas no geral, totalizando ", valorBalcao+valorTelefone, " reais.")
    else:
        print("informe uma opção válida")