from peewee import *

database = MySQLDatabase('douban', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '1qaz2wsx'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Douban(BaseModel):
    area = CharField(null=True)
    comment = CharField(null=True)
    create_tiem = DateTimeField(null=True)
    director = CharField(null=True)
    id = BigAutoField()
    image_urls = CharField(null=True)
    language = CharField(null=True)
    move_name = CharField(null=True)
    publish = CharField(null=True)
    quote = CharField(null=True)
    runtime = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    score = CharField(null=True)
    screen_writer = CharField(null=True)
    to_star = CharField(null=True)
    type = CharField(null=True)
    up_time = DateTimeField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'douban'

