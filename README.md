# Documentação da API

## Visão Geral

Esta API permite a criação, leitura, atualização e exclusão de usuários e postagens de blog.

**Base URL**: `127.0.0.1:8000/admin/` painel adminitrativo do django

---

## Recursos da API

### 1. Usuários

#### 1.1 Listar Usuários

- **Endpoint**: `GET 127.0.0.1:8000/api/`

#### 1.2 Listar Usuário pelo nome

- **Endpoint**: `GET 127.0.0.1:8000/user/<str:nick>`

---

## Model

### Classe `User(models.Model)`

### Comandos importantes para ambiente

**criar ambiente virtual
python -m venv venv

**ativar ambiente
./venv/Scripts/activate

**instalar bibliotecas
pip install -r requirements.txt

**comando para rodar aplicação
py manage.py runserver

**comando para criar banco
py manage.py makemigrations

**comando para criar dados no banco
py manage.py migrate

**comando para criar um usuario
py manage.py createsuperuser
username:enascente
email: "emanuel@teste"
password:teste

**comando para rodar aplicação
py manage.py runserver
