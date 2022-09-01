import sqlite3

def criar_tabela():

    banco = sqlite3.connect('table_users.db')
    cursor = banco.cursor()
    cursor.execute(
        '''CREATE TABLE USERS (nomecompleto text, cpf text, datanascimento text, email text, telefone integer, endereco text, cep text, numero text, logradouro text, senha text, aceitecontrato text, aceitelgpd text)''')
    banco.close()

def inserir_dados(nomeCompleto, cpf, dataNascimento, email, telefone, endereco, cep, numero, logradouro, senha, aceiteContrato, aceiteLgpd):

    try:
        banco = sqlite3.connect('table_users.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO USERS VALUES('"+nomeCompleto+"','"+cpf+"','"+dataNascimento+"','" +email+"','"+telefone+"','"+endereco+"','"+cep+"','"+numero+"','"+logradouro+"','"+senha+"','"+aceiteContrato+"','"+aceiteLgpd+"')")
        banco.commit()
        banco.close()
    except:
        banco.close()
        return