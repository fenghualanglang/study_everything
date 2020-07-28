import logging

from flask import Flask

app = Flask(__name__)
app.config['ENV'] = 'development'

logger = logging.getLogger(__name__)
# 创建一个文件对象  创建一个文件对象,以UTF-8 的形式写入 标配版.log 文件中
handler = logging.FileHandler('test.log',encoding='utf-8')
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
handler.setFormatter(formatter)  # 将格式绑定到两个对象上
logger.addHandler(handler)   # 将句柄绑定到logger

@app.route('/')
def index():
    logger.warning('首页')
    app.logger.warning('zzzzzzzzzzzzzzzzz')
    return {'code': 200, 'data': {'name': 'zhangsan'}, 'msg': 'ok'}


@app.route('/test')
def test():


    return {'code': 200, 'data': {'name': 'zhangsan'}, 'msg': 'ok'}

if __name__ == '__main__':
    app.run(debug=True)




















