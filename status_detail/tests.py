from django.test import TestCase
from status_detail.models import Employee
from status_detail.provisioning.provision_application import add_employee_to_db, employees


class AddEmployeeTestCase(TestCase):
    def test_can_add_employee(self):
        self.assertEqual(add_employee_to_db(employees[0]), True)
