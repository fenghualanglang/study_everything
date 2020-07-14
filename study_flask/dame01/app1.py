from flask import Flask


app = Flask(__name__)

# 通过这种方法可以改变默认的配置
app.config['ENV'] = 'development'

print(app.config)

@app.route('/')
def hello_world():

    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)




# flask 默认配置  Config
'''
ENV: production  环境 development  testing
DEBUG: False
TESTING: False
PROPAGATE_EXCEPTIONS: None
PRESERVE_CONTEXT_ON_EXCEPTION: None
SECRET_KEY: None
PERMANENT_SESSION_LIFETIME: datetime.timedelta(31)
USE_X_SENDFILE: False
SERVER_NAME: None   域名
APPLICATION_ROOT: /
SESSION_COOKIE_NAME: session
SESSION_COOKIE_DOMAIN: None
SESSION_COOKIE_PATH: None
SESSION_COOKIE_HTTPONLY: True
SESSION_COOKIE_SECURE: False
SESSION_COOKIE_SAMESITE: None
SESSION_REFRESH_EACH_REQUEST: True
MAX_CONTENT_LENGTH: None
SEND_FILE_MAX_AGE_DEFAULT: datetime.timedelta(0, 43200)
TRAP_BAD_REQUEST_ERRORS: None
TRAP_HTTP_EXCEPTIONS: False
EXPLAIN_TEMPLATE_LOADING: False
PREFERRED_URL_SCHEME: http
JSON_AS_ASCII: True
JSON_SORT_KEYS: True
JSONIFY_PRETTYPRINT_REGULAR: False
JSONIFY_MIMETYPE: application/json
TEMPLATES_AUTO_RELOAD: None
MAX_COOKIE_SIZE: 4093
'''






