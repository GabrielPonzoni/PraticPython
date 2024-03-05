# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Informe sua altura: '))
sexo_biologico = input('Informe seu sexo biológico (M) para masculino ou (F) para feminino: ').upper().strip()

if sexo_biologico == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'O peso ideal para uma pessoa masculina de {altura} é {peso_ideal:.2f} Kg')
elif sexo_biologico == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O peso ideal para uma pessoa feminina de {altura} é {peso_ideal:.2f} Kg')
else:
    print('Sexo biologico informado inválido')

