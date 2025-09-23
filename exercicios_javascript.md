# Exercícios de Introdução ao JavaScript

## Exercício 1: Alerta ao carregar a página
No seu arquivo `index.html`:
- Adicione um `<script>` que exiba um `alert("Bem-vindo!")` quando a página carregar.

---

## Exercício 2: Clique em botão
- Crie um botão com o texto "Clique aqui".
- Ao clicar no botão, mostre um alerta com a mensagem "Você clicou no botão!".

---

## Exercício 3: Alterar texto ao clicar
- Crie um parágrafo com algum texto.
- Ao clicar no parágrafo, o texto deve mudar para "Texto alterado!".

---

## Exercício 4: Hover em elemento
- Crie um `<div>` com um tamanho visível (ex: 150px x 150px) e cor de fundo.
- Ao passar o mouse sobre a `<div>`, a cor de fundo deve mudar.

---

## Exercício 5: Contador de cliques
- Crie um botão "Contar Cliques".
- Cada vez que o botão for clicado, aumente um número exibido ao lado do botão.

---

## Exercício 6: Input e exibição
- Crie um campo `<input>` e um botão "Mostrar Texto".
- Ao clicar no botão, exiba o texto digitado no input dentro de um parágrafo abaixo.

---

# Gabarito

## Exercício 1
```html
<script>
  window.onload = function() {
    alert("Bem-vindo!");
  }
</script>
```

## Exercício 2
```html
<button onclick="alert('Você clicou no botão!')">Clique aqui</button>
```

## Exercício 3
```html
<p id="meuParagrafo" onclick="this.innerText='Texto alterado!'">
  Clique neste parágrafo
</p>
```

## Exercício 4
```html
<div id="caixa" style="width:150px;height:150px;background-color:blue;"
     onmouseover="this.style.backgroundColor='red';"
     onmouseout="this.style.backgroundColor='blue';">
</div>
```

## Exercício 5
```html
<button id="botaoContar">Contar Cliques</button>
<span id="contador">0</span>

<script>
  let count = 0;
  document.getElementById('botaoContar').onclick = function() {
    count++;
    document.getElementById('contador').innerText = count;
  }
</script>
```

## Exercício 6
```html
<input type="text" id="meuInput">
<button onclick="document.getElementById('resultado').innerText = document.getElementById('meuInput').value;">
  Mostrar Texto
</button>
<p id="resultado"></p>
```
