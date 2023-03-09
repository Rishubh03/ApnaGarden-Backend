from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Department, Employees
from .serializers import DepartmentSerializer, EmployeesSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your tests here.


class DepartmentList(APIView):
    """
    List all Departments, or create a new Department
    """

    def get(self, request, format=None):
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DepartmentDetail(APIView):
    """
    Retrieve, update or delete Department instance
    """

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesList(APIView):
    """
    List all Position, or create a new employees
    """

    def get(self, request, format=None):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        


class EmployeesDetail(APIView):
    """
    Retrieve, update or delete Employees instance
    """

    def get_object(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employees = self.get_object(pk)
        serializer = EmployeesSerializer(employees)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        employees = self.get_object(pk)
        serializer = EmployeesSerializer(employees,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

