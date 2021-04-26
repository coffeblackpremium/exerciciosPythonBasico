"""
007)Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
multiplicacao = 1
vetor_inteiros = [float(input('Digite um número: ')) for v in range(5)]
soma_vetor = sum([v for v in vetor_inteiros])
mult_vetor = []
for v in vetor_inteiros:
    multiplicacao *= v
    mult_vetor.append(multiplicacao)
print(f'O Vetor é: {vetor_inteiros}\n a soma é {soma_vetor}\n E a multiplicação é {mult_vetor[4]}')
