nome = input()
salario = float(input())
tVendas = float(input())

qVendas = float(tVendas * (15 / 100))
total = salario + qVendas
print("TOTAL = R$ %0.2f" %total)