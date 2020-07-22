
import time
from rest_framework.throttling import BaseThrottle

from rest_framework.throttling import SimpleRateThrottle


# 内置访问频率（匿名用户）
class VisitThrottle(SimpleRateThrottle):

    scope = "Luffy"


    def get_cache_key(self, request, view):  #  内部封装

        return self.get_ident(request)   # 调用父类方法


# 内置访问频率（登陆用户）
class UserThrottle(SimpleRateThrottle):

    scope = 'LuffUser'

    def get_cache_key(self, request, view):

        return request.user.username




# 自定义
# VISIT_RECORD = {}
# # 限制访问频率的最大限度
# class VisitThrottle(BaseThrottle):
#
#     def __init__(self):
#
#         self.history = None
#
#     def allow_request(self, request, view):
#
#         # 获取主机ip
#         # remote_addr = request.META.get('REMOTE_ADDR')
#         remote_addr = self.get_ident(request)  #  继承父类的get_indent()函数
#
#         ctime = time.time()
#
#         if remote_addr not in VISIT_RECORD:
#             VISIT_RECORD[remote_addr] = [ctime]
#
#             print(
#                 VISIT_RECORD
#             )
#
#             return True
#
#         history = VISIT_RECORD.get(remote_addr)
#         self.history = history
#         while history and history[-1] < ctime - 15:
#
#             history.pop()
#
#         print(VISIT_RECORD)
#         if len(history) <= 3:
#             history.insert(0, ctime)
#
#             return True
#
#
#         # return False    # 访问的频率太高，被限制
#
#
#     def wait(self):
#            # 在等10秒可以访问
#         ctime = time.time()
#         return 60 - (ctime - self.history[-1])
#
#
