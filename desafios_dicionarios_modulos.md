
# 📘 Desafios em Python – Dicionários, módulos e pacotes

Este material contém exercícios simples para você praticar **dicionários**, **módulos** e **pacotes** em Python.  
Leia com atenção cada enunciado e tente resolver antes de olhar o gabarito no final.

---

### 📝 Desafio – Cadastro simples
Crie um programa que use um **dicionário** para guardar os dados de um aluno:
- Nome
- Idade
- Curso  

Depois, mostre as informações no formato:
```
Nome: João
Idade: 20
Curso: Informática
```

---

### 📝 Desafio – Tradutor de cores
Crie um dicionário com algumas cores em inglês como chave e a tradução em português como valor.  
Exemplo:
```python
{"red": "vermelho", "blue": "azul", "green": "verde"}
```

Peça ao usuário para digitar uma cor em inglês e mostre a tradução em português.  
Se a cor não existir no dicionário, mostre a mensagem: `"Cor não encontrada"`.

---

### 📝 Desafio – Agenda de contatos
Crie um programa que permita registrar contatos em um dicionário:
- A chave deve ser o nome da pessoa.
- O valor deve ser o número de telefone.  

Depois, peça ao usuário um nome e mostre o telefone correspondente.

---

### 📝 Desafio – Seu próprio módulo
Crie um arquivo chamado `meu_modulo.py` com uma função:
```python
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao estudo de módulos."
```
Depois, em outro arquivo Python, importe o módulo e use a função `saudacao`.

---

---

### 📝 Desafio – Pacote simples
Crie uma pasta chamada `utilidades` com dois arquivos:
- `texto.py` → função `conta_caracteres(txt)` que conta e retorna o número de letras de um texto.
- `matematica.py` → função `dobro(n)` que devolve o dobro de um número.

No programa principal, importe e use as duas funções.

---


# ✅ Gabarito dos Desafios

## Desafio – Cadastro simples
```python
aluno = {"nome": "João", "idade": 20, "curso": "Informática"}

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])
```

---

## Desafio – Tradutor de cores
```python
cores = {"red": "vermelho", "blue": "azul", "green": "verde"}

entrada = input("Digite uma cor em inglês: ")

if entrada in cores:
    print("Tradução:", cores[entrada])
else:
    print("Cor não encontrada")
```

---

## Desafio – Agenda de contatos
```python
agenda = {"Maria": "9999-1111", "João": "8888-2222"}

nome = input("Digite o nome do contato: ")

if nome in agenda:
    print("Telefone:", agenda[nome])
else:
    print("Contato não encontrado")
```

---

## Desafio – Seu próprio módulo
**meu_modulo.py**
```python
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao estudo de módulos."
```

**principal.py**
```python
import meu_modulo

print(meu_modulo.saudacao("Ana"))
```

---

## Desafio – Pacote simples
**utilidades/texto.py**
```python
def conta_caracteres(txt):
    return len(txt)
```

**utilidades/matematica.py**
```python
def dobro(n):
    return n * 2
```

**principal.py**
```python
from utilidades import texto, matematica

print("Caracteres:", texto.conta_caracteres("Olá"))
print("Dobro:", matematica.dobro(5))
```
