import datetime

from django.db import transaction
from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dangdang.settings")
django.setup()
from mainapp.models import *
#
# cate8 = Category.objects.get(id=14)
# #
# #
# try:
#     with transaction.atomic():
#         for i in range(30):
#             book = Product()
#             book.name ='从你的全世界路过'
#             book.author = '张嘉佳'
#             book.face = '/static/images/23353342-1_l'
#             book.publishing_house = '湖南文艺出版社'
#             book.edition = '2'
#             book.publishing_time = datetime.datetime.now()
#             book.print_time = '5'
#             book.isbn = '978-7-5404-5802-7'
#             book.word = '220000 '
#             book.number_of_page = 512
#             book.format_of_book = '16开本'
#             book.paper = '胶版纸'
#             book.packagin = '平装'
#             book.emboitement = '完整套装'
#             book.sales = '1000'
#             book.price = 168.0
#             book.dangdang_price = 96.0
#             book.review = 379
#             book.issue = datetime.datetime.now()
#             book.score = 8.5
#             book.sold_out = 'False'
#             book.recommand = 'True'
#             book.menus = cate8
#             book.extend = 'l'
#             book.save()
# except:
#     print('error')
#
# al = Product.objects.all()
# for i in al:
#     i.face = '/static/images/23353342-1_l.jpg'
#     i.save()


# new = []
# for i in range(1,3):
#     new.append(i)
# print(new)


# book = Product.objects.get(id=1)
# order_info = OrderInfo.objects.create(number=5,product=book)
# price = 0
# price += order_info.product.dangdang_price
# print(price)

# 创建地址条目
# user = User.objects.get(id=4)
# add = Address()
# add.address = '北京市顺义区五里仓仓上小区'
# add.m_phone = '12312312312'
# add.phone = '1234567'
# add.postcode = '100000'
# add.user = user
# add.save()
# print(Address.objects.all())





