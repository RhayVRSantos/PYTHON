# Implemente um jogo de adivinhação em que o computador escolhe um número aleatório entre 1 e 100, 
# e o jogador deve tentar adivinhar qual é esse número.
import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))

            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                break
            elif palpite < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")

        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()
