import datetime
from app import db


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco