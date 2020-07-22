import re
from datetime import datetime


from django.core.mail import send_mail
from django.conf import settings
from django_redis import get_redis_connection
from rest_framework import serializers
from core.models import User, EmailVerifyRecord, CustomerUser
from captcha.models import CaptchaStore


class UserSerializer(serializers.Serializer):

    """用户序列化器类"""
    username = serializers.CharField(max_length=16, label='用户名')
    # username = serializers.CharField(max_length=12, label='用户名', write_only=True)
    mobile = serializers.CharField(max_length=11, label='昵称')
    introduction = serializers.CharField(max_length=120,  label='昵称', read_only=True)
    gender = serializers.ChoiceField(label='性别', choices=((0, '男'), (1, '女')), default=0, read_only=True)
    birthday = serializers.DateField(label='生日', read_only=True)
    we_chat = serializers.CharField(max_length=255, read_only=True)
    qq = serializers.CharField(max_length=12, read_only=True)
    job = serializers.CharField(max_length=12, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    # last_login = serializers.DateTimeField(read_only=True)
    email = serializers.EmailField(max_length=64)
    is_active = serializers.ChoiceField(label='激活标志', choices=((0, '未激活'), (1, '已激活')), default=0, read_only=True)
    # dflag = serializers.ChoiceField(label='删除标志', choices=((0, '删除'), (1, '正常')), default=1, read_only=True)
    # status = serializers.ChoiceField(label='状态', choices=((0, '禁用'), (1, '正常')), default=1, read_only=True)
    password2 = serializers.CharField(label='重复密码', write_only=True)
    # sms_code = serializers.CharField(label='短信验证码', write_only=True)
    allow = serializers.CharField(label='同意协议', write_only=True)
    token = serializers.CharField(label='JWT token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'nickname', 'realname', 'password', 'mobile', 'qq', 'email', 'password2', 'sms_code', 'allow', 'token')

        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

    # 是否同意协议，手机号格式，手机号是否存在，两次密码是否一致，短信验证是否正确
    def validate_username(self, value):
        # 用户名不能全部为数字
        if re.match('^\d+$', value):
            raise serializers.ValidationError('用户名不能全部为数字')

        return value

    def validate_allow(self, value):
        # 是否同意协议
        if value != 'true':
            raise serializers.ValidationError('请同意协议')

        return value

    def validate(self, attrs):
        # 两次密码是否一致
        password = attrs['password']
        password2 = attrs['password2']

        if password != password2:
            raise serializers.ValidationError('两次密码不一致')

        return attrs


    def validate_mobile(self, value):
        # 手机号格式
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式不正确')

        return value

    def validate_email(self, value):
        # 邮箱格式
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', value):
            raise serializers.ValidationError('邮箱格式不正确')
        # 手机号是否存在
        user_info = User.objects.filter(email__exact=value)#.first() #.count()
        if user_info:
            for u in user_info:
                if u.is_active:
                    raise serializers.ValidationError('邮箱已经注册!')
                verify_url = u.generate_active_token()
                msg = f'<a href="{verify_url}" target="_blank">点击激活</a>'
                send_mail('注册激活', '', settings.EMAIL_FROM, [value], html_message=msg)
                raise serializers.ValidationError('请登录邮箱激活!')

        return value


class EmailSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField(max_length=64)
    password2 = serializers.CharField(label='重复密码', write_only=True)

    class Meta:
        model = User
        fields = ('password', 'email', 'password2')

        extra_kwargs = {
            'password': {
                'required': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            },
            'email': {'required': True}
        }

    def validate(self, attrs):
        # 两次密码是否一致
        password = attrs['password']
        password2 = attrs['password2']

        if password != password2:
            raise serializers.ValidationError('两次密码不一致')

        return attrs

    def validate_mobile(self, value):
        # 手机号格式
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式不正确')

        # 手机号是否存在
        count = User.objects.filter(mobile=value).count()

        if count > 0:
            raise serializers.ValidationError('手机号已存在')

        return value

    def validate_email(self, value):

        # 手机号是否存在
        count = User.objects.filter(email=value).count()

        if count == 0:
            raise serializers.ValidationError('邮箱未注册!')

        return value



class EmailVerifyRecordSerializer(serializers.ModelSerializer):

    # code = serializers.CharField(max_length=200, label=u"验证码", read_only=True)
    email = serializers.EmailField(max_length=50, label=u"邮箱", write_only=True)

    class Meta:
        model = EmailVerifyRecord
        fields = ('email',)

    def validate_email(self, value):
        # 邮箱格式
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', value):
            raise serializers.ValidationError('邮箱格式不正确')

        count = User.objects.filter(email=value).count()
        if count == 0:
            raise serializers.ValidationError('邮箱未注册!')
        return value


class ResetSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(label='重复密码', write_only=True)
    sign = serializers.CharField(label='重复密码', write_only=True)
    email = serializers.EmailField(max_length=50, label=u"邮箱", write_only=True)

    class Meta:
        model = EmailVerifyRecord
        fields = ('email', 'password', 'password2', 'sign')


    def validate(self, attrs):

        password = attrs['password']
        password2 = attrs['password2']
        sign = attrs['sign']

        if password != password2:
            raise serializers.ValidationError('密码不一致')

        count = EmailVerifyRecord.objects.filter(sign=sign, status=0).count()

        if count == 0:
            raise serializers.ValidationError('连接已失效')
        return attrs


class CustomerUserSerializer(serializers.ModelSerializer):
        start = ((1, '一星级'),
                 (2, '二星级'),
                 (3, "三星级"),
                 (4, '四星级'),
                 (5, '五星级'),
                 )

        status = (
            (1, '潜在客户'),
            (2, '目标客户'),
            (3, '成交客户'),
            (4, '现实客户'),
            (5, '流失客户'),
            (6, '死亡客户')
        )

        origin = (
            (1, '老客户'),
            (2, '独立开发'),
            (3, '客户介绍'),
            (4, '客户介绍'),
            (5, '促销活动'),
            (6, '展览展会'),
        )

        job = (
            (0, 'IT｜互联网｜通信｜电子'),
            (1, '金融｜银行｜保险'),
            (2, '房产｜建筑建设｜物业'),
            (3, '广告｜传媒｜印刷出版'),
            (4, '消费零售｜贸易｜交通物流'),
            (5, '加工制造｜仪表设备'),
            (6, '管理咨询|教育科研｜中介服务'),
            (7, '医药生物｜医疗保健'),
            (8, '酒店旅游'),
            (9, '能源矿产｜石油化工'),
            (10, '政府｜非营利机构｜科研'),
            (11, '其他'),
        )
        grade = (
            (0, '3万以下'),
            (1, '3-6万'),
            (2, '6-8万'),
            (3, '8-12万'),
            (4, '13-15万'),
            (5, '16-20万'),
            (6, '21-30万'),
            (7, '30-50万'),
            (8, '50-100万'),
            (9, '101-150万'),
            (10, '151-180万'),
            (11, '181-220万'),
            (12, '221-280万'),
            (13, '281-330万'),
            (14, '331-500万'),
            (15, '500万以上'),
        )

        customer = serializers.CharField(max_length=16, label='昵称', read_only=True)
        # name = serializers.CharField(max_length=12, label='用户名', read_only=True)
        mobile = serializers.CharField(max_length=11, label='昵称')
        introduction = serializers.CharField(max_length=120, label='昵称', read_only=True)
        gender = serializers.ChoiceField(label='性别',  choices=((0, '男'), (1, '女'),), default=0, read_only=True)
        birthday = serializers.DateField(label='生日', read_only=True)
        we_chat = serializers.CharField(max_length=255, read_only=True)
        qq = serializers.CharField(max_length=12, read_only=True)
        job = serializers.ChoiceField(label='职业', choices=job, default=4, read_only=True)
        email = serializers.CharField(max_length=64, read_only=True)
        # is_delete = serializers.ChoiceField(label='删除标志',  choices=((0, '删除'), (1, '正常')), default=1, write_only=True)
        status = serializers.ChoiceField(label='状态',  choices=status, default=1, read_only=True)
        star = serializers.ChoiceField(label='星级', choices=start, default=3, read_only=True)
        origin = serializers.ChoiceField(label='来源', choices=origin, default=2, read_only=True)
        # user_id = serializers.IntegerField(label='用户id', write_only=True)
        role = serializers.CharField(max_length=16, read_only=True)
        ctr_type = serializers.ChoiceField(label='客户类型',  choices=((0, '企业客户'), (1, '个人客户')), default=0, read_only=True)
        grade = serializers.ChoiceField(label='规模id', choices=grade, default=2, read_only=True)
        is_attention = serializers.ChoiceField(label='客户类型',  choices=((0, '微关注'), (1, '已经')), default=0, read_only=True)

        class Meta:
            model = CustomerUser
            fields = (
                'id', 'customer', 'mobile', 'email', 'gender', 'birthday',  'we_chat', 'is_attention',
                'status', 'qq', 'star', 'origin', 'role', 'introduction', 'grade', 'ctr_type', 'job', 'name'
            )

        def validate(self, attrs):
            value = attrs['mobile']
            # 手机号格式
            if not re.match(r'^1[3-9]\d{9}$', value):
                raise serializers.ValidationError('手机号格式不正确')
            return attrs






# from rest_framework import serializers
# class GoodSerializers(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     ship_free = serializers.BooleanField(default=True)
# class UserSerializers(serializers.Serializer):
#
#     name = serializers.CharField(max_length=30)
#     birthday = serializers.DateField()
#     gender = serializers.CharField(default="female")
#     mobile = serializers.CharField(max_length=11)
#     email = serializers.EmailField(max_length=100)
#     password = serializers.IntegerField(default=0)

# from rest_framework import serializers
# from core.serializers import zjb, LANGUAGE_CHOICES, STYLE_CHOICES
#
#
# class SnippetSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
#
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})      # style的设置等同于Django的widget=widgets.Textarea
#
#     linenos = serializers.BooleanField(required=False)                          # 用于对浏览器的上的显示
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return zjb.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#




    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.CharField(default='python')
    # style = serializers.CharField(default='friendly')
    #
    # def create(self, validated_data):
    #
    #     """如果数据合法就创建并返回一个snippet实例"""
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #
    #     """如果数据合法就更新并返回一个存在的snippet实例"""
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #
    #     return instance
    #










