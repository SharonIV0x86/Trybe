from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    role = models.CharField(max_length=12)

    def __str__(self):
        return self.firstName
