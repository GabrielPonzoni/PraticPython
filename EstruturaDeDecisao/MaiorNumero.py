# Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input('Informe um primeiro número qualquer: '))
numero2 = float(input('Informe um segundo número qualquer: '))

if numero1 > numero2:
    print(f'O maior numero foi o primeiro. ({numero1})')
elif numero2 > numero1:
    print(f'O maior numero foi o segundo. ({numero2})')
else: # elif numero1 == numero2:
    print(f'Os números são iguais')
