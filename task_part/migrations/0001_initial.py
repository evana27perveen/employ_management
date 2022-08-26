# Generated by Django 3.1.4 on 2021-03-16 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_part', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150)),
                ('work_description', models.TextField()),
                ('assigned_to', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=255, size=5)),
                ('deadline', models.DateTimeField()),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('project_dpt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='log_part.departmentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='VerifyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Done', 'Done')], max_length=15)),
                ('project_v', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_part.projectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('total_days', models.IntegerField()),
                ('reason', models.TextField()),
                ('apply_date', models.DateField(auto_now_add=True)),
                ('leave_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]