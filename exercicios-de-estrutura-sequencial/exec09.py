#09 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

C = 5 * ((F-32) / 9).

fahrenheit = float(input('Informe os graus em Fahrenheit: '))
celsius = 5 * ((fahrenheit - 32) / 9)
print('Os graus Fahrenheit trasnformados em Celsius é: {:.2f}c°'.format(celsius))

