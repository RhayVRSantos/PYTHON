def calcular_media(lista):
    # Verifica se a lista não está vazia
    if len(lista) == 0:
        return 0  # Retorna 0 se a lista estiver vazia para evitar divisão por zero

    # sun é responsavel por somar os valores na lista
    soma = sum(lista)

    # Calcula a média dividindo a soma pelo número de elementos na lista
    media = soma / len(lista)

    return media

numeros = []
fim = 5
while fim > 0:
    num = int(input("digite um  numero quando quiser parar digite 0:  "))
    numeros.append(num)
    fim = fim - 1


resultado = calcular_media(numeros)
print("A média dos valores na lista é:", resultado)
