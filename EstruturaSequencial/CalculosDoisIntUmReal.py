# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

numero_inteiro1 = int(input('Informe o primeiro numero inteiro: '))
numero_inteiro2 = int(input('Informe o segundo numero inteiro: '))
numero_real = float(input('Informe um numero REAL(com virgula): '))

resposta_1 = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
resposta_2 = (3 * numero_inteiro1) + numero_real
resposta_3 = numero_real**3

print(f'O produto do dobro do primeiro com metade do segundo: (2.{numero_inteiro1}) x ({numero_inteiro2}/2) = {resposta_1}')
print(f'a soma do triplo do primeiro com o terceiro: (3.{numero_inteiro1}) + {numero_real:.2f} = {resposta_2:.2f}')
print(f'o terceiro elevado ao cubo: {numero_real}³ = {resposta_3}')