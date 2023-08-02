# Escreva uma função que verifique se uma palavra é um palíndromo (ou seja, se pode ser lida da
#  mesma forma de trás para frente).
def eh_palindromo(palavra):
    # Converte a palavra para letras minúsculas para evitar problemas de maiúsculas e minúsculas
    palavra = palavra.lower()

    # Remove espaços em branco da palavra
    palavra = palavra.replace(" ", "")

    # Verifica se a palavra é igual à sua inversão (palavra de trás para frente)
    if palavra == palavra[::-1]:
        return True
    else:
        return False

# Exemplo de uso da função
palavra_teste = input("digite uma palavra: ")
if eh_palindromo(palavra_teste):
    print(f"A palavra '{palavra_teste}' é um palíndromo.")
else:
    print(f"A palavra '{palavra_teste}' não é um palíndromo.")
