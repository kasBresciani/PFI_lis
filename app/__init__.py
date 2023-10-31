from flask import Flask, session # Importa a classe principal (Flask)
from flask_sqlalchemy import SQLAlchemy # Importa a ORM SQLAlchemy

app = Flask(__name__) # Cria uma instância do Flask na a variável app


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True # Ativa o rastreamento de modificações
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@127.0.0.1/inclusion" # Define a URL do banco de dados
app.secret_key = "q4t7w!z%C*F-JaNd" # Define uma chave de segurança para a aplicação

db = SQLAlchemy(app) # Cria uma instância da ORM

@app.context_processor # Cria um contexto global, de forma que todas as páginas tenham acesso a sessão do usuário
def injetar_sessao():
    return dict(session=session)

from app.controllers import paginas # Importa as rotas da aplicação
from app.controllers import usuarioController
from app.controllers import mensagemController
from app.controllers import profissionalController