from django.urls import path
from . import views


urlpatterns = [
    path('recruit/', views.recruiting, name='recruiting'),
    path('add_manager/', views.manager_add, name='manager_add'),
    path('add_dpt/', views.dpt_add, name='dpt_add'),
    path('approve_leave/', views.approve_leave, name='approve_leave'),
    path('leave_detail/<int:my_pk>/', views.leave_detail, name='leave_detail'),

]
