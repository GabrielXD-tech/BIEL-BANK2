import os
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/add_usuario', methods=['GET', 'POST'])
def add_usuario():
    if request.method == 'POST':
        try:
            # Coleta os dados do formulário
            nome = request.form.get('nome')
            renda = request.form.get('renda')
            data_nascimento = request.form.get('data')
            nacionalidade = request.form.get('Nacionalidade')
            cpf = request.form.get('CPF')
            rg = request.form.get('RG')
            profissao = request.form.get('profissao')
            senha = request.form.get('senha')

            # Verifica se todos os campos foram preenchidos
            if not all([nome, renda, data_nascimento, nacionalidade, cpf, rg, profissao, senha]):
                return "Por favor, preencha todos os campos.", 400

            # Salva os dados em um arquivo de texto
            with open('usuarios.txt', 'a', encoding='utf-8') as f:
                f.write(f"Nome: {nome}, Renda: {renda}, Data de Nascimento: {data_nascimento}, "
                        f"Nacionalidade: {nacionalidade}, CPF: {cpf}, RG: {rg}, Profissão: {profissao}, Senha: {senha}\n")
        except KeyError as e:
            return f"Erro: Campo não encontrado - {str(e)}", 400
        
        return redirect(url_for('success'))
    
    # Retorna o formulário HTML caso o método seja GET
    return '''
    <form action="/add_usuario" method="post">
        <input type="text" name="nome" placeholder="Nome" required>
        <input type="text" name="renda" placeholder="Renda" required>
        <input type="date" name="data" placeholder="Data de Nascimento" required>
        <input type="text" name="Nacionalidade" placeholder="Nacionalidade" required>
        <input type="text" name="CPF" placeholder="CPF" required>
        <input type="text" name="RG" placeholder="RG" required>
        <input type="text" name="profissao" placeholder="Profissão" required>
        <input type="password" name="senha" placeholder="Senha" required>
        <button type="submit">Enviar</button>
    </form>
    '''

@app.route('/success')
def success():
    return "Usuário criado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True, port=5501)
