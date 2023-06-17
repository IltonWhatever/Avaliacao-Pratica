from flask import Flask, render_template, request, redirect, url_for
from utils import searchfuncionario
app = Flask(__name__, template_folder = 'templates')

lista_funcionario = []
ids = []

@app.route('/')
def index():
    return render_template('pages/index.html', titulo_pagina='Pagina Inicial')

@app.route('/cadastrar_funcionario')
def cadastrar_funcionario():
    msg = request.args.get("msg")
    color = request.args.get("color")
    return render_template('pages/cadastrar_funcionario.html', titulo_pagina='Cadastro de Funcionario', msg=msg, color=color)

@app.route('/funcionario')
def funcionario():
    msg = request.args.get("msg")
    color = request.args.get("color")
    return render_template('pages/funcionario.html', titulo_pagina='Lista dos Funcionarios', lista_funcionario=lista_funcionario, msg=msg)

@app.route('/register', methods = ['POST'])
def register():
    id = len(ids)
    ids.append(id)

    name = request.form['name']
    cpf = request.form['cpf']
    telefone = request.form['telefone']

    if len(name) == 0:
        return redirect(url_for('cadastrar_funcionario', msg = 'Nome não pode ser vazio', color='Red'))
    if len(cpf) == 0:
        return redirect(url_for('cadastrar_funcionario', msg = 'CPF não pode ser vazio', color='Red'))
    if len(telefone) == 0:
        return redirect(url_for('cadastrar_funcionario', msg = 'Telefone não pode ser vazio', color='Red'))


    lista_funcionario.append([id,name,cpf,telefone])

    return redirect(url_for('cadastrar_funcionario', msg=f'Funcionario {name} Cadastrado', color='Green'))

@app.route('/ver_funcionario/<int:id>')
def ver_funcionario(id):
    funcionario = searchfuncionario(id,lista_funcionario)
    
    return render_template('pages/ver_funcionario.html', titulo_pagina='Informações do funcionario', funcionario=funcionario)

@app.route('/edit_funcionario/<int:id>')
def edit_funcionario(id):
    funcionario = searchfuncionario(id,lista_funcionario)
    return render_template('pages/edit_funcionario.html', titulo_pagina=f'Editar funcionario {funcionario[0][1]}', id=id, funcionario=funcionario)

@app.route('/edit', methods=['POST'])
def edit():
    id = request.args.get('id')
    id = int(id)
    
    name = request.form['name']
    cpf = request.form['cpf']
    telefone = request.form['telefone']

    if len(name) != 0:
        lista_funcionario[id][1] = name
    if len(cpf) != 0:
        lista_funcionario[id][2] = cpf
    if len(telefone) != 0:
        lista_funcionario[id][3] =telefone

    return redirect(url_for('funcionario'))

@app.route('/delete_funcionario/<int:id>', methods=['DELETE', 'GET'])
def delete_funcionario(id):
    for indice, linha in enumerate(lista_funcionario):
        if linha[0] == id:
            indice_encontrado = indice
            break
    del lista_funcionario[indice]
    del ids[0]
    
    return redirect(url_for('funcionario', msg='Funcionario deletado !', color='Red'))

if __name__ == '__main__':
    app.run(debug= True)