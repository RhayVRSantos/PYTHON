# Crie uma função que receba uma lista de números e retorne a lista ordenada de forma crescente.

def ordenar_lista_crescente(lista_numeros):
    lista_numeros.sort()
    return lista_numeros

def main():
    lista_numeros = [int(numero) for numero in input("Digite a lista de números separados por espaço: ").split()]
    lista_ordenada = ordenar_lista_crescente(lista_numeros)

    print("Lista ordenada de forma crescente:")
    print(lista_ordenada)

if __name__ == "__main__":
    main()
