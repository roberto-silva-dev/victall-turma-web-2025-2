
# Exercícios Extras de Python – Listas, Tuplas e Strings

## 1. Listas
Crie uma lista com os números pares de 2 a 10.  
- Adicione o número 12 ao final.  
- Conte quantos elementos existem na lista.  
- Inverta a ordem da lista.  

**Sugestão:**  
```python
pares = [2, 4, 6, 8, 10]
pares.append(12)
print(len(pares))  # 6
pares.reverse()
print(pares)  # [12, 10, 8, 6, 4, 2]
```

---

## 2. Tuplas
Crie uma tupla com 4 cidades.  
- Mostre a primeira e a última cidade.  
- Verifique se `"São Paulo"` está na tupla.  

**Sugestão:**  
```python
cidades = ("Rio de Janeiro", "São Paulo", "Belo Horizonte", "Curitiba")
print(cidades[0])  # Rio de Janeiro
print(cidades[-1])  # Curitiba
print("São Paulo" in cidades)  # True
```

---

## 3. Strings
Dada a string `"aprendendo python"`, faça:  
- Coloque a primeira letra em maiúscula.  
- Verifique se a string começa com `"apr"`.  
- Separe as palavras em uma lista.  

**Sugestão:**  
```python
texto = "aprendendo python"
print(texto.capitalize())  # Aprendendo python
print(texto.startswith("apr"))  # True
print(texto.split())  # ['aprendendo', 'python']
```

---

## 4. Desafio combinado
- Crie uma lista com 3 números inteiros.  
- Converta essa lista em uma string no formato `"n1-n2-n3"`.  
- Depois, transforme a string de volta em lista.  

**Sugestão:**  
```python
numeros = [5, 10, 15]
texto = "-".join(map(str, numeros))
print(texto)  # "5-10-15"
lista_novamente = texto.split("-")
print(lista_novamente)  # ['5', '10', '15']
```

