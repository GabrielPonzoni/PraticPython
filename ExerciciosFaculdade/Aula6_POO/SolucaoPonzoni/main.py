from cabecalho import Cabecalho
from usuario import Usuario
import os

def menu(cabecalho_mensagem):
    while True:
        cabecalho_mensagem.cabecalho_principal()
        print("1- Ver acervo")
        print("2- Solicitar emprestimo")
        print("3- Solicitar reserva")
        print("4- Devolver livro")
        print("5- Sair do programa")
        resposta_do_menu = input()
        match resposta_do_menu:
            case '1':
                print("VENDO ACERVO")
                break
            case '2':
                print("VENDO EMPRESTIMO")
                break
            case '3':
                print("VENDO RESERVAS")
                break
            case '4':
                print("VENDO DEVOLUCAO")
                break
            case '5':
                print(">>> SAINDO")
                break
            case _ :
                print("OPCAO INVALIDA")
                input()
    
def main():
    cabecalho_mensagem = Cabecalho()
    cabecalho_mensagem.cabecalho_principal()
    
    nome_usuario = input("Qual seu nome? ")
    user = Usuario(nome_usuario, 0)
    
    cabecalho_mensagem.cabecalho_principal()
    print(f"Seja bem vindo a biblioteca {user.nome}!")
    while True:
        resposta_menu_sair = input("Deseja ver o menu ou sair da biblioteca?\n [S]Sair\n [M]Menu\nResposta: ")
        if resposta_menu_sair == 'M':
            menu(cabecalho_mensagem)
            break
        elif resposta_menu_sair == 'S':
            cabecalho_mensagem.cabecalho_principal()
            print(f"Tchau tchau {user.nome}")
            break
        else:
            input(f"Não entendi a opçao escolhida! Tente novamente...")
            cabecalho_mensagem.cabecalho_principal()

if __name__ == '__main__':
    main()