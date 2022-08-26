from django.urls import path
from . import views


urlpatterns = [
    path('', views.project, name='project'),
    path('details/<int:my_pk>/', views.project_detail, name='detail'),
    path('verify/', views.verify, name='verify'),
    path('leave/', views.leave, name='leave'),
]
