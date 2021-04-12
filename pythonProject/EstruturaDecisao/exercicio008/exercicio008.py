"""
008) Faça um programa que pergunte o preço de três produtos e informe qual produto
    você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
produto = []
for numeros in range(3):
    numero_digitado = float(input('Digite um numero'))
    produto.append(numero_digitado)
print(f'O Produto mais barato que você deve comprar é esse {min(produto)}R$')
