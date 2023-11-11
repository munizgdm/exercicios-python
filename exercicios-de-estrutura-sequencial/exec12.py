#12 - Desenvolva um algoritmo que receba o salário de um funcionário, calcule e mostre seu novo salário com reajuste de 15%.

salario = float(input('Informe seu salário: '))
novoSalario = salario * 1.15
print('O novo salário é: R${:.2f}'.format(novoSalario))
