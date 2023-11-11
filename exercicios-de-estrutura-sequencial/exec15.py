#15. Desenvolva um algoritmo que receba os coeficientes a, b e c de uma equação de segundo grau (ax2 + bx + c), calcule e mostre as raízes reais dessa equação, considerando uma equação que possui duas raízes reais.

import math

a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
c = int(input('Informe o valor de C: '))

delta = (b**2) - 4 * a * c

print(delta)

x1 = (-(b) + (math.sqrt(delta))) / (2 * a)
x2 = (-(b) - (math.sqrt(delta))) / (2 * a)
print(x1)
print(x2)
