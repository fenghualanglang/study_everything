


import hashlib

msg = 'hello world'


md5 = hashlib.md5(msg.encode('utf-8')).hexdigest()

print(md5)

sha1 = hashlib.sha1(msg.encode('utf-8')).hexdigest()

print(sha1)











