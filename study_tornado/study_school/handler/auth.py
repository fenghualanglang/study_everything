import datetime

from handler import BaseHandler
from model.models import User
from lib.util import (
    valid_phone_number,
    mask_phone,
    hashed_login_pwd,
    generate_salt,
    generate_random_str,
    generate_token,
    is_valid_idcard
)


from config.log import logger_user
from config import constant, status


class LoginHandler(BaseHandler):

    def post(self):

        username = self.req.body.username
        password = self.req.body.password

        user = User.select(
            User.id,
            # User.passwd,
            # User.user_name,
            # User.role_name,
            # User.emp_level
        ).where(User.user_name == username).first()
        if not user:
            return self.out(status.pwd_not_set.code, msg=status.pwd_not_set.msg)

        # if hashed_login_pwd(password, user.salt) != user.passwd:
        #     return self.out(status.password_error.code, status.password_error.msg)

        # uid = user.id
        #
        # # 记录用户登陆的有效时间
        # latest = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # self.redis.hset(constant.last_login, uid, latest)
        #
        # token = generate_token(str(uid), latest, self.conf['jwt_secret']).decode()
        res = {"token": 'token', 'user_name': user.user_name, 'role_name': user.role_name, 'emp_level': user.emp_level}
        return self.out(200, data=res)
