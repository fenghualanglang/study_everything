import time
import random
import datetime
from peewee import *
from model import BaseModel
# database = MySQLDatabase('jincuodao', host="106.13.168.8", user="root", passwd="!QAZ2wsx#edc" )
# database.connect()
# class BaseModel(Model):
#     class Meta:
#         database = database


# class Goods(BaseModel):
#     bookname = CharField(null=True)
#     category_id = IntegerField(null=True)
#     deiscount = DecimalField(null=True)
#     desc = CharField(null=True)
#     gmt_created = DateTimeField(null=True)
#     gmt_modified = DateTimeField()
#     hot = IntegerField(null=True)
#     id = BigAutoField()
#     price = DecimalField(null=True)
#     pub_name = CharField(null=True)
#     pub_user_id = BigIntegerField(null=True)
#     ship = IntegerField(null=True)
#     ship_price = DecimalField(null=True)
#     status = IntegerField(null=True)
#
#     class Meta:
#         table_name = 'goods'
#
# class GoodsImage(BaseModel):
#     goods_id = BigIntegerField(null=True)
#     goods_image = CharField(null=True)
#     id = BigAutoField()
#     status = IntegerField()
#
#     class Meta:
#         table_name = 'goods_image'
#
class SysAreas(BaseModel):
    id = BigAutoField()
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    area_name = CharField(null=True)
    parent_id = IntegerField(null=True)
    area_level = IntegerField(null=True)
    remark = CharField(null=True)
    area_code = CharField(null=True)

    class Meta:
        table_name = 'core_area'
#
# class SysCategory(BaseModel):
#     category = CharField(null=True)
#     channel_id = IntegerField(null=True)
#     id = BigAutoField()
#
#     class Meta:
#         table_name = 'sys_category'
#
# class SysChannel(BaseModel):
#     channel = CharField(null=True)
#     gmt_created = DateTimeField(null=True)
#     gmt_modified = DateTimeField()
#     id = BigAutoField()
#
#     class Meta:
#         table_name = 'sys_channel'
#
class SysCollege(BaseModel):
    college = CharField(null=True)
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    university_id = IntegerField(null=True)

    class Meta:
        table_name = 'sys_college'
#
class SysUniversity(BaseModel):
    addr = CharField(null=True)
    city = CharField(null=True)
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    hot = IntegerField(null=True)
    pinyin = CharField(null=True)
    province = CharField(null=True)
    university = CharField()

    class Meta:
        table_name = 'sys_university'


class User(BaseModel):
    addr = CharField()
    birthday = DateField(null=True)
    college = CharField(null=True)
    dflag = IntegerField(null=True)
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    notice = CharField(null=True)
    id = BigAutoField()
    is_active = IntegerField(null=True)
    sex = IntegerField(null=True)
    major = CharField(null=True)
    openid = CharField(null=True)
    phone = CharField(null=True)
    introduction = CharField(null=True)
    unionid = CharField(null=True)
    university = CharField(null=True)
    user_name = CharField(null=True)
    passwd = CharField(null=True)
    we_unionid = CharField(null=True)
    wx_avatarurl = CharField(null=True)
    wx_name = CharField(null=True)
    wx_openid = CharField(null=True)
    last_login_time = DateTimeField(null=True)
    class Meta:
        table_name = 'user'

class UserAddr(BaseModel):
    city_id = IntegerField(null=True)
    district_id = IntegerField(null=True)
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    id = BigAutoField()
    dflag = IntegerField(null=True)
    status = IntegerField(null=True)
    mobile = CharField(null=True)
    receiver = CharField(null=True)
    detail = CharField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'user_addr'

class UserCollect(BaseModel):
    collect = CharField(null=True)
    goods_id = BigIntegerField(null=True)
    id = BigAutoField()
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'user_collect'

class UserFriends(BaseModel):
    friendname = CharField(null=True)
    friends_id = IntegerField(null=True)
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    id = BigAutoField()
    remar = CharField(null=True)
    status = IntegerField(null=True)
    user_id = IntegerField(null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'user_friends'

class UserMessage(BaseModel):
    from_user_id = BigIntegerField(null=True)
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    id = BigAutoField()
    message = CharField(null=True)
    msg_type = IntegerField(null=True)
    status = IntegerField(null=True)
    to_user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'user_message'

class UserOrder(BaseModel):
    goods_id = BigIntegerField(null=True)
    id = BigAutoField()
    pub_name = CharField(null=True)
    pub_user_id = BigIntegerField(null=True)
    user_id = BigIntegerField(null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'user_order'

class UserVisitHistory(BaseModel):
    gmt_created = DateTimeField(null=True)
    gmt_modified = DateTimeField()
    goods_id = BigIntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'user_visit_history'

# m = [User]
# database.create_tables([SysAreas])