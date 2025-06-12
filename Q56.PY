peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
estado_nutricional = str
pesoIdeal = float (21.75*(altura*altura))



imc = float (peso /(altura*altura))

if (imc < 18.5):
        estado_nutricional = "baixo_peso"
        print(" Você está abaixo do peso.")
        print("Cardápio: Café da manhã: Vitamina de abacate com aveia. Almoço: Arroz integral, feijão, peito de frango grelhado e salada de folhas. Lanche da tarde: Mix de castanhas e frutas secas. Jantar: Omelete com legumes e batata-doce.")
elif (imc >= 18.5 and imc<= 24.9):
        estado_nutricional = "peso_normal"
        print("Você está no peso ideal.")
        print("Cardápio: Café da manhã: Iogurte natural com granola e frutas. Almoço: Salada de folhas verdes com peito de frango grelhado e quinoa. Lanche da tarde: Maçã. Jantar: Sopa de legumes .")
elif (imc >= 25 and imc <= 29.9):
        estado_nutricional = "sobrepeso"
        print("Você está com sobrepeso.")
        print("Cardápio: Café da manhã: Pão com ovos.Almoço: Arroz, feijão, peito de frango  e salada . Lanche da tarde: Mix de frutas. Jantar: Omelete.")

elif (imc >= 30 and imc < 35):
        estado_nutricional = "obesidade_1"
        print("Você está com obesidade grau I.")
        print("Cardápio: Café da manhã: Iogurte natural com granola e morangos. Almoço: Peito de frango grelhado com arroz integral e salada de folhas verdes. Lanche da tarde: Mix de castanhas e banana. Jantar: Sopa de legumes com carne magra.")

elif (imc >= 35 and  imc <= 40):
        estado_nutricional = "obesidade_2"
        print("Você está com obesidade grau II.")
        print("Cardápio: Café da manhã: granola e morangos. Almoço: Peito de frango grelhado com arroz integral e salada de folhas verdes. Lanche da tarde: Mix de castanhas e banana. Jantar: Sopa de legumes com carne magra.")

else:
        estado_nutricional = "obesidade_3 (mórbida)"
        print("Você está com obesidade grau III.")
        print("Cardápio: Café da manhã: Vitamina de banana com aveia. Almoço: Peito de frango grelhado com arroz integral e brócolis. Lanche da tarde: Iogurte natural com granola. Jantar: Sopa de legumes com carne magra.")



if (peso>pesoIdeal):
        calculoPeso = float (peso-pesoIdeal)
        print ("Seu imc atual é: " + str(imc) + "\nVoce esta com peso: " + str(peso) +"\n Seu peso ideal é : "+str(pesoIdeal)+ "\n voce precisa perder: "+str(calculoPeso))
else:
        calculoPeso = float (pesoIdeal-peso)
        print ("Seu imc atual é: " + str(imc) + "\nVoce esta com peso: " + str(peso) +"\n Seu peso ideal é : "+str(pesoIdeal)+ "\n voce precisa ganhar: "+str(calculoPeso))

