from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.departmentApi, name="departmentApi"),
    path("employeeApi/", views.employeeApi, name="employeeApi"),
    path("saveFile/", views.saveFile, name="saveFile"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)