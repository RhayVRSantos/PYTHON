def contar_ocorrencias_palavras(texto):
    palavras = texto.split()
    contagem_palavras = {}

    for palavra in palavras:
        # Remove qualquer pontuação que esteja junto com a palavra (pontuações ficam separadas).
        palavra = palavra.strip(".,!?;:'\"()[]{}")
        palavra = palavra.lower()  # Considera palavras em letras minúsculas (ignora diferença de caixa).

        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1

    return contagem_palavras

def main():
    texto = input("Digite o texto: ")
    resultado = contar_ocorrencias_palavras(texto)

    print("Contagem de ocorrências de cada palavra:")
    for palavra, ocorrencias in resultado.items():
        print(f"{palavra}: {ocorrencias}")

if __name__ == "__main__":
    main()
