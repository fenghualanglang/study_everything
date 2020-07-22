from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.models.news_model import *
from apps.models.user_model import *
from apps import create_app
from exts import db

app = create_app()



manager = Manager(app=app)
# 命令行工具
# flask 与数据库的映射关系
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)




if __name__ == '__main__':
    manager.run()


# python app.py db init
# python app.py db migrate
# python app.py db upgrade