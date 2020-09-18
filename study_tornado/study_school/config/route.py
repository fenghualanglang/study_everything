# -*- coding: utf-8 -*-
from tornado.web import url
from handler import (
    auth, demo, error
)

from handler import (
    user,
    user_addr,
    sys_university
)


def policy(auth=False):
    return {
        'auth': auth
    }


routes = [
    url(r"/hello", demo.DemoHandler, policy(auth=True)),
    url(r"/hello", demo.DemoHandler, policy(auth=True)),
    url(r'/login', user.LoginHandler),
    url(r'/logout', user.LogoutHandler, name='退出登录', kwargs=policy(auth=True)),
    url(r'/user', user.UserHandler, name='用户信息', kwargs=policy(auth=True)),
    url(r'/captcha', user.CaptchaHandler, name='验证码', kwargs=policy(auth=True)),

    url(r'/university', sys_university.SysUniversityHandler, name='大学列表', kwargs=policy(auth=False)),
    url(r'/university/([0-9]+)/conllege', sys_university.SysCollegeHandler, name='学院信息', kwargs=policy(auth=False)),
    url(r'/area', sys_university.SysAreasHandler, name='城市信息', kwargs=policy(auth=False)),
    url(r'/useraddr', user_addr.UserAddrHandler, name='收货地址', kwargs=policy(auth=True)),

    # url(r"/login2", auth.LoginHandler),
    # url(r".*", error.ErrorHandler),
]