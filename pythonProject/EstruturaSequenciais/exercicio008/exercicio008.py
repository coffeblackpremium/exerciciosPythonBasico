"""
008)Faça um Programa que pergunte quanto
você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
dinheiro_horas, qnt_trabalhada = float(input('Digite quanto você ganha por Hora: ')), float(input('Digite as horas Trabalhadas no mes: '))
salario = dinheiro_horas * qnt_trabalhada
print(f'Seu salario é {salario}')
