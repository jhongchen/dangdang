import hashlib

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mainapp.models import *
import random,string

# from userapp.email_part import *
from .captcha.image import ImageCaptcha


def regist(request):
    a = random.sample(string.digits, 6)
    a = ''.join(a)
    print(a)
    request.session['a']=a
    request.session['a2']=a
    return render(request, 'userapp/register.html',{'login_state': request.session.get('login_state'),
                                                    'login_user': request.session.get('login_user')})

def username_check(request):
    username = request.GET.get('username')
    res = User.objects.filter(name=username)
    if res:
        return HttpResponse('exist')
    return HttpResponse('ok')

def captcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_letters , 4)
    random_code = ''.join(code)
    print(random_code)
    request.session['captcha'] = random_code
    data = image.generate(random_code)
    return HttpResponse(data)

def cap_get(request):

    cap_old = request.session.get('captcha')
    return HttpResponse(cap_old)


def registlogic(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    users = User.objects.filter(name=username)
    if users:
        return HttpResponse('wrong')

    pwd,salt = encrypt(pwd)

    User.objects.create(name=username, password=pwd,salt=salt, email=username)   # 存储用户信息到数据库

    request.session['username']=username
    request.session['password']=pwd
    return HttpResponse('ok')


def regist_ok(request):
    username = request.GET.get('username')
    request.session['txt_username']=username
    user = User.objects.filter(name=username)
    request.session['login_state'] = 'ok'
    request.session['login_user'] = username
    request.session['login_userid'] = user[0].id

    return render(request, 'userapp/register ok.html',{'username':username,
                                                       'login_state': request.session.get('login_state'),'login_user': request.session.get('login_user'),})



def encrypt(pwd,salt=None):

    if salt is None:
        l = '1234567890-=qwertyuiop[]asdfghjklzxcvbnm,./'
        salt = ''.join(random.sample(l, 6))
    pwd += salt
    h = hashlib.md5()
    h.update(pwd.encode())
    pwd = h.hexdigest()
    return pwd,salt

#
def email_confirm(request):
    username=request.GET.get("username")
    return render(request,'userapp/email_confirm.html',{'username':username})


def login(request):
    username = request.session.get('username')
    pwd = request.session.get('password')
    user = User.objects.filter(name=username,password=pwd)
    if user:
        request.session['login_state'] = 'ok'
        request.session['login_user'] = username
        request.session['login_userid'] = user[0].id
        return redirect('mainapp:home')
    return render(request, 'userapp/login.html',{'login_state': request.session.get('login_state'),'login_user': request.session.get('login_user'),})

def loginlogic(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    cap = request.POST.get('cap')
    remember = request.POST.get('remember')
    cap_old = request.session.get('captcha')
    user = User.objects.filter(name=username)
    if user:
        pwd = encrypt(pwd,user[0].salt)[0]
        if pwd == user[0].password:
            request.session['login_state'] = 'ok'
            request.session['login_user'] = username
            request.session['login_userid'] = user[0].id
            res = HttpResponse('ok')
            if remember:
                res.set_cookie('username',username,max_age=3600*24*7)
                res.set_cookie('password', pwd,max_age=3600*24*7)
            return res
    return HttpResponse('wrong')


def loginout(request):
    # r1=request.session.get('login_userid')
    # r2=request.GET.get('k')
    # if r2==1:
    #     r1=''
    # return render(request,'home.html',{'r1':r1})
    del request.session['login_state']
    del request.session['login_user']
    del request.session['login_userid']
    del request.session['username']
    del request.session['password']
    res = redirect('userapp:after_user')
    res.delete_cookie('username')
    res.delete_cookie('password')
    return res


def yz(request):
    print(114)
    a1=request.GET.get('a')
    # request.session['a1']=a1
    print(a1)
    a=request.session.get('a')
    a2=request.session.get('a2')
    print(a,'144')
    print(a2,'146')
    # request.session['a2']=a2
    if a1==a and a1==a2:
        # request.session['a2']='嘿嘿嘿！'
        # l=request.session.get('a2')
        # print(l,'152')
        return HttpResponse('ok')
    else:
        # request.session['a2'] = '嘿嘿嘿！只能用一次哦'
        # l = request.session.get('a2')
        # print(l,'159')
        return HttpResponse('no')


def after_user(request):
    path = request.session.get('path')
    return redirect(path)