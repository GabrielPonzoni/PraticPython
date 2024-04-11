# Classe Calculadora:
# ◦ Uma calculadora possui uma memória e uma cor.
# ◦ Quando uma calculadora é criada, a memória deve ser inicializada com 0 e a cor
# deve ser recebida por parâmetro (construtor).
# ◦ Crie os métodos de acesso para os atributos da classe (get e set).
# ◦ Crie os métodos: soma, subtrai, multiplica e divide. Todos recebem dois
# valores (float) por parâmetro e retornam o valor da operação realizada.
# ◦ Crie os métodos eleva_ao_quadrado e eleva_ao_cubo. Ambos recebem
# apenas um valor (int) e retornam o valor da operação realizada.
# ◦ Crie um método imprime_info, que não recebe parâmetros e simplesmente
# imprime as informações da calculadora de maneira legível e organizada.

class Calculadora:
    """
    Classe que representa uma calculadora capaz de realizar operações matemáticas básicas.

    Attributes:
        cor (str): Cor da calculadora.
        memoria (int, opcional): Valor da memória da calculadora. Padrão é 0.

    Methods:
        soma(valor_1, valor_2): Retorna a soma de dois valores.
        subtrai(valor_1, valor_2): Retorna a subtração de dois valores.
        multiplica(valor_1, valor_2): Retorna a multiplicação de dois valores.
        divide(valor_1, valor_2): Retorna a divisão de dois valores.
        eleva_ao_quadrado(valor): Retorna o valor informado elevado ao quadrado.
        eleva_ao_cubo(valor): Retorna o valor informado elevado ao cubo.
        imprime_info(): Imprime informações sobre a calculadora, incluindo a cor e a memória.
    """
    def __init__(self, cor: str, memoria=0):
        self.__cor = cor
        self.__memoria = memoria

    # get e setter parâmetro privado: __memoria
    @property
    def memoria(self):
        return self.__memoria 
    
    @memoria.setter
    def memoria(self, memoria):
        self.__memoria = memoria
    
    #get e setter parâmetro privado: __cor
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
    
    # metodos
    
    def soma(self, valor_1: float, valor_2: float) -> float:
        """
        Metodo que calcula a soma de dois valores.
        
        Parameters:
        valor_1 (float): Primeira parcela a ser somada.
        valor_2 (float): Segundo parecla a ser somada.
        
        Return:
        float: O retorno soma.
        """
        return valor_1 + valor_2
    
    def subtrai(self, valor_1: float, valor_2: float) -> float:
        """
        Metodo que calcula a subtracao de dois valores.
        
        Parameters:
        valor_1 (float): Valor minuendo
        valor_2 (float): Valor subtraendo
        
        Return:
        float: Retorna o resto da operacao.
        """
        return valor_1 - valor_2
    
    def multiplica(self, valor_1: float, valor_2: float) -> float:
        """
        Metodo que calcula a mutiplicacao 
        
        Parameters:
        valor_1 (float): Primeiro fator
        valor_2 (float): Segundo fator
        
        Return:
        float: Retorna o produto
        """
        return valor_1 * valor_2
    
    def divide(self, valor_1: float, valor_2: float) -> float:
        """
        Metodo que divide dois valores informados
        
        Parameters:
        valor_1 (float): Dividendo 
        valor_2 (float): Divisor
        
        Return:
        float: Retorna o quociente
        """
        if valor_2 > 0:
            return valor_1 / valor_2
        return 0
    
    def eleva_ao_quadrado(self, valor: int) -> int:
        """
        Metodo que calcula o valor informado ao quadrado
        
        Parameters:
        valor (int): Um numero inteiro
        
        Return:
        int: Resultado do valor ao quadrado
        """
        return valor ** 2
    
    def eleva_ao_cubo(self, valor: int) -> int:
        """
        Metodo que calcula o valor informado ao cubo
        
        Parameters:
        valor (int): Um numero inteiro
        
        Return:
        int: Resultado do valor ao cubo 
        """
        return valor ** 3
    
    def imprime_info(self):
        """
        Metodo que imprime ao usuario informacoes sobre a calculadora
        
        Return:
        print: A memoria e a cor da calculadora
        """
        print("== Caracteristicas da calculadora ==")
        print(f"Memória: {self.memoria}\nCor: {self.cor}")
        print("====================================")
        