
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/flask-sqlalchemy'

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'