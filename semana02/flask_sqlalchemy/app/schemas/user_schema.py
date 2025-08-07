# Validar los datos que recibimos mendiante POST

from pydantic import BaseModel, EmailStr

class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str