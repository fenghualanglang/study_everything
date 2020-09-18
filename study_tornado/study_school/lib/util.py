#!usr/bin/env python
# -*- coding: utf-8 -*-

import json
from cgi import FieldStorage
from datetime import datetime
import hashlib
import random
import re
import urllib
import simplejson
import string

import jwt

import xml.etree.ElementTree as ET

def setting_from_object(obj, mode='dev'):
    setting = {}
    if obj:
        tmp_dict = obj.get(mode, {}) if obj else {}
        setting.update(tmp_dict)
        setting.update(obj)

    configs = dict()
    for key in setting:
        if key.isupper():
            configs[key.lower()] = setting[key]

    return configs


def vmobile(mobile):
    return re.match(r"((13|14|15|18)\d{9}$)|(\w+[@]\w+[.]\w+)", mobile)


def generate_token(uid, uname, latest=None, secret=''):
    """
    生成用户json web token
    :return: jwt值
    """
    payload = {
        'uid': uid,
        'uname':uname,
        'lastLogin': latest if latest else datetime.now().strftime('%Y%m%d%H%M%S'),
    }
    return jwt.encode(payload, secret, algorithm='HS256')


def generate_random_str(length=6, category="verify_code"):
    """
    生成随机字符串
    :param length: 
    :param category:
    :return: 
    """
    category_dict = {
        "verify_code": string.digits,
        "username": string.digits + string.ascii_letters
    }
    return ''.join([random.choice(category_dict.get(category)) for _ in range(length)])


def generate_salt(length=32):
    """
    生成随机盐
    :param length: 
    :return: 
    """
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for _ in range(length)])


def _hashed_with_salt(info, salt):
    """
    md5 + salt加密
    :param info: 待加密信息
    :param salt: 盐值
    :return: 加密后信息
    """
    m = hashlib.md5()
    info = info.encode('utf-8') if isinstance(info, unicode) else info
    salt = salt.encode('utf-8') if isinstance(salt, unicode) else salt
    m.update(info)
    m.update(salt)
    return m.hexdigest()


def hashed_login_pwd(pwd, salt):
    """
    加密登录密码
    :param pwd: 登录密码
    :return: 加密后的密码
    """
    return _hashed_with_salt(pwd, salt)


def valid_phone_number(phone_number):
    """
    手机号码合法性校验
    :param phone_number: 手机号
    :return: bool值
    """
    pattern = re.compile(r'^(13[0-9]|15[012356789]|17[0-9]|18[0-9]|14[57]|19[0-9]|16[0-9])[0-9]{8}$')
    return pattern.match(str(phone_number))


def valid_password(password):
    """
    密码合法性校验
    :param password: 密码
    :return: bool值
    """
    pattern = re.compile(r'^[\S]{10, }$')
    return pattern.match(str(password))


def mask_phone(phone):
    """
    加密手机号
    :param phone: 
    :return: 
    """
    if not valid_phone_number(phone):
        return ''
    return phone[0:3] + '****' + phone[7:]


def concat_params(params):
    pairs = []
    for key in sorted(params):
        if key == 'sig':
            continue
        val = params[key]
        if isinstance(val, unicode):
            val = urllib.quote_plus(val.encode('utf-8'))
        elif isinstance(val, str):
            val = urllib.quote_plus(val)
        elif isinstance(val, dict):
            val = json.dumps(val).replace(' ', '')
        if not isinstance(val, FieldStorage):
            pairs.append("{}={}".format(key, val))
    return '&'.join(pairs)


def is_valid_idcard(idcard):
    """Validate id card is valid."""

    IDCARD_REGEX = '[1-9][0-9]{14}([0-9]{2}[0-9X])?'
    if not idcard:
        return False

    if isinstance(idcard, int):
        idcard = str(idcard)

    if not re.match(IDCARD_REGEX, idcard):
        return False

    if not (14 < len(idcard) < 19):
        return False

    # 地域判断
    # if idcard[:6] not in AREA_CODES:
    #     return False

    return True

    # factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # items = [int(item) for item in idcard[:-1]]
    #
    # copulas = sum([a * b for a, b in zip(factors, items)])
    #
    # ckcodes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    #
    # print idcard[-1], ckcodes[copulas % 11]
    # return ckcodes[copulas % 11].upper() == idcard[-1].upper()


def gen_sig(path_url, params, consumer_secret):
    params = concat_params(params)

    to_hash = u'{}?{}{}'.format(
        path_url, params, consumer_secret
    ).encode('utf-8').encode('hex')

    sig = hashlib.new('sha1', to_hash).hexdigest()
    return sig


class Row(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            return None


class UtilMixin(object):
    def find_subclasses(self, klass, include_self=False):
        accum = []
        for child in klass.__subclasses__():
            accum.extend(self.find_subclasses(child, True))
        if include_self:
            accum.append(klass)
        return accum

    @staticmethod
    def sendmsg(settings, mobile, content):
        url = "%s?accesskey=%s&secretkey=%s&mobile=%s&content=%s" % (
            settings['sms_gateway'], settings['sms_key'], settings['sms_secret'], mobile, urllib.quote_plus(content))
        result = simplejson.loads(urllib.urlopen(url).read())

        if int(result['result']) > 1:
            raise Exception('无法发送')

    @staticmethod
    def get_pages(total, per_page_num):
        pages = total / per_page_num
        if total % per_page_num != 0:
            pages += 1
        return pages






