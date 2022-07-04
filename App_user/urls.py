from django.urls import path
from . import views

urlpatterns = [
    #path('', views.AccountRegistration.as_view(), name='registration'),
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
]