from veiculo import Veiculo

class Terrestre(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str, quantidade_rodas: int, quantidade_portas: int) -> None:
        super().__init__(ano, peso, tanque, modelo)
        self.__quantidade_rodas = quantidade_rodas
        self.__quantidade_portas = quantidade_portas