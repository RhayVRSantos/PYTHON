# Crie uma função que receba uma lista de strings e retorne uma nova lista 
# com todas as palavras em letras maiúsculas.



def converter_para_minusculas(lista_strings):
    # converte em minuscula cada palavra dentro da lista e retorna a lista 
    lista_minusculas = [palavra.lower() for palavra in lista_strings]
    return lista_minusculas

def main():
    lista_strings = input("Digite a lista de strings separadas por espaço: ").split() 
    # cada texto inserido na lista vai ser estudado separadamente por conta do "split()"
    lista_minusculas = converter_para_minusculas(lista_strings)
    #  a variavel "lista_minusculas" va receber o resultado que a função gerar 
    print("Lista com palavras em letras maiúsculas:")
    print(lista_minusculas)

if __name__ == "__main__":
    main()
