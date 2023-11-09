#08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salHora = float(input('Qual o salário hora? '))
trabHora = int(input('Quantas horas trabalhadas no mês? '))
salario = salHora * trabHora
print('Salario: R${}'.format(salario))
