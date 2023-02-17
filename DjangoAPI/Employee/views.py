from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Employee.models import Department, Employee
from Employee.serializers import DepartmentSerializer, EmployeeSerializer

# importing module to store the uploaded files for PhotoFiles of employees
from django.core.files.storage import default_storage


# Create your views here.

# Writing API methods for Department Screen
@csrf_exempt
# method receives an optional id which will be useful to delete a record using the id
def departmentApi(request, id=0):
    if request.method == 'GET':
        department = Department.objects.all()
        department_serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(
            DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(
            department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        department = Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

# API methods for Employee Screen


@csrf_exempt
# method receives an optional id which will be useful to delete a record using the id
def employeeApi(request, id=0):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(
            EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(
            employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
