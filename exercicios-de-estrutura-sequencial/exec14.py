#14. Desenvolva um algoritmo que receba dois valores inteiros para as variáveis x e y, efetue a troca dos valores, ou seja, x passa a ter o valor de y e y passa a ter o valor de x e mostre os valores trocados.

x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

aux = x
x = y
y = aux

print('Agora X vale: {}'.format(x))
print('Agora Y vale: {}'.format(y))
