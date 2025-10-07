# Exercícios de HTML Básico
## Exercício 1: Estrutura básica do HTML
Crie um arquivo `index.html` com a estrutura mínima de um documento HTML.

### Requisitos:
- Deve ter `<!DOCTYPE html>`.
- Deve ter `<html>`, `<head>` e `<body>`.

---

## Exercício 2: Títulos e parágrafos
No corpo do documento:
- Crie um título principal (`<h1>`) escrito "Meu Primeiro Site".
- Crie dois parágrafos (`<p>`) com qualquer texto.

---

## Exercício 3: Links e imagens
- Adicione um link (`<a>`) para `https://www.google.com` com o texto "Ir para o Google".  
- Adicione uma imagem (`<img>`) qualquer da internet.

---

## Exercício 4: Listas
- Crie uma lista ordenada (`<ol>`) com 3 itens.  
- Crie uma lista não ordenada (`<ul>`) com 3 itens.

---

## Exercício 5: CSS Inline
- Adicione um parágrafo com a cor do texto **vermelho** usando `style` direto na tag.

---

## Exercício 6: CSS Interno
No mesmo arquivo `index.html`, dentro da tag `<head>`, adicione um `<style>` e defina:  
- O corpo da página (`body`) com cor de fundo **cinza**.  
- Os títulos `<h1>` com cor **azul**.

---

## Exercício 7: CSS Externo
- Crie um arquivo `style.css`.  
- Nesse arquivo, defina que os parágrafos (`p`) tenham cor **verde**.  
- No `index.html`, faça a ligação com esse arquivo usando `<link rel="stylesheet">`.

---

# Gabarito

## Exercício 1
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo</title>
</head>
<body>
</body>
</html>
```

## Exercício 2
```html
<h1>Meu Primeiro Site</h1>
<p>Este é o primeiro parágrafo.</p>
<p>Este é o segundo parágrafo.</p>
```

## Exercício 3
```html
<a href="https://www.google.com">Ir para o Google</a>
<img src="https://via.placeholder.com/150" alt="Imagem de exemplo">
```

## Exercício 4
```html
<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>

<ul>
  <li>Item A</li>
  <li>Item B</li>
  <li>Item C</li>
</ul>
```

## Exercício 5
```html
<p style="color: red;">Texto em vermelho</p>
```

## Exercício 6
```html
<head>
  <style>
    body { background-color: gray; }
    h1 { color: blue; }
  </style>
</head>
```

## Exercício 7
**Arquivo style.css:**
```css
p {
  color: green;
}
```

**No index.html:**
```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```
