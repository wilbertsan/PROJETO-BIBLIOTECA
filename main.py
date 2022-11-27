import re
from flask import Flask, render_template, request

import database
app = Flask(__name__)

########### ROTAS ###########

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/cadastrar_usuarios')
def cadastrar_usuarios():
    return render_template('cadastro_usuarios.html')

@app.route('/adicionar_livros')
def adicionar_livros():
    return render_template('adicionar_livros.html')

@app.route('/solicitar_livros')
def solicitar_livros():
    return render_template('solicitar_livros.html')

@app.route('/devolver_livros')
def devolver_livros():
    return render_template('devolver_livros.html')

@app.route('/pesquisar')
def pesquisar():
    return render_template('pesquisar.html')

@app.route('/retorno_pesquisar')
def retorno_pesquisa():
    return render_template('retorno_pesquisar.html')

@app.route('/deletar')
def deletar_livros():
    return render_template('deletar_livros.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

@app.route('/usuario_nao_cadastrado')
def usuario_nao_cadastrado():
    return render_template('usuario_nao_cadastrado.html')

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

##############################
########## FUNÇÕES ###########

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

@app.route('/pesquisa_livros', methods=["POST"])
def pesquisa_livros():
    autor = request.form["autor"]
    nomeLivro = request.form["nomelivro"]
    edicao = request.form["edicao"]
    editora = request.form["editora"]
    genero = request.form["genero"]
    seccao = request.form["seccao"]
    prateleira = request.form["prateleira"]
    status = request.form["status"]
    consulta=database.consultar_livros(autor, nomeLivro, edicao, editora, genero, seccao, prateleira, status)
    return render_template("retorno_pesquisar.html", consulta=consulta, tamanho=len(consulta))

@app.route('/deleta_livro', methods=["POST"])
def deleta_livro():
    id = request.form["id"]
    database.deletar_livros(id)
    return render_template("deletar_livros.html")

@app.route('/solicita_livro', methods=["POST"])
def solicita_livro():
    id = request.form["id"]
    database.solicitar_livros(id)
    return render_template("solicitar_livros.html")

@app.route('/verifica_usuario', methods=["POST"])
def verifica_usuario():
    cpf = request.form["cpf"]
    senha = request.form["senha"]
    print(cpf)
    print(senha)
    print(database.verificar_usuario(cpf)[0][0])
    print(type(database.verificar_usuario(cpf)))
    if senha == database.verificar_usuario(cpf)[0][0]:
        return render_template("usuario.html")
    else:
        return render_template("usuario_nao_cadastrado.html")

@app.route('/devolve_livro', methods=["POST"])
def devolve_livro():
    id = request.form["id"]
    database.devolver_livros(id)
    return render_template("devolver_livros.html")

##############################
if __name__ == '__main__':
    app.run()
