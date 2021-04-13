"""
003)Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    nome = input('Digite o Seu Nome: ')
    idade = int(input('Digite a sua idade: '))
    salario = float(input('Digite o seu Salario: '))
    sexo = input('Digite seu Sexo (f) Feminino, (m) masculino: ')
    estado_civil = input('Digite seu Estado Cívil: s, c, v, d: ')

    if len(nome) < 3:
        print('Nome Invalido. Digite novamente')
        continue
    elif idade < 0 and idade > 150:
        print(f'Idade Invalido')
        continue
    elif salario < 0:
        print('Salario Invalido')
    elif sexo.lower() != 'f' or sexo.lower() != 'm':
        print('Sexo Invalido!')
        continue
    elif estado_civil.lower() != 's' or estado_civil.lower() != 'c' or estado_civil.lower() != 'v' or estado_civil.lower() != 'd':
        print('Estado Civil invalido. Por favor digitar as Abreviações!')
        continue
    else:
        break