from __future__ import annotations
import os

class Pais:
    def __init__(self, codigo_iso: str, nome_pais: str, populacao: int, dimensao: float):
        self.__codigo_iso = codigo_iso
        self.__nome_pais = nome_pais
        self.__populacao = populacao
        self.__dimensao = dimensao
        self.__lista_fronteira: list[Pais] = []
        
    #get e setter __codigo_iso
    @property
    def codigo_iso(self) -> str:
        return self.__codigo_iso
    
    @codigo_iso.setter
    def codigo_iso(self, codigo_iso) -> None:
        self.__codigo_iso = codigo_iso
    
    #get e setter __nome_pais
    @property
    def nome_pais(self) -> str:
        return self.__nome_pais
    
    @nome_pais.setter
    def nome_pais(self, nome_pais) -> None:
        self.__nome_pais = nome_pais
        
    #get e setter __populacao
    @property
    def populacao(self) -> int:
        return self.__populacao
    
    @populacao.setter
    def populacao(self, populacao) -> None:
        self.__populacao = populacao
    
    #get e setter __dimensao
    @property
    def dimensao(self) -> float:
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao) -> None:
        self.__dimensao = dimensao
    
    #get e setter __lista_fronteira
    @property
    def lista_fronteira(self) -> list[Pais]:
        return self.__lista_fronteira
    
    # @lista_fronteira.setter
    # def lista_fronteira(self, lista_fronteira) -> None:
    #     self.__lista_fronteira = lista_fronteira
    
    def __eq__(self, pais: Pais) -> bool:
        if id(self) == id(pais): #compara o id de memória
            return True
        elif self.codigo_iso == pais.codigo_iso: #compara o codigo iso da propria classe com a instancia 
            return True
        else: #caso contrario retorna false 
            return False
    
    def adiciona_fronteira(self, pais: Pais) -> None:
        self.lista_fronteira.append(pais)
    
    def pais_limitrofe_pais(self, pais: Pais) -> None:
        eh_limitrofe = pais in self.lista_fronteira
        if eh_limitrofe == True:
            print(f"{pais.nome_pais} é limítrofe de {self.nome_pais}")
        else:
            print(f"{pais.nome_pais} não é limítrofe de {self.nome_pais}")
    
    def densindade_populacional(self) -> float:
        return self.populacao / self.dimensao
    
    def vizinhos_em_comum(self, pais: Pais) -> list:
        lista_pais_vizinho = [] 
        for paises_1 in pais.lista_fronteira:
            for paises_2 in self.lista_fronteira:
                if paises_1 == paises_2:
                    lista_pais_vizinho.append(paises_2.nome_pais)
        return lista_pais_vizinho
        
        
        
# # Teste da classe        
# os.system('cls')                    
# pais_brasil = Pais("BRA", "Brasil", 216422446, 8358140)
# pais_argentina = Pais("ARG", "Argentina", 45773884, 2736690)
# pais_chile = Pais("CHL", "Chile", 19629590, 743532)
# pais_paraguai = Pais("PRY", "Paraguai", 6861524, 397300)

# pais_brasil.adiciona_fronteira(pais_argentina)
# pais_brasil.adiciona_fronteira(pais_paraguai)
# pais_argentina.adiciona_fronteira(pais_brasil)
# pais_argentina.adiciona_fronteira(pais_paraguai)

# lista_paises = pais_brasil.vizinhos_em_comum(pais_argentina)
# for item in lista_paises:
#     print(item)

# print(f"densidade populacional Brasil: {pais_brasil.densindade_populacional():.2f}")