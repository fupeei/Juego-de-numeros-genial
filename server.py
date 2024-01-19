from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'martina'

numero_secreto = random.randint(0,100)



@app.route('/')         
def index():
    if 'numero_secreto' not in session:
            session['numero_secreto'] = random.randint(1, 100)
            print(session['numero_secreto'])
    return render_template('index.html')


@app.route("/respuesta", methods=["POST"])
def respuesta():
    
    numero_adivinado = int(request.form['numero_respuesta'])
    numero_secreto = session['numero_secreto']
        
    if numero_adivinado < numero_secreto:
        mensaje = 'Demasiado bajo'
    elif numero_adivinado > numero_secreto:
        mensaje = 'Demasiado alto'
    else:
        mensaje = '¡Correcto! El número era ' + str(numero_secreto)
        session.pop('numero_secreto')

    return render_template('index.html', mensaje=mensaje)


if __name__=="__main__":   
    app.run(debug=True)