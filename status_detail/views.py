from django.shortcuts import render
from django.urls import resolve

from status_detail.models import Employee
from django.http import JsonResponse
import logging
import time,datetime

log = logging.getLogger(__name__)


def index(request):
    all_employees = Employee.objects.all()
    return render(request, "index.html", {'employees': all_employees})


def employees(request):
    all_employees = Employee.objects.all()
    return render(request, "employees.html", {'employees': all_employees})


def employees_ajax(request):
    all_employees = Employee.objects.all()
    return render(request, "employees_ajax.html", {'employees': all_employees})


def update_employee(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        message = f"Employee ID {employee_id} does not exist in the database."
        log.error(message)
        return JsonResponse(package_response(True, employee_id, message))

    if request.method == 'POST':
        current_url = resolve(request.path_info).url_name
        if current_url.find('change_name') != -1:
            if key_exist(request, "name"):
                original_name = employee.name
                employee.name = request.POST["name"]
                try:
                    existing_employee = Employee.objects.get(name=employee.name)
                    message = f"Cannot change, this name already exist with ID# {existing_employee.id}"
                    return JsonResponse(package_response(True, employee_id, message))
                except Employee.DoesNotExist:
                    employee.save()
                    message = f"Name changed from {original_name} to {employee.name}"
                    return JsonResponse(package_response(False, employee_id, message))
            else:
                message = "Can't find a posted 'name' field."
                log.error(message)
                return JsonResponse(package_response(True, employee_id, message))
        elif current_url.find('change_status') != -1:
            if key_exist(request, "status"):
                original_status = employee.status
                employee.status = request.POST["status"]
                employee.save()
                message = f"Status changed from {original_status} to {employee.status}"
                return JsonResponse(package_response(False, employee_id, message))
            else:
                message = "Can't find a posted 'status' field."
                log.error(message)
                return JsonResponse(package_response(True, employee_id, message))
        elif current_url.find('change_position') != -1:
            if key_exist(request, "position"):
                original_position = employee.position
                employee.position = request.POST["position"]
                employee.save()
                message = f"Position changed from {original_position} to {employee.position}"
                return JsonResponse(package_response(False, employee_id, message))
            else:
                message = "Can't find a posted 'position' field."
                log.error(message)
                return JsonResponse(package_response(True, employee_id, message))
        elif current_url.find('change_salary') != -1:
            if key_exist(request, "salary"):
                original_salary = employee.salary
                employee.salary = request.POST["salary"]
                employee.save()
                message = f"Salary changed from {original_salary} to {employee.salary}"
                return JsonResponse(package_response(False, employee_id, message))
            else:
                message = "Can't find a posted 'salary' field."
                log.error(message)
                return JsonResponse(package_response(True, employee_id, message))
        elif current_url.find('delete_employee') != -1:
            og_employee_name = employee.name
            employee.delete()
            message = f"{og_employee_name} deleted."
            return JsonResponse(package_response(False, employee_id, message))
        elif current_url.find('clone_employee') != -1:
            unique_time_stamp = time.mktime(datetime.datetime.today().timetuple())
            cloned_employee = Employee()
            cloned_employee.name = f"Clone-{employee.name}-{unique_time_stamp}"
            cloned_employee.status = employee.status
            cloned_employee.position = employee.position
            cloned_employee.salary = employee.salary
            cloned_employee.start_date = employee.start_date
            cloned_employee.save()

            message = f"Employee {employee.name} cloned successfully. New clone ID = {cloned_employee.id}"
            package = package_response(False, employee_id, message)
            package['clone_employee_id'] = cloned_employee.id
            package['clone_name'] = cloned_employee.name
            package['clone_status'] = cloned_employee.status
            package['clone_position'] = cloned_employee.position
            package['clone_salary'] = cloned_employee.salary
            package['clone_last_updated'] = cloned_employee.date_updated
            return JsonResponse(package)
        else:
            message = f"Entered through an un recognized url={current_url}."
            log.error(message)
            return JsonResponse(package_response(True, employee_id, message))
    else:
        message = f"Expected a POST."
        log.error(message)
        return JsonResponse(package_response(True, employee_id, message))


def key_exist(request, key_name):
    try:
        key_value = request.POST[key_name]
        return True
    except KeyError:
        return False


def package_response(error: bool, employee_id, message):
    data = {
        'employee_id': employee_id,
        'error': error,
        'message': message
    }
    return data


def get_employee(employee_id:int):
    try:
        employee = Employee.objects.get(pk=employee_id)
        return employee
    except Employee.DoesNotExist:
        log.critical(f"Employee ID passed that does not exist {employee_id}.")
        return Employee
