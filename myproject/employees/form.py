from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['cod', 'name', 'last_name', 'civil_status',
                  'photo', 'degree', 'category', 'department', 'bio', 'birth', 'email',
                  'address', 'city']
