

from flask import Blueprint
from flask_restful import Api, fields, marshal_with, Resource, reqparse


from apps.models.news_model import NewType, News
from apps.utils import login_required

from exts import api, db

news_bp = Blueprint('news', __name__, url_prefix='/api')

# 返回字段
types_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'desc': fields.String

}

# 添加验证
type_parser = reqparse.RequestParser()
type_parser.add_argument('typeName', type=str, required=True, help='请添加新闻分类')

# 修改验证
update_type_parser = type_parser.copy()
update_type_parser.add_argument('id', type=int, required=True, help='类型id')

# 删除的传入

delete_type_parser = reqparse.RequestParser()
delete_type_parser.add_argument('id', type=int, required=True, help='类型id')



# 新闻类型api
class NewsTypeHandler(Resource):

    @marshal_with(types_fields)
    def get(self):
        types = NewType.query.all()
        return types

    def post(self):
        args = type_parser.parse_args()
        type_name = args.get('typeName')

        # 添加数据库
        news_type = NewType()
        news_type.type_name = type_name
        db.session.add(news_type)
        db.commit()

        return marshal_with(news_type, types_fields)

    def patch(self):
        args = update_type_parser.parse_args()

        type_id = args.get('id')
        new_type_name = args.get('typeName')
        # 修改
        type_obj = NewType.query.get(type_id)
        if type_obj:
            type_obj.type_name = new_type_name
            db.session.commit()
            data = {
                'status': 200,
                'msg': 'ok',
                'type': marshal_with(type_obj, types_fields)
            }
            return data

        return {'status': 400, 'msg': '类型查找失败'}









        pass

    def put(self):

        pass

    def delete(self):
        args = delete_type_parser.parse_args()
        type_id = args.get('id')
        type_obj = NewType.query.get(type_id)
        if type_obj:
            db.session.delete(type_obj)
            db.session.commit()
            return {'status': 200, 'msg': '删除成功'}
        return {'status': 400, 'msg': '查无类别'}


# 评价的格式
comment_fields = {
    'content': fields.String,
    'love_num': fields.Integer(),
    'data_time': fields.DateTime()
}

#
news_fields = {
    'id': fields.Integer,
    'title': fields.String(attribute='type_name'),
    'comments': fields.List(fields.Nested(comment_fields))
}


news_parser = reqparse.RequestParser()
news_parser.add_argument('type_id', help="新闻id", reqired=True)
news_parser.add_argument('page', help="页码")

class NewsHandler(Resource):

    def get(self):
        args = news_parser.parse_args()
        type_id = args.get('type_id')
        page = args.get('page', 1)

        paginate = News.query.filter(News.news_id == type_id).paginate(page=page, pre_page=8)

        data = {
            'has_more': paginate.has_next,
            'data': marshal_with(paginate.items, news_fields),
            'return_count': paginate.pages,
            'html':'null',
        }
        return data

    def post(self):

        pass

    # 部分修改
    def patch(self):
        pass

    # 全部修改
    def put(self):

        pass

    def delete(self):

        pass








news_detail_filds = {
    'id': fields.Integer,
    'title': fields.String(attribute='type_name')
}

class NewsDetailHandler(Resource):

    @marshal_with(news_detail_filds)
    def get(self, id):
        news = News.query.get(id)
        return news

    # 登录验证
    @login_required
    def post(self):
        pass








api.add_resource(NewsTypeHandler, '/types')

api.add_resource(NewsHandler, '/news')

api.add_resource(NewsDetailHandler, '/newsdetail/<int:id>', endpoint='newsdetail')




