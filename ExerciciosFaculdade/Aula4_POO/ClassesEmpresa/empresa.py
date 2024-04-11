# Classe Empresa:
# ◦ Uma empresa tem um nome e dois funcionários do caixa.
# ◦ Crie um construtor que recebe todos os parâmetros para inicializar os atributos.
# ◦ Crie os métodos de acesso dos atributos desta classe (get e set).
# ◦ Crie um método imprime_info, que imprime as informações da classe.
from funcionario import FuncionarioCaixa

class Empresa:
    def __init__(self, nome_empresa: str, funcionario1: FuncionarioCaixa, funcionario2: FuncionarioCaixa):
        self.__nome_empresa = nome_empresa
        self.__funcionario1 = funcionario1
        self.__funcionario2 = funcionario2
    
    #get e setter de __nome_empresa    
    @property
    def nome_empresa(self):
        return self.__nome_empresa
    
    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        self.__nome_empresa = nome_empresa
        
    #get e setter de __funcionario1
    @property
    def funcionario1(self):
        return self.__funcionario1
    
    @funcionario1.setter
    def funcionario1(self, funcionario1):
        self.__funcionario1 = funcionario1
    
    #get e setter de __funcionario2
    @property
    def funcionario2(self):
        return self.__funcionario2
    
    @funcionario2.setter
    def funcionario2(self, funcionario2):
        self.__funcionario2 = funcionario2
    
    def imprime_info(self):
        print("==== Dados da Empresa ====")
        print(f"Dados do funcionário {self.funcionario1.nome}:")
        self.funcionario1.imprime_info()
        print(f"Dados do funcionário {self.funcionario2.nome}:")
        self.funcionario2.imprime_info()
    
