from datetime import datetime

from jsonschema import validate
from playhouse.shortcuts import model_to_dict

from handler import UserBaseHandler
from model.models import User, SysUniversity, SysCollege, SysAreas

from config import constant, status


class SysUniversityHandler(UserBaseHandler):

    def get(self):
        """
        ---
        tags:
        - 系统信息
        summary: 大学信息
        parameters:
        -   in: query
            name: city
            description: "城市"
            required: false
        -   in: query
            name: pinyin
            description: "大学拼音首字母"
            required: false
        -   in: query
            name: province
            description: "省份"
            required: false
        -   in: query
            name: hot
            description: "是否是热门1是0否"
            required: true
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
                "city": {"type": "string"},
                "pinyin": {"type": "string"},
                "province": {"type": "string"},
                "hot": {"type": "string", "enum": ["0", "1"]}
            }
        }
        query_params = self.req.query
        validate(query_params, json_schema)
        condition = []
        if query_params.get("hot") == '1':
            condition.append(SysUniversity.hot == query_params.get("hot"))
        if query_params.get("city"):
            condition.append(SysUniversity.city == query_params.get("city"))
        if query_params.get("pinyin"):
            condition.append(SysUniversity.pinyin.contains(query_params.get("pinyin")))
        if query_params.get("province"):
            condition.append(SysUniversity.province == query_params.get("province"))
        query = SysUniversity.select(
            SysUniversity.id,
            SysUniversity.hot,
            SysUniversity.city,
            SysUniversity.addr,
            SysUniversity.pinyin,
            SysUniversity.university
        )
        if condition:
            query = query.where(*condition)
        res = query.dicts()
        return self.out(code=status.success.code, data=list(res), msg=status.success.msg)


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
        deprecated:
        -   true
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
        deprecated:
        -   true
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






