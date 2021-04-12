"""
009)Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
numero = []
for numeros in range(3):
    numero_digitado = float(input('Digite um numero: '))
    numero.append(numero_digitado)
numero.sort()
print(f'os numeros em ordem são: {numero} ')
