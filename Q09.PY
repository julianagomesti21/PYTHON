numero1 = int (input("Informe o valor do numero 1: "))

numero2 = int (input("Informe o valor do numero 2: "))

escolha = int (input(" Escolha: \n [1] -> soma \n [2] -> subtração \n [3]-> multiplicação \n [4] -> divisão \n"))

if(escolha==1):
 calculo = int (numero1+numero2)
 print ("o calculo entre os numero de soma é: " +str(calculo) )

elif(escolha==2):
 calculo = int (numero1-numero2)
 print ("o calculo entre os numero de subtração é: " +str(calculo) )

elif(escolha==3):
  calculo = int (numero1*numero2)
  print ("o calculo entre os numero de multiplicação é: " +str(calculo) )

elif(escolha==4):
  calculo = int (numero1/numero2)
  print ("o calculo entre os numero de divisão é: " +str(calculo) )
  
else:
    print("Opção inválida. Por favor, escolha um número entre 1 e 4.")


