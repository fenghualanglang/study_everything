
from flask import Flask

app = Flask(__name__)

@app.route('/index')
def hello_world():
    return "hello world"

@app.route('/detil')
def detil_page():
    return "detil_page"

# 带参数路由
@app.route('/index/<name>')
def hello_world(name):
    return f"hello world {name} "

if __name__ == '__main__':
    # app.run()
    # 调试模式
    app.run(debug=1)