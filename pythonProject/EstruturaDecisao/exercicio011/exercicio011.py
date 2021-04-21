"""
011)As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario_funcionario = float(input('Digite o Salario do Funcionario: '))
novo_salario = 0


def aumenta_salario(salario, porcentagem):
    salario = salario * porcentagem + salario
    salario_percentual = round(salario * porcentagem, 2)
    return salario, f'Aumento de {salario_percentual}R$'


if salario_funcionario <= 0:
    print('Salario Invalido!')
else:
    if salario_funcionario <= 280:
        print(
            f'Seu salario que é {salario_funcionario} ganhou 20% e '
            f'ficou {aumenta_salario(salario_funcionario, 0.20)}')

    elif salario_funcionario >= 280 and salario_funcionario <= 700:
        print(f'Seu salario que é {salario_funcionario} ganhou 15% e '
              f'ficou{aumenta_salario(salario_funcionario, 0.15)}')

    elif salario_funcionario > 700 and salario_funcionario <= 1500:
        print(f'Seu salario que é {salario_funcionario} ganhou 10% e'
              f' ficou {aumenta_salario(salario_funcionario, 0.10)} ')
    elif salario_funcionario > 1500:
        print(f'Seu salario é {salario_funcionario} ganhou 5% e'
              f'ficou {aumenta_salario(salario_funcionario, 0.05)}')
