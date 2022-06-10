"""occu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from status_detail import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.employees, name='employees'),
    path('employees-ajax/', views.employees_ajax, name='employees_ajax'),
    path('<int:employee_id>/change-name', views.update_employee, name='change_name'),
    path('<int:employee_id>/change-status', views.update_employee, name='change_status'),
    path('<int:employee_id>/change-position', views.update_employee, name='change_position'),
    path('<int:employee_id>/change-salary', views.update_employee, name='change_salary'),
    path('<int:employee_id>/delete-employee', views.update_employee, name='delete_employee'),
    path('<int:employee_id>/clone-employee', views.update_employee, name='clone_employee'),
    path('admin/', admin.site.urls),
]
