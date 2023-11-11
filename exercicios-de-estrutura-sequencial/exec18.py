#18. Desenvolva um algoritmo que receba o valor de um depósito em poupança, calcule e mostre o valor após um mês de aplicação na poupança, sabendo que a poupança rende 5% ao mês.

deposito = float(input('Informe o valor de deposito: '))
rendeu = deposito * 1.05

print('Depois de um mês a poupança rendeu: R${:.2f}'.format(rendeu))
