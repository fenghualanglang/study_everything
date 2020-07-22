

from django.http import JsonResponse, HttpResponse
from rest_framework.request import Request
from rest_framework import exceptions
# 检验是否有误
from core.models import UserToken


from rest_framework.authentication import BaseAuthentication








class FirstAuthentication(BaseAuthentication):

    def authenticate(self, request):

        pass

    def authenticate_header(self, request):

        pass


class Authtication(BaseAuthentication):  # 继承BaseAuthentication， 重写BaseAuthentication

    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = UserToken.objects.filter(token=token).first()

        if not token_obj:

            raise exceptions.AuthenticationFailed("用户认证失败")
        # 在rest—framework 内部会将整个/两个字段赋值给request， 以备后续使用
        return (token_obj.user, token_obj)


    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        # return 'Basic realm="基于浏览器认证"'
        pass
