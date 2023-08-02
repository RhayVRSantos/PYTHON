# Escreva um programa que leia uma sequência de números do usuário e imprima o maior e o menor número da sequência.



def encontrar_maior_menor_numero(sequencia_numeros):
    if not sequencia_numeros:
        return None, None

    maior_numero = menor_numero = sequencia_numeros[0]
    # para cada numero dentro da sequencia 
    for numero in sequencia_numeros:
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero

    return maior_numero, menor_numero

def main():
    entrada = input("Digite uma sequência de números separados por espaço: ")
    sequencia_numeros = [float(numero) for numero in entrada.split()]
    
    maior_numero, menor_numero = encontrar_maior_menor_numero(sequencia_numeros)

    if maior_numero is not None and menor_numero is not None:
        print(f"Maior número: {maior_numero}")
        print(f"Menor número: {menor_numero}")
    else:
        print("Sequência vazia. Não foi possível encontrar o maior e o menor número.")

if __name__ == "__main__":
    main()
