

class Config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1qaz2wsx@192.168.60.177:3306/leqiaosu"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'wrfetgyhujyikuoilp43f5t4g6y5h7u6ji8'


class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False


