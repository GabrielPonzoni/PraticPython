# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = int(input('Informe a temperatura em graus Fahrenheit: '))

celsius = (5/9) * (fahrenheit - 32)
print(f'Isso equivale a {celsius:.1f} graus Celsius')