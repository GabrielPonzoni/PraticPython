import os

restaurantes = [{'nome': 'Bella Gula', 'categoria': 'Brasileira', 'ativo': False},
                {'nome': 'Fratello Tutti', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Cia das Pizzas', 'categoria': 'Pizzas', 'ativo': True},
                {'nome': 'Koh pee pee', 'categoria': 'Tailandesa', 'ativo': False}]

def exibir_nome_do_programa():
    '''
    Exibe o titulo principal do programa: Sabor Express.
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    ''' Exibe as informações principais do programa.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Funcao que apenas finaliza o app.'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    ''' Funcao que volta ao menu princiapal, no caso chama a main.'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    ''' Opcao que retorna a main, informando que o usuário informou input inválido.'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Funcao que exibe um minicabecalho para cada opcao específica do menu.'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''
    Funcao para cadastrar novos restaurantes no dicioário restaurantes.
    
    Inputs:
    nome_do_restaurante (str): Coleta o nome do restaurante para cadastro
    categoria_do_restaurante (str): Armazena a categoria do restaurante
    
    Output:
    dicionario_novo_restauramte: Popula o nome, a categoria e o ativo para o dicionário restaurantes.
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a cadegoria do restaurante {nome_do_restaurante}: ')
    dicionario_novo_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dicionario_novo_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista as informacoes dos restaurantes de forma formatada '''
    exibir_subtitulo('Listando restaurantes')

    cabecalho = f'  {"Nome:".ljust(20)} | {"Categoria:".ljust(20)} | Status:'
    
    print(cabecalho)
    print(f'-' * (len(cabecalho)))
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}')

    voltar_ao_menu_principal()
    
def alternar_valor_restaurante():
    ''' Alterna o valor de True para False do restaurante ou False para True, substituindo os termos bool para 'Ativo' ou 'Desativado'.'''
    exibir_subtitulo('Alterando estado do restaurante')

    restaurante_encontrado = False
    nome_restaurante = input('Informe o nome do restaurante que deseja ativar ou desativar: ')
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']         # troca o valor True ou False do restaurante 
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    
    voltar_ao_menu_principal()
    
def escolher_opcao():
    ''' Funcao que valida a entrada do usuário para o menu e chama a funcao correta para cada opcao do menu.'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_valor_restaurante()        
            case 4:
                finalizar_app()
            case _:
                print(f'A resposta {opcao_escolhida} não aestá dentro das opções!')
    except:
        opcao_invalida()
        
def main():
    ''' Função principal que inicia o programa.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()