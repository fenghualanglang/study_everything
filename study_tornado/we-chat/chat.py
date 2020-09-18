import os
from datetime import datetime

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.websocket import WebSocketHandler


class IndexHandler(RequestHandler):

    def get(self):
        self.render('index.html')
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

class ChatIndexHandler(RequestHandler):

    def get(self):
        self.render('chat.html')


class ChatHandler(WebSocketHandler):

    userList = set()

    def open(self, *args, **kwargs):

        # 用户加入链接
        self.userList.add(self)
        for user in self.userList:
            print(self.request.remote_ip)
            user.write_message('%s-%s: 上线了' % (self.request.remote_ip, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def on_message(self, message):
        for user in self.userList:
            user.write_message('%s-%s说：%s' % (self.request.remote_ip, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message))

    def on_close(self):
        for user in self.userList:
            user.write_message('%s-%s：下线了' % (self.request.remote_ip, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def check_origin(self, origin):
        # 允许跨域
        return True



app = Application([
    # (r'^/$', IndexHandler),
    # (r'^/websocket$', SocketHandler),
    (r'^/chat$', ChatIndexHandler),
    (r'^/chatsocket$', ChatHandler),

],
template_path=os.path.join(os.getcwd(), "templates")
)
app.listen(8100, address='192.168.0.242')

IOLoop.instance().start()








