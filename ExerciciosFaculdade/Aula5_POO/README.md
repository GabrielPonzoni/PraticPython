# 1. Classe Pais:
◦ Classe que representa um país.

◦ Um país possui um código ISO 3166-1 (ex.: BRA), um nome (ex.: Brasil), uma
população (ex.: 193.946.886) e uma dimensão em Km2
(ex.: 8.515.767,049).
Além disso, um país mantém uma lista de outros países com os quais ele faz
fronteira.

◦ Crie um construtor que inicialize o código ISO, o nome e a dimensão do país.

◦ Crie os métodos de acesso e modificadores (getter/setter) para os atributos
código ISO, nome, população e dimensão.

◦ Crie um método que permita verificar se dois objetos representam o mesmo país
(igualdade semântica). Dois países são iguais se tiverem o mesmo código ISO.

◦ Crie um método que informe se outro país é limítrofe do país que recebeu a
mensagem.

◦ Crie um método que retorne a densidade populacional do país.

◦ Crie um método que receba um país como parâmetro e retorne a lista de
vizinhos comuns aos dois países. Considere que um país tem no máximo 40
outros países com os quais ele faz fronteira.
# 2. Classe Continente:
◦ Um continente possui um nome e é composto por um conjunto de países.

◦ Crie um construtor que inicialize o nome do continente.

◦ Crie um método que permita adicionar países aos continentes.

◦ Crie um método que retorne a dimensão total do continente.

◦ Crie um método que retorne a população total do continente.

◦ Crie um método que retorne a densidade populacional do continente.

◦ Crie um método que retorne o país com maior população no continente.

◦ Crie um método que retorne o país com menor população no continente.

◦ Crie um método que retorne o país de maior dimensão territorial no continente.

◦ Crie um método que retorne o país de menor dimensão territorial no continente.

◦ Crie um método que retorne a razão territorial do maior país em relação ao
menor país.
# 3. Na função main:
• Crie nove objetos do tipo Pais que estejam situados em três continentes
diferentes.

• Crie os três objetos do tipo Continente.

• Adicione os países aos respectivos continentes.

• Chame os métodos que apresentam as informações dos países e dos
continentes.