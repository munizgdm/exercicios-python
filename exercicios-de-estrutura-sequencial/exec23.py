#23. Desenvolva um algoritmo que receba dois valores numérico real, calcule e mostre o quadrado da diferença desses dois números.

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

diferenca = (num1**2) - (num2**2)

print('A diferença entre os valores elevado ao quadrado: {}'.format(diferenca))
