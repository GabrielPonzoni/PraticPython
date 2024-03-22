# Faça um programa que leia um nome de usuário e a sua senha 
# e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome_user = input('Informe o nome do usuário: ')

while True:
    senha_user = input('Informe a senha do usuário (diferente do nome de usuário): ')

    if senha_user == nome_user:
        print('Senha igual ao nome! tente novamente')
    
    else:
        print(f'Senha salva com sucesso! Bem-vindo {nome_user}')
        break

