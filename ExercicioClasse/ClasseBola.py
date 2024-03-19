# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.nova_cor = input(f'A cor da bola atualmente é {self.cor}.\nPara qual cor queres trocar?')
        self.cor = self.nova_cor

    def mostraCor(self):
        print(f'A cor da bola é: {self.cor}')

def main():
    Bola1 = Bola('Amarela', 10.0, 'Plástico')

    print(f'\tBola 1:\nCor: {Bola1.cor}\nCircunferencia: {Bola1.circunferencia}\nMaterial: {Bola1.material}')

    while True:
        condicional_lasso = input('Quer trocar a cor da bola? (S = Sim/N = Não)').upper()

        if condicional_lasso == 'S':
            Bola1.trocaCor()
        elif condicional_lasso == 'N':
            while True:
                    condicional_lasso2 = input('Quer ver a cor da bola? (S = Sim/N = Não)').upper()

                    if condicional_lasso2 == 'S':
                        Bola1.mostraCor()
                        return False
                    elif condicional_lasso2 == 'N':
                        return False
                    else:
                        print('Informação inválida 2')            
        else:
            print('Informação inválida 1')
   

if __name__ == '__main__':
    main()