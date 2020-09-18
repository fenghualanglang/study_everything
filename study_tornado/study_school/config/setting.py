# -*- coding: utf-8 -*-
import os

import logging

PUB_CONF = {
    'TITLE': 'DMS',
    'dev': {
        'LOG_LEVEL': logging.DEBUG,
        'DB_HOST': '106.13.168.8',
        'DB_PORT': 3306,
        'DB_USER': 'root',
        'DB_PASSWD': '!QAZ2wsx#edc',
        'DB_BASE': 'jincuodao',
        # redis配置
        'REDIS_HOST': '106.13.168.8',
        'REDIS_PORT': 6379,
        'REDIS_PASSWD': '123456',
        'REDIS_DB': 0,
        # jwt
        'JWT_SECRET': '99a6afea88fc0ee763ebe9574c1d1b98',
    # API
    },
    #
    'online': {
    }

}




















