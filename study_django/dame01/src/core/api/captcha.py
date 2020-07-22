from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from captcha.models import CaptchaStore
from captcha.helpers import  captcha_image_url
from django.http import HttpResponse
import json

from libs.captcha import captcha, jarge_captcha



class CaptchaView(APIView):

    permission_classes = ()  # 权限类型
    authentication_classes = ()  # 身份验证

    def get(self, request):

        return HttpResponse(json.dumps(captcha()), content_type='application/json')

    def post(self, request):

        capt=request.POST.get("captcha",None)         #用户提交的验证码
        key=request.POST.get("hashkey",None)          #验证码答案

        if jarge_captcha(capt, key):
            return HttpResponse("验证码正确")
        else:
            return HttpResponse("验证码错误")




    # def get(self, request):
    #
    #     capt=request.data.get("captcha",None)         #用户提交的验证码
    #
    #     key=request.data.get("hashkey",None)          #验证码答案
    #
    #     if jarge_captcha(capt, key):
    #
    #         return HttpResponse("验证码正确")
    #     else:
    #         return HttpResponse("验证码错误")
