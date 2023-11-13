#24. Desenvolva um algoritmo que receba a altura de um degrau, calcule e mostre quantos degraus uma pessoa precisa subir se deseja estar a uma altura de 5 quilômetros.

centimetros = int(input('Informe a altura do degrau: '))
metros = centimetros /100
qtdDegraus = 5 // metros

print('Serão necessários {} degraus'.format(qtdDegraus))
