from django.conf.urls import url
from django.urls import path
from . import views



app_name = 'cartapp'

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('cart_add/',views.cart_add,name='cart_add'),
    path('cart_remove/',views.cart_remove,name='cart_remove'),
    path('cart_change_amount/',views.cart_change_amount,name='cart_change_amount'),
    path('cart_recover/',views.cart_recover,name='cart_recover'),
    path('indent/', views.indent, name='indent'),
]