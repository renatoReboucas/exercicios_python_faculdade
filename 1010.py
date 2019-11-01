peca1 = input().split(" ")
cod1, qtd1, val1 = peca1

peca2 = input().split(" ")
cod2, qtd2, val2 = peca2

total = ( ( int(qtd1) * float(val1) ) + ( int(qtd2) * float(val2) ) )
print("VALOR A PAGAR: R$ %.2f" %total)
