from flask import Blueprint, request
from resources.user_resource import UserResource

user_router = Blueprint('router', __name__, url_prefix='/api/user')

user_resource = UserResource()

@user_router.get('/list')
def listUsers():
    user_resource = UserResource()
    return user_resource.list()
    
@user_router.post('/create')
def createUser():
    json = request.get_json()
    user_resource = UserResource()
    return user_resource.create(json)

@user_router.put('/<int:id>/update')
def updateUser(id):
    json = request.get_json()
    user_resource = UserResource()
    return user_resource.update(id, json)

@user_router.delete('/<int:id>/delete')
def deleteUser(id):
    user_resource = UserResource()
    return user_resource.delete(id)