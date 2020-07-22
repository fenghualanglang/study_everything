






import json
from uuid import uuid4

# from libs.serializers import UserSerializers
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import (IsAuthenticated)
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from django import db
from django.contrib.auth import authenticate, logout
from django.core.mail import send_mail
from django.conf import settings
from libs import baseview
from libs.serializers import (
    CustomerUserSerializer,
    UserSerializer,
    EmailSerializer,
    ResetSerializer,
    EmailVerifyRecordSerializer,
)

from libs.captcha import captcha, jarge_captcha
from libs.util import send_verify_email, decrypt

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 加密
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


from core.models import (
    CustomerUser,
    CallOnDtl,
    User,
    EmailVerifyRecord,

)




class CallOnDtlView(APIView):

    permission_classes = ()  # 权限类型
    authentication_classes = ()  # 身份验证

    def get(self, request):

        customer_id = request.GET.get('customer_id')
        customer = request.GET.get('customer')

        condition = {}

        if customer_id:
            condition['id'] = customer_id
        if customer:
            condition['customer'] = customer
        if mobile:
            condition['mobile'] = mobile
        if gender:
            condition['gender'] = gender
        if birthday:
            condition['birthday'] = birthday
        if qq:
            condition['qq'] = qq
        if job:
            condition['job'] = job
        if star:
            condition['star'] = star
        if origin:
            condition['origin'] = origin
        if role:
            condition['role'] = role
        if ctr_type:
            condition['ctr_type'] = ctr_type
        if grade_id:
            condition['grade_id'] = grade_id
        if condition:
            condition['user_id'] = 1
            customer = CustomerUser.objects.filter(**condition)
            goods_serializer = CustomerUserSerializer(customer, many=True)

            return Response({'code': 200, 'data': goods_serializer.data, 'msg': 'ok'})

        condition['user_id'] = 1
        customer = CustomerUser.objects.filter(**condition)
        goods_serializer = CustomerUserSerializer(customer, many=True)
        return Response({'code': 200, 'data': goods_serializer.data, 'msg': 'ok'})

    def post(self, request):

        serializer = CustomerUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = request.data.get('mobile')
        count = CustomerUser.objects.filter(mobile=mobile, user_id=1).count()
        if count > 0:
            return Response({'code': 412, 'data': {}, 'msg': '客户已存在'})
        CustomerUser.objects.create(
            customer=request.data.get('customer'),
            mobile=request.data.get('mobile'),
            introduction=request.data.get('introduction'),
            gender=request.data.get('gender'),
            birthday=request.data.get('birthday'),
            we_chat=request.data.get('we_chat'),
            qq=request.data.get('qq'),
            job=request.data.get('job'),
            email=request.data.get('email'),
            status=request.data.get('status'),
            star=request.data.get('star'),
            origin=request.data.get('origin'),
            role=request.data.get('role'),
            grade=request.data.get('grade'),
            ctr_type=request.data.get('ctr_type'),
            user_id=1
        )
        return Response({'code': 200, 'data': {}, 'msg': 'ok'})

    def put(self, request):

        customer_id = request.data.get('customer_id')
        customer = request.data.get('customer')
        mobile = request.data.get('mobile')
        gender = request.data.get('gender')
        birthday = request.data.get('birthday')
        we_chat = request.data.get('we_chat')
        qq = request.data.get('qq')
        job = request.data.get('job')
        email = request.data.get('email')
        status = request.data.get('status')
        star = request.data.get('star')
        origin = request.data.get('origin')
        role = request.data.get('role')
        ctr_type = request.data.get('ctr_type')
        grade_id = request.data.get('grade_id')
        is_attention = request.data.get('is_attention')

        condition = {}

        if customer_id:
            condition['id'] = customer_id
        if customer:
            condition['customer'] = customer
        if mobile:
            condition['mobile'] = mobile
        if gender:
            condition['gender'] = gender
        if birthday:
            condition['birthday'] = birthday
        if qq:
            condition['qq'] = qq
        if job:
            condition['job'] = job
        if star:
            condition['star'] = star
        if origin:
            condition['origin'] = origin
        if role:
            condition['role'] = role
        if ctr_type:
            condition['ctr_type'] = ctr_type
        if grade_id:
            condition['grade_id'] = grade_id
        if is_attention:
            condition['is_attention'] = is_attention

        if condition:
            CustomerUser.objects.filter(id=customer_id, user_id=1).update(**condition)
            return Response({'code': 200, 'data': {}, 'msg': 'ok'})
        return Response({'code': 412, 'data': {}, 'msg': '参数有误'})


    def delete(self, request):

        customer_id = request.data.get('customer_id')
        CustomerUser.objects.filter(id=customer_id, user_id=1).update(is_delete=0)
        return Response({'code': 200, 'data': {}, 'msg': 'ok'})
















        # user_id = Account.objects.filter(username=request.user).first().id
        # if user_id == 1:
        #     user_info = UserProfile.objects.all()
        #     user_info_serializer = UserSerializers(user_info, many=True)
        #     return Response(user_info_serializer.data)








