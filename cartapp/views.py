import datetime
import hashlib
import random,string
import time

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from mainapp.models import *
from .cart import *

def cart_add(request):
    info_book = request.GET.get('book_id')
    info_amount = (int(request.GET.get('amount')) if request.GET.get('amount') else 1)
    cart = request.session.get('cart')
    print(cart)
    info = Info(Product.objects.get(id=info_book), info_amount)
    if cart is None:
        cart = Cart()
    cart.add(info)
    request.session['cart'] = cart
    return HttpResponse('ok')

def cart_remove(request):
    info_id = request.GET.get('info_id')
    cart = request.session.get('cart')
    cart.remove(info_id)
    request.session['cart'] = cart
    return HttpResponse('ok')

def cart_recover(request):
    info_id = request.GET.get('info_id')
    cart = request.session.get('cart')
    cart.recover(info_id)
    request.session['cart'] = cart
    return HttpResponse('ok')

def cart_change_amount(request):
    info_id = request.GET.get('info_id')
    new_amount = int(request.GET.get('new_amount'))
    cart = request.session.get('cart')
    cart.change_amount(info_id,new_amount)
    request.session['cart'] = cart
    return HttpResponse('ok')

def cart(request):
    cart = request.session.get('cart')
    user = request.session.get('login_user')
    login_state=request.session.get('login_state')
    return render(request, 'cartapp/car.html',{'cart':cart,'login_user':user,'login_state':login_state})

def indent(request):
    if not request.session.get('login_state'):
        return redirect('userapp:login')
    order_fail = False
    if request.GET.get('order_fail') == 'True':
        order_fail = True

    username = request.session.get('login_user')
    userid = request.session.get('login_userid')
    address = Address.objects.filter(user=userid)
    cart = request.session.get('cart')
    return render(request, 'cartapp/indent.html',{'cart':cart,'address':address,'username':username,'order_fail':order_fail})


def pay_ok(request):
    #
    # ship_man=request.POST.get('ship_man')
    # address=request.POST.get('address')
    # postcode=request.POST.get('postcode')
    # m_phone=request.POST.get('m_phone')
    # phone=request.POST.get('phone')
    #
    email=request.session.get('login_user')
    userid=User.objects.get(email=email).id
    # print(userid)
    # # Address.objects.create(address=address,ship_man=ship_man,postcode=postcode,m_phone=m_phone,phone=phone,user=userid)
    addr=Address()
    addr.address=request.POST.get('address')
    addr.ship_man=request.POST.get('ship_man')
    addr.phone=request.POST.get('phone')
    addr.m_phone=request.POST.get('m_phone')
    addr.postcode=request.POST.get('postcode')
    addr.user=userid
    addr.save()

    cart=request.session.get('cart')
    login_user = request.session.get('login_user')
    haor=random.sample(string.digits,8)
    hao=''.join(haor)
    return render(request,'cartapp/indent ok.html',{'user':login_user,'cart':cart,'hao':hao})
