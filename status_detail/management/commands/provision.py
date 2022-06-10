from django.core.management.base import BaseCommand
from status_detail.provisioning.provision_application import employees, add_employee_to_db

import logging
log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Provision employee application.'

    def handle(self, *args, **options):
        for employee in employees:
            if add_employee_to_db(employee):
                self.stdout.write(self.style.SUCCESS(f"Success adding {employee['name']}."))
            else:
                self.stdout.write(f"Failed adding {employee['name']}.")
        self.stdout.write(self.style.SUCCESS(f"Success provisioning application"))
