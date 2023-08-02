# Implemente um programa que simule o lançamento de dois dados e calcule a soma dos valores obtidos.
import random

def lancar_dados():
    # Simula o lançamento de um dado (gera um número aleatório de 1 a 6)
    dado1 = random.randint(1, 6)

    # Simula o lançamento do segundo dado
    dado2 = random.randint(1, 6)

    # Calcula a soma dos valores obtidos
    soma = dado1 + dado2

    return dado1, dado2, soma

# Exemplo de uso do programa
dado1_resultado, dado2_resultado, soma_resultado = lancar_dados()
print(f"Lançamento do primeiro dado: {dado1_resultado}")
print(f"Lançamento do segundo dado: {dado2_resultado}")
print(f"Soma dos valores obtidos: {soma_resultado}")


