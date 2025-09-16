from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def index():
    return 'Olá Mundo'

@app.route('/contato')
def contato():
    return '<h1> sabe se la o que </h1>'

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html')

#isto tem que ser a >>ÚLTIMA<< coisa do código
if __name__ == '__main__':
    app.run()
