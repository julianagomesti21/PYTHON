peso = float (input("Por gentileza informar o peso: "))

dias = int (input("Quaantos dias vai a cademia nesse anos? "))

ganhoMassa = float  (dias * 0.20)
perdaGordura = float (dias * 0.40)

pesoAtual = (peso + ganhoMassa - perdaGordura)

print(
      "Você pesava " + str(peso) + " e perdeu " +str(perdaGordura)
      + " kilos porem ganhou "+str(ganhoMassa)+ 
      " de massa muscular, pensando hoje " + str(pesoAtual)
     )
