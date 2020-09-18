from datetime import datetime

from jsonschema import validate
from playhouse.shortcuts import model_to_dict

from handler import UserBaseHandler
from lib.util import generate_token
from model.models import User
from config import constant, status
from lib.utils import send_single_sms, captcha_code

class UserRegisterHandler(UserBaseHandler):

    def get(self):
        req_data = self.req.query
        phone = req_data.get('phone')
        register_captcha = self.redis.hget(constant.register_captcha, phone)
        if register_captcha:
            return self.out(code=status.success.code, data={"captcha" : register_captcha}, msg="ok")
        return self.out(code=status.validate_error.code, data={"captcha" : register_captcha}, msg="验证码错误")

    def post(self):
        """
        ---
        tags:
        - 用户
        summary: 修改信息
        produces:
        - "application/json"
        parameters:
        -   in: body
            name: body
            description: "json"
            required: true
            example: {
                "user_name":"python",
                "???user_name":"用户名",
                "birthday":"2020-08-24",
                "???birthday":"生日",
                "introduction":"物竞天择，适者生存; 世道必进，后胜于今",
                "???introduction":"介绍",
                "university":"清华大学",
                "???university":"大学",
                "college":"光华管理学院",
                "???college":"院系",
                "profession":"国际政治与贸易",
                "???profession":"专业"
            }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "user_name": {"type": "string"},
                "birthday": {"type": "string", "format": "date"},
                "college": {"type": "string"},
                "university": {"type": "string"},
                "introduction": {"type": "string"},
                "profession": {"type": "string"}
            }
        }
        json_data = self.req.json
        validate(json_data, json_schema)
        cur_user_id = self.user.id

        condition = [User.gmt_modified == datetime.now()]

        if json_data.get('user_name'):   # 用户名
            condition.append(User.user_name == json_data.get('user_name'))
        if json_data.get('birthday'):    # 生日
            condition.append(User.birthday == json_data.get('birthday'))
        if json_data.get('college'):     # 学院
            condition.append(User.college == json_data.get('college'))
        if json_data.get('university'):  # 大学
            condition.append(User.university == json_data.get('university'))
        if json_data.get('introduction'):  # 介绍
            condition.append(User.introduction == json_data.get('introduction'))
        if json_data.get('sex'):  # 性别
            condition.append(User.sex == json_data.get('sex'))
        if json_data.get('addr'):  # 性别
            condition.append(User.addr == json_data.get('addr'))

        query = User.update(*condition).where(User.id == cur_user_id).dicts()
        return self.out(code=status.success.code, data=list(query), msg=status.success.msg)


# 调用发送发送验证码服务
class CaptchaHandler(UserBaseHandler):

    def post(self):
        """
        ---
        tags:
        - 用户
        summary: 验证码
        parameters:
        -   in: body
            name: body
            required: true
            example: {
                    "register_phone": "18236766380",
                    "???register_phone":"手机号"
             }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "captcha": "039421"
                    }
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "user_name": {"type": "string"},
                "register_phone": {"type": "string", "pattern": "^1[35678]\d{9}$"},
            }
        }
        json_data = self.req.json
        cur_user_id = self.user.id
        username= self.user.user_name
        validate(json_data, json_schema)
        register_phone = json_data.get('register_phone')
        register_key = f"{constant.register_captcha}:{cur_user_id}"
        if self.redis.exists(register_key):
            return self.out(code=status.success.code, msg="验证已发送")
        captcha = captcha_code()
        resp_sms = send_single_sms(username=username, phone=register_phone, captcha=captcha)
        if resp_sms.get("code"):
            return self.out(code=status.validate_error.code, msg=resp_sms.get("msg"))
        register_value = {"register_phone": register_phone, "register_captcha": captcha}
        self.redis.hmset(register_key,  register_value)
        self.redis.expire(register_key, 60*15)
        return self.out(code=status.success.code, msg="ok")


