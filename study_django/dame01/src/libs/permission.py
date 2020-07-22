

from rest_framework.permissions import BasePermission



class MyPermission(BasePermission): #继承django 默认的BasePagination

    def has_permission(self, request, view):

        message = '必须是SVIP才能访问'

        print(request.user.user_type)
        if request.user.user_type == 3:
            return False  # 无权访问
        return True



class MyPermission2(BasePermission):

    def has_permission(self, request, view):

        print(request.user.user_type)
        if request.user.user_type != 2:
            return False
        return True