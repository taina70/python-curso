salario = 1550

if salario >= 1600 :
    novosalario = salario + (salario * 8) /100
    print("Salário com bonus de 5%", novosalario )
elif salario >= 1500:
    novosalario = salario + (salario * 8) /100
    print("Salário com bonus de 8%" , novosalario)
else:
    print("Salário normal." , salario)
