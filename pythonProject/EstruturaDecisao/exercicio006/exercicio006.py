"""
006)Faça um Programa que leia três números e mostre o maior deles.
"""
numero01, numero02, numero03 = float(input('Digite um numero: ')), float(input('Digite um numero: ')), float(
    input('Digite um numero: '))

if numero01 > numero02 and numero01 > numero03:
    print(f'{numero01} é o maior numero')
elif numero02 > numero01 and numero02 > numero03:
    print(f'{numero02} é o maior numero')
elif numero03 > numero02 and numero03 > numero01:
    print(f'{numero03} é o maior numero')
