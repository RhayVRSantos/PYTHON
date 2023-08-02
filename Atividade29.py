# Crie uma função que receba uma lista de números e retorne a mediana 
# dos valores (o valor que fica no meio quando os números são ordenados).

def calcular_mediana(lista_numeros):
    if not lista_numeros:
        return None

    lista_ordenada = sorted(lista_numeros) # "sorted()" a função retorna uma nova lista com os elementos ordenados.
    tamanho_lista = len(lista_ordenada)#conta os elementos da lista 
    indice_meio = tamanho_lista // 2

    if tamanho_lista % 2 == 1:
        # Se a lista tiver um número ímpar de elementos, a mediana é o valor central.
        mediana = lista_ordenada[indice_meio]
    else:
        # Se a lista tiver um número par de elementos, a mediana é a média dos valores centrais.
        mediana = (lista_ordenada[indice_meio - 1] + lista_ordenada[indice_meio]) / 2

    return mediana

def main():
    lista_numeros = [float(numero) for numero in input("Digite a lista de números separados por espaço: ").split()]
    mediana = calcular_mediana(lista_numeros)

    if mediana is not None:
        print(f"Mediana dos valores: {mediana}")
    else:
        print("Lista vazia. Não foi possível calcular a mediana.")

if __name__ == "__main__":
    main()
