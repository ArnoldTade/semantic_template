from django.shortcuts import render, redirect
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
    if request.method == "POST":
        employeeForm = EmployeeForm(request.POST, request.FILES)
        if employeeForm.is_valid():
            employeeForm.save()
            messages.success(request, "Employee Added!")
            return redirect("table")
        else:
            messages.warning(request, employeeForm.errors)

    else:
        employeeForm = EmployeeForm()
    title = "Table"
    context = {
        "title": title,
        "employeeForm": employeeForm,
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
