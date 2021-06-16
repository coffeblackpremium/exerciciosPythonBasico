"""
012)Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

"""
print(40 * '#', 'PROGRAMA DA TABUADA', 40 * '#')
numero1 = float(input('Digite um número para saber a Tabuada'))
taboada = [print(f'{numero1} X {vezes} = {vezes*numero1}') for vezes in range(11)]
