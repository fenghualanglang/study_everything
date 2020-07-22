from django.conf import settings
from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as TJWSSerializer


from core.models import (
    EmailVerifyRecord,
    User

)

from base64 import b64encode
from uuid import uuid4


def encrypt(send_type, email):

    data = {'email': email, 'send_type': send_type, }
    serializer = TJWSSerializer(secret_key=settings.SECRET_KEY, expires_in=3000)

    token = serializer.dumps(data)  # bytes
    token = token.decode()  # bytes->str

    return token


def decrypt(token):

    serializer = TJWSSerializer(secret_key=settings.SECRET_KEY)
    try:
        data = serializer.loads(token)
    except:
        return None  # 解密失败
    else:
        # 解密成功
        return data





def sign():

    sign = b64encode(uuid4().bytes + uuid4().bytes)

    return sign
















def send_verify_email(send_type, email):

    # if email_type == "register":
    #     email_title = "慕学在线网注册激活链接"
    #     email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
    #
    #     # send_mail('注册激活', '', settings.EMAIL_FROM, [email], html_message=msg)
    #
    #     send_status = send_mail(email_title, '', email_body, email, [email])
    #
    #     if send_status:
    #         pass

    token = encrypt(send_type, email)
    if send_type == "forget":
        EmailVerifyRecord.objects.create(
            email=email,
            send_type='forget'
        )
        email_title = "最上川在线网注册密码重置"
        email_body = f"请点击下面的链接重置密码: {settings.BASE_URL}reset?token={token}"

        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:
            pass

    # elif email_type == "update_email":
    #     email_title = "慕学在线邮箱修改验证码"
    #     email_body = "你的邮箱验证码为: {0}".format(code)
    #
    #     send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    #     if send_status:
    #         pass
