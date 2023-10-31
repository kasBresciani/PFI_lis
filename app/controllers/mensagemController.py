from flask import request, redirect, url_for, session
from app import app, db

from app.model.Usuario import Usuario
from app.model.Mensagem import Mensagem

@app.route('/enviar', methods=['POST']) # rota para inserir novo usuário no banco
def adicionar_mensagem():
    # Coleta os dados da mensagem
    usuario_id = Usuario.query.filter_by(email=session['email']).first().toJson()['id'] # Consulta o id do usuário logado
    mensagem = request.form['mensagem']

    nova_mensagem = Mensagem(usuario_id=usuario_id, mensagem=mensagem)

    db.session.add(nova_mensagem) # Adiciona o novo usuário no banco
    db.session.commit() # Salva as alterações do banco

    return redirect(url_for('geral')) # Redireciona para a página principal da aplicação

@app.route('/remover/<int:id>', methods=['GET'])
def deletar_mensagem(id):
    mensagem = Mensagem.query.get(id)  # Seleciona a mensagem com base no ID

    db.session.delete(mensagem)  # Deleta a mensagem
    db.session.commit() # Salva a alteração

    return redirect(url_for('painel_adm')) # Redireciona para a página com as questões

@app.route('/aceitar/<int:id>', methods=['GET'])
def aceitar_mensagem(id):
    mensagem = Mensagem.query.get(id)  # Seleciona a mensagem com base no ID

    mensagem.aprovada = True  # Define o atributo "aprovada" como True
    db.session.commit()  # Salva a alteração

    return redirect(url_for('painel_adm')) # Redireciona para a página com as questões

def retornar_mensagens():
    consulta_mensagens = Mensagem.query.all() # Consulta as mensagens
    return [mensagem.toJson() for mensagem in consulta_mensagens] # Retonar a lista de mensagens