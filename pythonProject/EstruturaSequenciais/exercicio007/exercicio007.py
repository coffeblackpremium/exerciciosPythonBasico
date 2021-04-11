"""
007)Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
base, altura = float(input('Digite a base do quadrado: ')), float(input('Digite a Altura do Quadrado: '))
area_quadrado, area_quadrado_dobro = base * altura, (base * altura) * 2
print(f'A Area do Quadrado é {area_quadrado} e o Dobro dessa Area é {area_quadrado_dobro}')
