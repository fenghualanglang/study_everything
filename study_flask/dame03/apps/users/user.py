from flask import Blueprint

user_bp = Blueprint('user', __name__)  # user 为蓝图名字

'''
此时用户url绑定在蓝图上， 用户蓝图未有与app建立联系

所以在create_app那里注册蓝图, 建立联系
'''




@user_bp.route('/')
def user_center():
    return 'yonghu zhongxin'

@user_bp.route('/register', methods=["POST", "POST"])
def user_register():
    return 'yong hu register'


@user_bp.route('/login', methods=["POST", "POST"])
def user_login():
    return 'yong hu login'


@user_bp.route('/logout', methods=["POST", "POST"])
def user_logout():
    return 'yong hu logout'


















