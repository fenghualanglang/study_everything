# -*-coding:utf-8-*-
from peewee import *

database = MySQLDatabase(None)


class TinyIntegerField(IntegerField):
    db_field = 'tinyint'


class BaseModel(Model):
    class Meta:
        database = database

    @classmethod
    def getOne(cls, *query, **kwargs):
        # 查询不到返回None，而不抛出异常
        try:
            return cls.get(*query, **kwargs)
        except DoesNotExist:
            return None
