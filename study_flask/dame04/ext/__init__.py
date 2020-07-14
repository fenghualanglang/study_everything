


# ext 一个扩展对象

from flask_sqlalchemy import SQLAlchemy


# 创建映射对象
db = SQLAlchemy()









'''
方法一
app = Flask(__name__)
db = SQLAlchemy(app)


方法二
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


'''