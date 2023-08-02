# Implemente um programa que converta uma temperatura em Celsius para Fahrenheit
#  ou vice-versa, de acordo com a escolha do usuário.

def Graus():
    Fahrenheit = float(input(" digite o valor em Fahrenheit: "))

    C = 5 * ((Fahrenheit-32) / 9)

    print("{} Fahrenheit é o mesmo que {} Graus".format(Fahrenheit, C))

def Fahrenheit():
    Graus = float(input(" digite a temperatura: "))

    Fahrenheit = (Graus * 9/5) + 32 

    print("{} Graus é o mesmo que {} Fahrenheit".format(Graus, Fahrenheit))


entrada = int(input("Deseja converte a temperatura para qual? \n 1 - Fahrenheit \n 2 - Graus Celsius \n : "))

if entrada == 1 :
     Fahrenheit = Fahrenheit()
     print(Fahrenheit)

elif entrada == 2:
     Graus = Graus()
       
else:
     print("digite uma resposta valida!")
        

