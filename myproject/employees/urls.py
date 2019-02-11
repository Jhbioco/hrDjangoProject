from django.urls import path
from .views import home
from .views import employeeList
from .views import employeeNew
from .views import employeeEdit
from .views import employeeDelete
from .views import employeeDetail

urlpatterns = [
    path('', home, name='home'),
    path('employees/', employeeList, name='employee_list'),
    path('employee/', employeeNew, name='employee_new'),
    path('employee_edit/<int:pk>', employeeEdit, name='employee_edit'),
    path('employee_delete/<int:pk>', employeeDelete, name='employee_delete'),
    path('employee_detail/<int:pk>', employeeDetail, name='employee_detail')
]
