from flask import Flask, request

app = Flask(__name__) # Siempre el argumento debe ser '__name__'

@app.route('/')       # -> decorador, es como un función padre, recibe la ruta y ejecuta la función siguiente.
def home():
    return 'Bienvenido a mi aplicación de Flask 🤑'

@app.route('/html')
def html():
    return '<button>Dame click</button>'

@app.route('/user/<name>')
def hello(name):
    return f'Hola {name}'

@app.route('/login', methods=['POST']) #GET, POST, PUT, DELETE, PATCH
def login():
    if request.method == 'POST':
        json = request.get_json()
        return json

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    print(file)
    return 'Uploaded'

@app.route('/client', methods=['GET'])
def client():
    return {
        'id': 1,
        'name': 'Juan',
        'email': 'juan@gamil.com'
    }

if __name__ == '__main__':
    app.run(debug=True)