"""
013)Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

base = int(input('Digite a base: '))
expoente = int(input('Digite o Expoente: '))
contador = 0
while contador < expoente:
    potencia = base
    potenciacao = base * potencia
    contador += 1
print(f'O Resultado da Potenciacao de: {base} elevado a {expoente} é: {potenciacao}')
