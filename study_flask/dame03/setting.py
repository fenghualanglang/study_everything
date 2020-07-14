

class Config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1qaz2wsx@192.168.43.187:3306/leqiaosu"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False


