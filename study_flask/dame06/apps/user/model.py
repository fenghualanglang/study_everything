

from exts import db


from datetime import datetime



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    passworld = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(20))
    create_time = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return self.username, self.content, self.phone