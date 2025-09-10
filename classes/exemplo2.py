class Saudacao:
    def __init__(self, nome):
        self.nome = nome

    def dizer_ola(self):
        return f"Olá, {self.nome}!"

# Como usar?
saudacao = Saudacao("Ana")
print(saudacao.dizer_ola())  # Olá, Ana!