from data import Data
from atleta import Atleta
from nadador import Nadador
from corredor import Corredor
from competicao import Competicao
from informacoes import InformacoesAtletas

def main():
    data_competicao = Data(25, 9, 2024)
    competicao = Competicao("Correr é Show", data_competicao)
    print(f"O nome da competição é {competicao.nome}")
    competicao.imprime_data()
    print()
    
    nadador1 = Nadador("Cielo", 36, "Borboleta")
    nadador1.imprime_info()
    print()
    
    corredor1 = Corredor("Josenildo", 91, 68, competicao)
    corredor1.competicao.data.mes = 10
    competicao.imprime_data()
    print()
    
    data_competicao2 = Data(31,12,2024)
    competicao2 = Competicao("São Silvestre", data_competicao2)
    corredor2 = Corredor("Petrolina", 100, 60, competicao2)
    
    corredor2.imprime_info()
    print()
    

    while True:
        resposta = int(input('Digite para criar:\n1- Nadador\n2- Corredor\n'))
        if resposta == 1:
            nadador_novo = Nadador(input("Informe o nome do nadador: "),int(input("Informe a idade do nadador: ")),input("Informe a categoria do nadador: "))
            informacao_atleta = InformacoesAtletas()
            informacao_atleta.imprime_exlusivos_atleta(nadador_novo)
            nadador_novo.categoria = "Livre"
            print()
            informacao_atleta.imprime_informacoes_atleta(nadador_novo)
            break
        
        elif resposta == 2:
            corredor_novo = Corredor(input("Informe o nome deste corredor: "), int(input("Informe a idade deste corredor: ")), float(input("Informe o peso do corredor: ")), competicao)
            informacao_atleta = InformacoesAtletas()
            informacao_atleta.imprime_exlusivos_atleta(corredor_novo)
            corredor_novo.peso = 89
            print()
            informacao_atleta.imprime_informacoes_atleta(corredor_novo)
            break
        else:
            print("Resposta inválida, tente novamente")
    
    print("---")

if __name__ == "__main__":
    main()