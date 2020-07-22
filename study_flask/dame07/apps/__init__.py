from flask import Flask


from settings import DevelopmentConfig
from apps.api.news import news_bp
from apps.api.user import user_bp


from exts import db, api,cors, cache


config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379
}








def create_app():

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    # db.metadata.clear()
    db.init_app(app=app)
    api.init_app(app=app)
    cors.init_app(app=app, supports_credentials=True)
    cache.init_app(app=app, config=config)

    # 注册蓝图
    app.register_blueprint(news_bp)
    app.register_blueprint(user_bp)
    print(app.url_map)

    return app

