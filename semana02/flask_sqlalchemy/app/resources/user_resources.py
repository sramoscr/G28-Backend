from flask_restful import Resource
from app.models.user_model import UserModel
from flask import request
from app.schemas.user_schema import CreateUserSchema
from pydantic import ValidationError
from db import db




class UserResources(Resource):
    def get(self):
        try:
            users = UserModel.query.all()

            response_data = []
            for user in users:
                response_data.append({
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                })
            return response_data, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def post(self):
        try:
            data = request.get_json()
            validated_data = CreateUserSchema(**data)
            user = UserModel(
                name=validated_data.name,
                email=validated_data.email,
                password=validated_data.password
            )
            db.session.add(user)
            db.session.commit()

            return {
                'message': 'User created succesfully'
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500
