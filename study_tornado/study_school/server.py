# -*- coding: utf-8 -*-
import logging
import tornado
import os
import tornado.web
import tornado.ioloop

from tornado.httpserver import HTTPServer
from tornado_swagger.setup import setup_swagger
from tornado.options import define, parse_command_line, options

define('cmd', default='runserver', metavar='runserver|syncdb')
define('port', default=8880, type=int)
define('mode', default='dev', metavar='dev|online')
parse_command_line()

from config import log
from script.init import init_db
from config import setting
from lib.util import setting_from_object

from config.route import routes


logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict()
        # configs = setting_from_object(setting.PUB_CONF, options.mode)
        # settings.update(configs)
        print(options.mode)
        if options.mode == "dev":
            configs = setting_from_object(setting.PUB_CONF, options.mode)
            settings.update(configs)
            setup_swagger(
                routes,
                swagger_url='/doc',
                api_base_url='/',
                description='',
                api_version='1.0.0',
                title='Journal API',
                contact='name@domain',
                schemes=['http'],
                security_definitions={
                    "Token": {"type": "apiKey", "name": "Authorization", "in": "header"}
            },
        )

        if options.mode == "online":
            configs = setting_from_object(setting.PUB_CONF, options.mode)
            settings.update(configs)
        tornado.web.Application.__init__(self, routes, **settings)

def runserver():
    log.setup_logger(options.port)
    http_server = HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':

    if options.cmd == 'init':
        init_db()
    elif options.cmd == 'runserver':
        runserver()
