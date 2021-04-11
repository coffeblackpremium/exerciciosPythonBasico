"""
009)Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9).
"""
graus_fahrenheit = float(input('Digite a Temperatura em Fahrenheit: '))
celsius = 5 * ((graus_fahrenheit-32) / 9)
print(f'A Temperatura {graus_fahrenheit}F é Equivalente em Celsius: {celsius}°C')
