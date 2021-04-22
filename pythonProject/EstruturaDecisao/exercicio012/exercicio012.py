"""
012)Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na
    tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
def aumenta_salario(ir):
    ir_total = salario * ir
    print(f'Sálario Bruto ({mes_trabalhado} * {ganho_horas}):\t\t\tR${salario}')
    print(f'(-) IR ({ir})%:\t\t\t\t\t\t\tR${ir_total}')
    print(f'(-) INSS:\t\t\t\t\t\t\t\tR${salario * 0.10}')
    print(f'(-) FGTS:\t\t\t\t\t\t\t\tR${salario * 0.11}')
    print(f'Total de Descontos:\t\t\t\t\t\tR${(salario * 0.11) + (salario * 0.10) + (ir_total)}')
    print(f'Salario Líquido:\t\t\t\t\t\tR${salario * 0.11 * 0.10 * 0.05 + salario}')
    return ''


ganho_horas = float(input('Digite quanto você ganha por horas trabalhada: '))
mes_trabalhado = float(input('Digite a quantidade de horas trabalhada no mês: '))
salario = ganho_horas * mes_trabalhado
if salario < 0:
    print('Valor Invalido!')
elif salario < 900:
    print(f'Insento de qualquer tributo extra seu salario é: {salario}')
elif salario > 900 and salario < 1500:
    print(aumenta_salario(0.05))
elif salario > 1500 and salario < 2500:
    print(aumenta_salario(0.10))
elif salario >= 2500:
    print(aumenta_salario(0.20))
