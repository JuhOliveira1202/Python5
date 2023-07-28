#Exercício 8:
#Elabora um programa que imprima o maior
#de dois números reais

numero1 = int (input("intruduza um número"))
numero2 = int (input("introduza um número"))

if numero1>numero2:
    print("O número", numero1, "é maior que o ", numero2)

elif numero1 == numero2:
    print("Os números são iguais")

elif numero1<numero2:
    print("O número", numero2, "é maior que o ", numero1)
    
else:
    print("condição não pensada, contace o administrador!")

    
