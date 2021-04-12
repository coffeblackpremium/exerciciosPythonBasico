"""
007)Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
numero = []
for numeros in range(3):
    numero_digitado = float(input('Digite o numero: '))
    numero.append(numero_digitado)
print(f'O Maior valor é {max(numero)} e o menor valor é {min(numero)}')
