from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps.users.models import User, UserInfo
from apps.orders.models import Article, Photo

from apps import create_app
from ext import db

app = create_app()

manager = Manager(app=app)

# 命令行工具
# flask 与数据库的映射关系
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)

# 自定义添加命令
@manager.command
def init():
    print('初始化')
    # 运行命令python3 app.py init

@manager.command
def migrate():
    print('数据表迁移成功')



if __name__ == '__main__':
    manager.run()


'''
此时 manager后
python app.py 无法运行啦

usage: app.py [-?] {shell,runserver} ...
positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.
    runserver        Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help         show this help message and exit



运行 python app.py runserver --help


启动程序
python app.py runserver
python app.py runserver -p 5001

'''

'''
python app.py db --help


python app.py db init
python app.py db migrate
python app.py db upgrade


'''




























