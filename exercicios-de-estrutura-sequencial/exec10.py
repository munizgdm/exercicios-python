#10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Informe os graus em Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print('Os graus Celsius trasnformados em fahrenheit é: {}c°'.format(fahrenheit))
