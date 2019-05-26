from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    parent_id = models.IntegerField()
    class Meta:
        db_table = 't_category'


class Address(models.Model):
    address = models.CharField(max_length=20, )
    m_phone = models.CharField(max_length=20, )
    phone = models.CharField(max_length=20, )
    postcode = models.CharField(max_length=20, )
    # user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    user=models.IntegerField()
    ship_man = models.CharField(max_length=20 , default='username')

    class Meta:
        db_table = 't_address'


class HistoryOrder(models.Model):
    order_num = models.IntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING, )
    address = models.CharField(max_length=100, )
    content = models.TextField()

    class Meta:
        db_table = 't_history_order'


class Order(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey('User', models.DO_NOTHING, )
    address = models.ForeignKey(Address, models.DO_NOTHING, )
    time = models.DateTimeField()

    class Meta:
        db_table = 't_order'


class OrderInfo(models.Model):
    number = models.IntegerField()
    order = models.ForeignKey(Order, models.DO_NOTHING, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, )

    class Meta:
        db_table = 't_order_info'


class Product(models.Model):
    name = models.CharField(max_length=50, )
    author = models.CharField(max_length=50, )
    face = models.CharField(max_length=100, )
    publishing_house = models.CharField(max_length=50, )
    edition = models.SmallIntegerField()
    publishing_time = models.DateTimeField()
    print_time = models.SmallIntegerField()
    isbn = models.CharField(max_length=30, )
    word = models.CharField(max_length=20, )
    number_of_page = models.IntegerField()
    format_of_book = models.CharField(max_length=20, )
    paper = models.CharField(max_length=20, )
    packagin = models.CharField(max_length=20, )
    emboitement = models.CharField(max_length=10, )
    sales = models.CharField(max_length=20, )
    price = models.FloatField()
    dangdang_price = models.FloatField()
    review = models.BigIntegerField()
    issue = models.DateTimeField()
    score = models.FloatField()
    sold_out = models.CharField(max_length=10, )
    recommand = models.CharField(max_length=10, )
    menus = models.ForeignKey(Category, models.DO_NOTHING, db_column='menus', )
    extend = models.CharField(max_length=50, )

    class Meta:
        db_table = 't_product'


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='邮箱')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='用户的创建时间')
    has_confirm = models.BooleanField(default=False, verbose_name='邮箱是否确认')

    class Meta:
        db_table = 't_user'


class ConfirmString(models.Model):
    code = models.CharField(max_length=256, verbose_name='邮箱注册码')
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='关联的用户')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='注册码的生成时间')

    class Meta:
        db_table = 't_confirmString'
