genero = int(input("Ola poderia nos informa seu genero: \n 1- FEMININO \n 2- MASCULINO \n"))
altura = float(input("Qual sua altura? "))

if (genero == 1 ):
    pesoIdeal = (62.1*altura) - 44.7
    print("O seu peso ideal é {}".format(pesoIdeal))

elif(genero == 2):
     pesoIdealM = (72.7*altura) - 58
     print("O se peso ideal é {}".format(pesoIdealM))
    
else:
     print("Fim do programa")




