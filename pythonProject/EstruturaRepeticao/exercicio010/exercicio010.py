"""
010)Faça um programa que r
Receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
numero_inteiro1, numero_inteiro2 = int(input('Digite um numero Inteiro: ')), int(input('Digite outro numero Inteiro: '))
lista = []
if numero_inteiro1 > numero_inteiro2:
    while numero_inteiro1 > numero_inteiro2:
        numero_inteiro2 += 1
        if numero_inteiro2 == numero_inteiro1:
            break
        lista.append(numero_inteiro2)
elif numero_inteiro2 > numero_inteiro1:
    while numero_inteiro2 > numero_inteiro1:
        numero_inteiro1 += 1
        if numero_inteiro1 == numero_inteiro2:
            break
        lista.append(numero_inteiro1)
print(lista)
