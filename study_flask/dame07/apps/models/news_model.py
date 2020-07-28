
from datetime import datetime

from exts import db


from apps.models import BaseModel

from exts import db


class NewType(BaseModel):
    __tablename__='news_type'
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # date_time = db.Column(db.DateTime, default=datetime.now())
    type_name = db.Column(db.String(50), nullable=True)

class News(BaseModel):
    __tablename__ = 'news'
    title = db.Column(db.String(100), nullable=False)
    content =db.Column(db.Text, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('news_type.id'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='news')

    def __str__(self):
        return self.title

class Comment(BaseModel):

    __tablename__='Comment'

    content = db.Column(db.String(255), nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))






