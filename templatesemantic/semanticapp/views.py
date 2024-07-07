from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        userform = LoginForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data["username"]
            password = userform.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Wrong username or password")
    loginform = LoginForm()

    title = "Login"
    context = {
        "title": title,
        "loginform": loginform,
    }
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def home(request):
    title = "Home"
    context = {
        "title": title,
    }
    return render(request, "home.html", context)


def dashboard(request):
    title = "Dashboard"
    context = {
        "title": title,
    }
    return render(request, "dashboard.html", context)


def table(request):
    employees = Employee.objects.all()
    total_employees = employees.count()
    active_employee = employees.filter(status="Active").count()
    inactive_employee = employees.filter(status="Inactive").count()

    if request.method == "POST":
        employeeForm = EmployeeForm(request.POST, request.FILES)
        if employeeForm.is_valid():
            employeeForm.save()
            messages.success(request, "Employee Added!")
            return redirect("table")

    else:
        employeeForm = EmployeeForm()
    context = {
        "title": "Table",
        "employeeForm": employeeForm,
        "employees": employees,
        "total_employees": total_employees,
        "active_employee": active_employee,
        "inactive_employee": inactive_employee,
    }
    return render(request, "table.html", context)


def scan(request):
    title = "Scan"
    context = {
        "title": title,
    }
    return render(request, "scan.html", context)


def attendance(request):
    title = "Attendance"
    context = {
        "title": title,
    }
    return render(request, "attendance.html", context)


def delete_employee(request, id=None):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, "Employee Deleted!")
    return redirect("table")


def edit_employee(request, id=None):
    employee = get_object_or_404(Employee, id=id)
    employeeForm = EmployeeForm(request.POST, request.FILES, instance=employee)
    if employeeForm.is_valid():
        employeeForm.save()
        messages.success(request, "Employee Updated!")
        return redirect("edit-employee", id=employee.id)

    employeeForm = EmployeeForm(instance=employee)
    context = {
        "title": "Table",
        "employeeForm": employeeForm,
    }
    return render(request, "employee-profile.html", context)
