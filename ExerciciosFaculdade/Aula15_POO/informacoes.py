from atleta import Atleta
from nadador import Nadador
from corredor import Corredor

class InformacoesAtletas:
    def imprime_exlusivos_atleta(self, a: Atleta) -> None:
        if isinstance(a, Nadador):
            print(f"É um nadador, e sua categoria é {a.categoria}")
        elif isinstance(a, Corredor):
            print(f"É um corredor, e o peso deste corredor é {a.peso}")
        else:
            print(f"Atleta não possui instancia {a}")
    
    def imprime_informacoes_atleta(self, a: Atleta) -> None:
        a.imprime_info()