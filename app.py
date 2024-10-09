import mysql.connector
from flask import Flask, request, redirect, url_for, abort

app = Flask(__name__)

# Função para conectar ao banco de dados MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",      # Host do MySQL
        user="seu_usuario",    # Seu nome de usuário do MySQL
        password="sua_senha",  # Sua senha do MySQL
        database="nome_do_banco_de_dados"  # O banco de dados onde está a tabela 'usuarios'
    )

@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    try:
        # Coleta os dados do formulário
        nome = request.form['nome']
        renda = request.form['renda']
        data_nascimento = request.form['data']
        nacionalidade = request.form['Nacionalidade']
        cpf = request.form['CPF']
        rg = request.form['RG']
        profissao = request.form['profissiao']
        senha = request.form['senha']

        # Conecta ao banco de dados MySQL e insere os dados
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, renda, data_nascimento, nacionalidade, cpf, rg, profissao, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (nome, renda, data_nascimento, nacionalidade, cpf, rg, profissao, senha))
        conn.commit()  # Confirma as alterações no banco de dados
        cursor.close()  # Fecha o cursor
        conn.close()    # Fecha a conexão
    except KeyError as e:
        return f"Erro: Campo não encontrado - {str(e)}", 400  # Retorna um erro ao usuário
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao inserir dados!", 500

    return redirect(url_for('criar_usuario'))

if __name__ == '__main__':
    app.run(debug=True)
