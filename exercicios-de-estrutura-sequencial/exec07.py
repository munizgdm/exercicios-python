#07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input('Informe o lado do quadrado: '))
area = lado ** 2
dobro = area * 2
print('O dobro da área do quadrado é: {}'.format(dobro))
