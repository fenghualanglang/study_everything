# -*- coding: utf-8 -*-

import json
import time
import urllib
import random
import traceback
import decimal
import jwt
import hashlib
import jsonschema
import peewee
import model
from concurrent.futures import ThreadPoolExecutor

import datetime
from config import log
from config.constant import last_login
from lib.util import Row
from tornado.web import RequestHandler, Finish
from lib.session import Session
from lib.redis import RedisDB
from model.models import (
    fn,
    JOIN,
    User,
    # SysAuth,
    # SysUserAuth,
    # SysDict
)
from playhouse.shortcuts import model_to_dict
import logging

logger = logging.getLogger(__name__)


class JsonParseError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg


class TokenInvalid(Exception):
    pass


class TokenExpire(Exception):
    pass




class BaseHandler(RequestHandler):
    TOKEN_INVALID = -2
    TOKEN_EXPIRE = -1
    TOKEN_MISSING = 0

    # EXPIRE_IN_SECOND = 60
    EXPIRE_IN_SECOND = 3600 * 24 * 2

    def initialize(self, auth=None):
        self.user = Row()
        self.auth = auth
        self.conf = self.application.settings

        self.redis = RedisDB(self.conf)

        model.database.init(
            database=self.conf['db_base'],
            host=self.conf['db_host'],
            port=self.conf.get('db_port', 3306),
            user=self.conf['db_user'],
            passwd=self.conf['db_passwd'],
            charset='utf8',
        )

    @staticmethod
    def dump_json(data):
        def converter(o):
            if isinstance(o, datetime.date):
                return str(o)
            if isinstance(o, decimal.Decimal):
                return float(o)

        ret = json.dumps(data, default=converter, ensure_ascii=False)
        return ret

    def out(self, code=200, data=None, msg='', **kwargs):
        output = {
            'code': code,
            'message': msg
        }
        if data is not None:
            output.setdefault('data', data)
        if kwargs:
            output.update(kwargs)

        res = self.dump_json(output)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(res)

    def abort(self, code=200, data=None, msg='', **kwargs):
        self.out(code=code, data=data, msg=msg, **kwargs)
        raise Finish()

    def get_current_user(self):

        token = self.request.headers.get('Authorization')
        if not token:
            raise TokenInvalid(401, "Invalid Token")
        try:
            payload = jwt.decode(token, self.conf['jwt_secret'], algorithms='HS256')
        except jwt.DecodeError as e:
            raise TokenInvalid()
        else:
            token_uid = payload.get('uid')
            token_uname = payload.get('uname')
            token_last_login = payload.get('lastLogin')

        redis_user_key = "users:{}-{}".format(token_uname, token_uid)
        cache_last_login = self.redis.hget(last_login, token_uid)
        if not cache_last_login:
            self.redis.delete(redis_user_key)
            raise TokenInvalid()

        # 判断是否过期
        now = datetime.datetime.now()
        last = datetime.datetime.strptime(token_last_login, '%Y%m%d%H%M%S')
        elapsed_seconds = (now - last).total_seconds()
        if elapsed_seconds > self.EXPIRE_IN_SECOND:
            self.redis.delete(redis_user_key)
            raise TokenExpire()
        user_info = self.cache_user(token_uid, token_uname, elapsed_seconds=elapsed_seconds)


        return user_info

    def cache_user(self, uid, uname, elapsed_seconds=0):
        redis_user_key = "users:{}-{}".format(uname, uid)
        expire_seconds = int(self.EXPIRE_IN_SECOND - elapsed_seconds)
        cached = None
        if not self.redis.hexists(redis_user_key, 'user'):
            user = User.select().where(User.id == uid).dicts()
            if user.exists():
                user_json = self.dump_json(user.get())
                self.redis.hset(redis_user_key, 'user', user_json)
                self.redis.expire(redis_user_key, expire_seconds)
                cached = Row(user.get())
        else:
            user_dict = self.redis.hget(redis_user_key, 'user')
            cached = Row(json.loads(user_dict))
        self.user = cached
        return cached

    def clean_cache_user(self, uid, uname):
        redis_user_key = "users:{}-{}".format(uname, uid)
        self.redis.delete(redis_user_key)
        self.redis.hdel(last_login, uid)

    def on_close(self):
        self.finish()

    def on_finish(self):
        if not model.database.is_closed():
            model.database.close()

        return super(BaseHandler, self).on_finish()

    @staticmethod
    def md5(text):
        result = hashlib.md5(text)
        return result.hexdigest()

    def get_request_data(self):
        content_type = self.request.headers.get('Content-Type')
        method = self.request.method
        chunk = {k: self.get_argument(k) for k in self.request.arguments}
        chunk['query'] = Row({k: self.get_query_argument(k) for k in self.request.query_arguments})

        if content_type and self.request.body:
            if 'application/x-www-form-urlencoded' in content_type or \
                    'multipart/form-data' in content_type:
                chunk['body'] = Row({k: self.get_body_argument(k) for k in self.request.body_arguments})
            elif 'application/json' in content_type:
                try:
                    chunk['json'] = json.loads(self.request.body)
                except ValueError:
                    raise JsonParseError(400, "Parse json failed")

        logger.info('{method} {uri} {data}'.format(
            uri=self.request.uri,
            method=method,
            data=json.dumps(chunk))
        )
        return Row(chunk)

    def prepare(self):
        if self.auth and self.request.method.upper() in ["POST", "GET", "PUT", "PATCH", "DELETE"]:
            current_user = self.get_current_user()
            self.user = current_user
        self.req = self.get_request_data()
        self.req['uid'] = self.user.id

    def set_default_headers(self):

        self.request.headers.get('Origin')

        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "accept, content-type")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.set_header("Expires", -1)
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, PATCH, DELETE, OPTIONS')

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.on_close()

    @property
    def session(self):
        if hasattr(self, '_session'):
            return self._session
        else:
            sessionid = self.get_secure_cookie('sid')
            self._session = Session(self.application.session_store, sessionid, expires_days=1)
            if not sessionid:
                self.set_secure_cookie('sid', self._session.id, expires_days=1)
            return self._session

    @property
    def now(self):
        return int(time.time())

    def write_error(self, status_code, **kwargs):

        if "exc_info" in kwargs:
            error_obj = kwargs["exc_info"][1]
            error_trace_list = traceback.format_exception(*kwargs.get("exc_info"), limit=5)
            status, message = None, ''
            if isinstance(error_obj, jsonschema.exceptions.ValidationError):
                status = 400
                message = str(error_obj)  # "Bad Request "
            elif isinstance(error_obj, JsonParseError):
                status = 400
                message = "Request JSON Parsing Failed "
            elif isinstance(error_obj, peewee.IntegrityError):
                status = 4000
                message = str(error_obj)
            elif isinstance(error_obj, peewee.DoesNotExist):
                status = 404
                message = "Does Not Exist"
            # elif isinstance(error_obj, model.ModelException404):
            #     status = 404
            #     message = "No Model Instance"
            elif isinstance(error_obj, TokenInvalid):
                status = 401
                message = "请登录"
            elif isinstance(error_obj, TokenExpire):
                status = 412
                message = "登陆过期，请重新登录"
            elif self.settings.get("serve_traceback"):
                logger.debug(str(error_trace_list))

            if status and message:
                self.set_status(200)
                self.out(status, msg=message)
            else:
                self.set_status(status_code)
                self.out(status_code, msg=self._reason)
        else:
            self.set_status(status_code)
            self.out(status_code, msg=self._reason)

    def _request_summary(self):
        return "%s %s (%s)" % (
            self.request.method,
            self.request.uri,
            self.request.remote_ip
        )


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


class UserBaseHandler(BaseHandler):
    executor = ThreadPoolExecutor(2)

    def data_received(self, chunk):
        pass

    def prepare(self):
        super(UserBaseHandler, self).prepare()
