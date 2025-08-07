import datetime
import os
from dotenv import load_dotenv

load_dotenv() #Para que carguen las variables de entorno.

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= os.getenv('DATABASE_URI')
    JWT_SECRET_LEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=5) #timedelta convierte la fecha en segundos

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG: False