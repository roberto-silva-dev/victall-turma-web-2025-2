class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []

    def adicionar_nota(self, nota):
        # self.notas é uma lista, então usamos o método append para adicionar um item (no caso, uma nota)
        self.notas.append(nota)

    def calcular_media(self):
        # Usamos a função len() para obter o tamanho da lista self.notas
        # Usamos a função sum() para somar todos os números de uma lista
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def apresentar(self):
        media = self.calcular_media()
        return f"{self.nome}, {self.idade} anos, Média: {media:.2f}"


# Exemplo de uso
aluno = Aluno("Carlos", 20)
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(9.0)
aluno.adicionar_nota(7.5)

print(aluno.apresentar())  # Saída: Carlos, 20 anos, Média: 8.33
