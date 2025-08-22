while True:
    print("Calculadora do Roberto v2")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = int(input("Qual operação? "))
    if operacao == 0:
        print("Saindo ...")
        break
    if operacao not in [1, 2, 3, 4]:
        print("Opção inválida!")
        continue

    numero1 = float(input("Número 1: "))
    numero2 = float(input("Número 2: "))

    if operacao == 1:
        print("A soma de", numero1, "e", numero2, "é", numero1+numero2)
    elif operacao == 2:
        print("A subtração de", numero1, "e", numero2, "é", numero1-numero2)
    elif operacao == 3:
        print("A multiplicação de", numero1, "e", numero2, "é", numero1*numero2)
    elif operacao == 4:
        if numero2 == 0:
            print("Divisão por zero não permitida!")
            continue
        print("A divisão de", numero1, "por", numero2, "é", numero1/numero2)