

from ext import db


from datetime import datetime



class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    pdatatime = db.Column(db.DateTime, default=datetime.now())
    click_num = db.Column(db.Integer, default=0)
    save_num = db.Column(db.Integer, default=0)
    love_num = db.Column(db.Integer, default=0)
    # 一对多关系, 同步到数据库外键的关系
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外检不允许为空
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 外检不允许为空
    comments = db.relationship('Comment', backref='article')

    def __str__(self):
        return self.title, self.content, self.phone





class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gname = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # 一对多关系, 同步到数据库外键的关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外检不允许为空



    def __str__(self):
        return self.gname, self.price


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_name = db.Column(db.String(100), nullable=False)
    photo_time = db.Column(db.DateTime, default=datetime.now())
    # 一对多关系, 同步到数据库外键的关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外检不允许为空




    def __str__(self):
        return self.photo_name


class Commet(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commet = db.Column(db.String(100), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    photo_time = db.Column(db.DateTime, default=datetime.now())
    # 一对多关系, 同步到数据库外键的关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外检不允许为空


    def __str__(self):
        return self.commet








'''
python 框架中不方便直接写链接或子查询

1. 一对多
        常见： 班级对学生， 部门对员工， 用户对文章， 用户对订单
        通过外键 和  体现。 外键是给映射关系说的  relationship是给模板使用的
        
'''










