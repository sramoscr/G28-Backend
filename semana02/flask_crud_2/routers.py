from flask import Blueprint, Request
from resources.user_resource import UserResource

user_router = Blueprint('router', __name__, url_prefix='/api2/user')

user_resource = UserResource()

@user_router.get('/list')
def listUsers():
    user_resource = UserResource()
    return user_resource.list()

@user_router.post('/create')
def createUser():
    return user_resource.create()

@user_router.put('/<int:id>/update')
def updateUser(id):
    return user_resource.update()

@user_router.delete('/<int:id>/delete')
def deleteUser(id):
    return user_resource.delete()