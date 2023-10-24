from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def bienvenida():
    return render_template("index.html")

@app.route('/gustos')
def gustos():
    return render_template('gustos.html')

@app.route('/quiensoy')
def quiensoy():
    return render_template('quinesoy.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run()
