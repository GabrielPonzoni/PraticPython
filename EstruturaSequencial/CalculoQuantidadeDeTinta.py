# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# comprar apenas latas de 18 litros;

# comprar apenas galões de 3,6 litros;

# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

print('======= Loja de Tinta =========')
metros_para_pintar = float(input('Quantos metros² de área a ser pintada? '))
litros_tinta = metros_para_pintar / 6
litros_tinta_margem = litros_tinta + (litros_tinta * 10/100)
print(f'Para pintar {metros_para_pintar:.1f} m² você usaria {litros_tinta:.2f} litros de tinta (com 10%: {litros_tinta_margem:.2f});') #OUTRA FORMA DE ARREDONDAR PARA CIMA

def opcaoLatas (litros_tinta_margem):
    litros = litros_tinta_margem
    latas = math.ceil(litros / 18) 
    preço = latas * 80.00
    return latas, preço

def opcaoGaloes (litros_tinta_margem):
    litros = litros_tinta_margem
    galoes = math.ceil(litros / 3.6)
    preço = galoes * 25.00
    return galoes, preço

def opcaoLatasGaloes (litros_tinta_margem):
    litros = litros_tinta_margem
    latas_maximas = math.floor(litros / 18) #ARREDONDO PARA BAIXO ASSIM POSSSO UTILIZAR O RESTO COM GALAO
    galoes_maximo = math.ceil((litros - (latas_maximas * 18)) / 3.6)
    preço_latas = latas_maximas * 80.00
    preço_galoes = galoes_maximo * 25.00
    return latas_maximas, galoes_maximo, preço_latas, preço_galoes
    

latas, preço_latas = opcaoLatas(litros_tinta_margem)
print(f'Para {latas} lata(s) de 18.0 l o valor fica: R$ {preço_latas:.2f}')

galoes, preço_galoes = opcaoGaloes(litros_tinta_margem)
print(f'Para {galoes} galao(loes) de 3.6 l o valor fica: R$ {preço_galoes:.2f}')

latas_otimizado, galoes_otimizado, preço_latas_otimizadas, preço_galoes_otimizados = opcaoLatasGaloes(litros_tinta_margem)
print(f'Para {litros_tinta:.2f} l considerando 10% de folga para nao ocorrer o risco de ficar sem tinta ficamos com {litros_tinta_margem:.2f} l\n Assim evitando o disperdício pode ser comprado {latas_otimizado} lata(s) e {galoes_otimizado} galao(loes) pelo valor R$ {preço_latas_otimizadas:.2f} e R$ {preço_galoes_otimizados:.2f} totalizando R$ {(preço_latas_otimizadas + preço_galoes_otimizados):.2f}')