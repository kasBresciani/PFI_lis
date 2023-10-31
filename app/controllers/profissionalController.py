from flask import request, redirect, url_for, session
from app import app, db

from app.model.Profissional import Profissional

@app.route('/enviar-profissional', methods=['POST']) # rota para inserir novo usuário no banco
def adicionar_profissional():
    # Coleta os dados da mensagem
    nome = request.form['nome']
    telefone = request.form['telefone']
    especialidade = request.form['especialidade']
    estado = request.form['estado']
    cidade = request.form['cidade']

    novo_profissional = Profissional(nome=nome, telefone=telefone, especialidade=especialidade, estado=estado, cidade=cidade)

    db.session.add(novo_profissional) # Adiciona o novo profissional no banco
    db.session.commit() # Salva as alterações do banco

    return redirect(url_for('geral')) # Redireciona para a página principal da aplicação

@app.route('/remover-profissional/<int:id>', methods=['GET'])
def deletar_profissional(id):
    profissional = Profissional.query.get(id)  # Seleciona o profissional com base no ID

    db.session.delete(profissional)  # Deleta a mensagem
    db.session.commit() # Salva a alteração

    return redirect(url_for('painel_adm')) # Redireciona para a página com as questões

@app.route('/aceitar-profissional/<int:id>', methods=['GET'])
def aceitar_profissional(id):
    profissional = Profissional.query.get(id)  # Seleciona a mensagem com base no ID

    profissional.aprovado = True  # Define o atributo "aprovado" como True
    db.session.commit()  # Salva a alteração

    return redirect(url_for('painel_adm')) # Redireciona para a página com as questões

def retornar_profissionais():
    consulta_profissionais = Profissional.query.all() # Consulta os profissionais
    return [profissional.toJson() for profissional in consulta_profissionais] # Retonar a lista de profissionais