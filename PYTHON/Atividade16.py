import math

def calcular_latas(area):
    cobertura_por_litro = 3
    capacidade_lata = 18
    preco_lata = 80.00

    litros_necessarios = area / cobertura_por_litro
    latasNecessarias = math.ceil(litros_necessarios / capacidade_lata)
    preco_total = latasNecessarias * preco_lata

    return latasNecessarias, preco_total

def calcular_galao(area):
    cobertura_por_litro = 6
    capacidade_galao = 3.6
    preco_galao = 25.00

    litros_necessarios = area / cobertura_por_litro
    galoesNecessarias = math.ceil(litros_necessarios / capacidade_galao)
    preco_total = galoesNecessarias * preco_galao

    return galoesNecessarias, preco_total

try:
    tamanho_area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
    latas, preco_total = calcular_latas(tamanho_area)
    galoes, preco_total2= calcular_galao(tamanho_area)

    print(f"\nQuantidade de latas de tinta necessárias: {latas}")
    print(f"Preço total: R$ {preco_total:.2f}")

    print(f"\nQuantidade de galoes de tinta necessárias: {galoes}")
    print(f"Preço total: R$ {preco_total2:.2f}")

except ValueError:
    print("Digite um valor válido para a área da pintura.")