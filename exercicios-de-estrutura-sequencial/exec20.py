#20. Desenvolva um algoritmo que receba um valor em Euro, calcule e mostre o valor convertido para Real.

euro = float(input('Informe o valor do EURO: '))

real = euro * 5.25

print('O valor do euro convertido para Real é: R${:.2f}'.format(real))
