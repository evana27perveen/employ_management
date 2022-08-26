from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class OfficeAdminModel(models.Model):
    o_admin_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='o_admin_name')

    def __str__(self):
        return f"{self.o_admin_name}"
