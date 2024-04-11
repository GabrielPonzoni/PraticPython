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
    def __init__(self, cor, memoria = 0):
        self.__memoria = memoria
        self.__cor = cor

    # def get_memoria(self):
    #     return self.__memoria
    
    # def set_memoria(self, memoria):
    #     self.__memoria = memoria
    
    # def get_cor(self):
    #     return self.__cor
    
    # def set_cor(self, cor):
    #     self.__cor = cor

    @property 
    def memoria(self):
        return self.__memoria
    
    @memoria.setter
    def memoria(self, memoria):
        self.__memoria = memoria
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def adicao(self, valor1:float, valor2:float):
        resultado = valor1 + valor2
        return resultado
    
    def subtracao(self, valor1:float, valor2:float):
        resultado = valor1 - valor2
        return resultado
    
    def multiplicacao(self, valor1:float, valor2:float):
        resultado = valor1 * valor2
        return resultado
    
    def divisao(self, valor1:float, valor2:float):
        resultado = valor1 / valor2
        return resultado
    
    def eleva_ao_quadrado(self, valor1:int):
        valor1_ao_quadrado = valor1 ** 2
        return valor1_ao_quadrado
    
    def eleva_ao_cubo(self, valor1:int):
        valor1_ao_cubo = valor1 ** 3
        return valor1_ao_cubo
    
    def imprime_info(self):
        print(f'Cor da calculadora: {self.__cor}')
        print(f'Memoria da calculadora: {self.__memoria}')

def main():
    Calculadora1 = Calculadora("Azul")

    valor1 = float(input('Informe o primeiro valor : '))
    valor2 = float(input('Informe o segundo valor : '))

    valor3 = int(input('Informe o numero que vai ser elevado ao cubo e ao quadrado: '))

    resultado_adicao = Calculadora1.adicao(valor1,valor2)
    
    print(f'{valor1} + {valor2} = {resultado_adicao}')
    print(f'{valor1} - {valor2} = {Calculadora1.subtracao(valor1,valor2)}')
    print(f'{valor1} : {valor2} = {Calculadora1.divisao(valor1,valor2)}')
    print(f'{valor3}² = {Calculadora1.eleva_ao_quadrado(valor3)}')
    print(f'{valor3}³ = {Calculadora1.eleva_ao_cubo(valor3)}')

if __name__ == '__main__':
    main()