from flask import Flask

import setting
from apps.users.user import user_bp

def create_app():

    app = Flask(__name__)   # 核心对象
    app.config.from_object(setting)  # 加载配置

    # 注册蓝图（将蓝图绑定到app上）
    app.register_blueprint(user_bp)


    return app

