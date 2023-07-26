import math

def calcular_latas(area):
    cobertura_por_litro = 3
    capacidade_lata = 18
    preco_lata = 80.00

    litros_necessarios = area / cobertura_por_litro
    latasNecessarias = math.ceil(litros_necessarios / capacidade_lata)
    preco_total = latasNecessarias * preco_lata

    return latasNecessarias, preco_total

try:
    tamanho_area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
    latas, preco_total = calcular_latas(tamanho_area)

    print(f"\nQuantidade de latas de tinta necessárias: {latas}")
    print(f"Preço total: R$ {preco_total:.2f}")
except ValueError:
    print("Digite um valor válido para a área da pintura.")
