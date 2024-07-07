from django.urls import path
from semanticapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.user_login, name="login"),
    path("home/", views.home, name="home"),
    path("table/", views.table, name="table"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("scan/", views.scan, name="scan"),
    path("attendance/", views.attendance, name="attendance"),
    # path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("delete-employee/<int:id>", views.delete_employee, name="delete-employee"),
    path("edit-employee/<int:id>", views.edit_employee, name="edit-employee"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
