

from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    BasePermission
)



from rest_framework.views import APIView


class BaseView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, args: str = None):
        pass

    def post(self, request, args: str = None):
        pass

    def put(self, request, args: str = None):
        pass

    def delete(self, request, args: str = None):
        pass

class AnyLogin(APIView):

    permission_classes = ()  # 权限类型
    authentication_classes = ()  # 身份验证

    def get(self, request, args: str = None):
        pass

    def post(self, request, args: str = None):
        pass

    def put(self, request, args: str = None):
        pass

    def delete(self, request, args: str = None):
        pass

# AllowAny 允许所有用户
# IsAuthenticated 仅通过认证的用户
# IsAdminUser 仅管理员用户
# IsAuthenticatedOrReadOnly 认证的用户可以完全操作，否则只能get读取

