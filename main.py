from flask import Flask, render_template, request
import database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=["POST"])
def cadastrar():
    nomeCompleto = request.form["nome"]
    cpf = request.form["cpf"]
    dataNascimento = request.form["nascimento"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    cep = request.form["cep"]
    numero = request.form["numero"]
    logradouro = request.form["logradouro"]
    senha = request.form["senha"]
    senhaConfirma = request.form["confirmacao"]
    aceiteContrato = request.form["contrato"]
    aceiteLgpd = request.form["lgpd"]
    
    database.inserir_dados_usuarios(nomeCompleto, cpf, str(dataNascimento), email, telefone, endereco, cep, numero, logradouro, senha, aceiteContrato, aceiteLgpd) 
     
    return render_template("index.html")


@app.route('/cadastrar_usuarios')
def cadastrar_usuarios():
    return render_template('cadastro_usuarios.html')

@app.route('/adicionar_livro', methods=["POST"])
def adicionar_livro():
    autor = request.form["autor"]
    nomeLivro = request.form["nomelivro"]
    edicao = request.form["edicao"]
    editora = request.form["editora"]
    genero = request.form["genero"]
    seccao = request.form["seccao"]
    prateleira = request.form["prateleira"]
    status = request.form["status"]
    
    
    database.inserir_dados_livro(autor, nomeLivro, edicao, editora, genero, seccao, prateleira, status)
     
    return render_template("index.html")

@app.route('/adicionar_livros')
def adicionar_livros():
    return render_template('adicionar_livros.html')

if __name__ == '__main__':
    app.run()