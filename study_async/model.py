from peewee import *

database = MySQLDatabase('crm', **{'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '1qaz2wsx'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Article(BaseModel):
    title = CharField(null=True)

    class Meta:
        db_table = 'article'
        primary_key = False

class CodePost(BaseModel):
    code = CharField(null=True)
    one_addr = CharField(null=True)
    thr_addr = CharField(null=True)
    tow_addr = CharField(null=True)

    class Meta:
        db_table = 'code_post'

class PostCode(BaseModel):
    area = CharField(null=True)
    city = CharField()
    code = CharField()
    county = CharField()
    latitude = CharField()
    longitude = CharField()
    township = CharField()

    class Meta:
        db_table = 'post_code'

