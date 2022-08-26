from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('test_part/', include('log_part.urls')),
    path('project/', include('task_part.urls')),
    path('office_admin/', include('admin_part.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
