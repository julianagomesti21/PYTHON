print("Qual humorista você escolheu?")
print("[1] Fábio Porchat")
print("[2] Danilo Gentili")
print("[3] Rafinha Bastos")
humorista = int(input("Digite o número correspondente ao humorista: "))

cidade = input("Em qual cidade você está? ")

if (humorista == 1 and cidade == "araxá"):
    idade = int(input("Qual a sua idade? "))
    if (idade >= 18):
        print("Tem show do Fábio Porchat em Araxá!")
    else:
        print("Você precisa ter 18 anos ou mais para assistir ao show do Fábio Porchat em Araxá.")
elif (humorista == 2 and cidade == "são paulo"):
    print("Tem show do Danilo Gentili em São Paulo!")
elif (humorista == 3 and cidade == "rio grande do sul"):
    print("Tem show do Rafinha Bastos no Rio Grande do Sul!")
else:
    print("Não tem show do humorista escolhido na cidade informada.")
