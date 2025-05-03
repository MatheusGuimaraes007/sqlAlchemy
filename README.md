# 🐍 Projeto SQLAlchemy Assíncrono com MySQL

Este repositório foi criado como parte da aplicação prática do curso [SQLAlchemy Essencial](https://www.udemy.com/course/sql-alchemy-essencial/), onde aprendi a utilizar o **ORM SQLAlchemy** para manipulação de bancos de dados relacionais com foco em **boas práticas, modelagem e execução de queries**.

---

## 📚 O que você vai encontrar aqui

✅ Projeto completo utilizando **SQLAlchemy ORM** com **MySQL**  
✅ Estrutura com **Python Assíncrono**  
✅ Boas práticas de **modelagem**, **inserção**, **seleção**, **atualização** e **remoção** de dados  
✅ Experiência aplicada para integrar com frameworks como o **FastAPI**  

> 💡 Aprender SQLAlchemy dessa forma me permitiu entender na prática como estruturar uma aplicação mais escalável e moderna, com foco em performance e legibilidade de código.

---

## 🛠 Tecnologias utilizadas

- **Python 3.11+**
- **SQLAlchemy 2.0 (com suporte a async)**
- **MySQL** (pode ser facilmente adaptado para SQLite ou PostgreSQL)
- **AsyncMy** como driver
- **TQDM, Colorama** e outras libs auxiliares

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/MatheusGuimaraes007/sqlAlchemy.git
cd sqlAlchemy/05sqla_sync

```

### 2. Crie e ative um ambiente virtual
```bash
# Windows
python -m venv ambiente_05sqla_async
ambiente_05sqla_async\Scripts\activate

# Linux/macOS
python3 -m venv ambiente_05sqla_async
source ambiente_05sqla_async/bin/activate

```
### 3. Instale as dependências
```bash
pip install -r requirements.txt

```

### 4. Configure seu banco MySQL
No arquivo de configuração db_session.py, defina sua DATABASE_URL com as credenciais do seu banco local, por exemplo:
```python
DATABASE_URL = "mysql+asyncmy://usuario:senha@localhost:3306/nome_do_banco"

```
### 5. Execute os scripts conforme necessário
```bash
python create_main.py       # Cria as tabelas
python insert_main.py       # Insere dados
python select_main.py       # Faz queries
python update_main.py       # Atualiza dados
python delete_main.py       # Remove registros

```

