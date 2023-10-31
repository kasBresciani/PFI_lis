from app import db # Importa do arquivo principal a instância que controla o banco de dados

class Mensagem(db.Model): # Cria a classe usuário, herdando um modelo da instância db
    __tablename__ = "mensagens" # Define o nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True) # Coluna ID do tipo inteiro - declarada como chave primária
    usuario_id = db.Column(db.Integer) # Coluna usuario_id do tipo inteiro
    mensagem = db.Column(db.String(255)) # Coluna mensagem do tipo String
    aprovada = db.Column(db.Boolean) # Coluna aprovada do tipo Boolean

    def __init__(self, usuario_id, mensagem, aprovada = False): # Método construtor da classe
        self.usuario_id = usuario_id
        self.mensagem = mensagem
        self.aprovada = aprovada

    def toJson(self): # Método que retorna todas as informações existentes da classe em formato de dicionário
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "mensagem": self.mensagem,
            "aprovada": self.aprovada
        }