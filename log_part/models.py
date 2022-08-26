from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_(
    "Enter a valid international mobile phone number starting with +(country code)"))
gender_choice = (
    ("male", "Male"),
    ("Female", "Female"),
    ("Third Gender", "Third Gender")
)


# Create your models here.
class DepartmentModel(models.Model):
    dpt_name = models.CharField(max_length=100, unique=True)
    dpt_location = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return f"{self.dpt_name}-{self.dpt_location}"


class EmployeeProfileModel(models.Model):
    emp_picture = models.ImageField(upload_to='EmployeeProfileModel/emp_pic')
    emp_name = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='emp_name')
    emp_contact = models.CharField(validators=[phone_regex], verbose_name=_("Employee's Mobile phone"), max_length=17,
                                   blank=True, null=True)
    Date_of_Birth = models.DateField(blank=False)
    gender = models.CharField(choices=gender_choice, max_length=15)
    emp_nid = models.IntegerField(unique=False)
    emp_address = models.CharField(max_length=200)
    e_resume = models.ImageField(upload_to='EmployeeProfileModel/E_resume')
    emp_id = models.CharField(max_length=50, unique=True)
    emp_dpt = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, related_name='emp_dpt')
    emp_designation = models.CharField(max_length=100)
    emp_salary = models.IntegerField(unique=False)
    emp_assigned_leaves = models.IntegerField(unique=False)
    manager = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='manager_of_epm')
    joining_date = models.DateField(blank=False)

    def __str__(self):
        return f"{self.emp_id} {self.emp_name} {self.emp_designation}"


class ManagerModel(models.Model):
    mgr_name = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mgr_name')
    mgr_id = models.ForeignKey(EmployeeProfileModel, on_delete=models.CASCADE, related_name='mgr_id')
    head_of_dpt = models.ForeignKey(DepartmentModel, default=1, on_delete=models.SET_DEFAULT,
                                    related_name='head_of_dpt')

    def __str__(self):
        return f"{self.mgr_name} {self.head_of_dpt}"

