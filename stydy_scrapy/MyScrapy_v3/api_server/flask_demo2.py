
'''

请求方法  get  post  put delete
获取参数  request.form

'''


from flask import Flask, render_template, request, redirect, url_for, abort, make_response

app = Flask(__name__)


# 返回页面
@app.route('/index')
def index_page():
    return render_template('index.html')

# 根据请求方法返回
@app.route('/login', methods=['GET', "POST"])
def detil_page():
    '''获取参数'''
    username = request.form['username']
    password = request.form['password']
    if username != None and password != None:
        return render_template('sucess.html', msg='登陆成功')
    return render_template('index.html', msg='账号或密码不正确却')


# 重定向
@app.route('/url')
def return_url():
    return redirect(url_for('index_page'))

# 返回状态吗
@app.route('/code')
def return_error():
    abort(403)


# 返回自定义
@app.route('/set')
def return_set():
    res = make_response('返回自定义的响应')
    res = res.headers['cookie'] = 'abcdef'
    return res



# 带参数路由
@app.route('/index/<name>')
def hello_world(name):
    return f"hello world {name} "






if __name__ == '__main__':
    # app.run()
    # 调试模式
    app.run(debug=1)