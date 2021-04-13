"""
008)Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
lista = []
for inteiros in range(5):
    entrada_de_inteiros = int(input('Digite um Numero: '))
    lista.append(entrada_de_inteiros)
media = sum(lista) / 5
print(f'A Soma dos numeros é {sum(lista)} e a media é {media}')
