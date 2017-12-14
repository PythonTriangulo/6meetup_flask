from flask import Flask, request
import json
app = Flask('mitap6')

@app.route('/')
def index():
	return '''
<h1>Ola do meetup 6 da Python Triangulo</h1>
<p>
Qual eh o seu nome?
</p>
<form action="/registrar" method="post">
<input name="nome" type="text"/>
<input type="submit" value="enviar">
</form>
'''

@app.route('/about')
def about():
	return '''
<h1>Sobre</h1>
<p>
O sexto mitap de Python esta sendo realizado no CIAEM, Universidade
Federal de Uberlandia, no dia 13/12/2017.
</p>
<ul>
	<li>Gabriel</li>
	<li>George</li>
	<li>Joao</li>
	<li>Julia</li>
	<li>Sidney</li>
</ul>
'''

@app.route('/registrar', methods=['POST'])
def registrar():
	# import pdb; pdb.set_trace()
	nome = request.form.get('nome')
	if not nome:
		nome = 'mitap'
	return '''
<h1>Ola</h1>
<h2>Seja bem vindo(a), %s</h2>
''' % nome

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)