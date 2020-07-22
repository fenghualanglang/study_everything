


tt = {
    "username": "python11",
    "mobile": 18345678904,
    "password": "1QAZ2wsx",
    "email": "1316864657@qq.com",
    "password2": "1QAZ2wsx",
    "allow": "true"
}

from base64 import b64encode
from uuid import uuid4, uuid5

sign = b64encode(uuid4().bytes)

print(sign)
tt = b'hCnyl3vARVqFHIej9pUvcA'
print(len(str(uuid4())))