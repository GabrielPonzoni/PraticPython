# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

print('========= Joao Pescados ==========')
peso_de_peixes = float(input('João informe o peso dos peixes pescados: '))
excedente_pescados = peso_de_peixes - 50.00
valor_multa = excedente_pescados * 4.00

if valor_multa == 0:
    print('Oba! Joao você não pescou além do que deveria! 0 reais de multas.')
else:
    print(f'João você pescou {excedente_pescados:.1f} Kg a mais do que é permitido por lei, sua multa equivale a R$ {valor_multa:.2f}')