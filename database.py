import sqlite3

def criar_tabela_usuarios():

    banco = sqlite3.connect('table_users.db')
    cursor = banco.cursor()
    cursor.execute(
        '''CREATE TABLE USERS (nomecompleto text, cpf text, datanascimento text, email text, telefone integer, endereco text, cep integer, numero integer, logradouro text, senha text, aceitecontrato text, aceitelgpd text)''')
    banco.close()

def criar_tabela_livros():

    banco = sqlite3.connect('table_livros.db')
    cursor = banco.cursor()
    cursor.execute(
        '''CREATE TABLE LIVROS (Id text, autor text, nomelivro text, edicao text, editora text, genero text, seccao text, prateleira text)''')
    banco.close()

def inserir_dados_usuarios(nomeCompleto, cpf, dataNascimento, email, telefone, endereco, cep, numero, logradouro, senha, aceiteContrato, aceiteLgpd):

    try:
        banco = sqlite3.connect('table_users.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO USERS VALUES('"+nomeCompleto+"','"+cpf+"','"+dataNascimento+"','" +email+"','"+telefone+"','"+endereco+"','"+cep+"','"+numero+"','"+logradouro+"','"+senha+"','"+aceiteContrato+"','"+aceiteLgpd+"')")
        banco.commit()
        banco.close()
    except:
        banco.close()
        return
criar_tabela_livros()