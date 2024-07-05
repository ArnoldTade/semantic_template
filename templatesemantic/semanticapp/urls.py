from django.urls import path
from semanticapp import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("home/", views.home, name="home"),
    path("table/", views.table, name="table"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("scan/", views.scan, name="scan"),
    path("attendance/", views.attendance, name="attendance"),
    # path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
