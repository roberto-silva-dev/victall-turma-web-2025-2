while True:
    print("Calculadora do Roberto v2")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    tentativa = 1
    operacao = None
    while operacao is None:
        try:
            mensagem = "Qual operação? "
            if tentativa > 1:
                mensagem = "Não é um número. Escolha uma opção: "
            operacao = int(input(mensagem))
        except:
            pass
        tentativa = tentativa + 1

    if operacao == 0:
        print("Saindo ...")
        break
    if operacao not in [1, 2, 3, 4]:
        print("Opção inválida!")
        continue

    tentativa = 1
    numero1 = None
    while numero1 is None:
        try:
            mensagem = "Número 1: "
            if tentativa > 1:
                mensagem = "Não é um número. Número 1: "
            numero1 = float(input(mensagem))
        except:
            pass
        tentativa = tentativa + 1
    
    tentativa = 1
    numero2 = None
    while numero2 is None:
        try:
            mensagem = "Número 2: "
            if tentativa > 1:
                mensagem = "Não é um número. Número 2: "
            numero2 = float(input(mensagem))
        except:
            pass
        tentativa = tentativa + 1

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