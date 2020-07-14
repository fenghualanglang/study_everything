from flask import Flask
app = Flask (__name__)

app.config['ENV'] = 'developmemt'


@app.route('/')
def hello() -> str:
    return '撸起袖子加油干!'

if __name__ == '__main__':
