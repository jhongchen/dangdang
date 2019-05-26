from django.urls import path
from . import views,email_part



app_name = 'userapp'

urlpatterns = [
    path('regist/',views.regist,name='regist'),
    path('registlogic/', views.registlogic, name='registlogic'),
    path('email_confirm/', views.email_confirm, name='email_confirm'),
    # path('confirm/', email_part.confirm, name='confirm'),
    path('registOk/', views.regist_ok, name='regist_ok'),
    path('login/', views.login, name='login'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),
    path('username_check/',views.username_check, name='username_check'),
    path('loginout/',views.loginout,name='loginout'),
    path('captcha/',views.captcha,name='captcha'),
    path('cap_get/',views.cap_get,name='cap_get'),
    path('after_user/',views.after_user,name='after_user'),
    path('regist1/',email_part.regist1,name='regist1'),
    path('yz/',views.yz,name='yz')
]