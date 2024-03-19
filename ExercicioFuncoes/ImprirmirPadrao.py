# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. 
# Use uma função que receba um valor n inteiro 
# e imprima até a n-ésima linha.

numero = int(input('Quer imprimir um padrao até qual linha? '))
def imprimirAte(numero):
    for contador in range(1,numero + 1):
        linha = " ".join(str(contador) for _ in range(contador))
        print(linha)
    

imprimirAte(numero)