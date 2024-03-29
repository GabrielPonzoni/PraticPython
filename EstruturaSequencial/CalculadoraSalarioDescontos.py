# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. <- input
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

print('====== Calculadora de Despesas =======')
ganhos_hora = float(input('\nQuanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou no mês? '))
salario_bruto = ganhos_hora * horas_trabalhadas

print(f'Salário bruto: R$ {salario_bruto:.2f}')

imposto_renda = salario_bruto * 11/100

print(f'Pago ao Imposto de Renda: R$ {imposto_renda:.2f}')

inss = salario_bruto * 8/100

print(f'Pago ao INSS: R$ {inss:.2f}')

sindicato = salario_bruto * 5/100

print(f'Pago ao Sindicato: R$ {sindicato:.2f}')

print('\n>>>Calculando: ')

print(f'+ Salário Bruto: R$ {salario_bruto:.2f}')
print(f'- IR (11%): R$ {imposto_renda:.2f}')
print(f'- INSS (8%): R$ {inss:.2f}')
print(f'- Sindicato (5%): R$ {sindicato:.2f}')

salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f'= Salário liquido: R$ {salario_liquido:.2f}')
