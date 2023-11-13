#23. Desenvolva um algoritmo que receba uma quantidade de um alimento em quilos, calcule e mostre quantos dias durará esse alimento para uma pessoa que consome 50 gramas desse alimento por dia.

qtdAlimentos = int(input('Informe a quantidade de alimentos em (QUILOS): '))
gramas = qtdAlimentos * 1000
qtdDias = gramas // 50

print('O alimento sera consumido em {} dias'.format(qtdDias))
