# Crie um objeto do tipo FuncionarioCaixa, chamado funcionario. Tudo que
# for necessário para criar este objeto, deve ser solicitado para o usuário.
# • Imprima o resultado das operações: 2+2, 5-4, 2x3, 6/3, 7+2, 8x3. As operações
# devem ser feitas através da calculadora do objeto funcionário criado.
# • Neste método, crie um objeto do tipo Empresa chamado empresa1, com nome
# solicitado para o usuário, com o funcionário criado anteriormente e um novo
# funcionário que deve ser criado. Tudo que for necessário para criar esta empresa
# (que já não tenha sido criado) deve ser solicitado para o usuário.
# • Imprima as informações desta empresa
from calculadora import Calculadora
from funcionario import FuncionarioCaixa
from empresa import Empresa


def main():
    calculadora_1 = Calculadora("Lilás", 400)
    calculadora_2 = Calculadora("Azul", 500)

    funcionario_1 = FuncionarioCaixa(input("Informe o nome do primeiro funcionário: "), input("Endereço do funcionário: "), calculadora_1)
    funcionario_2 = FuncionarioCaixa(input("Informe o nome do segundo funcionário: "), input("Endereço do funcionário: "), calculadora_2)

    empresa = Empresa(input("Informe o nome da empresa: "), funcionario_1, funcionario_2)
    empresa.imprime_info()

    print(f"\nOperações realizadas pelo funcionário: {funcionario_1.nome}")
    print(f"2 + 2: {funcionario_1.soma(2.0, 2.0)}")
    print(f"5 - 4: {funcionario_1.subtrai(5.0, 4.0)}")
    print(f"2 x 3: {funcionario_1.multiplica(2.0, 3.0)}")
    print(f"\nOperações realizadas pelo funcionário: {funcionario_2.nome}")
    print(f"6 / 3: {funcionario_2.divide(6.0, 3.0)}")
    print(f"7 + 2: {funcionario_2.soma(7.0, 2.0)}")
    print(f"8 x 3: {funcionario_2.multiplica(8.0, 3.0)}")


if __name__ == '__main__':
    main()