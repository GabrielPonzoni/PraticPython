# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Quanto voce ganha por hora?'))
horas_trabalhadas = int(input('Quantas horas voce trabalha ao mes?'))

salario_mes = valor_hora * horas_trabalhadas

print(f'Salario recebido se ganhar R$ {valor_hora:.2f} por hora, totalizando no mes = R$ {salario_mes:.2f}')