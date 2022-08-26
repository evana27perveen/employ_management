from django.contrib import admin
from .models import DepartmentModel, EmployeeProfileModel, ManagerModel


# Register your models here.
admin.site.register(DepartmentModel)
admin.site.register(EmployeeProfileModel)
admin.site.register(ManagerModel)

