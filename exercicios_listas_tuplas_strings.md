
# Exercícios de Python – Listas, Tuplas e Strings

## 1. Listas
Crie uma lista com os números de 1 a 5.  
- Adicione o número 6 no final.  
- Insira o número 0 no início.  
- Remova o número 3.  
- Mostre a lista final.  

**Sugestão:**  
```python
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.insert(0, 0)
numeros.remove(3)
print(numeros)  # [0, 1, 2, 4, 5, 6]
```

---

## 2. Tuplas
Crie uma tupla com os nomes de 3 cores.  
- Tente alterar uma cor (o que acontece?).  
- Acesse a segunda cor.  

**Sugestão:**  
```python
cores = ("vermelho", "verde", "azul")
# cores[0] = "amarelo"  # ERRO: tuplas são imutáveis
print(cores[1])  # verde
```

---

## 3. Strings
Dada a string `"Python é incrível"`, faça:  
- Mostre a quantidade de caracteres.  
- Transforme em maiúsculas.  
- Substitua `"incrível"` por `"poderoso"`.  
- Inverta a string.  

**Sugestão:**  
```python
texto = "Python é incrível"
print(len(texto))  # 16
print(texto.upper())  # PYTHON É INCRÍVEL
print(texto.replace("incrível", "poderoso"))  # Python é poderoso
print(texto[::-1])  # levírcni é nohtyP
```

---

## 4. Desafio combinado
- Crie uma lista com 5 palavras.  
- Transforme essa lista em uma tupla.  
- Una todas as palavras em uma única string, separadas por espaço.  

**Sugestão:**  
```python
palavras = ["eu", "amo", "programar", "em", "python"]
tupla_palavras = tuple(palavras)
frase = " ".join(tupla_palavras)
print(frase)  # eu amo programar em python
```
