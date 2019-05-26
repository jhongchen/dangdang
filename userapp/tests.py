# from django.test import TestCase

# Create your tests here.
from _md5 import md5
import random
def get_salt():
	#做盐罐
    l='1234567890-=qwertyuiop[]asdfghjklzxcvbnm,./'
    #随机取6粒盐
    salt=''.join(random.sample(l,6))
    print(salt)
    return salt

pwd = '123456'+get_salt()

a = md5(pwd.encode())

print(a.decode())