class UserHandler(UserBaseHandler):

    def get(self):
        """
        ---
        tags:
        - 用户
        summary: 用户
        produces:
        - "application/json"
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code":200,
                    "message":"",
                    "data":{
                        "token":"eyJ0eXAiLCQ1qZWCSLpzc",
                        "res":{
                            "id":1,
                            "addr":"北京市朝阳区故宫博物院",
                            "birthday":"2020-07-10",
                            "college":"光华管理学院",
                            "notice":"计算机科学与技术",
                            "major":"国际经济与贸易",
                            "phone":"18236766280",
                            "introduction":"签名",
                            "university":"wetwe",
                            "user_name":"python",
                            "wx_avatarurl":"https://csdnimg.cn/feed/20200817/23f9fef9eeb10a423a3e72bc60861ff9.jpg",
                            "wx_name":"python"
                        }
                    }
                }
        security:
        -   Token: []
        """
        user_id = self.user.id
        query = User.select(
            User.id,
            User.sex,
            User.addr,
            User.birthday,
            User.college,
            User.notice,
            User.is_active,
            User.major,
            User.introduction,
            User.university,
            User.user_name,
            User.wx_avatarurl,
            User.wx_name,
            User.last_login_time
        ).where(
            User.id == user_id
        ).dicts()

        if not query.exists():
            return self.out(code=status.not_found.code, data={}, msg="用户不存在")
        return self.out(code=status.success.code, data=query.first(), msg="ok")

    def put(self):
        """
        ---
        tags:
        - 用户
        summary: 修改信息
        produces:
        - "application/json"
        parameters:
        -   in: body
            name: body
            description: "json"
            required: true
            example: {
                "user_name":"python",
                "???user_name":"用户名",
                "birthday":"2020-08-24",
                "???birthday":"生日",
                "introduction":"物竞天择，适者生存; 世道必进，后胜于今",
                "???introduction":"介绍",
                "university":"清华大学",
                "???university":"大学",
                "college":"光华管理学院",
                "???college":"院系",
                "major":"国际政治与贸易",
                "???major":"专业"
            }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "user_name": {"type": "string"},
                "birthday": {"type": "string", "format": "date"},
                "college": {"type": "string"},
                "university": {"type": "string"},
                "introduction": {"type": "string"},
                "major": {"type": "string"}
            }
        }
        json_data = self.req.json
        validate(json_data, json_schema)
        cur_user_id = self.user.id

        condition = {'gmt_modified': datetime.now()}

        if json_data.get('user_name'):   # 用户名
            condition["user_name"] = json_data.get('user_name')
        if json_data.get('birthday'):    # 生日
            condition["birthday"] = json_data.get('birthday')
        if json_data.get('college'):     # 学院
            condition["college"] = json_data.get('college')
        if json_data.get('university'):  # 大学
            condition["university"] = json_data.get('university')
        if json_data.get('introduction'):  # 介绍
            condition["introduction"] = json_data.get('introduction')
        if json_data.get('sex'):  # 性别
            condition["sex"] = json_data.get('sex')
        if json_data.get('addr'):  # 性别
            condition["addr"] = json_data.get('addr')
        if json_data.get('major'):  # 性别
            condition["major"] = json_data.get('major')

        User.update(**condition).where(User.id == cur_user_id).dicts()
        return self.out(code=status.success.code, data=condition, msg=status.success.msg)

    def patch(self):
        """
        ---
        tags:
        - 用户
        summary: 修改手机号
        parameters:
        -   in: body
            name: body
            required: true
            example: {
                    "captcha": "2345678",
                    "???captcha":"验证码"
             }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "captcha": "039421"
                    }
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "captcha": {"type": "string"},
                # "register_phone": {"type": "string", "pattern": "^1[35678]\d{9}$"},
            }
        }
        json_data = self.req.json
        validate(json_data, json_schema)
        captcha = json_data.get('captcha')
        cur_user_id = self.user.id
        register_key = f"{constant.register_captcha}:{cur_user_id}"
        register_phone = self.redis.hget(register_key, "register_phone").decode("utf8")
        register_captcha = self.redis.hget(register_key, "register_captcha").decode("utf8")
        if captcha != register_captcha:
            return self.out(code=status.validate_error.code, msg="验证码错误")
        User.update(phone=register_phone).where(User.id == cur_user_id).execute()
        self.redis.delete(register_key)
        return self.out(code=status.success.code, msg="ok")


class LoginHandler(UserBaseHandler):

    def login(self, check_func=None):
        username = self.req.body.username
        password = self.req.body.password
        user = User.select().where(User.user_name == username).first()
        if not user or user.passwd != password:
            return self.out(code=status.auth_failed.code, msg="用户名或者密码不正确")
        if callable(check_func):
            check_func(user)
        uid = user.id
        uname = user.user_name
        user_info = self.cache_user(uid, uname)
        # 记录用户登陆的有效时间
        latest = datetime.now().strftime('%Y%m%d%H%M%S')
        self.redis.hset(constant.last_login, uid, latest)
        token = generate_token(str(uid), uname, latest=latest, secret=self.conf['jwt_secret']).decode()
        res = user_info
        User.update(last_login_time=latest).where(User.id == uid).execute()
        return self.out(200, data={"token": token, "res": res})

    def post(self):
        """
        ---
        tags:
        - 用户
        summary: 登录
        consumes:
        -   "application/x-www-form-urlencoded"
        produces:
        - "application/json"
        parameters:
        -   in: formData
            name: username
            description: "用户登录名"
            required: true
            example: python
        -   in: formData
            name: password
            description: "用户登录密码"
            required: true
            example: 123456
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "wo_no": "DDL20190327"
                    }
                }
        """
        return self.login()


class LogoutHandler(UserBaseHandler):
    def data_received(self, chunk):
        pass

    def post(self):
        """
        ---
        tags:
        - 用户
        summary: 退出登录
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                }
        security:
        -   Token: []
        """
        uid = self.user.id
        uname = self.user.user_name
        self.clean_cache_user(uid, uname)
        return self.out(code=status.success.code, msg=status.success.msg)
