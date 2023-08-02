# Crie uma função que receba uma lista de números e
# retorne uma nova lista contendo apenas os números pares.

def numeros_pares(lista):
    # Filtra os números pares da lista usando uma compreensão de lista
    numeros_pares = [num for num in lista if num % 2 == 0]
    return numeros_pares

# Exemplo de uso da função
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = numeros_pares(numeros)
print("Números pares na lista:", numeros_pares)


