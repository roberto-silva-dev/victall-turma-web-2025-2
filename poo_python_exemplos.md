# Programação Orientada a Objetos em Python

Exemplos didáticos com explicações rápidas.

---

## 1. Classe e Objeto
```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"O {self.marca} {self.modelo} está ligado!")

# Criando objetos
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

carro1.ligar()
carro2.ligar()
```
➡️ Aqui temos classe, construtor (`__init__`) e métodos de instância.

---

## 2. Encapsulamento
```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria("Roberto", 100)
conta.depositar(50)
conta.sacar(30)
print(conta.ver_saldo())  # 120
```
➡️ `__saldo` não pode ser acessado diretamente, só por métodos.

---

## 3. Herança
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} está falando...")

class Aluno(Pessoa):  # herda de Pessoa
    def estudar(self):
        print(f"{self.nome} está estudando.")

class Professor(Pessoa):  # herda de Pessoa
    def ensinar(self):
        print(f"{self.nome} está ensinando.")

aluno = Aluno("Beto")
prof = Professor("João")

aluno.falar()
aluno.estudar()
prof.falar()
prof.ensinar()
```
➡️ Reuso de código por herança.

---

## 4. Polimorfismo
```python
class Animal:
    def falar(self):
        raise NotImplementedError("Implemente o método falar!")

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

animais = [Cachorro(), Gato()]

for a in animais:
    print(a.falar())
```
➡️ Mesmo método (`falar`), comportamentos diferentes.

---

## 5. Abstração (usando ABC)
```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

quad = Quadrado(5)
print(quad.area())  # 25
```
➡️ Classe abstrata define contrato que as filhas devem cumprir.
