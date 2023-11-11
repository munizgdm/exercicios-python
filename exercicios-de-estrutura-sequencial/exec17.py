#17. Desenvolva um algoritmo que receba o salário bruto de um funcionário, calcule e mostre o salário líquido desse funcionário, sabendo que ele recebe 10% de gratificação calculados sobre o salário bruto, mas paga 20% de imposto de renda também calculados sobre o salário bruto.

salBruto = float(input('Informe seu sálario BRUTO: '))
bonus = (salBruto * 10) / 100
ir = (salBruto * 20) / 100

salLiquido = salBruto + bonus - ir

print('O salário liquido do funcionário é: R${:.2f}'.format(salLiquido))
