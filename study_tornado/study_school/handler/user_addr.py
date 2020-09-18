from datetime import datetime

from jsonschema import validate
from playhouse.shortcuts import model_to_dict

from handler import UserBaseHandler
from model.models import User, SysUniversity, SysCollege, SysAreas, UserAddr

from config import constant, status


class UserAddrHandler(UserBaseHandler):

    def get(self):
        """
        ---
        tags:
        - 用户地址
        summary: 地址列表
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": [
                    {
                    "addr_id": 7,
                    "???addr_id": "收件人id",
                    "city_id": 1123,
                    "???city_id": "城市id",
                    "district_id": 1157,
                    "???district_id": "区县id",
                    "dflag": 1,
                    "???status": "状态(0常规/1置顶)",
                    "mobile": "18236766280",
                    "???mobile": "mobile",
                    "receiver": "python",
                    "???receiver": "收件人",
                    "detail": "河南财政金融学院",
                    "???detail": "收件详细地址"
                    }
                    ]
                }
        security:
        -   Token: []
        """
        cur_user_id = self.user.id
        query = UserAddr.select(
            UserAddr.id.alias('addr_id'),
            UserAddr.city_id,
            UserAddr.district_id,
            UserAddr.gmt_created,
            UserAddr.gmt_modified,
            UserAddr.dflag,
            UserAddr.mobile,
            UserAddr.receiver,
            UserAddr.detail
        ).where(
            UserAddr.user_id == cur_user_id,
            UserAddr.status == 0
        ).dicts()
        return self.out(code=status.success.code, data=list(query), msg=status.success.msg)

    def post(self):
        """
        ---
        tags:
        - 用户地址
        summary: 新增用户地址
        parameters:
        -   in: body
            name: body
            required: true
            example: {
                "city_id": "1123",
                "???city_id":"城市id",
                "district_id": "1157",
                "???district_id":"县区id",
                "mobile": "18236766280",
                "???mobile":"手机号",
                "receiver": "python",
                "???receiver":"接收人",
                "detail": "河南财政金融学院",
                "???detail":"详细地址"
             }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "captcha": "039421"
                    }
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "detail": {"type": "string"},
                "mobile": {"type": "string", "pattern": "^1[35678]\d{9}$"},
                "receiver": {"type": "string"},
                "district_id": {"type": "number"},
                "city_id": {"type": "number"}

            }
        }
        json_data = self.req.json
        validate(json_data, json_schema)
        cur_user_id = self.user.id
        user_addr = UserAddr.create(
            city_id=json_data.get('city_id'),
            district_id=json_data.get('district_id'),
            mobile=json_data.get('mobile'),
            receiver=json_data.get('receiver'),
            detail=json_data.get('detail'),
            user_id=cur_user_id,
            dflag=0,
            status=0
        )
        return self.out(code=status.success.code, msg=status.success.msg)

    def put(self):
        """
        ---
        tags:
        - 用户地址
        summary: 新增用户地址
        parameters:
        -   in: body
            name: body
            required: true
            example: {
                "addr_id": 7,
                "???addr_id": "收件id",
                "city_id": 1123,
                "???city_id":"城市id",
                "district_id": 1157,
                "???district_id":"县区id",
                "mobile": "18236766280",
                "???mobile":"手机号",
                "receiver": "python",
                "???receiver":"接收人",
                "detail": "河南财政金融学院",
                "???detail":"详细地址"
             }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "captcha": "039421"
                    }
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "required": ["addr_id"],
            "properties": {
                "detail": {"type": "string"},
                "mobile": {"type": "string", "pattern": "^1[35678]\d{9}$"},
                "receiver": {"type": "string"},
                "district_id": {"type": "number"},
                "city_id": {"type": "number"},
                "addr_id": {"type": "number"},
            }
        }
        json_data = self.req.json
        validate(json_data, json_schema)
        cur_user_id = self.user.id

        condition = {}
        if json_data.get('city_id'):
            condition['city_id'] = json_data.get('city_id')
        if json_data.get('district_id'):
            condition['district_id'] = json_data.get('district_id')
        if json_data.get('mobile'):
            condition['mobile'] = json_data.get('mobile')
        if json_data.get('receiver'):
            condition['receiver'] = json_data.get('receiver')
        if json_data.get('detail'):
            condition['detail'] = json_data.get('detail')
        if json_data.get('addr_id'):
            condition['id'] = json_data.get('addr_id')
        UserAddr.update(condition).where(
            UserAddr.user_id == cur_user_id,
            UserAddr.id == json_data.get('addr_id')
        ).execute()
        return self.out(code=status.success.code, msg=status.success.msg)













