from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .models import Department
from .models import Category
from .models import Document
from .form import EmployeeForm


# Create home view
def home(request):
    return render(request, 'home.html')


def employeeList(request):
    employees = Employee.objects.all()
    return render(request, 'employeelist.html', {'employees':employees})


def employeeNew(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee.html', {'form':form})


def employeeEdit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee.html', {'form':form})


def employeeDelete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'delete.html', {'employee':employee})


def employeeDetail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'detail.html', {'employee':employee})


