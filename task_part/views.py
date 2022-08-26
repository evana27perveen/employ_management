from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import ProjectForm, LeaveForm, VerifyForm
from log_part.models import EmployeeProfileModel, ManagerModel, DepartmentModel
from task_part.models import ProjectModel, LeaveModel, VerifyModel
from admin_part.models import OfficeAdminModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


@login_required()
def project(request):

    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.assigned_by = request.user
            my_form.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'task_part/project_assign.html',
                  context={'form': form, 'profile': profile, 'manager': manager, 'my_admin': my_admin, })


@login_required()
def project_detail(request, my_pk):

    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)
    project_expand = ProjectModel.objects.filter(id=my_pk)[0]
    a_manager = ManagerModel.objects.filter(mgr_name=request.user)[0]
    my_key = project_expand.assigned_to
    m_name = []
    v_manage_s = VerifyModel.objects.all().filter(status='Done')
    v_manage = []
    for i in v_manage_s:
        v_manage.append(i.project_v_id)

    form = VerifyForm()
    if request.method == 'POST':
        form = VerifyForm(data=request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.project_v = project_expand
            my_form.save()
            return HttpResponseRedirect(reverse('verify'))

    emp_view = EmployeeProfileModel.objects.values_list('emp_id')
    for i in my_key:
        m_name.append(EmployeeProfileModel.objects.filter(emp_id=i).only('emp_id', 'emp_name', 'emp_contact')[0])
    return render(request, 'task_part/project_detail.html',
                  {'v_manage': v_manage, 'form': form, 'm_names': m_name, 'project_expand': project_expand,
                   'a_manager': a_manager, 'profile': profile, 'manager': manager, 'my_admin': my_admin, })


@login_required()
def leave(request):

    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]

    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)

    form = LeaveForm()
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.leave_for = request.user
            my_form.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'task_part/leave_application.html', context={'form': form, 'profile': profile, 'manager': manager, 'my_admin': my_admin, })


@login_required()
def verify(request):
    vp = []
    vq = []
    find_v_result = ''
    v_manage_s = VerifyModel.objects.all().filter(status='Done')
    v_manage = []
    for i in v_manage_s:
        v_manage.append(i.project_v_id)
    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]
    if request.method == 'POST' and 'search_btn' in request.POST:
        query = request.POST.get('search_input')
        try:
            find_v_result = ProjectModel.objects.filter(project_name__icontains=query)
            for v_project in find_v_result:
                if request.user == v_project.assigned_by:
                    vq.append(v_project)
        except ValueError:
            vq = find_v_result

    v_projects = ProjectModel.objects.all()
    for v_project in v_projects:
        if request.user == v_project.assigned_by:
            vp.append(v_project)
    # done_or_not = {}
    # for i in vp:
    #     if i in v_manage:
    #         done_or_not[i] = 'done'
    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)

    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)
    return render(request, 'task_part/manager_verification.html',
                  {'v_manage': v_manage, 'profile': profile, 'manager': manager, 'projects': vp, 'query_result': vq, 'my_admin': my_admin,  })
