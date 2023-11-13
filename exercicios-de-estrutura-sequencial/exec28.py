#21. Desenvolva um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre a idade dessa pessoa e quantos anos essa pessoa terá daqui a 10 anos.

anoNasce = int(input('Informe o ano em que nasceu: '))
anoAtual = int(input('Informe o ano atual: '))

idade =  anoAtual - anoNasce

print('Você tem {} anos'.format(idade))
