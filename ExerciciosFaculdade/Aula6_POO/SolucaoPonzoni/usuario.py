class Usuario:
    def __init__(self, nome: str, quantidade_livros: int):
        self.__nome = nome
        self.__quantidade_livros = quantidade_livros
        
    #get e setter __nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    #get e setter __quantidade_livros
    @property
    def quantidade_livros(self):
        return self.__quantidade_livros
    
    @quantidade_livros.setter
    def quantidade_livros(self, quantidade_livros):
        self.__quantidade_livros = quantidade_livros
        
    