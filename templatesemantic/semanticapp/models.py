from django.db import models


class Employee(models.Model):
    STATUS = [
        ("Active", "ACTIVE"),
        ("Inactive", "INACTIVE"),
    ]
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    birthDate = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f"{self.firstName},{self.lastName}"
