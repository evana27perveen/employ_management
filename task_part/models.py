from django.db import models
from django.urls import reverse

from log_part.models import EmployeeProfileModel, DepartmentModel
from django.contrib.auth.models import User
from django_mysql.models import ListCharField

verify_choice = (
    ("Done", "Done"),
    ("Rejected", "Rejected"),
)

# Create your models here.


class ProjectModel(models.Model):
    project_name = models.CharField(max_length=150)
    project_dpt = models.ForeignKey(DepartmentModel, on_delete=models.DO_NOTHING)
    work_description = models.TextField()
    assigned_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='assigned_to')
    assigned_to = ListCharField(base_field=models.CharField(max_length=50), size=5, max_length=(5 * 51))
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.project_name}-{self.deadline}"

    def get_absolute_url(self):
        return reverse('home')


class LeaveModel(models.Model):
    leave_for = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    total_days = models.IntegerField()
    reason = models.TextField()
    apply_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.leave_for}-{self.total_days}"


class VerifyModel(models.Model):
    project_v = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    status = models.CharField(choices=verify_choice, max_length=15)

    def __str__(self):
        return f"{self.project_v}-{self.status}"

    def get_absolute_url(self):
        return reverse('verify')


class ApproveLeave(models.Model):
    leave_id = models.ForeignKey(LeaveModel, on_delete=models.CASCADE)
    status = models.CharField(choices=verify_choice, max_length=15)

    def __str__(self):
        return f"{self.leave_id}-{self.status}"

    def get_absolute_url(self):
        return reverse('approve_leave')
