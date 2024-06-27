class Data:
    def __init__(self, dia: int, mes: int, ano: int) -> None:
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    #get e setter __dia
    @property
    def dia(self) -> int:
        return self.__dia
    
    @dia.setter
    def dia(self, dia: int):
        self.__mes = dia
        
    #get e setter __mes
    @property
    def mes(self) -> int:
        return self.__mes

    @mes.setter
    def mes(self, mes:int):
        self.__mes = mes
            
    #get e setter __ano
    @property
    def ano(self) -> int:
        return self.__ano
        
    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano
        
    def imprime_data(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
    