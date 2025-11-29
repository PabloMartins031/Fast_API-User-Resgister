📘 Descrição Completa do Projeto — FastAPI User Register API

Este projeto é uma API RESTful desenvolvida em FastAPI com o objetivo de realizar operações de CRUD (Create, Read, Update, Delete) para gerenciamento de usuários.
Simples, rápida e totalmente didática — ideal para estudos, testes e primeiros passos no backend com Python.

A API funciona 100% em memória, sem banco de dados, mas sua estrutura foi preparada para expansão futura, permitindo facilmente adicionar SQLite, PostgreSQL ou qualquer outro banco.

🎯 Objetivo do Projeto

O principal objetivo deste projeto é servir como uma base sólida para estudos, permitindo que o usuário aprenda:

Estrutura fundamental de um projeto FastAPI

Criação de rotas e métodos HTTP

Uso de modelos (Pydantic Models)

Validação de dados automaticamente

Organização limpa e extensível para APIs reais

É um ponto de partida excelente para quem deseja evoluir para APIs maiores.

🧱 Arquitetura do Projeto
1️⃣ Modelos (Pydantic Models)

Responsáveis pela definição da estrutura dos dados dos usuários, incluindo:

Nome

Idade

CPF

Email

O FastAPI usa esses modelos para validar automaticamente tudo o que entra e sai da API.

2️⃣ Rotas da API (Endpoints)

A aplicação oferece endpoints completos para CRUD:

Método	Rota	Descrição
GET	/User	Lista todos os usuários
POST	/User	Cria um novo usuário
GET	/User/{id}	Busca usuário específico
PUT	/User/{id}	Atualiza usuário existente
DELETE	/User/{id}	Deleta um usuário
3️⃣ Armazenamento

Os dados são armazenados em:

✔ Uma lista Python
❌ Banco de dados (não implementado)

Esse formato é perfeito para estudo e facilita entender o funcionamento interno das operações.

🛠️ Tecnologias Utilizadas

Python 3.10+

FastAPI — Framework rápido e moderno

Uvicorn — Servidor ASGI

Pydantic — Validação de dados

📌 Funcionalidades Implementadas

✔ Criar usuários
✔ Validar automaticamente os dados enviados
✔ Listar todos os usuários
✔ Buscar usuário por ID
✔ Atualizar dados
✔ Deletar usuário
✔ Documentação automática via Swagger
✔ Código limpo, simples e educativo

🔮 Melhorias Futuras (Roadmap)

O projeto está preparado para receber:

Persistência com banco de dados (SQLite / PostgreSQL / etc.)

Autenticação JWT

Divisão por camadas (routers, services, models)

Testes automatizados

Containerização com Docker

CI/CD

Frontend simples utilizando a API

🚀 Como Rodar o Projeto
pip install fastapi uvicorn
uvicorn main:app --reload

📄 Documentação automática:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📂 Estrutura do Projeto
Fast_API-User-Register/
│── main.py
│── README.md
│── .gitignore

👤 Autor

Projeto criado com dedicação por Pablo Martins.
Este repositório é aberto para sugestões, melhorias e contribuições.
