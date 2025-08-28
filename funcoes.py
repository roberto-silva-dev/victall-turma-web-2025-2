# Definindo a função numero_par
# Essa função recebe um número como entrada (parâmetro)
# e retorna True se o número for par, ou False se for ímpar.
def numero_par(numero):
    if numero % 2 == 0:   # verifica se o resto da divisão por 2 é zero
        return True
    else:
        return False


# Programa principal
# Aqui vamos usar um loop for para percorrer os números de 1 a 20
for n in range(1, 21):
    # Chamamos a função numero_par passando o número atual (n)
    if numero_par(n):  # se a função retornar True
        print(f"O número {n} é par")
    else:              # se a função retornar False
        print(f"O número {n} é ímpar")