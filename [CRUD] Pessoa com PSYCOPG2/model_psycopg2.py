from flask import Flask
import psycopg2
import sys

app = Flask(__name__)

db = None
db = psycopg2.connect(database='teste', user='postgres', password='postgres', port='5470')
cursor = db.cursor()
#cursor.execute("CREATE TABLE pessoa (id SERIAL PRIMARY KEY, nome VARCHAR, idade VARCHAR, telefone VARCHAR);")
#db.commit()

#Create the Post Class
class Pessoa():
    id = 0
    nome = ""
    telefone = ""
    idade = ""    
 
    def __init__(self, id,  nome, telefone, idade):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.idade = idade
 
    def add(self,pessoa):
        cursor.execute("INSERT INTO pessoa (nome, idade, telefone) VALUES (%s, %s, %s)",(pessoa.nome,pessoa.idade,pessoa.telefone))
        return db.commit()

    def update(self, pessoa):
        cursor.execute("UPDATE pessoa SET nome = %s, idade = %s, telefone = %s WHERE id=%s;",(pessoa.nome,pessoa.idade,pessoa.telefone, pessoa.id))
        return db.commit()
 
    def delete(self, pessoa_id):
        cursor.execute("DELETE FROM pessoa WHERE id={}".format(pessoa_id))
        return db.commit()
 
    def session_commit():
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            reason=str(e)
 
