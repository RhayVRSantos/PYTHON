# Faça um programa que leia uma lista de palavras e retorne a maior e a menor palavra da lista.

def encontrar_maior_menor_palavra(lista_palavras):

    if not lista_palavras:
        return None, None

    maior_palavra = menor_palavra = lista_palavras[0]
    # para cada palavra dentro de "lista"
    for palavra in lista_palavras:
        # "len" ira contar a quantidade de letras em cada palavra presente na lista "palavra" e comparar qual é maior 
        # e adicionar ela a variavel "maior_palavra"

        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        elif len(palavra) < len(menor_palavra):
            menor_palavra = palavra

    return maior_palavra, menor_palavra

def main():
    lista_palavras = input("Digite a lista de palavras separadas por espaço: ").split() 
    # "split()" é especialmente útil quando você deseja dividir uma string em partes menores para processá-las
    #  individualmente ou analisar os dados contidos na string.
    maior_palavra, menor_palavra = encontrar_maior_menor_palavra(lista_palavras)

    if maior_palavra and menor_palavra:
        print(f"Maior palavra: {maior_palavra}")
        print(f"Menor palavra: {menor_palavra}")
    else:
        print("Lista vazia. Não foi possível encontrar maior e menor palavra.")

if __name__ == "__main__":
    main()
