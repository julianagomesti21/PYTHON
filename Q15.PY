print("Seu conhecimento de Excel é:")
print("[1] Básico")
print("[2] Intermediário")
print("[3] Avançado")
nivel = int(input("Digite o número correspondente ao seu nível de conhecimento: "))

if (nivel == 1):
    print("\nEscolha uma fórmula dentre as opções abaixo:")
    print("[1] SOMA")
    print("[2] MÉDIA")
    print("[3] MÁXIMO")
    escolha = int(input("Digite o número correspondente à fórmula: "))
    if (escolha == 1):
        print("A fórmula =SOMA")
    elif (escolha == 2):
        print("A fórmula =MÉDIA")
    elif (escolha == 3):
        print("A fórmula =MÁXIMO")
    else:
        print("Opção inválida.")

elif (nivel == 2):
    print("\nEscolha uma fórmula dentre as opções abaixo:")
    print("[1] SE")
    print("[2] SOMASE")
    print("[3] CONT.SE")
    escolha = int(input("Digite o número correspondente à fórmula: "))
    if escolha == 1:
        print("A fórmula =SE")
    elif escolha == 2:
        print("A fórmula =SOMASE")
    elif escolha == 3:
        print("A fórmula =CONT.SE")
    else:
        print("Opção inválida.")
   
elif (nivel == 3):

    print("\nEscolha uma fórmula dentre as opções abaixo:")
    print("[1] ORDEM.EQ")
    print("[2] PROCV")
    print("[3] PROCH")
    escolha = int(input("Digite o número correspondente à fórmula: "))
    if escolha == 1:
        print("A fórmula =ORDEM.EQ")
    elif escolha == 2:
        print("A fórmula =PROCV")
    elif escolha == 3:
        print("A fórmula =PROCH")
    else:
        print("Opção inválida.")
   
else:
    print("Opção inválida.")