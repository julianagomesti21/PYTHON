valorA = int (input("Informe o primeiro numero : "))
valorB = int (input("Informe o segundo  numero : "))

if(valorA==valorB):
 valorC = valorA+valorB
 print ("O valor do primeiro numero mais o segundo é: " + str(valorC))
else:
 valorC = valorA-valorB
 print ("O valor do primeiro numero menos o segundo é: " + str(valorC))