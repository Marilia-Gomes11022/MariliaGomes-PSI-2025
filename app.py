from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def index():
    return 'Olá Mundo'

@app.route('/contato')
def contato():
    x = 'Maria'
    y = 'maria@email.com'
    return render_template('contato.html', nome = x, email = y)
#esquerda é a variável que vai ser passadas(nome), enquanto à direita é a variável declarada antes e FORA do render template(x)
# return render_template('contato.html', nome='Maria')
#'<h1> sabe se la o que </h1>'

@app.route('/perfil', defaults={'nome':'fulano'})

@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome = nome)

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html')

@app.route('/semestre/<int:x>')
def semestre(x):
    y = x + 1
    return render_template('semestre.html', x = x, y = y)

@app.route('soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return str(n1+n2)


#isto tem que ser a >>ÚLTIMA<< coisa do código
if __name__ == '__main__':
    app.run()
