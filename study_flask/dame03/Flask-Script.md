Flask-Script是一个让你的命令行支持自定义命令的工具，它为Flask程序添加一个命令行解释器。可以让我们的程序从命令行直接执行相应的程序

通过使用Flask-Script扩展，我们可以在Flask服务器启动的时候，通过命令行的方式传入参数。
不仅仅通过app.run()方法中传参，比如我们可以通过python hello.py runserver –host ip地址，告诉服务器在哪个网络接口监听来自客户端的连接。
默认情况下，服务器只监听来自服务器所在计算机发起的连接，即localhost连接。
我们可以通过python hello.py runserver --help来查看参数。

Flask-Script插件为在Flask里编写额外的脚本提供了支持。包括了一个开发服务器，一个定制的Python命令行，用于执行初始化数据库、定时任务和其他属于web应用之外的命令行任务的脚本


# 使用里面Manager 进行命令得到管理和使用

1. 构建manager = Manager(app=app)
2. 启动 manager.run()
3. 使用命令在终端 
  python3 app.py runserver
  python3 app.py runserver -h 0.0.0.0 -p 50001
  
  
# 自定义添加明令
@manager.command
def init():
    print('初始化')
    
 运行命令 python3 app.py init
 
 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  