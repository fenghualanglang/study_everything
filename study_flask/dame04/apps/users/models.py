

from ext import db


from datetime import datetime



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    passworld = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(20))
    icon = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now())
    is_delete = db.Column(db.Boolean, default=False)

    # 增加一个字段，代码层面的关系
    articles = db.relationship('Article', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user')

    # def __str__(self):
    #     return self.username, self.email, self.phone

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    realname = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Boolean, default=False)


    def __str__(self):
        return self.realname

