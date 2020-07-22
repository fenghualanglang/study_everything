from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from core.api.user import (
    LoginView,
    ForgetPwdView,
    RegisterView,
    ActiveView,
    ResetView
)


from core.api.customer import (
    CustomerUserView
)


from core.api.captcha import (
    CaptchaView
)


from django.urls import path
urlpatterns = [

    # url(r'^api/v1/goods', GoodsListView.as_view()),

    # 登录的url
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('captcha', include('captcha.urls')),

    url(r'captcha-image', CaptchaView.as_view()),

    url(r'api/v1/login', LoginView.as_view()),

    url(r'api/v1/forget', ForgetPwdView.as_view()),

    url(r'api/v1/reset', ResetView.as_view()),

    url(r'api/v1/active', ActiveView.as_view()),

    url(r'api/v1/register', RegisterView.as_view()),

    url(r'api/v1/customer', CustomerUserView.as_view()),

    # # 匿名用户登陆
    # url(r'api/v1/user', UserInfoView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

