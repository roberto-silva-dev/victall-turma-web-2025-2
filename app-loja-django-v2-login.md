# Tutorial da App Loja Django (v2) + Login por Sessão (App: autenticacao)

Este documento é uma versão atualizada do tutorial original, adicionando autenticação simples via sessão do Django (login / logout) através de um novo app chamado **autenticacao**, sem remover o código original da loja.

---

## Sumário

1. Visão geral do projeto  
2. Modelos (Models)  
3. Administração (Admin)  
4. Views e URLs da loja  
5. Templates da loja  
6. Criação do app `autenticacao`  
7. Autenticação via sessão  
   - Formulário de login  
   - Views de login / logout  
   - Middleware / mixins de proteção  
   - URLs de autenticação  
   - Templates de login / logout  
8. Detalhes adicionais e dicas  
9. Conclusão

---

## 1. Visão geral do projeto

*(Conteúdo original do tutorial até as views da loja, sem alterações.)*

## 2. Modelos (Models)

*(Mesmos models originais da loja.)*

## 3. Administração (Admin)

*(Sem alterações.)*

## 4. Views e URLs da loja

*(Views e URLs originais da loja, sem modificações.)*

## 5. Templates da loja

*(Mantenha os templates existentes: base, listagem de produtos, detalhe, carrinho, etc.)*

---

## 6. Criação do app `autenticacao`

Crie um novo app para gerenciar login e logout de usuários:

```bash
python manage.py startapp autenticacao
```

Adicione o app ao `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'autenticacao',
]
```

Crie também o diretório de templates:

```
autenticacao/
│
├── forms.py
├── views.py
├── urls.py
└── templates/
    └── autenticacao/
        └── login.html
```

---

## 7. Autenticação via sessão (login / logout)

### 7.1 Formulário de login (`autenticacao/forms.py`)

```python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
```

### 7.2 Views de login e logout (`autenticacao/views.py`)

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("loja:produto_list")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get("next") or reverse("loja:produto_list"))
            else:
                messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = LoginForm()
    return render(request, "autenticacao/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("autenticacao:login")
```

### 7.3 Protegendo views com login obrigatório

Use o decorator `login_required` nas views que exigem autenticação:

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url="autenticacao:login")
def minha_view_protegida(request):
    ...
```

Ou use o mixin em views baseadas em classe (CBV):

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class MinhaView(LoginRequiredMixin, View):
    login_url = "autenticacao:login"
```

### 7.4 URLs de autenticação (`autenticacao/urls.py`)

```python
from django.urls import path
from .views import login_view, logout_view

app_name = "autenticacao"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
```

Adicione no `urls.py` principal do projeto:

```python
from django.urls import path, include

urlpatterns = [
    path("autenticacao/", include("autenticacao.urls")),
    path("", include("loja.urls")),  # app da loja
]
```

### 7.5 Template de login (`templates/autenticacao/login.html`)

```html
{% extends "base.html" %}

{% block content %}
  <h2>Login</h2>
  {% if messages %}
    <ul class="messages">
      {% for msg in messages %}
        <li>{{ msg }}</li>
      {% endfor %}
    </ul>
  {% endif %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
  </form>
{% endblock %}
```

### 7.6 Ajustes no template base (`templates/base.html`)

```html
<nav>
  {% if user.is_authenticated %}
    <span>Olá, {{ user.username }}!</span>
    <form action="{% url 'autenticacao:logout' %}" method="post" style="display:inline;">
      {% csrf_token %}
      <button type="submit">Sair</button>
    </form>
  {% else %}
    <a href="{% url 'autenticacao:login' %}?next={{ request.path }}">Login</a>
  {% endif %}
</nav>
```

---

## 8. Detalhes adicionais

Verifique se `django.contrib.auth` e `django.contrib.sessions` estão ativos no `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    ...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
]
```

E defina os redirecionamentos padrão no arquivo `loja/settings.py`:

```python
LOGIN_URL = 'autenticacao:login'
LOGIN_REDIRECT_URL = 'loja:produto_list'
LOGOUT_REDIRECT_URL = 'autenticacao:login'
```

---

## 9. Conclusão

Você agora possui um sistema funcional de login por sessão no Django através do app **autenticacao**, integrado à aplicação da loja.  
Essa estrutura permite proteger partes específicas da aplicação (como checkout, área do cliente etc.) sem interferir nas demais funcionalidades já existentes.
