from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('department/', views.DepartmentList.as_view()),
    path('department/<int:pk>/', views.DepartmentDetail.as_view()),
    
    path('employees/', views.EmployeesList.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)