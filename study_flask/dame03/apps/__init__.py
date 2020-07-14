from flask import Flask

import setting
from ext import db
from apps.users.user import user_bp

def create_app():

    app = Flask(__name__)   # 核心对象

    app.config.from_object(setting.DevelopmentConfig)  # 加载配置class

    db.init_app(app) # 将db 与app 进行关联

    # 注册蓝图（将蓝图绑定到app上）
    app.register_blueprint(user_bp)


    return app

