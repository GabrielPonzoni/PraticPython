class Atleta:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    # get e setter __nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    # get e setter __idade
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    def imprime_info(self) -> None:
        print(f">>> Atleta {self.nome} com idade de {self.idade}")