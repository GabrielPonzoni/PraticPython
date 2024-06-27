from atleta import Atleta
class Nadador(Atleta):
    def __init__(self, nome: str, idade: int, categoria: str) -> None:
        super().__init__(nome, idade)
        self.__categoria = categoria
    
    @property
    def categoria(self) -> str:
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria: str):
        self.__categoria = categoria
    
    def imprime_info(self) -> None:
        super().imprime_info()
        print(f"A categoria do nadador {self.nome} é {self.categoria}")
        
        