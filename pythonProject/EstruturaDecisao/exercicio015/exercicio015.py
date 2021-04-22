"""
015)Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""
lado_triangulo_1 = float(input('Digite o Primeiro lado do Triângulo: '))
lado_triangulo_2 = float(input('Digite o Segundo lado do Triângulo: '))
lado_triangulo_3 = float(input('Digite o Terceiro lado do Triângulo: '))

if lado_triangulo_1 == lado_triangulo_2 and lado_triangulo_1 == lado_triangulo_3:
    print('É um Triangulo Equilátero')
elif lado_triangulo_1 != lado_triangulo_2 and lado_triangulo_2 != lado_triangulo_3:
    print('É um Traingulo Escaleno!')
elif lado_triangulo_1 == lado_triangulo_2 and lado_triangulo_1 != lado_triangulo_3:
    print('É um Triangulo Isósceles')
elif lado_triangulo_2 == lado_triangulo_3 and lado_triangulo_2 != lado_triangulo_1:
    print('É um Triangulo Isósceles')
elif lado_triangulo_1 == lado_triangulo_3 and lado_triangulo_1 != lado_triangulo_2:
    print('É um Triangulo Isósceles')
    