class SysCollegeHandler(UserBaseHandler):

    def get(self, university_id):
        """
        ---
        tags:
        - 系统信息
        summary: 学院信息
        parameters:
        -   in: path
            name: university_id
            description: "大学id"
            required: true
        -   in: query
            name: hot
            description: "是否是热门1是0否"
            required: false
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "to_user": "",
                        "???to_user": "接收人",
                        "from_user": "",
                        "???from_user": "发送人",
                        "send_time": "",
                        "???send_time": "发送时间",
                        "status": "",
                        "???status": "状态(0未读/1已读)",
                        "title": "",
                        "???title": "标题",
                        "content": "",
                        "???content": "内容",
                    }
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "hot": {"type": "string", "enum": ["0", "1"]}
            }
        }
        query_params = self.req.query
        validate(query_params, json_schema)

        college = SysCollege.select().where(SysCollege.university_id == university_id).dicts()
        return self.out(code=status.success.code, data=list(college), msg=status.success.msg)


    def post(self, university_id):
        """
        ---
        tags:
        - 系统信息
        summary: 添加学院信息
        parameters:
        -   in: path
            name: university_id
            description: "大学id"
            required: true
        -   in: body
            name: body
            required: true
            example: {
                    "college": "光华管理学院",
                    "???college":"院系名称"
             }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "captcha": "039421"
                    }
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "college": {"type": "string"}
            }
        }
        json_data = self.req.json
        validate(json_data, json_schema)
        college = json_data.get('college')

        new_college = SysCollege.create(
            college=college,
            university_id=university_id
        )
        return self.out(code=status.success.code, data=model_to_dict(new_college), msg=status.success.msg)


class SysAreasHandler(UserBaseHandler):
    def get(self):
        """
        ---
        tags:
        - 系统信息
        summary: 城市信息
        parameters:
        -   in: query
            name: area_level
            description: "层级1省/2市/3县区"
            required: false
        -   in: query
            name: parent_id
            description: "父级id"
            required: false
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "id": 1,
                            "gmt_created": "",
                            "SysDepartment": "",
                            "is_leaf": "",
                            "???is_leaf": "是否为叶节点（0否 1是）",
                            "dept_name":"",
                            "dept_type": "",
                            "???dept_type": "部门类别",
                            "parent_id": "",
                            "???parent_id": "父节点",
                            "tree_path": "",
                            "???tree_path": "结构树",
                            "level_no": "",
                            "???level_no": "所处级别"
                    }
                }
        security:
        -   Token: []
        """
        query_params = self.req.query

        json_schema = {
            "type": "object",
            "properties": {
                "area_level": {"type": "string", "pattern": r"^([0-9]+)$"},
                "area_id": {"type": "string", "pattern": r"^([0-9]+)$"}
            }
        }
        validate(query_params, json_schema)

        query_params = self.req.query
        condition = []
        if query_params.get('parent_id'):
            condition.append(SysAreas.parent_id == query_params.get('parent_id'))

        if query_params.get('area_level'):
            condition.append(SysAreas.area_level == query_params.get('area_level'))

        if condition:
            areas = SysAreas.select().where(*condition).dicts()
            return self.out(code=status.success.code, data=list(areas), msg=status.success.msg)
        areas = SysAreas.select().dicts()
        return self.out(code=status.success.code, data=list(areas), msg=status.success.msg)

    def post(self):
        """
        ---
        tags:
        - 系统信息
        summary: 添加城市信息
        parameters:
        -   in: body
            name: body
            required: true
            example: {
                    "college": "光华管理学院",
                    "???college":"院系名称"
             }
        responses:
            200:
                description: 通信成功, 处理结果由object.code 来判断
                example: {
                    "code": 200,
                    "message": "detail message",
                    "data": {
                        "captcha": "039421"
                    }
                }
        security:
        -   Token: []
        """
        json_schema = {
            "type": "object",
            "properties": {
                "college": {"type": "string"}
            }
        }
        json_data = self.req.json
        validate(json_data, json_schema)
        college = json_data.get('college')
        SysAreas.create(
            area_name='name',
            area_level=3,
            parent_id=1123
        )











