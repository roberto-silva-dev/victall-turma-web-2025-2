
# Tutorial: Criando um Aplicativo Web de TODO com Django

## Configuração do Ambiente - Opcional
Crie e ative um ambiente virtual Python. Em seguida, instale o Django:
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
pip install django
```

## Criação do Projeto
Crie um novo projeto Django chamado `todoproject` e um app chamado `todo`:
```bash
django-admin startproject todoproject
cd todoproject
python manage.py startapp todo
```

Adicione `'todo'` em `INSTALLED_APPS` dentro de `todoproject/settings.py`.

## Configuração do Banco de Dados
O Django já vem configurado com SQLite3 por padrão. Apenas aplique as migrações iniciais:
```bash
python manage.py migrate
```

## Modelo TODO
No arquivo `todo/models.py`:
```python
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

Aplique a migração:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Views Baseadas em Função
Edite `todo/views.py`:
```python
from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('index')

def toggle(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
```

## URLs do App
Crie o arquivo `todo/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('toggle/<int:todo_id>/', views.toggle, name='toggle'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
```

E inclua no `todoproject/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
```

## Templates Django
Crie o diretório `todo/templates/todo/` e dentro dele o arquivo `index.html`:
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>TODO List</title>
</head>
<body>
    <h1>Minha Lista de Tarefas</h1>
    <form action="{% url 'add' %}" method="post">
        {% csrf_token %}
        <input type="text" name="title" placeholder="Nova tarefa">
        <button type="submit">Adicionar</button>
    </form>
    <ul>
        {% for todo in todos %}
        <li>
            <form action="{% url 'toggle' todo.id %}" method="post" style="display:inline;">
                {% csrf_token %}
                <button type="submit">
                    {% if todo.completed %}✅{% else %}⬜{% endif %}
                </button>
            </form>
            {{ todo.title }}
            <form action="{% url 'delete' todo.id %}" method="post" style="display:inline;">
                {% csrf_token %}
                <button type="submit">🗑</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Executando o Projeto
Inicie o servidor e acesse em `http://127.0.0.1:8000/`:
```bash
python manage.py runserver
```
