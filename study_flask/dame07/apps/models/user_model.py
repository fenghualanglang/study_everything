





















from datetime import datetime

from exts import db


from apps.models import BaseModel

from exts import db


class User(BaseModel):
    __tablename__='user'
    type_name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(11), nullable=False, unique=True)
    icon = db.Column(db.String(128))

    def __str__(self):
        return self.username

# class News(BaseModel):
#     __tablename__ = 'news'
#     title = db.Column(db.String(100), nullable=False)
#     content =db.Column(db.Text, nullable=False)
#     type_id = db.Column(db.Integer, db.ForeignKey('news_type.id'))
#












