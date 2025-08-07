from flask_restful import Api
from app import app
from app.resources.user_resources import UserResources

api = Api(app, prefix='/api')

api.add_resource(UserResources, '/users')
