# Importa as funções necessárias do módulo Flask
from flask import render_template, redirect, url_for
# Importa a instância Flask e a sessão a partir do módulo app
from app import app, session

from app.model.Usuario import Usuario
from app.controllers.mensagemController import retornar_mensagens
from app.controllers.usuarioController import retornar_usuarios
from app.controllers.profissionalController import retornar_profissionais

import base64

# Define a rota para a página inicial
@app.route("/")
def index():
    if 'email' in session:
        return redirect(url_for('geral'))
    return render_template('index.html')

# Define a rota para a página de cadastro
@app.route("/cadastrar", methods=['GET'])
def cadastrar():
    if 'email' in session:
        return redirect(url_for('geral'))
    return render_template('cadastro.html')

# Define a rota para a página de login
@app.route("/entrar", methods=['GET'])
def entrar():
    if 'email' in session:
        return redirect(url_for('geral'))
    return render_template('login.html')

# Define a rota para a página geral, verificando se a sessão está ativa
@app.route("/geral", methods=['GET'])
def geral():
    if 'email' in session:
        mensagens = tratar_mensagens()
        print("#############")
        print(retornarImagem())
        return render_template('geral.html', foto=retornarImagem(), mensagens=mensagens)
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('index'))

# Define a rota para a página de contato, verificando se a sessão está ativa
@app.route("/contato", methods=['GET'])
def contato():
    if 'email' in session:

        profissionais = retornar_profissionais()

        return render_template('contato.html', foto=retornarImagem(), profissionais=profissionais)
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('index'))

# Define a rota para a página "tea", verificando se a sessão está ativa
@app.route("/tea", methods=['GET'])
def tea():
    if 'email' in session:
        return render_template('tea.html', foto=retornarImagem())
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('index'))

# Define a rota para a página de acidentes, verificando se a sessão está ativa
@app.route("/acidentes", methods=['GET'])
def acidentes():
    if 'email' in session:
        return render_template('acidentes.html', foto=retornarImagem())
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('index'))

# Define a rota para a página de educação, verificando se a sessão está ativa
@app.route("/educacao", methods=['GET'])
def educacao():
    if 'email' in session:
        return render_template('educacao.html', foto=retornarImagem())
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('index'))

# Define a rota para a página de terceira idade, verificando se a sessão está ativa
@app.route("/terceira-idade", methods=['GET'])
def terceira_idade():
    if 'email' in session:
        return render_template('terceira-idade.html', foto=retornarImagem())
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('index'))

# Define a rota para a página de postagem, verificando se a sessão está ativa
@app.route("/postar", methods=['GET'])
def postar():
    if 'email' in session:
        return render_template('postar.html', foto=retornarImagem())
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('index'))

@app.route("/alterar-foto", methods=['get'])
def foto():
    if 'email' in session:
        return render_template('alterar-foto.html', foto=retornarImagem())
    # Se a sessão não estiver ativa, redireciona para a página inicial
    return redirect(url_for('index'))

@app.route("/postar-profissional", methods=['GET'])
def postar_profissional():
    if 'email' in session:
        return render_template('adicionar-profissional.html', foto=retornarImagem())
    # Se a sessão não estiver ativa, redirecione para a página inicial
    return redirect(url_for('adicionar_profissional.html'))

@app.route("/adm", methods=['GET']) # Rota para abrir o painel de administrador
def painel_adm():
    if ('email' in session) and (session['adm'] == True): # Verifica se o usuário está logado e se é administrador

        mensagens = tratar_mensagens()
        profissionais = retornar_profissionais()

        return render_template('administrar.html', mensagens=mensagens, profissionais=profissionais) # Carrega o painel de adm
    return redirect(url_for('geral'))

def retornarImagem():
    usuario = Usuario.query.filter_by(email=session['email']).first().toJson()
    return base64.b64encode(usuario['foto']).decode('utf-8')


def tratar_mensagens():
    mensagens = retornar_mensagens()
    mensagens = retornar_usuarios(mensagens)
    return mensagens