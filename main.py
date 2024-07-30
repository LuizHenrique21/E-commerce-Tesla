from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_manager
from form import LoginForm, ShowPassword

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['DATABASE'] = 'db'
app.config['SECRET_KEY'] = 'Tesla123@'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return Pessoa.query.filter_by(_id=id).first()

class Pessoa(db.Model):
	__tablename__ = 'cliente'

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(50))
	sobrenome = db.Column(db.String(100))
	email = db.Column(db.String(100))
	senha = db.Column(db.String(255))
	confirmar_senha = db.Column(db.String(255))
	
	@property
	def is_authenticated(self):
		return True
	
	@property
	def is_active(self):
		return True
	
	@property
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return str(self._id)

	def __init__(self, nome, sobrenome, email, senha, confirmar_senha):
		self.nome = nome
		self.sobrenome = sobrenome
		self.email = email
		self.senha = senha
		self.confirmar_senha = confirmar_senha

with app.app_context():
    db.create_all()

def verificar_email_existente(email):
	return Pessoa.query.filter_by(email=email).first() is not None

@app.route('/')
@app.route('/home')
def index():
	return render_template('tesla.html')

@app.route("/logar")
def logar():
	form = LoginForm()
	return render_template('login.html', form=form)

@app.route('/login', methods =['GET', 'POST'])
def login():
	form = LoginForm()
	nome_usuario = request.cookies.get('usuario_logado')
	if nome_usuario:
		print(nome_usuario)
		form.username.data = nome_usuario
	if form.validate_on_submit():
		senha = request.form['password']
		pessoa = Pessoa.query.filter_by(email=form.username.data).first()
		lembrar = form.remember_me.data
		
		if pessoa and pessoa.senha == senha:
			print("Deu bom")
			login_user(pessoa)
			resposta = make_response(redirect('home'))
			if lembrar:
				resposta.set_cookie('usuario_logado', form.username.data)
			return resposta
		else:
			print("Errou tudo")
			flash("Senha ou usuário inválido")
			return render_template('login.html', form=form)
	else:
		print(form.errors)
	
	return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	resposta = make_response(redirect(url_for('index')))
	resposta.set_cookie('usuario_logado', ' ', expires=0)
	return resposta

@app.route("/alternarusuario")
def alternarusuario():
	logout_user()
	return redirect(url_for('login'))

@app.route("/lista")
def lista():
	pessoas = Pessoa.query.all()
	return render_template("lista.html", pessoas=pessoas)

@app.route("/excluir/<int:id>")
def excluir(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return redirect(url_for("lista"))

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@app.route('/cadastro', methods =['GET', 'POST'])
def cadastro():
	if request.method == 'POST':
		nome = request.form.get("nome")
		sobrenome = request.form.get("sobrenome")
		email = request.form.get("email")
		senha = request.form.get("senha")
		confirmar_senha = request.form.get("confirmar_senha")

		resposta = redirect(url_for('cadastrar'))
		length = len(senha)

		if verificar_email_existente(email):
			flash('Este email já está cadastrado. Por favor, use outro email.', 'error')	
			return resposta

		if length < 5:
			flash('A senha deve ter no mínimo 5 caracteres', 'error')
			return resposta
		elif not any(char.isupper() for char in senha):
			flash('A senha deve conter pelo menos uma letra maiúscula', 'error')
			return resposta
		elif not any(char in '?!@#$%^&*()_-.,;:[]+=°' for char in senha):
			flash('A senha deve conter pelo menos um caractere especial', 'error')
			return resposta
		elif (senha != confirmar_senha):
			flash('As senhas informadas não conferem', 'error')
			return resposta
		else:
			if nome and sobrenome and email and senha and confirmar_senha:
				p = Pessoa(nome, sobrenome, email, senha, confirmar_senha)
				db.session.add(p)
				db.session.commit()
				return redirect(url_for("login"))
@app.route("/ver-cookie")
def ver_cookie():
    cookies = request.cookies
    return cookies

@app.route("/models")
def models():
	return render_template("checkout.html")

if __name__ == '__main__':
    app.run(debug=True)
