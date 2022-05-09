import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


# APLICAÇÃO FLASK
app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


# CONTROLLERS
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/gravar', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        preco = request.form['preco']
        post = Post(nome, categoria, preco)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port, debug=True)
