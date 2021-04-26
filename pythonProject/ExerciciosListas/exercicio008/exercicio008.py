"""
008)Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""
idade_pessoa = [int(input('Digite a sua idade: ')) for nova_idade in range(5)]
altura_pessoa = [float(input('Digite a sua altura: ')) for nova_altura in range(5)]
print(idade_pessoa.reverse(), altura_pessoa.reverse())
