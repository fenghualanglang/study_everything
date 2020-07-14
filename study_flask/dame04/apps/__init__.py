from flask import Flask

import setting
from ext import db
from apps.users.user import user_bp
from apps.orders.acticle import article_bp

def create_app():

    app = Flask(__name__)   # 核心对象
    # app = Flask(__name__, template_folder='../templates', static_folder='../static')

    app.config.from_object(setting.DevelopmentConfig)  # 加载配置class

    db.init_app(app) # 将db 与app 进行关联

    # 注册蓝图（将蓝图绑定到app上）
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)

    return app

