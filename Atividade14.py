horaS = float(input("Quanto voce ganha por hora? "))
horasT = float(input("Quantas horas voce trabalhou esse mes? "))

SalarioBruto = horaS * horasT
IR = SalarioBruto * 0.11
INSS = SalarioBruto * 0.08
Sindicato = SalarioBruto * 0.05

Descontos = IR + INSS + Sindicato

SalarioLiquido = SalarioBruto - IR - INSS - Sindicato

print("Abaixo suas Aliquotas \n tatal descontos {}".format(Descontos))
print("+ Salário Bruto : R${}".format(SalarioBruto))
print("- IR (11%) : R$ {}".format(IR))
print("- INSS (8%) : R${}".format(INSS))
print(" Sindicato ( 5%) : R${}".format(Sindicato))
print("Salário Liquido : R${}".format(SalarioLiquido))