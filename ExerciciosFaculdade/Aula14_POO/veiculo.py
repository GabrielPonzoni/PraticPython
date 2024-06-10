class Veiculo:
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str) -> None:
        self.__ano = ano
        self.__peso = peso
        self.__tanque = tanque
        self.__modelo = modelo
    
    # get e setter __ano
    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
        
    # get e setter __peso
    @property
    def peso(self) -> int:
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
      
    # get e setter __tanque
    @property
    def tanque(self) -> float:
        return self.__tanque
    
    @tanque.setter
    def tanque(self, tanque):
        self.__tanque = tanque
    
    # get e setter __modelo
    @property
    def modelo(self) -> str:
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
        
    def info(self):
        print(f'--- Info Veículo ---')
        print(f'Ano: {self.ano}')
        print(f'Peso: {self.peso}')
        print(f'Tanque: {self.tanque}')
        print(f'Modelo: {self.modelo}')
        