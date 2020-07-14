

from ext import db


from datetime import datetime



class User(db.Model):
    __tablename__ = 'user_article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    passworld = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(20))
    content = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return self.username, self.content, self.phone

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    realname = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Boolean, default=False)


    def __str__(self):
        return self.realname

