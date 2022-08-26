from django.contrib import admin
from .models import ProjectModel, LeaveModel, VerifyModel


# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(LeaveModel)
admin.site.register(VerifyModel)



