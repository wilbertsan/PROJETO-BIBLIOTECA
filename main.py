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
    
    database.inserir_dados(nomeCompleto, cpf, str(dataNascimento), email, telefone, endereco, cep, numero, logradouro, senha, aceiteContrato, aceiteLgpd) 
    #database.inserir_dados(nomeCompleto, cpf, str(dataNascimento), email, telefone, endereco, int(cep), int(numero), logradouro, senha, str(aceiteContrato), str(aceiteLgpd))    
    return render_template("index.html")

if __name__ == '__main__':
    app.run()