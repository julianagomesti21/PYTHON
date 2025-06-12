peso = float (input("digite seu peso no planeta terra: "))
planeta = str
escolha = int (input(" Escolha: \n [1] -> Mercurio \n [2] -> Venus \n [3]-> Marte \n [4] -> Jupiter \n [5] -> Saturno \n [6] -> Urano \n"))

if(escolha==1):
 planeta = ("Mercúrio")
 calculo = int (peso*0.37)
 print ("Se você estivesse no planeta : " +str(planeta) +"você pesaria"+str(calculo))

elif(escolha==2):
 planeta = ("Venus")
 calculo = int (peso*0.88)
 print ("Se você estivesse no planeta : " +str(planeta) +" você pesaria"+str(calculo))

elif(escolha==3):
 planeta = ("Marte")
 calculo = int (peso*0.38)
 print ("Se você estivesse no planeta : " +str(planeta) +" você pesaria"+str(calculo))

elif(escolha==4):
 planeta = ("Jupiter")
 calculo = int (peso*2.64)
 print ("Se você estivesse no planeta : " +str(planeta) +" você pesaria"+str(calculo))

elif(escolha==5):
 planeta = ("Saturno")
 calculo = int (peso*1.15)
 print ("Se você estivesse no planeta : " +str(planeta) +" você pesaria"+str(calculo))

elif(escolha==6):
 planeta = ("Urano")
 calculo = int (peso*1.17)
 print ("Se você estivesse no planeta : " +str(planeta) +" você pesaria"+str(calculo))



else:
    print("Opção inválida. Por favor, escolha um número entre 1 e 6.")

