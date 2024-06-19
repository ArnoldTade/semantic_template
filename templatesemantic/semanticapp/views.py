from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    title = "Login"
    context = {
        "title": title,
    }
    return render(request, "login.html", context)


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
    title = "Table"
    context = {
        "title": title,
    }
    return render(request, "table.html", context)


def scan(request):
    title = "Scan"
    context = {
        "title": title,
    }
    return render(request, "scan.html", context)
