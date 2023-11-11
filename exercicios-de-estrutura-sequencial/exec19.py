#19. Desenvolva um algoritmo que receba um valor em Real, calcule e mostre o valor convertido para Dólar.

real = float(input('Informe o valor em REAL: '))

dolar = real / 4.90

print('O valor do REAL convertido em DOLAR é: ${:.2f}'.format(dolar))
