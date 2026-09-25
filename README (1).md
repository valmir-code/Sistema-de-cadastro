# Sistema de Cadastro e Login com PostgreSQL

Projeto back-end simples em Python para praticar conexão com banco de dados PostgreSQL, usando a biblioteca `psycopg2`. O sistema permite cadastrar um usuário e realizar login com validação de tentativas.

## 🎯 Objetivo

Praticar conceitos de back-end como:
- Conexão com banco de dados relacional (PostgreSQL)
- Execução de queries SQL (INSERT e SELECT) via Python
- Manipulação de cursor e commits
- Lógica de autenticação com controle de tentativas

## 🛠️ Tecnologias

- Python 3
- PostgreSQL
- psycopg2

## 📋 Pré-requisitos

- Python instalado
- PostgreSQL instalado e rodando
- Biblioteca `psycopg2` instalada:

```bash
pip install psycopg2
```

## 🗄️ Estrutura do banco

Crie um banco de dados e a tabela `usuarios` antes de rodar o projeto:

```sql
CREATE DATABASE teste_cadastro;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);
```

## ⚙️ Configuração

No arquivo principal, ajuste os dados de conexão de acordo com o seu ambiente:

```python
conexao = psycopg2.connect(
    host="localhost",
    database="teste_cadastro",
    user="postgres",
    password="sua_senha",
    port="5432"
)
```

## ▶️ Como executar

```bash
python nome_do_arquivo.py
```

O programa vai:
1. Pedir nome, e-mail e senha para cadastrar um novo usuário
2. Em seguida, pedir e-mail e senha para login
3. Permitir até 3 tentativas de login antes de bloquear o acesso

## 📌 Observações

Este é um projeto de estudo focado em lógica de back-end e integração com banco de dados. Por simplicidade, as senhas são armazenadas em texto puro — em uma aplicação real, o recomendado é usar hash (ex: `bcrypt`) para armazenar senhas com segurança.

## 📄 Licença

Projeto de estudo, livre para uso e modificação.
