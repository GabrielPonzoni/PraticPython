Programação Orientada a Objetos
Profa. Andriele Busatto do Carmo
Exercícios

Crie o diagrama de classes para as classes descritas abaixo. Em seguida,
implemente as classes do projeto.

1. Classe Calculadora:
◦ Uma calculadora possui uma memória e uma cor.
◦ Quando uma calculadora é criada, a memória deve ser inicializada com 0 e a cor
deve ser recebida por parâmetro (construtor).
◦ Crie os métodos de acesso para os atributos da classe (get e set).
◦ Crie os métodos: soma, subtrai, multiplica e divide. Todos recebem dois
valores (float) por parâmetro e retornam o valor da operação realizada.
◦ Crie os métodos eleva_ao_quadrado e eleva_ao_cubo. Ambos recebem
apenas um valor (int) e retornam o valor da operação realizada.
◦ Crie um método imprime_info, que não recebe parâmetros e simplesmente
imprime as informações da calculadora de maneira legível e organizada.

2. Classe FuncionarioCaixa:
◦ Possui um nome, um endereço e uma calculadora.
◦ Crie um construtor que recebe os parâmetros para inicializar todos os atributos.
◦ Crie os métodos de acesso dos atributos desta classe (get e set).
◦ Crie os métodos soma, subtrai, multiplica, divide,
eleva_ao_quadrado e eleva_ao_cubo. Cada método destes deve chamar o
método correspondente da calculadora, retornando o valor obtido na operação.
◦ Crie um método chamado imprime_info, que não recebe parâmetros de
entrada e imprime na tela as informações da classe, inclusive da calculadora
(sem as operações, apenas os atributos).

3. Classe Empresa:
◦ Uma empresa tem um nome e dois funcionários do caixa.
◦ Crie um construtor que recebe todos os parâmetros para inicializar os atributos.
◦ Crie os métodos de acesso dos atributos desta classe (get e set).
◦ Crie um método imprime_info, que imprime as informações da classe.

4. Na função main:
• Crie um objeto do tipo FuncionarioCaixa, chamado funcionario. Tudo que
for necessário para criar este objeto, deve ser solicitado para o usuário.
• Imprima o resultado das operações: 2+2, 5-4, 2x3, 6/3, 7+2, 8x3. As operações
devem ser feitas através da calculadora do objeto funcionário criado.
• Neste método, crie um objeto do tipo Empresa chamado empresa1, com nome
solicitado para o usuário, com o funcionário criado anteriormente e um novo
funcionário que deve ser criado. Tudo que for necessário para criar esta empresa
(que já não tenha sido criado) deve ser solicitado para o usuário.
• Imprima as informações desta empresa.