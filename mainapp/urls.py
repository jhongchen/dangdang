from django.urls import path
from . import views



app_name = 'mainapp'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('booklist/',views.booklist,name='booklist'),
    path('detail/', views.detail, name='detail'),
]