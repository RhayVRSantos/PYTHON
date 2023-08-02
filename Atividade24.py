# Escreva uma função que receba um número inteiro e retorne o fatorial desse número.
import math

def fatorial(numero):
    # Caso base: o fatorial de 0 e 1 é sempre 1
    if numero == 0 or numero == 1:
        return 1
    else:
        # Inicializa o resultado com 1
        resultado = 1

        # Loop para calcular o fatorial
        for i in range(2, numero + 1):
            resultado *= i

        return resultado


numero = int(input("digite um numero: "))
resultado_fatorial = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado_fatorial}")
