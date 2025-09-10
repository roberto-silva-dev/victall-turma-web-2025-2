class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def envelhecer(self, anos):
        self.idade += anos
        return f"{self.nome} agora tem {self.idade} anos."

# Como usar?
pessoa1 = Pessoa("João", 30) 
print(pessoa1.apresentar()) # Olá, meu nome é João e tenho 30 anos.
print(pessoa1.envelhecer(5)) # João agora tem 35 anos.