from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from log_part.models import EmployeeProfileModel, ManagerModel
from task_part.models import ProjectModel, VerifyModel
from admin_part.models import OfficeAdminModel


@login_required()
def home(request):
    pp = []
    qq = []
    find_result = ''
    v_manage_s = VerifyModel.objects.all().filter(status='Done')
    v_manage = []
    for i in v_manage_s:
        v_manage.append(i.project_v_id)
    profile = EmployeeProfileModel.objects.filter(emp_name=request.user)[0]
    if request.method == 'POST' and 'search_btn' in request.POST:
        query = request.POST.get('search_input')
        try:
            find_result = ProjectModel.objects.filter(project_name__icontains=query)
            for project in find_result:
                if profile.emp_id in project.assigned_to:
                    qq.append(project)
        except ValueError:
            qq = find_result
    manager_list = ManagerModel.objects.all()
    manager = []
    for i in manager_list:
        manager.append(i.mgr_name_id)
    my_admin_list = OfficeAdminModel.objects.all()
    my_admin = []
    for i in my_admin_list:
        my_admin.append(i.o_admin_name_id)

    projects = ProjectModel.objects.all()
    for project in projects:
        if profile.emp_id in project.assigned_to:
            pp.append(project)

    search_show = True
    return render(request, 'employee_management_project/home.html',
                  {'search_show': search_show, 'v_manage': v_manage, 'profile': profile, 'manager': manager,
                   'projects': pp, 'query_result': qq,
                   'my_admin': my_admin, })
