for n in range(2, 51):  # números de 2 até 50
    eh_primo = True
    for i in range(2, n):  # testa todos menores que n
        if n % i == 0:  # se dividir exato, não é primo
            eh_primo = False
            break
    if eh_primo:
        print(n)