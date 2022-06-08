from django import views
from django.urls import URLPattern, path
from App_Login import views
app_name='App_Login'

urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.login_user,name='login'),
    path('edit/',views.edit_profile,name='edit'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('user/<username>/',views.user,name='user'),
    path('follow/<username>/',views.follow,name='follow'),
    path('unfollow/<username>/',views.unfollow,name='unfollow'),
    

]