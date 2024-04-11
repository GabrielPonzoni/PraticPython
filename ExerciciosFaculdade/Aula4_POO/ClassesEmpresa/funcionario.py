# Possui um nome, um endereço e uma calculadora.
# ◦ Crie um construtor que recebe os parâmetros para inicializar todos os atributos.
# ◦ Crie os métodos de acesso dos atributos desta classe (get e set).
# ◦ Crie os métodos soma, subtrai, multiplica, divide,
# eleva_ao_quadrado e eleva_ao_cubo. Cada método destes deve chamar o
# método correspondente da calculadora, retornando o valor obtido na operação.
# ◦ Crie um método chamado imprime_info, que não recebe parâmetros de
# entrada e imprime na tela as informações da classe, inclusive da calculadora
# (sem as operações, apenas os atributos).
from calculadora import Calculadora

class FuncionarioCaixa:
    """
    Classe que representa um cadastro de funcionario.
    
    Attributes:
        nome (str): Nome do funcionario.
        endereco (str): Endereco do funcionario.
        calculadora (Calculadora): Instância de uma calculadora associada ao funcionário.
    
    Methods:
        soma()
        subtrai()
        multiplica()
        divide()
        eleva_ao_quadrado()
        eleva_ao_cubo()
        imprime_info()
    """
    def __init__(self, nome: str, endereco: str, calculadora: Calculadora):
        self.__nome = nome
        self.__endereco = endereco
        self.__calculadora = calculadora
    
    # get e setter do parametro __nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    # get e setter do parametro __endereco
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    # get e setter do atributo __calculadora 
    @property
    def calculadora(self):
        return self.__calculadora
    
    @calculadora.setter
    def calculadora(self, calculadora):
        self.__calculadora = calculadora
    
    def soma(self, valor_1: float, valor_2: float) -> float:
        """ 
        Metodo que usa os metodos da classe calculadora para somar.
        
        Parameters:
        valor_1 (float): Primeiro valor enviado a calculadora.
        valor_2 (float): Segundo valor enviado a calculadora.
        
        Return: 
        float: Resultado da operacao.
        """
        return self.calculadora.soma(valor_1, valor_2)
    
    def subtrai(self, valor_1: float, valor_2: float) -> float:
        """
        Metodo usa os metodos da classe calculadora para subtrair.
        
        Parameters:
        valor_1 (float): Primeiro valor enviado a calculadora.
        valor_2 (float): Segundo valor enviado a calculadora.
        
        Return:
        float: Resultado da operacao.
        """
        return self.calculadora.subtrai(valor_1, valor_2)
    
    def multiplica(self, valor_1: float, valor_2: float) -> float:
        """
        Metodo o qual utiliza os metodo multiplica() da classe calculadora.
        
        Parameters:
        valor_1 (float): Primeiro valor enviado a calculadora.
        valor_2 (float): Segundo valor enviado a calculadora.
        
        Return:
        float: Resultado da operacao.
        """
        return self.calculadora.multiplica(valor_1, valor_2)
    
    def divide(self, valor_1: float, valor_2: float) -> float:
        """
        Metodo o qual utiliza os metodos divide() da classe calculadora.
        
        Parameters:
        valor_1 (float): Primeiro valor enviado a calculadora.
        valor_2 (float): Segundo valor enviado a calculadora.
        
        Return:
        float: Resultado da operacao.
        """
        return self.calculadora.divide(valor_1, valor_2)
    
    def eleva_ao_quadrado(self, valor: int) -> int:
        """
        Metodo o qual utiliza os metodo eleva_ao_quadrado() da classe calculadora.
        
        Parameters:
        valor (int): Primeiro valor enviado a calculadora.
        
        Return:
        int: Resultado da operacao.
        """
        return self.calculadora.eleva_ao_quadrado(valor)
    
    def eleva_ao_cubo(self, valor: int) -> int:
        """
        Metodo o qual utiliza os metodo eleva_ao_cubo() da classe calculadora.
        
        Parameters:
        valor (int): Primeiro valor enviado a calculadora.
        
        Return:
        int: Resultado da operacao.
        """
        return self.calculadora.eleva_ao_cubo(valor)
    
    def imprime_info(self):
        print("==== Dados do Funcionário ====")
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}")
        self.calculadora.imprime_info()
        print("==============================")