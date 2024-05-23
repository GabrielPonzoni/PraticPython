class ItemCardapio:
    def __init__(self, nome: str, preco: float) -> None:
        self.__nome = nome
        self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco