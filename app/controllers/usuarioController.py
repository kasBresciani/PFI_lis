from flask import request, redirect, url_for, session, flash
from datetime import datetime
import base64
from app import app, db

from app.model.Usuario import Usuario

@app.route('/cadastrar', methods=['POST']) # rota para inserir novo usuário no banco
def adicionar_usuario():
    nome = request.form['nome'] # Coleta os dados do usuário
    email = request.form['email']
    senha = request.form['senha']
    foto = None

    if 'foto' in request.files: # Verifica se existe uma foto na requisição
        foto = request.files['foto']

    data_nascimento = datetime.strptime(request.form['data_nascimento'], '%Y-%m-%d') # Calcula a data de nascimento

    hoje = datetime.now() # Verifica a data atual
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)) # Calcula a idade

    if (idade < 12): # Verifica se possui menos de 12 anos
        flash('Idade mínima de 12 anos para cadastro na plataforma!')
        return redirect(url_for('cadastrar')) # Redireciona para a página de cadastro

    try:

        novo_usuario = Usuario( # Instancia o novo usuário
            nome=nome,
            email=email,
            senha=senha,
            foto=foto.read()
        )

        db.session.add(novo_usuario) # Adiciona o novo usuário no banco
        db.session.commit() # Salva as alterações do banco

        session['email'] = email # Coloca o novo usuário em sessão
        session['adm'] = False

        return redirect(url_for('geral')) # Redireciona para a página principal da aplicação
    except:
        flash('Email já cadastrado!')
        return redirect(url_for('cadastrar'))

@app.route('/entrar', methods=['POST']) # Rota para fazer login
def fazer_login():
    email = request.form['email'] # Coleta os dados
    senha = request.form['senha']

    usuario = Usuario.query.filter_by(email=email).first() # Consulta o usuário pelo email

    if (usuario == None):
        flash('Email não encontrado!')
        return redirect(url_for('entrar'))

    usuario = usuario.toJson()

    if (senha == usuario['senha']): # Verifica se a senha fornecida corresponde à senha no banco
        session['email'] = usuario['email'] # Coloca o usuário em sessão
        session['adm'] = usuario['adm']
        return redirect(url_for('geral')) # Redireciona para a página principal

    flash('Senha incorreta!')
    return redirect(url_for('entrar')) # Redireciona de volta para a página de cadastro se a senha estiver incorreta

@app.route("/sair", methods=['GET']) # método para apagar a sessão do usuário
def sairUsuario():
    chaves = list(session.keys()) # Coleta todos os dados do usuário armazenados em cachê

    for chave in chaves: # Percorre cada chave encontrada na sessão
        del session[chave] # Deleta a chave

    return redirect(url_for('index')) # Retorna para a página home

@app.route("/alterar-foto", methods=['POST'])
def alterarFoto():
    usuario = Usuario.query.filter_by(email=session['email']).first()
    usuario.foto = request.files['foto'].read()
    db.session.commit()
    return redirect(url_for('geral'))



def retornar_usuarios(mensagens):

    for mensagem in mensagens:
        usuario = Usuario.query.filter_by(id=mensagem['usuario_id']).first().toJson()
        mensagem['usuario'] = usuario
        mensagem['usuario']['foto'] = base64.b64encode(usuario['foto']).decode('utf-8')

    return mensagens