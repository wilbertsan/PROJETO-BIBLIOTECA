from fileinput import close
import sqlite3

def criar_tabela_usuarios():

    banco = sqlite3.connect('table_users.db')
    cursor = banco.cursor()
    cursor.execute(
        '''CREATE TABLE USERS (nomecompleto text, cpf text, datanascimento text, email text, telefone integer, endereco text, cep integer, numero integer, logradouro text, senha text, aceitecontrato text, aceitelgpd text)''')
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

def verificar_usuario(cpf):
    try:    
        banco = sqlite3.connect('table_users.db')
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM USERS WHERE cpf='%s'"%cpf)
        consulta=cursor.fetchall()
        banco.close()
        return consulta
        
    except:
        banco.close()
        return    


###################### Código Referente aos Livros ##############################################
def criar_tabela_livros():

    banco = sqlite3.connect('table_livros.db')
    cursor = banco.cursor()
    cursor.execute(
        '''CREATE TABLE LIVROS (id text, nomelivro text, autor text, edicao text, editora text, genero text, seccao text, prateleira text, status text)''')
    banco.close()

def inserir_dados_livro(autor, nomeLivro, edicao, editora, genero, seccao, prateleira, status):

    try:
        banco = sqlite3.connect('table_livros.db')
        cursor = banco.cursor()
        cursor.execute("SELECT id FROM LIVROS")
        contador_id=cursor.fetchall()
        id_livro=str(len(contador_id)+1)
        cursor.execute("INSERT INTO LIVROS VALUES('"+id_livro+"','"+nomeLivro+"','"+autor+"','"+edicao+"','" +editora+"','"+genero+"','"+seccao+"','"+prateleira+"','"+status+"')")
        banco.commit()
        banco.close()
    except:
        banco.close()
        return
def consultar_livros(autor, nomeLivro, edicao, editora, genero, seccao, prateleira, status):
    try:    
        banco = sqlite3.connect('table_livros.db')
        cursor = banco.cursor()
        lista1=[ 'nomeLivro','autor', 'edicao', 'editora', 'genero', 'seccao', 'prateleira', 'status']
        lista2=[autor, nomeLivro, edicao, editora, genero, seccao, prateleira, status]
        for item_string in lista1:
            for item_consulta in lista2:
                cursor.execute("SELECT * FROM LIVROS WHERE %s='%s'"%(item_string,item_consulta))
                consulta=cursor.fetchall()
                if len(consulta)!=0:
                    banco.close()
                    return consulta
        return
    except:
        banco.close()
        return    

def deletar_livros(id):
    try:
        banco = sqlite3.connect('table_livros.db')
        cursor = banco.cursor()
        cursor.execute("DELETE FROM LIVROS WHERE id=%s"%(id))
        banco.commit()
        banco.close()
    except:
        banco.close()
        return    

def solicitar_livros(id):
    try:
        banco = sqlite3.connect('table_livros.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE LIVROS SET status='Alugado' WHERE id=%s"%(id))
        banco.commit()
        banco.close()
    except:
        banco.close()
        return

def devolver_livros(id):
    try:
        banco = sqlite3.connect('table_livros.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE LIVROS SET status='Disponível' WHERE id=%s"%(id))
        banco.commit()
        banco.close()
    except:
        banco.close()
        return   