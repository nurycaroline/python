from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import text
from sqlalchemy.exc import SQLAlchemyError
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:postgres@localhost:5470/teste'
app.secret_key = 'some_secret'
db = SQLAlchemy(app)
 
#Create Database migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
 
#Create the Post Class
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(10), nullable=False)
    idade = db.Column(db.String(2), nullable=False)    
 
    def __init__(self, nome, telefone, idade):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade
 
    def add(self,pessoa):
        db.session.add(pessoa)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self,pessoa):
        db.session.delete(pessoa)
        return db.session.commit()
 
    def session_commit():
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            reason=str(e)
 
    if __name__ == '__main__':
        manager.run()