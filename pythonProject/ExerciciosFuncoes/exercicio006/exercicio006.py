"""
006)Faça um
    programa que converta da
    notação de 24 horas para a notação de 12 horas.
    Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
    A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
    uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
    como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um
    parâmetro formal para registrar se é A.M. ou P.M.
    Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""

def converter_notacao_horario(horas, minutos):
    if horas > 12:
        print(f'São: {horas - 12}:{minutos} P.M')
    else:
        print(f'São: {horas}:{minutos} A.M')

    return

while True:
    print(30 * '#','Digite -1 para sair', 30 * '#')
    horario_usuario = int(input('\nDigite as Horas: '))
    if horario_usuario < 0:
        break
    minutos_usuario = int(input('Digite os Minutos: '))
    converter_notacao_horario(horario_usuario,minutos_usuario)
