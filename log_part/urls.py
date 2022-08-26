from django.urls import path
from . import views


urlpatterns = [
    path('new_user/', views.signup, name='add_user'),
    path('login/', views.login_sys, name='login'),
    path('logout/', views.logout_sys, name='logout',)


]
