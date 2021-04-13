"""
002)Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
login, senha = input('Digite o seu Login: '), input('Digite sua Senha: ')
while login == senha:
    print('Senha e Login são iguais, favor Digite novamente: ')
    login, senha = input('Digite o seu Login: '), input('Digite sua Senha: ')
