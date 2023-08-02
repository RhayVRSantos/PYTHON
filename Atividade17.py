def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
   
    velocidade_internet_mbps = velocidade_internet_mbps / 8
    tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mbps
    tempo_download_minutos = tempo_download_segundos / 60

    return tempo_download_minutos

try:
        tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
        velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

        tempo_download_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)
        print(f"Tempo aproximado de download: {tempo_download_minutos:.2f} minutos")

except ValueError:
    print("Digite valores válidos para o tamanho do arquivo e a velocidade da Internet.")

    