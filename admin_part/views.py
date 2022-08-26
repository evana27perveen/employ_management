from django.shortcuts import render, HttpResponseRedirect, reverse
from task_part.forms import ProjectForm, LeaveForm, VerifyForm, ApproveLeaveForm
from log_part.forms import DepartmentForm, EmployeeProfileForm, ManagerForm
from log_part.models import EmployeeProfileModel, ManagerModel, DepartmentModel
from task_part.models import ProjectModel, LeaveModel, VerifyModel, ApproveLeave
from django.contrib.auth.decorators import login_required
from admin_part.models import OfficeAdminModel
from django.contrib.auth.models import User


# Create your views here.


@login_required()
def recruiting(request):
    form = EmployeeProfileForm()
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.save()
            return HttpResponseRedirect(reverse('recruiting'))

    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)

    employees = EmployeeProfileModel.objects.all()

    return render(request, 'admin_part/recruiting_employees.html',
                  context={'employees': employees, 'form': form, 'profile': profile, 'manager': manager,
                           'my_admin': my_admin, })


@login_required()
def manager_add(request):
    form = ManagerForm()
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.save()
            return HttpResponseRedirect(reverse('manager_add'))

    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)
    return render(request, 'admin_part/specify_manager.html',
                  context={'m_list': manager_list, 'form': form, 'profile': profile, 'manager': manager,
                           'my_admin': my_admin, })


@login_required()
def dpt_add(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.save()
            return HttpResponseRedirect(reverse('dpt_add'))

    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)

    dpts = DepartmentModel.objects.all()
    return render(request, 'admin_part/add_dpt.html',
                  context={'dpts': dpts, 'form': form, 'profile': profile, 'manager': manager, 'my_admin': my_admin, })


@login_required()
def approve_leave(request):
    leave_list_d = ApproveLeave.objects.all().filter(status='Done')
    approved_leaves = []
    for i in leave_list_d:
        approved_leaves.append(i.leave_id_id)

    leave_list_r = ApproveLeave.objects.all().filter(status='Rejected')
    rejected_leaves = []
    for i in leave_list_r:
        rejected_leaves.append(i.leave_id_id)

    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)
    leaves = LeaveModel.objects.all()
    return render(request, 'admin_part/approve_leave.html',
                  context={'rejected_leaves': rejected_leaves, 'approved_leaves': approved_leaves, 'leaves': leaves,
                           'profile': profile, 'manager': manager, 'my_admin': my_admin, })


@login_required()
def leave_detail(request, my_pk):
    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)

    leave_expand = LeaveModel.objects.filter(id=my_pk)[0]

    leave_list_d = ApproveLeave.objects.all().filter(status='Done')
    approved_leaves = []
    for i in leave_list_d:
        approved_leaves.append(i.leave_id_id)

    leave_list_r = ApproveLeave.objects.all().filter(status='Rejected')
    rejected_leaves = []
    for i in leave_list_r:
        rejected_leaves.append(i.leave_id_id)

    form = ApproveLeaveForm()
    if request.method == 'POST':
        form = ApproveLeaveForm(data=request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.leave_id = leave_expand.id
            my_form.save()
            return HttpResponseRedirect(reverse('approve_leave'))

    return render(request, 'admin_part/leave_detail.html',
                  context={'rejected_leaves': rejected_leaves, 'form': form, 'approved_leaves': approved_leaves,
                           'leave_expand': leave_expand, 'profile': profile, 'manager': manager,
                           'my_admin': my_admin, })
