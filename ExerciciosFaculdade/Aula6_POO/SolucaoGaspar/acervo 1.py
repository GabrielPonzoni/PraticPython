from random import randrange

class Exemplar:

    def __init__(self, rotulo:str, disponivel:bool):
        self.__disponivel = disponivel
        self.__rotulo = rotulo

    @property
    def rotulo(self) -> str:
        return self.__rotulo

    @rotulo.setter
    def rotulo(self, rotulo) -> None:
        self.__rotulo = rotulo

    @property
    def disponivel(self) -> bool:
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel) -> None:
        self.__disponivel = disponivel

    def verifica_disponibilidade(self) -> bool:
        if (self.__disponivel == True):
            print(f'Item {self.__rotulo} está disponível.')
        else:
            print(f'Item {self.__rotulo} já está emprestado.')

    def retira_exemplar(self) -> None:
        self.__disponivel = False

    def devolve_exemplar(self) -> None:
        self.__disponivel = True

    def remove_exemplar(self) -> None:
        pass

class Obra:

    def __init__(self, name:str):
        self.__name = name
        # self.__lista_de_exemplares: list(Exemplar) = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def lista_de_exemplares(self) -> list:
        return self.__lista_de_exemplares

    # @lista_de_exemplares.setter
    # def lista_de_exemplares(self, lista:[]) -> None:
    #     self.__lista_de_exemplares = lista

    def adiciona_exemplar(self, livro:Exemplar) -> None: 
        self.__lista_de_exemplares.append(livro)

    def adiciona_exemplar_c_input(self, n_de_exemplares: int) -> None:
        for n in range(n_de_exemplares):
            rotulo = '0' + str(n+1)
            self.adiciona_exemplar(Exemplar(rotulo, True))

    # exibe tabela com rótulos e disponibilidade de todos os seus exemplares
    def mostra_exemplares(self):
        print('')
        print(f'Obra: {self.__name}:')
        print(f'Rótulo\tDisponível?')
        for livro in self.__lista_de_exemplares:
            print(f'{livro.rotulo}\t{livro.disponivel}')

class Acervo:

    def __init__(self, name:str):
        self.__name = name
        # self.__lista_de_obras: list(Obra) = []
        # self.__lista_de_usuarios: list(Usuario) = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def lista_de_obras(self) -> list:
        return self.__lista_de_obras

    # @lista_de_obras.setter
    # def lista_de_obras(self, lista:[]) -> None:
    #     self.__lista_de_obras = lista

    def adiciona_obra(self, obra:Obra) -> None:
        self.__lista_de_obras.append(obra)

    # Este método permite ao usuário adicionar obras em tempo de execução.abs
    # Exigirá também que informe quantos exemplares serão gerados.
    def adiciona_obra_c_input(self) -> None:
        print('')
        print('*** CADASTRAR NOVA OBRA ***\n')
        
        # validação do input do usuário para o nome da obra:
        input_valido: bool = False
        while(input_valido == False):
            print('\tDigite o nome da obra a ser cadastrada no acervo (sem aspas):\n')

            nome_da_nova_obra = input()
            if ((nome_da_nova_obra == '') or (nome_da_nova_obra == None)):
                print("Nome inválido para obra.\n")
            else:
                nova_obra = Obra(nome_da_nova_obra)
                self.adiciona_obra(nova_obra)

                print(f'A obra \'{nome_da_nova_obra.upper()}\' foi cadastrada.\n')
                input_valido = True

        print('Quantos exemplares desta obra serão disponibilizados?')

        # validação do input do usuário para o número de exemplares da obra:
        input_valido = False
        while(input_valido == False):
            print('\tDigite um número inteiro:')
            
            try:
                numero_de_exemplares = int(input())
                if (isinstance(numero_de_exemplares, int)) and (numero_de_exemplares != 0):
                    nova_obra.adiciona_exemplar_c_input(numero_de_exemplares)
                    print(f'{numero_de_exemplares} exemplares foram adicionados à estante.\n')
                    input_valido = True
                else:
                    print('Número inválido de exemplares.\n')
            except ValueError:
                print('Número inválido de exemplares.\n')

    # Exibe tabela com o catálogo de obras do acervo
    def mostra_obras(self):
        print('')
        print(f'Acervo de {self.__name}:')
        print(f'=================================')
        for obra in self.__lista_de_obras:
            print(f'\t{obra.name}')

    # Este método permite ao usuário REMOVER obras em tempo de execução.
    # Os exemplares da obra serão removidos automaticamente.
    def remove_obra_c_input(self) -> None:
        print('')
        print('*** REMOVER OBRA ***')
        print('')
        print('\tDigite o nome da obra a REMOVER (sem aspas).')
        print('\tAbaixo, lista de obras existentes no acervo atualmente:')
        self.mostra_obras()
        print('')
        nome_da_obra = input()
        
        # procura obra com mesmo nome do input e remove-a, se ela existir
        obra_encontrada: bool = False
        for obra in self.lista_de_obras:
            if (obra.name == nome_da_obra):
                obra_encontrada = True
                print(f'\tObra \'{obra.name}\' foi removida do acervo.')
                self.lista_de_obras.remove(obra)
                break
        if (obra_encontrada == False):
            print('Obra não encontrada no acervo.')

    def menu_principal(self) -> None:
        print(f'BEM-VINDO(A) AO ACERVO DE {self.__name}')
        print(f'=============================================')
        print(f'Escolha a opção desejada:\n')

class Usuario:

    def __init__(self, name:str):
        self.__name = name
        # self.__itens_possuidos: list(Exemplar)
        # self.__itens_reservados: list(Exemplar)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def itens_possuidos(self) -> list:
        return self.__itens_possuidos

    # @itens_possuidos.setter
    # def itens_possuidos(self, lista:[]) -> None:
    #     self.__lista_de_obras = lista
        
def main():

    # gera acervo, obras e exemplares
    biblioteca_Unisinos = Acervo('Biblioteca da Unisinos')

    # obs: estas obras não possuem um identificador,
    # mas possuem um atributo 'string' declarado na sua construção.
    biblioteca_Unisinos.adiciona_obra(Obra('O Pequeno Príncipe'))
    biblioteca_Unisinos.adiciona_obra(Obra('Dom Casmurro'))
    biblioteca_Unisinos.adiciona_obra(Obra('Tudo sobre Fortran 77'))
    biblioteca_Unisinos.adiciona_obra(Obra('Audiovisualidades'))
    biblioteca_Unisinos.adiciona_obra(Obra('Roteiros audiovisuais'))
    biblioteca_Unisinos.adiciona_obra(Obra('Crie seu formigueiro'))
    biblioteca_Unisinos.adiciona_obra(Obra('Clássicos da culinária francesa'))
    biblioteca_Unisinos.adiciona_obra(Obra('中文词典'))

    # gera um número de 1 a 4 exemplares aleatoriamente para cada obra do acervo
    for obra in biblioteca_Unisinos.lista_de_obras:
        for n in range(randrange(1,5,1)):
            rotulo = '0' + str(n+1)
            obra.adiciona_exemplar(Exemplar(rotulo, True))

    # gera um usuário
    # usuario_Jarbas = Usuario("Jarbas")

    biblioteca_Unisinos.mostra_obras()
    biblioteca_Unisinos.adiciona_obra_c_input()
    biblioteca_Unisinos.mostra_obras()
    biblioteca_Unisinos.lista_de_obras[3].mostra_exemplares()

main()