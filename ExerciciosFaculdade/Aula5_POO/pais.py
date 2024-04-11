#  1. Classe Pais:
# ◦ Classe que representa um país.

# ◦ Um país possui um código ISO 3166-1 (ex.: BRA), um nome (ex.: Brasil), uma
# população (ex.: 193.946.886) e uma dimensão em Km2
# (ex.: 8.515.767,049).
# Além disso, um país mantém uma lista de outros países com os quais ele faz
# fronteira.

# ◦ Crie um construtor que inicialize o código ISO, o nome e a dimensão do país.

# ◦ Crie os métodos de acesso e modificadores (getter/setter) para os atributos
# código ISO, nome, população e dimensão.

# ◦ Crie um método que permita verificar se dois objetos representam o mesmo país
# (igualdade semântica). Dois países são iguais se tiverem o mesmo código ISO.

# ◦ Crie um método que informe se outro país é limítrofe do país que recebeu a
# mensagem.

# ◦ Crie um método que retorne a densidade populacional do país.

# ◦ Crie um método que receba um país como parâmetro e retorne a lista de
# vizinhos comuns aos dois países. Considere que um país tem no máximo 40
# outros países com os quais ele faz fronteira.
from __future__ import annotations

class Pais:
    def __init__(self, codigo_Iso: str, nome: str, dimensao: float):
        self.__codigo_Iso = codigo_Iso
        self.__nome = nome
        self.__populacao = 0
        self.__dimensao = dimensao
        self.__fronteira: list[Pais] = []

        
    
    #get e setter do atributo __codigo_Iso
    @property
    def codigo_Iso(self) -> str:
        return  self.__codigo_Iso
    
    @codigo_Iso.setter
    def codigo_Iso(self, codigo_Iso: str) -> None:
        self.__codigo_Iso = codigo_Iso
        
    #get e setter do atributo __nome
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome
        
    #get e setter do atributo __populacao
    @property
    def populacao(self) -> int:
        return self.__populacao
    
    @populacao.setter
    def populacao(self, populacao: int) -> None:
        self.__populacao = populacao
        
    #get e setter do atributo __dimensao
    @property
    def dimensao(self) -> float:
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao: float) -> None:
        self.__dimensao = dimensao
        
    #get do atributo __fronteira
    @property
    def fronteira(self) -> list[Pais]:
        return self.__fronteira
    
    def __eq__(self, pais: Pais) -> bool:
        if id(self) == id(pais):
            return True
        elif self.codigo_Iso == pais.codigo_Iso:
            return True
        else:
            return False
    
    #>>>>>>>>>>>>>>>> PAREI AKI <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def adiciona_fronteira(self, pais: Pais) -> None:
        self.__fronteira.append(pais)

    #def verifica_fronteira(self, )