import os

class Config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1qaz2wsx@localhost:3306/leqiaosu"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'wrfetgyhujyikuoilp43f5t4g6y5h7u6ji8'

    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False

if __name__ == '__main__':
    print(Config.BASE_DIR)

