from flask import Flask, render_template, url_for
from datetime import datetime
from markupsafe import escape

app = Flask(__name__)

# Uso correcto del decorador para filtros de plantillas
@app.template_filter('today')
def today(date):
    return date.strftime('%d-%m-%Y')  # %m es para el mes en números, %M sería para minutos.

# Función para repetir cadenas
@app.add_template_global
def repeat(s, n):
    return s * n

@app.route('/code/<code>')
def code_view(code):
    # Puedes procesar el 'code' o simplemente pasarlo a la plantilla
    return render_template('code.html', code=code)

# Ruta principal
@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    print(url_for('hello', name='Alex', age=32))
    print(url_for('code', code='print("Hola")'))
    name = 'Alex'
    amigos = ["Arnaldo", "José", "Agustin", "Marcelo", "Ivan"]
    date = datetime.now()  # Se obtiene la fecha actual con datetime.now()
    
    return render_template(
        'index.html',
        name=name,
        amigos=amigos,
        date=date,
    )

# Ruta /hello con manejo de parámetros
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name=None, age=None, email=None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data=my_data)

# Ruta para mostrar código
@app.route('/code/<path:code>')
def code(code):
    return render_template('code.html', code=code)  # Escapa el código para evitar vulnerabilidades XSS

if __name__ == '__main__':
    app.run(debug=True)
