import os
from datetime import datetime
import tornado
import torndb as torndb
import tornado.httpserver
from tornado.options import define, options
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler#, Application
from tornado.websocket import WebSocketHandler

define("port", default=8000, type=int)

class IndexHandler(RequestHandler):

    def get(self):

        self.render('webchat.html')
        pass

    def post(self):
        pass

    def put(self):
        pass

class SocketHandler(WebSocketHandler):

    def open(self, *args, **kwarg):
        print("建立服务器连接")

    def on_message(self, message):
        print("收到客户端的消息%s" % message)

        # 发送消息给客户端
        self.write_message("hello client")

    def on_close(self):
        print("断开服务器连接")

    def check_origin(self, origin):
        # 允许跨域
        return True

class WebChatIndexHandler(RequestHandler):

    def get(self):
        self.render('chat.html')


class WebChatHandler(WebSocketHandler):

    userList = set() # 用来存放在线用户的容器

    def open(self, *args, **kwargs):
        self.userList.add(self)   # 建立连接后添加用户到容器中
        for user in self.userList: # 向已在线用户发送消息
            print(self.request.remote_ip)
            user.write_message('[%s]-[%s]-进入聊天室' % (self.request.remote_ip, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def on_message(self, message):
        for user in self.userList: # 向在线用户广播消息
            user.write_message('%s-%s说：%s' % (self.request.remote_ip, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message))

    def on_close(self):
        self.userList.remove(self)  # 用户关闭连接后从容器中移除用户
        for user in self.userList:
            user.write_message('%s-%s：下线了' % (self.request.remote_ip, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求




class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):

        self.db = torndb.Connection(
            host='127.0.0.1',
            database='jincuodao',
            user='root',
            password='123456'
        )
        super(Application,self).__init__(*args, **kwargs)
if __name__ == '__main__':

    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    settings = dict(
        static_path=os.path.join(current_path, 'static'),
        template_path=os.path.join(current_path, 'templates'),
        cookie_secret='wfghjuikikq56kijegwfqdfght',
        debug=True
    )
    app = Application([
        # (r'^/$', IndexHandler),
        # (r'^/websocket$', SocketHandler),
        (r'^/webchat$', WebChatIndexHandler),
        (r'^/webchatsocket$', WebChatHandler),

    ],
    **settings
    )
    # app.listen(8000, address='192.168.43.187')
    import tornado.httpserver
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()









