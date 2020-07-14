

- 一对多
        常见： 班级对学生， 部门对员工， 用户对文章， 用户对订单
        通过外键ForeignKey和relationship体现。 外键是给映射关系说的  relationship是给模板使用的
'''


    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(100), nullable=False)
        passworld = db.Column(db.Text, nullable=False)
        phone = db.Column(db.String(11), nullable=False, unique=True)
        email = db.Column(db.String(20))
        icon = db.Column(db.String(100))
        desc = db.Column(db.DateTime, default=datetime.now())
        is_delete = db.Column(db.Boolean, default=False)
    
        # 增加一个字段，代码层面的关系
        articles = db.relationship('Article', backref='user', lazy='dynamic')
        
        
        lazy='dynamic'  什么从数据库中加载数据
        select 默认 查询时会执行
        joined 使用JOIN语句作为父级在统一关系中加载数据
        subquery   类似joined 使用子查询
        dynamic 在有多条数据特别有用的，而不是直接加载这些数据
        
        
        
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
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外检不允许为空   
    
'''



- 多对多(正着说，反着说均可)
    常见的的多对多： 用户对文章评论， 用户对商品， 学生对课程
    
    一个用户可以购买多个商品， 返货来这个商品也可以被多个用户购买
    一个学生可以选择多门课程， 返货来这个课程也可以被多个学生选择











