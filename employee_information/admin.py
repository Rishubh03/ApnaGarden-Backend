from django.contrib import admin
from .models import Department, Employees, Leave

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
        list_display = ['job_id', 'job_dept', 'name', 'description', 'date_updated']
        ordering = ['job_id']
        search_fields = ['job_dept', 'name', 'description']

@admin.register(Employees)       
class EmployeesAdmin(admin.ModelAdmin):
        list_display = ['user', 'user_firstname','user_lastname','contact_no','department_id','status','date_updated']
        search_fields = ['user__firstname', 'user__lastname', 'contact_no', 'department_id__name']
        ordering = ['user__firstname','user__lastname']

        def user_firstname(self, instance):
                return instance.user.firstname
        
        def user_middlename(self, instance):
                return instance.user.middlename
        
        def user_lastname(self, instance):
                return instance.user.lastname        

@admin.action(description='Mark selected as Approved')
def make_approve(modeladmin, request, queryset):
    queryset.update(status=2)

@admin.action(description='Mark selected as Rejected')
def make_rejected(modeladmin, request, queryset):
    queryset.update(status=3)

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
        list_display = ['leave_id', 'emp_id', 'leave_type', 'date_from', 'date_to', 'reason', 'status']
        ordering = ['date_from','leave_id']
        search_fields = ['emp_id__user__firstname', 'emp_id__user__lastname', 'leave_type', 'reason']
        
        actions = [make_approve,make_rejected]

