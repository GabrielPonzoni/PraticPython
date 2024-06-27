from atleta import Atleta
from competicao import Competicao

class Corredor(Atleta):
    def __init__(self, nome: str, idade: int, peso: float, competicao: Competicao) -> None:
        super().__init__(nome, idade)
        self.__peso = peso
        self.__competicao = competicao
    
    @property
    def peso(self) -> float:
        return self.__peso
    
    @peso.setter
    def peso(self, peso: float):
        self.__peso = peso
    
    @property
    def competicao(self) -> Competicao:
        return self.__competicao
    
    @competicao.setter
    def competicao(self, competicao: Competicao):
        self.__competicao = competicao
    
    def imprime_competicao(self):
        print(f"O corredor {self.nome} está participando da competição {self.competicao.nome}")
        self.competicao.imprime_data()
        
    def imprime_info(self) -> None:
        super().imprime_info()
        print(f"Corredor: {self.nome}")
        print(f"Peso: {self.peso}")
        print(f"Idade: {self.idade}")
        self.imprime_competicao()