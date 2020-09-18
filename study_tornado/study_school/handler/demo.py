#!usr/bin/env python
# -*- coding:utf-8 -*-

import re

from handler import BaseHandler, UserBaseHandler
from model.models import User, BaseModel
from jsonschema import validate
from config import status


class DemoHandler(UserBaseHandler):

    def post(self):
        # Example
        # ��ȡǰ�δ�������
        # URL query args
        args = self.req.query
        # POST data
        post_data = self.req.body
        # JSON data
        json_data = self.req.json

        # jsonschema
        post_schema = {
            "type": "object",
            "required": ["num_key", "str_key"],
            "properties": {
                "num_key": {"type": "number"},
                "str_key": {"type": "string", "pattern": r"^(\d+)$"}
            }
        }

        if post_data:
            validate(post_data, post_schema)

        # ��ȡ��¼�û�ID
        user_id = self.get_current_user()

        # ��ȡ���� ORM ��ʽ
        temp = User.select().dicts()

        # ��ȡ���� Raw SQL ��ʽ
        temp = BaseModel.raw('select * from user').dicts()

        return self.out(status.success.code, data=list(temp), msg=status.success.msg)
