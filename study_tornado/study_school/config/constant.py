# -*- coding:utf-8 -*-

from enum import *


class Status(Enum):
    SUBMIT = 1
    PAY = 2
    SHIPMENTS = 3
    FINISH = 4
    CLOSE = 5

# Redis key area
last_login = 'UserLastLogin'

register_captcha = 'captcha'