from flask import Request, request, g
from flask import Blueprint
from sqlalchemy import or_, and_, not_

from apps.users.models import User
from apps.orders.models import Article
from ext import db

article_bp = Blueprint('artical', __name__)  # user 为蓝图名字



@article_bp.route('/publist', methods=["GET", "POST"])
def publist():

    if request.method == 'GET':
        # users = User.query.filter(User.is_delete == False).all()

        # 分页
        pagination = Article.query.filter(
            Article.is_delete == False
        ).order_by(
            -Article.pdatatime
        ).paginate(
            page=2,  # 当前页数
            per_page=10  # 每页几条
        )
        print(pagination.items)  #
        print(pagination.page)   # 当前页面
        print(pagination.prev_num)  # 当前页面的前一页面页码数
        print(pagination.next_num)  # 当前页面的下一页面页码数
        print(pagination.has_next)  # 当前页面的是否有下一页面页 true
        print(pagination.has_prev)  # 当前页面的是否有前一页面页 true
        print(pagination.pages)  # 总共多少页
        print(pagination.total)  # 总的条数
        return {}

    if request.method == "POST":
        title = request.form.get('title')
        type_id = request.form.get('type_id')
        content = request.form.get('content')
        uid = request.form.get('uid')

        print(title, '========================================')
        # 添加文章
        article = Article()
        article.title = title
        article.type_id = type_id
        article.content = content

        article.user_id = g.user.id
        db.session(article)
        db.session.commit()






















