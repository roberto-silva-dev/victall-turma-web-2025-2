# Tutorial: App de gerenciamneto de produtos em Django (views function-based + templates)
---

## Pré-requisitos

- Python 3.8+ instalado.
- Noções básicas de terminal.
- Django instalado em ambiente virtual.

Criação e ativação do ambiente:

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\Activate.ps1

pip install django
```

---

## Criar o projeto e app

```bash
django-admin startproject loja .
python manage.py startapp produtos
```

---

## Configurações em settings.py

No arquivo `loja/settings.py`:

- Adicione `'produtos'` em `INSTALLED_APPS`.

```py
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'produtos',
]
```

---

## Criar o model (models.py)

Um produto simples terá: nome, preço e descrição.

```py
# produtos/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
```

Gerar e aplicar migrações:

```bash
python manage.py makemigrations produtos
python manage.py migrate
```

---

## Criar o formulário (forms.py)

```py
# produtos/forms.py
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao']
```

---

## Criar as views function-based

```py
# produtos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all().order_by('-criado_em')
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:lista')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:lista')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form, 'produto': produto})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos:lista')
    return render(request, 'produtos/confirma_exclusao.html', {'produto': produto})
```

---

## Configurar URLs

`produtos/urls.py`:

```py
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista'),
    path('novo/', views.novo_produto, name='novo'),
    path('editar/<int:pk>/', views.editar_produto, name='editar'),
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir'),
]
```

E no `loja/urls.py`:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),
]
```

---

## Templates

Crie a pasta `templates/produtos/` dentro do app `produtos` e adicione os arquivos abaixo.

`templates/base.html`:

```html
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Loja{% endblock %}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    {% block content %}{% endblock %}
  </div>
</body>
</html>
```

`templates/produtos/lista.html`:

```html
{% extends 'base.html' %}
{% block title %}Produtos{% endblock %}
{% block content %}
<h1>Lista de Produtos</h1>
<a href="{% url 'produtos:novo' %}" class="btn btn-primary mb-3">Novo Produto</a>
<table class="table table-bordered">
  <thead>
    <tr><th>Nome</th><th>Preço</th><th>Descrição</th><th>Ações</th></tr>
  </thead>
  <tbody>
  {% for produto in produtos %}
    <tr>
      <td>{{ produto.nome }}</td>
      <td>R$ {{ produto.preco }}</td>
      <td>{{ produto.descricao|default:'-' }}</td>
      <td>
        <a href="{% url 'produtos:editar' produto.pk %}" class="btn btn-warning btn-sm">Editar</a>
        <a href="{% url 'produtos:excluir' produto.pk %}" class="btn btn-danger btn-sm">Excluir</a>
      </td>
    </tr>
  {% empty %}
    <tr><td colspan="4">Nenhum produto cadastrado.</td></tr>
  {% endfor %}
  </tbody>
</table>
{% endblock %}
```

`templates/produtos/form.html`:

```html
{% extends 'base.html' %}
{% block title %}Cadastro de Produto{% endblock %}
{% block content %}
<h1>{% if produto %}Editar{% else %}Novo{% endif %} Produto</h1>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit" class="btn btn-primary">Salvar</button>
  <a href="{% url 'produtos:lista' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

`templates/produtos/confirma_exclusao.html`:

```html
{% extends 'base.html' %}
{% block title %}Excluir Produto{% endblock %}
{% block content %}
<h1>Excluir Produto</h1>
<p>Tem certeza que deseja excluir o produto <strong>{{ produto.nome }}</strong>?</p>
<form method="post">
  {% csrf_token %}
  <button type="submit" class="btn btn-danger">Sim, excluir</button>
  <a href="{% url 'produtos:lista' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## Testar e rodar servidor

```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/`

Cadastre produtos e teste edição e exclusão.

---

## Exercícios extras para alunos

- Adicionar campo `estoque` (IntegerField) e exibir na tabela.
- Criar filtro de produtos acima de determinado preço.
- Implementar busca simples por nome.
- Exibir a data de criação formatada (use filtro `date` no template).

---

## Objetivo

- Praticar o fluxo completo: **Model → Form → View → Template → QuerySet**.
- Com esse CRUD clássico, aprenderá conceitos de ORM e renderização dinâmica no Django.

