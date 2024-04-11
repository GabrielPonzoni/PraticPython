# Crie o diagrama de classes para as classes descritas abaixo. Em seguida,
# implemente as classes do projeto.
# >>>>> 1. Classe Calculadora:
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
# >>>>>> 2. Classe FuncionarioCaixa:
# ◦ Possui um nome, um endereço e uma calculadora.
# ◦ Crie um construtor que recebe os parâmetros para inicializar todos os atributos.
# ◦ Crie os métodos de acesso dos atributos desta classe (get e set).
# ◦ Crie os métodos soma, subtrai, multiplica, divide,
# eleva_ao_quadrado e eleva_ao_cubo. Cada método destes deve chamar o
# método correspondente da calculadora, retornando o valor obtido na operação.
# ◦ Crie um método chamado imprime_info, que não recebe parâmetros de
# entrada e imprime na tela as informações da classe, inclusive da calculadora
# (sem as operações, apenas os atributos).
# >>>>>> 3. Classe Empresa:
# ◦ Uma empresa tem um nome e dois funcionários do caixa.
# ◦ Crie um construtor que recebe todos os parâmetros para inicializar os atributos.
# ◦ Crie os métodos de acesso dos atributos desta classe (get e set).
# ◦ Crie um método imprime_info, que imprime as informações da classe.
# 4. Na função main:
# • Crie um objeto do tipo FuncionarioCaixa, chamado funcionario. Tudo que
# for necessário para criar este objeto, deve ser solicitado para o usuário.
# • Imprima o resultado das operações: 2+2, 5-4, 2x3, 6/3, 7+2, 8x3. As operações
# devem ser feitas através da calculadora do objeto funcionário criado.
# • Neste método, crie um objeto do tipo Empresa chamado empresa1, com nome
# solicitado para o usuário, com o funcionário criado anteriormente e um novo
# funcionário que deve ser criado. Tudo que for necessário para criar esta empresa
# (que já não tenha sido criado) deve ser solicitado para o usuário.
# • Imprima as informações desta empresa.

class Calculadora:
    def __init__(self, cor, memoria = 0):
        self.__memoria = memoria
        self.__cor = cor
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
        print('== Informacoes Calculadora ==')
        print(f'Cor da calculadora: {self.cor}')
        print(f'Memoria da calculadora: {self.memoria}')

class FuncionarioCaixa:
    def __init__(self, nome, endereco, calculadora):
        self.__nome = nome
        self.__endereco = endereco
        self.__calculadora = calculadora
    
    # get e setter __nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    # get e setter __endereco
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    # get e setter __calculadora
    @property
    def calculadora(self):
        return self.__calculadora
    
    @calculadora.setter
    def calculadora(self, calculadora):
        self.__calculadora = calculadora
    
    def funcionarioSoma(self, valor1:float, valor2:float):
        return self.calculadora.adicao(valor1, valor2)
    
    def funcionarioSub(self, valor1:float, valor2:float):
        return self.calculadora.subtracao(valor1, valor2)
    
    def funcionarioMult(self, valor1:float, valor2:float):
        return self.calculadora.multiplicacao(valor1, valor2)

    def funcionarioDivi(self, valor1:float, valor2:float):
        return self.calculadora.divisao(valor1, valor2)
    
    def imprime_info(self):
        print('==== Informacoes Funcionario =====')
        print(f'Nome: {self.nome}')
        print(f'Endereco: {self.endereco}')
        print(f'Calculadora: {self.calculadora}')
        print(self.calculadora.imprime_info())
    
class Empresa:
    def __init__(self, nome_empresa, funcionario_empresa, funcionario_empresa2):
        self.__nome_empresa = nome_empresa
        self.__funcionario_empresa = funcionario_empresa
        self.__funcionario_empresa2 = funcionario_empresa2
    
    # get e setter de __nome_empresa
    @property
    def nome_empresa(self):
        return self.__nome_empresa
    
    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        self.__nome_empresa = nome_empresa
    
    # get e setter de __funcionario_empresa
    @property
    def funcionario_empresa(self):
        return self.__funcionario_empresa
    
    @funcionario_empresa.setter
    def funcionario_empresa(self, funcionario_empresa):
        self.__funcionario_empresa = funcionario_empresa
    
    # get e setter de __funcionario_empresa2
    @property
    def funcionario_empresa2(self):
        return self.__funcionario_empresa2
    
    @funcionario_empresa2.setter
    def funcionario_empresa2(self, funcionario_empresa2):
        self.__funcionario_empresa2 = funcionario_empresa2 
    
def main():
    calculadora_funcionario = Calculadora(cor = 'Azul')
    
    nome_funcionario = input('Nome: ')
    endereco_funcionario = input('Endereco: ')
    
    funcioanrio = FuncionarioCaixa(nome_funcionario, endereco_funcionario, calculadora_funcionario)
    while True:
        mensagem_terminal = 'Qual calculo queres fazer?\n"+" p/ soma\n"-" p/ subtrair\n"x" p/ multiplicacao:'
        resposta_operacao = input(mensagem_terminal)
        
        match resposta_operacao:
            case '+':
                valor_1 = float(input(f'{funcioanrio.nome} qual o primeiro valor da soma: '))
                valor_2 = float(input(f'{funcioanrio.nome} informe o segundo valor da soma: '))
            case '-':
                valor_1 = float(input(f'{funcioanrio.nome} qual o primeiro valor da subtracao: '))
                valor_2 = float(input(f'{funcioanrio.nome} informe o segundo valor da subtracao: '))
            case 'x':
                valor_1 = float(input(f'{funcioanrio.nome} qual o primeiro valor da multiplicacao: '))
                valor_2 = float(input(f'{funcioanrio.nome} informe o segundo valor da multiplicacao: '))
            case _:
                print('Valor invalido')
        
        break

    # resultado_soma = funcioanrio.funcionarioSoma(valor_1, valor_2)
    # resultado_subtracao = funcioanrio.funcionarioSub(valor_1, valor_2)
    # resultado_multiplicacao = funcioanrio.funcionarioMult(valor_1, valor_2)
    
    # print(f'{valor_1} + {valor_2} = {resultado_soma}')
    # print(f'{valor_1} - {valor_2} = {resultado_subtracao}')
    # print(f'{valor_1} x {valor_2} = {resultado_multiplicacao}')
    

if __name__ == '__main__':
    main()