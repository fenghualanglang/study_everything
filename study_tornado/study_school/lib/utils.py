import json
import random
import requests

# from config.setting import 'API_KEY'

def captcha_code():
    captcha = ''.join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 6))
    return captcha


def send_single_sms(username, phone, captcha):
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    code = '【张俊波】亲爱的{}，您的验证码是{}。有效期为15分钟，请尽快验证'.format(username, captcha)
    API_KEY = ''
    res = requests.post(url, data={
        "apikey": API_KEY,
        "mobile": phone,
        "text": code,
    })
    return json.loads(res.text)


if __name__ == '__main__':
    res = send_single_sms("张俊波", "18236766280", '123456')
    print(res)

