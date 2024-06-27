from data import Data
class Competicao:
    def __init__(self, nome, data: Data) -> None:
        self.__nome = nome
        self.__data = data
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def data(self) -> Data:
        return self.__data
    
    @data.setter
    def data(self, data: Data):
        self.__data = data
        
    def imprime_data(self):
        print(f"A competição será em: ", end = "")
        self.data.imprime_data()