


from ext import db


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gname = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外检不允许为空
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 外检不允许为空

    def __str__(self):
        return self.gname

