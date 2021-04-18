"""
005)Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
vetor = [x for x in range(20)]
vetor_par = [par for par in vetor if par % 2 == 0]
vetor_impar = [impar for impar in vetor if not impar % 2 == 0]
print(f'Os Vetores são: {*vetor,}\ne o Vetor par é: {*vetor_par,}\ne o Vetores Impar são: {*vetor_impar,}')
