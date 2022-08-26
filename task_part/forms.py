from django.contrib.auth.forms import forms
from .models import ProjectModel, LeaveModel, VerifyModel, ApproveLeave


class ProjectForm(forms.ModelForm):
    deadline = forms.DateTimeField(required=True, widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = ProjectModel
        exclude = ('assigned_by',)


class LeaveForm(forms.ModelForm):
    from_date = forms.DateTimeField(input_formats=['%d/%m/%Y'],
                                    widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy'}))
    to_date = forms.DateTimeField(input_formats=['%d/%m/%Y'],
                                  widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy'}))

    class Meta:
        model = LeaveModel
        exclude = ('leave_for',)


class VerifyForm(forms.ModelForm):
    class Meta:
        model = VerifyModel
        exclude = ('project_v', )


class ApproveLeaveForm(forms.ModelForm):
    class Meta:
        model = ApproveLeave
        exclude = ('leave_id', )
