from flask import Flask, make_response, Response, request

import settings

app = Flask(__name__)

# 通过这种方法可以改变默认的配置(加载文件)
app.config.from_object(settings)

# 通过这种方法可以改变默认的配置(加载文件路径字符)
app.config.from_pyfile('settings.py')

@app.route('/')
def hello_world():

    return 'hello world'


@app.route('/hello2')
def hello_world2():
    res = Response('zhangsan')
    res.content_encoding = 'utf8'
    return res

@app.route('/hello3')
def hello_world3():
    res = make_response('zhangsan')
    res.headers['mytest'] = '1234567'
    res.headers = 'tttt'
    res.status_code = 200  # 整形
    res.status = 300  # 带ok
    return res

@app.route('/hello4', methods=['GET', "POST"])
def hello_world4():
    if request.method == 'POST':
        username = request.form.get('username')
        passsword = request.form.get('passsword')
        passsword = request.args.get('passsword')


    return '注册成功'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

