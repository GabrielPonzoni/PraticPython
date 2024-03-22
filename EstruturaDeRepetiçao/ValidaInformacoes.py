# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
import os

# metodo que retorna a quantidade de caracteres e remove espaçoes em branco da contagem;
def contaLetras(nome):
    return len(retiraEspacos(nome))

# metodo que retorna o texto sem os espacamento entre as palavras
def retiraEspacos(texto):
    return texto.replace(" ","")

# metodo que retorna o nome validado, utilizando o metodo contaLetras() conseguimos ter o numero de letras na string, retornamos o nome informado pelo usuário;
def verificaNome():
    while True:
        nome = input("Informe um nome (maior que 3 caracteres): ")
        
        if contaLetras(nome) > 3:
            print('Nome válido')
            break
        elif contaLetras(nome) <= 3:
            print('Nome inválido, menos de 3 letras, tente novamente.')
        else:
            print('Nome inválido, tente novamente.')
    
    return nome

# metodo que verifica a idade, retorna idade apenas se o valor informado for válido
def verificaIdade():
    while True:
        idade = int(input("Informe uma idade entre 0 e 150: "))
        
        if idade > 0 and idade <= 150:
            print('Idade válida!')
            break
        else:
            print('Idade inválida, tente novamente.')
    
    return idade

# metodo que verifica o salario, menor que 0 invalida, ao contrario ele retorna o valor;            
def verificaSalario():
    while True:
        salario = float(input('Informe um salário maior que 0: R$'))
        
        if salario > 0.0:
            print('Salário válido!')
            break
        else:
            print('Salário inválido, tente novamente.')
            
    return salario

# metodo que verifica se o primeiro char se é m ou f, retorna o sexo de acordo
def verificaSexo():
    while True:
        sexo = retiraEspacos(input('Informe seu sexo (f/m): ').lower())[0]
        
        if sexo == 'm':
            print('Sexo Masculino definido.')
            return 'Masculino'
            
        elif sexo == 'f':
            print('Sexo Feminino definido.')
            return 'Feminino'
        
        else:
            print('Não entendi o sexo informado, tente novamente. ')
        
    
def verificaEstadoCivil(sexo):
    while True:
        texto_terminal = 'Informe seu estado civil ("s" - solteiro, "c" - casado, "v" - viúvo, "d" - divorciado): ' if sexo == 'Masculino' else 'Informe seu estado civil ("s" - solteira, "c" - casada, "v" - viúva, "d" - divorciada): '
        estado_civil = retiraEspacos(input(texto_terminal).lower())
        
        match estado_civil:
            case 's' | 'solteiro' | 'solteira':
                return 'Solteir' + ('o' if sexo == 'Masculino' else 'a')
            case 'c' | 'casado' | 'casada':
                return 'Casad' + ('o' if sexo == 'Masculino' else 'a')
            case 'v' | 'viuvo' | 'viuva':
                return 'Viúv' + ('o' if sexo == 'Masculino' else 'a')
            case 'd' | 'divorciado' | 'divorciada':
                return 'Divorciad' + ('o' if sexo == 'Masculino' else 'a')
            case _:
                print(f'Estado civil {estado_civil} é inválido, tente novamente')
            


def main():
    os.system('cls')
    
    nome = verificaNome()
    idade = verificaIdade()
    salario = verificaSalario()
    sexo = verificaSexo()
    estado_civil = verificaEstadoCivil(sexo)
    
    os.system('cls')
    print('Perfil salvo no sistema com sucesso! Verifique se está tudo certo:')
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f"R${salario:.2f}")
    print(f'Sexo: {sexo}')
    print(f'Estado civil: {estado_civil}')
    
        
if __name__ == '__main__':
    main()