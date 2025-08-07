from flask import Flask
from db import db # La app tiene acceso a la base de datos a través de sqlalchemi
from flask_migrate import Migrate
from config import DevelopmentConfig

from app.models import(
    user_model,
    post_model,
)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig) # Seteamos las credenciales a la Base de Datos.
db.init_app(app)
migrate = Migrate(app, db)

from app.routes import api