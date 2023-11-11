#16. Desenvolva um algoritmo que receba os valores do comprimento (C), da largura (L) e da altura (H) de um paralelepípedo, calcule e mostre o volume desse paralelepípedo. Fórmula do volume de um paralelepípedo: V = C . L . H.

comprimento = int(input('Informe o valor do COMPRIMENTO: '))
largura = int(input('Informe o valor da LARGURA: '))
altura = int(input('Informe o valor da ALTURA: '))

volume = comprimento * largura * altura
print('O volume do PARALELEPÍPEDO é: {}'.format(volume))
