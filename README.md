# 🚀 FastAPI User Register API

API RESTful desenvolvida com **FastAPI** para gerenciamento de usuários (CRUD completo).
Projeto simples, rápido e didático — ideal para estudos e primeiros passos no backend com Python.

---

## 📘 Descrição

Esta API permite criar, listar, atualizar e deletar usuários.
Os dados são armazenados **em memória**, sem banco de dados, mas com estrutura preparada para evolução futura.

---

## 🎯 Objetivo

Este projeto foi criado para ajudar no aprendizado de:

* Estrutura de uma API com FastAPI
* Criação de rotas e métodos HTTP
* Uso de **Pydantic Models**
* Validação automática de dados
* Organização limpa e escalável

---

## 🧱 Arquitetura do Projeto

### 1️⃣ Modelos (Pydantic)

Responsáveis pela estrutura dos dados:

* Nome
* Idade
* CPF
* Email

---

### 2️⃣ Endpoints (CRUD)

| Método | Rota       | Descrição               |
| ------ | ---------- | ----------------------- |
| GET    | /User      | Lista todos os usuários |
| POST   | /User      | Cria um novo usuário    |
| GET    | /User/{id} | Busca usuário por ID    |
| PUT    | /User/{id} | Atualiza um usuário     |
| DELETE | /User/{id} | Remove um usuário       |

---

### 3️⃣ Armazenamento

* ✔ Lista Python (em memória)
* ❌ Banco de dados (não implementado)

---

## 🛠️ Tecnologias Utilizadas

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic

---

## 📌 Funcionalidades

* ✔ Criar usuários
* ✔ Validação automática de dados
* ✔ Listar usuários
* ✔ Buscar por ID
* ✔ Atualizar dados
* ✔ Deletar usuário
* ✔ Documentação automática (Swagger e ReDoc)

---

## 🚀 Como Rodar o Projeto

### 🔹 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd Fast_API-User-Register
```

---

### 🔹 2. (Opcional, recomendado) Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 🔹 3. Instalar dependências

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install fastapi uvicorn
```

---

### 🔹 4. Rodar a API

```bash
uvicorn main:app --reload
```

---

## 📄 Documentação automática

Após rodar o projeto:

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

## 📦 Gerando o requirements.txt

Caso queira gerar ou atualizar as dependências do projeto:

```bash
pip freeze > requirements.txt
```

---

## 🔮 Melhorias Futuras

* Banco de dados (SQLite / PostgreSQL)
* Autenticação JWT
* Arquitetura em camadas (routers, services, models)
* Testes automatizados
* Docker
* CI/CD
* Frontend consumindo a API

---

## 📂 Estrutura do Projeto

```
Fast_API-User-Register/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 👤 Autor

Desenvolvido por **Pablo Martins**

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

