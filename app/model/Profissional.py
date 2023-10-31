from app import db # Importa do arquivo principal a instância que controla o banco de dados

class Profissional(db.Model): # Cria a classe usuário, herdando um modelo da instância db
    __tablename__ = "profissionais" # Define o nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True) # Coluna ID do tipo inteiro - declarada como chave primária
    nome = db.Column(db.String(255)) # Coluna nome do tipo String
    telefone = db.Column(db.String(255)) # Coluna telefone do tipo String
    aprovado = db.Column(db.Boolean) # Coluna aprovada do tipo Boolean
    especialidade = db.Column(db.String(255)) # Coluna especialidade do tipo String
    cidade = db.Column(db.String(255)) # Coluna cidade do tipo String
    estado = db.Column(db.String(255)) # Coluna estado do tipo String

    def __init__(self, nome, telefone, especialidade, estado, cidade, aprovado = False): # Método construtor da classe
        self.nome = nome
        self.telefone = telefone
        self.especialidade = especialidade
        self.estado = estado
        self.cidade = cidade
        self.aprovado = aprovado

    def toJson(self): # Método que retorna todas as informações existentes da classe em formato de dicionário
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "aprovado": self.aprovado,
            "especialidade": self.especialidade,
            "estado": self.estado,
            "cidade": self.cidade
        }