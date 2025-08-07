from flask import Flask
from router import user_router
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app) # le pasamos la inst. de flask

app.register_blueprint(user_router) #registramos el blueprint de las rutas / Blueprint agrupa rutas

if __name__ == '__main__':
    app.run(debug=True)