"""
003)Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
nota = [float(input('Digite sua nota: ')) for i in range(4)]
media = sum([x for x in nota]) / 4
print(f'Todas as notas foram {list(nota)} e a media é {media}')
