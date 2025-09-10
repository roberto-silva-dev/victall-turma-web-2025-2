class Saudacao:
    def dizer_ola(self, nome):
        return f"Olá, {nome}!"

# Como usar?
saudacao = Saudacao()
print(saudacao.dizer_ola("Ana"))  # Olá, Ana!