from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('usercreate/', views.usercreate, name='usercreate'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adminhome',views.adminhome,name='adminhome'),
]
