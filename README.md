---

## 🧠Funcionalidades.
- Cadastro, edição e exclusão de Pokémons com tipos primário e secundário (opcional).
- Cadastro, edição e exclusão dos tipos de Pokémons.
- Listagem e filtro dos Pokémons e tipos cadastrados.
- Interface responsiva com formulários e selects para facilitar a escolha dos tipos.
- Feedback ao usuário via mensagens flash.
- Persistência dos dados usando SQLAlchemy.

---

## 🛠️ Ferramentas e Tecnologias Utilizadas:
Flask – Microframework em Python para desenvolvimento web.

SQLAlchemy – ORM (Object Relational Mapper) usado para manipulação do banco de dados.

PostgreSQL – Banco de dados relacional utilizado no projeto.

HTML/CSS – Para estruturação e estilização da interface web.

Jinja2 – Motor de templates utilizado pelo Flask.

Python – Linguagem principal do projeto.


## ✅ Principais dependências.
Flask – Framework web principal.

psycopg2-binary – Driver para PostgreSQL.

SQLAlchemy – ORM usado para comunicação com o banco de dados.

Werkzeug – (Instalado automaticamente com Flask, mas relevante para sessões e flash).

Jinja2 – (Instalado com Flask; usado para renderizar templates HTML).


## Instalação e execução local.

### 1. Clone o repositório (ou baixe o ZIP).
Configure sua conexão com o banco no arquivo conexao.py (ou conforme sua estrutura).

Certifique-se que o banco está criado e acessível.

### 2. Instale as dependências.
Utilize o pip para instalar as bibliotecas necessárias:

pip install flask <br>
pip install sqlalchemy <br>
pip install psycopg2-binary

### 3. Configure o banco de dados e crie o database.
Crie seu database manualmente, caso queira usar outro SGBD, atente-se à estrutura da string de conexão.

string de conexão para o PostgresSQL - postgresql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>

No arquivo "conexao.py", verifique se a string de conexão com o banco está definida corretamente.


### 4. Rode o projeto.
Rode o arquivo "main.py" uma vez para estabelecer a conexão, em seguida rode o arquivo "base_de_dados.py" para povoar as tabelas.

### 5. Tabelas carregadas e projeto funcionando.
Execute novamente o arquivo "main.py" para estabelecer a conexão e acessar o sistema.

### 6. 	Link do vídeo no YouTube mostrando o projeto.
https://youtu.be/Q104AfhqpbU?si=AZs2u4JSwVQ_dtgp
