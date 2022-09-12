from re import I


inicio = float(input("Valor real inicial da contagem:"))
final = float(input("Valor real final da contagem:"))
passo = float(input("Valor real do passo de contagem:"))

i = inicio

print("inicio")

while i<= final:
  print("I", i)

i+= passo

print("fim")