import random

import requests

from celery_app.main import app, log


def captcha_code():
    captcha = ''.join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 6))
    return captcha


def send_single_sms(username, phone, captcha):
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    code = '【张俊波】亲爱的{}，您的验证码是{}。有效期为15分钟，请尽快验证'.format(username, captcha)
    res = requests.post(url, data={
        "apikey": '046dcfa04c46d780dae6344d7f9af126',
        "mobile": phone,
        "text": code,
    })
    # return json.loads(res.text)

@app.task
def send_sms(phone):
    code = captcha_code()
    send_single_sms("柯丽萍", phone, code)

# if __name__ == '__main__':
#     send_sms('18236766280')