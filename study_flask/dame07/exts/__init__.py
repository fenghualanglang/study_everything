# ext 一个扩展对象
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

# 创建映射对象
db = SQLAlchemy()


# 创建api对象

api = Api()


# 创建跨域对象
cors = CORS()

# 缓存对象
cache = Cache()







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