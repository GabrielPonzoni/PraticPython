# Supondo que a população de um país A seja da ordem de 80000 habitantes 
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
# e escreva o número de anos necessários para que a população do país A 
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

def main():
    pais_A = 80000
    pais_B = 200000
    
    contador_anos = 0
    while True:
        pais_A = pais_A + (pais_A * 3/100)
        pais_B = pais_B + (pais_B * 1.5/100)
        contador_anos += 1
        
        if pais_A > pais_B:
            break
    
    print(f"Pais A: {pais_A}")
    print(f"Pais B: {pais_B}")
    print(f"Contador anos: {contador_anos}")
    
if __name__ == "__main__":
    main()