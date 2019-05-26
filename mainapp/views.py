import datetime
from _md5 import md5

from django.core.paginator import Paginator
from django.shortcuts import render
from mainapp.models import *


def home(request):
    # 左侧的边栏分类
    sidemenu = cate()
    # 新书上架
    newbooks = Product.objects.order_by("issue")
    new = []
    for i in range(1,4):
        new.append(Paginator(newbooks,per_page=8).page(i))
    #主编推荐
    recoms = []
    recombooks = Product.objects.filter(recommand='True').order_by('issue')
    for i in range(1,4):
        recoms.append(Paginator(recombooks,per_page=8).page(i))
    #新书热卖
    hotbooks = Product.objects.filter(issue__month=datetime.datetime.now().month).order_by('sales')
    hots = Paginator(hotbooks,per_page=10).page(1)
    content = {
        'cates':sidemenu[0],
        'cate_sons':sidemenu[1],
        'new':new,
        'recoms':recoms,
        'hots':hots,
        'login_state': request.session.get('login_state'),#登录状态
        'login_user': request.session.get('login_user'),
    }
    return render(request, 'mainapp/home.html',content)


def detail(request):
    id = request.GET.get('id')
    if id is None:
        id=1
    book = Product.objects.get(id=id)
    cate_son = Category.objects.get(id=book.menus_id)   #二级目录
    cate = Category.objects.get(id=cate_son.parent_id)  #一级目录

    content = {
        'book': book,
        'cate': cate,
        'cate_son': cate_son,
        'login_state': request.session.get('login_state'),
        'login_user': request.session.get('login_user'),
    }
    return render(request, 'mainapp/Book details.html',content)


def booklist(request):

    try:
        cates = int(request.GET.get('cates'))
    except:
        cates = 1
    try:
        num = int(request.GET.get('num'))
    except:
        num = 1
    try:
        sort = request.GET.get('sort')
        if sort not in ('issue','sales','dangdang_price','publishing_time'):
            sort = 'issue'
    except:
        sort = 'issue'

    cate_target = Category.objects.get(id=cates)
    cate_two = '0'
    if cate_target.parent_id == 0:
        cate_one = cate_target
        books = Product.objects.filter(menus__parent_id=cates).order_by(sort)
    else:
        cate_two = cate_target
        cate_one = Category.objects.get(id=cate_two.parent_id)
        books = Product.objects.filter(menus__id=cates).order_by(sort)
    page = Paginator(books, per_page=8).page(num)

    sidemenu = cate()
    content = {
        'page':page,
        'cates':cates,
        'cate_one':cate_one,
        'cate_two':cate_two,
        'cate_parents':sidemenu[0],
        'cate_sons':sidemenu[1],
        'sort':sort,
        'login_state': request.session.get('login_state'),
        'login_user': request.session.get('login_user'),
    }
    return render(request, 'mainapp/booklist.html',content)



def cate():

    cates = Category.objects.filter(parent_id=0)
    cate_sons = Category.objects.filter(parent_id__gt=0)
    return cates,cate_sons



