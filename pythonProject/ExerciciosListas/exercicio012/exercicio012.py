"""
012)Faça um programa que receba a temperatura média de
cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
import random
contador = 1
temp_por_mes = [random.randint(20, 40) for meses_ano in range(1, 12)]
media_temp = sum(temp_por_mes) / 12
meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                'Novembro', 'Dezembro']
media_anual = [(mes, temperatura) for mes, temperatura in zip(meses_do_ano, temp_por_mes) if temperatura > media_temp]
for a, extenso in media_anual:
    print(f'{contador}° {a}')
    contador += 1
