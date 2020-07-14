from flask import Request, request, Response, make_response, session, g
from flask import Blueprint
from sqlalchemy import or_, and_, not_
from werkzeug.security import generate_password_hash, check_password_hash

from apps.orders.models import Photo
from apps.users.models import User
from ext import db

user_bp = Blueprint('user', __name__)  # user 为蓝图名字

'''
此时用户url绑定在蓝图上， 用户蓝图未有与app建立联系

所以在create_app那里注册蓝图, 建立联系
'''




@user_bp.route('/register', methods=['GET', "POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        passworld = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')

        print(username, '222222222222222222222')

        if passworld == repassword:
            # 找到模型类
            user = User()
            # 给模型类赋值
            user.username = username
            user.passworld = passworld
            # user.repassword = repassword
            user.repassword = generate_password_hash(passworld)
            user.phone = phone
            # 将user对象添加到session中(类似预缓存)
            db.session.add(user)
            # 提交数据
            db.session.commit()

    return 'yonghu zhongxin'

@user_bp.route('/user_center', methods=["POST", "POST"])
def user_center():

    users = User.query.all()

    return users

@user_bp.route('/login', methods=["POST", "POST"])
def user_login():

    if request.method == "POST":
        username = request.form.get('username')
        passworld = request.form.get('password')
        # passworld = request.args.get('password')

        User.query.all()
        User.query.count()
        users = User.query.filter_by(username=username)
        users = User.query.filter_by(username=username).first()
        users = User.query.filter_by(username=username).all()
        users = User.query.filter_by(username=username).exists()
        users = User.query.filter(User.id == 4).all()
        # 根据主键查询用户
        user = User.query.get(2)
        user = User.query.filter(User.username.startswith('z')).all()
        user = User.query.filter(User.username.endswith('z')).all()
        user = User.query.filter(User.username.contains('z')).all()
        user = User.query.filter(User.username.like('%俊%')).all()

        user = User.query.filter(or_(User.username.like('z%'), User.username.contains('san'))).all()
        user = User.query.filter(and_(User.username.like('z%'), User.content < '2020-09-20 08:08:20')).all()
        user = User.query.filter(User.username.like('z%'), User.content < '2020-09-20 08:08:20').all() # 与adnd相同
        user = User.query.filter(and_(User.username.like('z%'), User.content.__lt__('2020-09-20 08:08:20'))).all()
        # __gt__ ___lt__ ___ge__ __le___ 适用日期 整形
        user = User.query.filter(not_(User.username.contains('z'))).all()
        user = User.query.filter(User.phone.in_([12345667, 2456789])).all()
        user = User.query.filter(User.age.between(15, 30)).all()
        user = User.query.order_by().all()
        user = User.query.filter(User.username.contains('z')).order_by(User.id).all()
        user = User.query.order_by(-User.id).all()
        user = User.query.limit(2).all()  # 获取所有数据的前两条
        user = User.query.offset(2).limit(2).all()  # 先偏移2个再取两个
        user = User.query.filter(User.username)


        print(user, '-----------')

        for u in users:
            flag = check_password_hash(user.passworld, passworld)
            if flag:
                Response.set_cookie('uid', user.uid, max_age=1800)
                # make_response()

                # Response.set_cookie('uid', user.uid, expires=1800)
                return '登陆成功'
        '''
        获取cookie信息 前端传来的cookie信息
        uid = request.cookies.get('uid')
        根据uid 查找用户的到用户信息
        '''



    # return '登陆失败'

@user_bp.route('/delete', methods=["POST", "POST"])
def user_delete():

    # 逻辑删除
    id = request.args.get('id')
    user = User.query.get(id)
    user.is_delete = True
    db.session.commit()

    # 物理删除
    user = User.query.get(id)
    # 讲对象放到缓存准备物理删除
    db.session.delete(user)
    # 提交删除
    db.session.commit()

    return 'yong hu logout'

@user_bp.route('/logout', methods=["POST", "POST"])
def user_logout():
    return 'yong hu logout'

# 发送短信通知
@user_bp.route('/sendmsg', method=['GET'])
def send_message():
    pass

# 可以上传图片的扩展名
ALLOWED_EXTENSIONS = ['jpg', 'png', 'gif']

# 用户信息修改
@user_bp.route('/change', method=['GET', 'POST'])
def user_change():
    if request.method == 'POST':
        username = request.form.get('username')
        username = request.form.get('username')
        icon = request.files.get('icon')

        icon_name = icon.filename
        suffix = icon_name.rsplit[-1]
        if suffix in ALLOWED_EXTENSIONS:
            pass
        return '头像不合格'









# 上传图片
@user_bp.route('/upload_pjoto', methods=['GET', 'POST'])
def upload_photo():

    # 获取上传文件内容
    photo = request.files.get('photo')
    # 工具模块中封装方法
    from apps.utils.util import upload_qiniu
    ret, info = upload_qiniu(photo)

    if info.status_code == 200:
        photo = Photo()
        photo.photo_name = ret['key']
        photo.user_id = g.user.id
        db.session.add(photo)
        db.session.commit()
        return '上传成功'
        pass
    else:
        return '上传失败'



# 上传图片
@user_bp.route('/delete_pjoto', methods=['GET', 'POST'])
def upload_photo():
    from apps.utils.util import delete_qiniu
    pid = request.args.get('pid')
    photo = Photo.query.get(pid)
    filename = photo.photo_name
    info = delete_qiniu(filename)

    if info.status_code == 200:
        # 删除数据库的内容
        db.session.delete(photo)
        db.session.commit()
        return '删除成功'
    else:
        return '删除失败'












'''
用户登录
短信登录账号密码登录传个参数 f区分一下
'''


'''
登录权限认证
只要走center路由，判断用户是否是登录状态
如果用户登录，可以正常显示页面
如果用户没有登录，则自动跳转到登录页面进行登录，登陆之后才可以查看
'''


'''
钩子函数
直接应用在app上
before_first_request
before_request
after_request
teardown_request
'''

'''
应用到蓝图
before_app_first_request
before_app_request
after_app_request
teardown_app_request
'''

# 要求过滤登录的路由
requred_login_list = ['/user/center', '/artical/publist']

@user_bp.before_app_first_request
def first_request():

    print('before_app_first_request')

@user_bp.before_app_request
def before_request1():
    if request.path in requred_login_list:
        id = session.get('uid')
        if not id:
            return '跳出页面'
        else:
            user = User.query.get(id)
            # g 对象，本次请求的对象
            g.user = user

    print('before_app_request')


@user_bp.after_app_request
def fter_app_request_test(response):

    response.set_cookie('a', 'bbb', max_age=1200)
    return response























