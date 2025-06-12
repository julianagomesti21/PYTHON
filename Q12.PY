preco = float (input("Informe o preço de um produto: "))

epoca = int (input("Informe qual época do ano estamos: \n Escolha: \n [1] -> Carnaval \n [2] -> Férias escolares  \n [3]-> Dia das Crianças  \n [4] -> Black Friday \n [5]-> Natal \n"))

if(epoca==1):
 calculo = float (preco+(preco*0.1))
 print ("O preço final em cada caso é : " +str(calculo) )

elif(epoca==2):
 calculo = float (preco+(preco*0.2))
 print ("O preço final em cada caso é : " +str(calculo) )

elif(epoca==3):
  calculo = float (preco+(preco*0.5))
  print ("O preço final em cada caso é : " +str(calculo) )

elif(epoca==4):
  calculo = float (preco+(preco*0.3))
  print ("O preço final em cada caso é : " +str(calculo) )
  
elif(epoca==5):
 calculo = float (preco+(preco*0.5))
 print ("O preço final em cada caso é : " +str(calculo) )


else:
    print("Opção inválida. Por favor, escolha um número entre 1 e 5.")

