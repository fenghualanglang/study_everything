# -*-coding:utf-8-*-
import requests
# from config.setting import APP_ID, SECRET
from config.parameter import RDS_ACCESS_TOKEN_INFO

from lib.redis import RedisDB

#获取access_token
def get_user_access_token():

    APP_ID = ''
    SECRET = ''
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (APP_ID,SECRET)
    respone = requests.get(url, timeout=50)
    errcode = respone.json().get("errcode")
    if (errcode == 0) or (errcode == None):
        access_token = respone.json()
        access_token['expires_in'] = 3600
        return access_token


# def set_access_token_info():
#     data = get_user_access_token()
#     self._redis_con.hmset(RDS_ACCESS_TOKEN_INFO, data)
#     self._redis_con.expire(RDS_ACCESS_TOKEN_INFO, data['expires_in'])
#