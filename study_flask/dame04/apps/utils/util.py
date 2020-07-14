import qiniu as qiniu
from qiniu import Auth, put_file, etag, BucketManager


def upload_qiniu(filetorage):

    # 填写你的access_key 和 secret_key
    access_key = '替换成你的'
    # 个人中心->密匙管理->SK
    secret_key = '替换成你的'
    # 构建鉴权对象
    q = qiniu.Auth(access_key, secret_key)
    # 上传七牛空间名
    bucket_name = '替换成你的'
    # 上传后保存的文件名
    filename = filetorage.filename
    key = '文件名'
    # 生成上传token， 可以指定过期时间
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = qiniu.put_data(token, key, filetorage.read())

    return info, ret


def delete_qiniu(filename):

    # 填写你的access_key 和 secret_key
    access_key = '替换成你的'
    # 个人中心->密匙管理->SK
    secret_key = '替换成你的'
    # 构建鉴权对象
    q = qiniu.Auth(access_key, secret_key)
    # 上传七牛空间名
    bucket_name = '替换成你的'
    # 初始化BuketManager
    bucket = BucketManager(q)
    # 要删除文件的名字
    key = filename
    ret, info = bucket.delete(bucket_name, key)

    return info, ret















