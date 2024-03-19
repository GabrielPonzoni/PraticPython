# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado
    
    def mudarValorLado(self):
        self.tamanho_do_lado = float(input('Tamanho do lado: '))
        return self.tamanho_do_lado
    
    def calcularArea(self):
        self.area = self.tamanho_do_lado ** 2
        return self.area
    
def main():
    Quadrado1 = Quadrado(1.0)
    print(f'Seu quadrado inicial tem {Quadrado1.tamanho_do_lado}')

    while True:
        pergunta_lasso = input('Gostaria de mudar o lado? (S/N)')

        if pergunta_lasso == 'S':
            Quadrado1.tamanho_do_lado = Quadrado1.mudarValorLado()
            break
        elif pergunta_lasso == 'N':
            break
        else:
            print('Opçao inválida, tente novamente:')
    
    while True:
        pergunta_lasso = input(f'Gostaria de saber a área do quadrado de lado {Quadrado1.tamanho_do_lado}? ')

        if pergunta_lasso == 'S':
            area = Quadrado1.calcularArea()
            print(f'A área de um quadrado de lado {Quadrado1.tamanho_do_lado} é de {area}')
            break
        elif pergunta_lasso == 'N':
            break
        else:
            print('Opçao inválida, tente novamente:')

    

if __name__ == '__main__':
    main()