try:
    # lança erro se o usuário digitar texto ao invés de número
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    
    # lança erro de divisão por zero se numero2 for zero
    print(numero1/numero2)
except:
    print("Houve um erro!")
