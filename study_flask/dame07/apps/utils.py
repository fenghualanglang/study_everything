








import random

from apps.sms_send import SecretPair, SmsSendAPIDemo


def send_duanxin(phone):

    SECRET_ID = '' # 产品id， 产品标识
    SECRET_KEY = ''  # 产品私有密钥，服务端生成签名信息
    BUSINESS_ID = ''  # 业务id， 易盾根据业务特点

    secret_pair = SecretPair(SECRET_ID, SECRET_KEY)
    api = SmsSendAPIDemo(BUSINESS_ID, secret_pair)

    # 产生验证码
    code = ''
    for i in range(4):
        ran = random.randint(0, 9)
        code += str(ran)

    params = {
        "mobile": phone,
        'templateId': '123456',
        "paramType": 'json',
        'params': {'code': code}
    }

    ret = api.send(params)

    return ret, code





























