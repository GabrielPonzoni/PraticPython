# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input('Informe o raio do circulo:'))
area = math.pi * raio**2

print(f'O circulo com raio {raio} metros tem aproximadamente {area:.2f} m² de area') 