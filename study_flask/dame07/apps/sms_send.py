
import time
import json
import random
import hashlib
import urllib
import urllib.parse
import urllib.request

import ssl

class SecretPair(object):

    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key



class SmsSendAPIDemo(object):
    '''网易短信发送接口示例代码'''
    API_URL = "https://api.netease.im/sms/sendcode.action"
    VERSION = 'v2'

    def __init__(self, business_id, secret_pair):

        self.bussine_id = business_id
        self.secret_pair = secret_pair

    def gen_signature(self, params=None):
        '''生成签名信息
        Args：
            params(object) 请求参数
        Returns:
            参数签名md5值
        '''
        buff = ''
        for k in sorted(params.keys()):
            buff += str(k) + str(params[k])

        buff += self.secret_pair.secret_key
        buff = buff.encode('utf-8')
        return hashlib.md5(buff).hexdigest()


    def send(self, params):
        '''
        请求易盾接口
        Args：
            param 请求参数
        Returns:
            请求结果，json格式
        '''
        params['secretId'] = self.secret_pair.secret_id
        params['bussineId'] = self.bussine_id
        params['version'] = self.VERSION
        params['timetamp'] = int(time.time() * 1000)
        params['nonce'] = int(random.random() * 10000000)
        params['signature'] = self.gen_signature(params)

        try:
            params = urllib.parse.urlencode(params)
            params = params.encode('utf-8')
            context = ssl._create_unverified_context() # 忽略安全
            resquest = urllib.request.Request(self.API_URL, params)

            response = urllib.request.urlopen(resquest, timeout=1, context=context)
            content = response.read()
            return json.loads(content)

        except Exception as ex:

            print('调用API接口失败：', str(ex))
            pass


if __name__ == '__main__':
    '''示例代码入口'''
    SECRT_ID = ''  # 产品密钥ID, 产品标识
    SECRT_KEY = ""   #  产品私有密钥, 服务端生成签名


































