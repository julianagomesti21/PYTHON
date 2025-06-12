salario = float (input("Informe seu salário: "))

ferias = float (salario*1.33)
bonus = float (salario*0.74)
promocao = float (salario*1.45)

print(
   "Baseado no seu salario suas férias seriam: " + str(ferias) +
   " , seu bônus seria: " +str(bonus)+  
   " e caso você fosse promovida seria: " + str(promocao)
   )