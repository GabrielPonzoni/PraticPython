# Modelar, usando diagrama de classes UML e, implementar em Python, um Sistema para Gerenciamento de Empréstimos de Livros de uma Biblioteca.
### – Neste sistema, é importante que o usuário possa:
* Consultar livros
* Solicitar o empréstimo de livros (locar)
* Solicitar a reserva, caso o livro não esteja disponível
* Devolver o livro emprestado
### – Estruturar o sistema de modo que:
* Os livros possuam um ou mais exemplares
* Novos livros possam ser cadastrados no acervo
* Livros antigos sejam removidos do acervo
* Os usuários possam solicitar o empréstimo de um ou mais livros
* Relatórios sejam gerados para saber:
    * Quantos livros há no acervo da biblioteca
    * Quantos livros estão emprestados a um determinado usuário
    * Quantos exemplares estão emprestados e quantos estão disponíveis de um determinado livro

> Primeiro sabemos que temos uma Classe Usuário, quais são as caracterísiticas intrísicas a um usuário de uma biblioteca? Nome. 

#### Main
1. Precisamos pedir para o usuário fornecer as informações do seu usuário
   1. Nome;
2. Preciso criar um menu no qual o usuário possa:
   1. Consultar livros;