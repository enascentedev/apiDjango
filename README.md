# Documentação da API

## Visão Geral

Esta API permite a criação, leitura, atualização e exclusão de usuários e postagens de blog.

**Base URL**: `hhttp://127.0.0.1:8000/api/`

---

## Recursos da API

### 1. Usuários

#### 1.1 Listar Usuários

- **Endpoint**: `GET /api/users/`

---

## Model

### Classe `User(models.Model)`


### comandos importantes para ambiente 
	**ativar ambiente
	./venv/Scripts/activate

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