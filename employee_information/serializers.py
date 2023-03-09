from rest_framework import serializers
from .models import Department,Employees


class DepartmentSerializer(serializers.ModelSerializer):
        class Meta:
                model = Department
                fields = ('__all__')

class EmployeesSerializer(serializers.ModelSerializer):
        class Meta:
                model = Employees
                fields = ('__all__')