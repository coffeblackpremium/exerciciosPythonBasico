"""
005)Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""
digito_usuario = int(input('Digite o número: '))
def imprimir_valor(valor):
    for i in range(1, valor+ 1):
        lista = []
        for inteiro in range(i):
            lista.append(str(inteiro + 1))
        print('  '.join(lista))

imprimir_valor(digito_usuario)
