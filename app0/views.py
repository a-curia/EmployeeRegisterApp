from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app0.forms import EmployeeForm
from app0.models import Employee


def hello(request):
    return HttpResponse("Hello")

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "app0/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "app0/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')