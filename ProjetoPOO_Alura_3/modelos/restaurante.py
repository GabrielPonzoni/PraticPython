from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.__nome = nome.title()
        self.__categoria = categoria.upper()
        self.__ativo = False
        self.__avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.__nome} | {self.__categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.__nome.ljust(25)} | {restaurante.__categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self.__ativo else '☐'
    
    def alternar_estado(self):
        self.__ativo = not self.__ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self.__avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self.__avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self.__avaliacao)
        quantidade_de_notas = len(self.__avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media