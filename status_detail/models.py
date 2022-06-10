from django.db import models

STATUS = (
    (u'pass', u'Pass'),
    (u'warn', u'Warning'),
    (u'fail', u'Fail'),
)


class Employee(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255, choices=STATUS, blank=True)
    position = models.CharField(max_length=255, blank=True)
    salary = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    extension = models.CharField(max_length=255, blank=True)

    date_inserted = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
