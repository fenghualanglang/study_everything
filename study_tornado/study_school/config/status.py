# -*- coding: utf-8 -*-


class Status(object):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

# common
success = Status(200, 'success')
auth_failed = Status(4003, u'认证错误')
not_found = Status(4004, u'无记录')
arguments_error = Status(4005, u'参数错误')
request_timeout = Status(4006, u'请求超时')
validate_error = Status(4007, u'参数校验错误')
json_parse_error = Status(4008, u'JSON 格式错误')
time_format_error = Status(4008, u'TIME 格式错误')
pwd_not_set = Status(4008, u'passwd not set')

class JsonParseError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
