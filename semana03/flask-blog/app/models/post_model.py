from db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class PostModel(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    tittle = Column(String(200))
    content = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('UserModel') #Para acceder a los datos de users

    def __repr__(self):
        return f'<Post {self.tittle}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'tittle': self.tittle,
            'content': self.content,
            'user': {
                'id': self.user.id,
                'name': self.user.name,
                'email': self.user.email
            }
        }