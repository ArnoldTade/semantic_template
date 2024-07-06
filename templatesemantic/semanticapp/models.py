from django.db import models
from .validators import validate_image_size


class Employee(models.Model):
    STATUS = [
        ("Active", "ACTIVE"),
        ("Inactive", "INACTIVE"),
    ]
    profile_picture = models.ImageField(
        upload_to="img/", validators=[validate_image_size], null=True
    )
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    birthDate = models.DateField()
    position = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f"{self.firstName},{self.lastName}"
