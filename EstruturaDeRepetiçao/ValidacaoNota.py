# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo 
# até que o usuário informe um valor válido.
nota_verificada = True

def verificacaoGenerica(nota_verificada):
    while nota_verificada:
        nota = float(input('Informe uma nota de 0 a 10 : '))
        if nota > 10:
            print('>>> Nota maior que 10 é invalida')
        elif nota < 0:
            print('>>> Nota menor que 0 é invalida')
        else:
            print(f'>>> Nota {nota} é válida. Armazenando ela com sucesso')
            return False
        
nota_verificada = verificacaoGenerica(nota_verificada)
print('Fim do programa')