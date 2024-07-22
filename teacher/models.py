from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    date_of_birth = models.DateField
    country = models.CharField(max_length = 28)
    gender = models.CharField(max_length = 6)
    Bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
