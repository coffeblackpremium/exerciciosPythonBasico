"""
001)Faça um programa para imprimir:

  1
  2   2
  3   3   3
   .....
   n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""
def imprimir_valor(valor):
    for i in range(0, valor+1):
        print(f'{str(i)}\t' * i)
    return
imprimir_valor(10)
