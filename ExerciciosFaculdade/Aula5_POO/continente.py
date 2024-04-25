from __future__ import annotations
from pais import Pais

class Continente:
    def __init__(self, nome_continente: str):
        self.__nome_continente = nome_continente
        self.__conjunto_paises: list[Pais] = []
    
    #get e setter __nome_coninente 
    @property
    def nome_continente(self) -> str:
        return self.__nome_continente
    
    @nome_continente.setter
    def nome_continente(self, nome_continente) -> None:
        self.__nome_continente = nome_continente
        
    #get __conjunto_paises
    @property
    def conjunto_paises(self) -> list[Pais]:
        return self.__conjunto_paises
    
    def adiciona_pais(self, pais: Pais) -> None:
        self.conjunto_paises.append(pais)
    
    def dimensao_total(self) -> float:
        dimensoes = []
        for pais in self.conjunto_paises:
            dimensoes.append(pais.dimensao)
        return sum(dimensoes)
    
    def populacao_total(self) -> int:
        populacoes = []
        for pais in self.conjunto_paises:
            populacoes.append(pais.populacao)
        return sum(populacoes)
    
    def densidade_populacional(self) -> float:
        densidade_total = []            
        for pais in self.conjunto_paises:
            densidade_total.append(pais.densindade_populacional())
        return sum(densidade_total)

    def pais_maior_populacao(self) -> Pais:
        maior = self.conjunto_paises[0]
        for pais in self.conjunto_paises:
            if pais.populacao > maior.populacao:
                maior = pais
        return maior
    
    def pais_menor_populacao(self) -> Pais:
        menor = self.conjunto_paises[0]
        for pais in self.conjunto_paises:
            if pais.populacao < menor.populacao:
                menor = pais
        return menor
    
    def pais_maior_dimensao(self) -> Pais:
        maior = self.conjunto_paises[0]
        for pais in self.conjunto_paises:
            if pais.dimensao > maior.dimensao:
                maior = pais
        return maior
    
    def pais_menor_dimensao(self) -> Pais:
        menor = self.conjunto_paises[0]
        for pais in self.conjunto_paises:
            if pais.dimensao < menor.dimensao:
                menor = pais
        return menor
    
    def maior_com_menor_razao(self) -> float:
        maior = self.pais_maior_dimensao()
        menor = self.pais_menor_dimensao()
        return maior.dimensao / menor.dimensao