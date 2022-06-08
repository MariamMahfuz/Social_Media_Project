from importlib.resources import path
from django.urls import URLPattern,path
from App_Post import views

app_name='App_Post'

urlpatterns=[
    path('',views.home,name='home'),
    path('liked/<pk>/',views.liked,name='liked'),
    path('unliked/<pk>/',views.unliked,name='unliked'),

]
