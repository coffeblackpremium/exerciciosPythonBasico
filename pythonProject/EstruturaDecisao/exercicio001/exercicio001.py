"""
001)Faça um Programa que peça dois números e imprima o maior deles.
"""
numero01, numero02 = int(input('Digite um numero: ')), int(input('Digite outro número: '))

if numero01 > numero02:
    print(f'{numero01} é maior que {numero02}')
else:
    print(f'{numero02} é maior que {numero01}')
    