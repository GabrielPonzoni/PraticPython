# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

pessoa = {
    'nome' : 'Gabriel Ponzoni',
    'idade' : 22,
    'cidade' : 'Porto Alegre'
}

pessoa['profissao'] = 'Estudante'

# del pessoa['idade']

# for elemento in pessoa:
#     print(elemento,': ',pessoa[elemento]) 

numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

# for elemento in numeros_quadrados:
#     print(elemento,': ',numeros_quadrados[elemento])

pessoadicionario = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
print(f"A chave {pessoadicionario['nome']} existe no dicionário." if 'nome' in pessoadicionario else f"A chave {pessoadicionario['nome']} não existe no dicionário.")