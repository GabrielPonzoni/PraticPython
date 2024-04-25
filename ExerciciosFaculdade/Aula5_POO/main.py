from continente import Continente
from pais import Pais
import os

def main():
    
    os.system('cls')
    #paises america
    pais_brasil = Pais("BRA", "Brasil", 216422446, 8358140)
    pais_argentina = Pais("ARG", "Argentina", 45773884, 2736690)
    pais_chile = Pais("CHL", "Chile", 19629590, 743532)

    #PAISES EUROPA
    pais_ucrania = Pais("UKR", "Ucrânia", 36744634, 579320)
    pais_belarusia = Pais("BLR", "Belarussia", 9498238, 202910)
    pais_polonia = Pais("POL", "Polônia", 41026067, 306230)


    #PAISES ASIA
    pais_russia = Pais("RUS", "Rússia", 144444359, 16376870)
    pais_mongolia = Pais("MNG", "Mongólia", 3447157, 1553560)
    pais_china = Pais("CHN", "China", 1425671352, 9388211)

    #fronteiras
    pais_russia.adiciona_fronteira(pais_mongolia)
    pais_russia.adiciona_fronteira(pais_ucrania)
    pais_russia.adiciona_fronteira(pais_belarusia)
    pais_mongolia.adiciona_fronteira(pais_russia)
    pais_mongolia.adiciona_fronteira(pais_china)
    pais_china.adiciona_fronteira(pais_mongolia)
    pais_ucrania.adiciona_fronteira(pais_belarusia)
    pais_ucrania.adiciona_fronteira(pais_russia)
    pais_ucrania.adiciona_fronteira(pais_polonia)
    pais_belarusia.adiciona_fronteira(pais_russia)
    pais_belarusia.adiciona_fronteira(pais_ucrania)
    pais_belarusia.adiciona_fronteira(pais_polonia)
    pais_polonia.adiciona_fronteira(pais_ucrania)
    pais_polonia.adiciona_fronteira(pais_belarusia)
    pais_brasil.adiciona_fronteira(pais_argentina)
    pais_argentina.adiciona_fronteira(pais_brasil)
    pais_argentina.adiciona_fronteira(pais_chile)
    pais_chile.adiciona_fronteira(pais_argentina)

    #CONTINENTES
    continente_america = Continente("America do Sul")
    continente_europa = Continente("Europa")
    continente_asiatico = Continente("Asia")
    #continente Americano
    continente_america.adiciona_pais(pais_brasil)
    continente_america.adiciona_pais(pais_argentina)
    continente_america.adiciona_pais(pais_chile)
    #continente Europeu
    continente_europa.adiciona_pais(pais_ucrania)
    continente_europa.adiciona_pais(pais_belarusia)
    continente_europa.adiciona_pais(pais_polonia)
    #continente Asiatico
    continente_asiatico.adiciona_pais(pais_russia)
    continente_asiatico.adiciona_pais(pais_mongolia)
    continente_asiatico.adiciona_pais(pais_china)
    
    pais_argentina.pais_limitrofe_pais(pais_brasil)
    print(f"Densidade populacional de {pais_china.nome_pais}: {pais_china.densindade_populacional():.2f} hab/km²")
    pais_ucrania.vizinhos_em_comum(pais_russia)
    
    print(f"{pais_ucrania.nome_pais} tem o seguinte vizinho em comum com {pais_russia.nome_pais}:")
    for paises in pais_ucrania.vizinhos_em_comum(pais_russia):
        print(paises)
    
    print(f"{pais_polonia.nome_pais} tem o seguinte vizinho em comum com {pais_ucrania.nome_pais}:")
    for paises in pais_polonia.vizinhos_em_comum(pais_ucrania):
        print(paises)
    
    print(f"{continente_asiatico.nome_continente} tem dimensao total de: {continente_asiatico.dimensao_total():.2f}")
    print(f"{continente_europa.nome_continente} tem populacao total de: {continente_europa.populacao_total()}")
    print(f"{continente_asiatico.nome_continente} tem densidade populacional total de: {continente_asiatico.densidade_populacional():.2f}")
    print(f"O pais com MAIOR populacao no {continente_asiatico.nome_continente} é: {continente_asiatico.pais_maior_populacao().nome_pais} com {continente_asiatico.pais_maior_populacao().populacao}")
    print(f"O pais com MENOR populacao no {continente_asiatico.nome_continente} é: {continente_asiatico.pais_menor_populacao().nome_pais} com {continente_asiatico.pais_menor_populacao().populacao}")
    print(f"O pais com MAIOR dimensao no {continente_asiatico.nome_continente} é: {continente_asiatico.pais_maior_dimensao().nome_pais} com {continente_asiatico.pais_maior_dimensao().dimensao:.2f} Km²")
    print(f"O pais com MENOR dimensao no {continente_asiatico.nome_continente} é: {continente_asiatico.pais_menor_dimensao().nome_pais} com {continente_asiatico.pais_menor_dimensao().dimensao:.2f} Km²")
    print(f"A razão entre a extensao territorial do maior país ({continente_asiatico.pais_maior_dimensao().nome_pais}) em relação ao menor país ({continente_asiatico.pais_menor_dimensao().nome_pais}) é de: {continente_asiatico.maior_com_menor_razao():.2f}")
    

if __name__ == "__main__":
    main()