"""
007)Faça um programa que leia 5 números e informe o maior número.
"""
lista = []
for inteiro in range(5):
    entrada_de_inteiro = int(input('Digite um numero: '))
    lista.append(entrada_de_inteiro)
print(f'O Maior numero é {max(lista)}')
