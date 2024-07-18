from django.db import models

# Create your models here.

class Class(models.Model):
    class_id = models.PositiveSmallIntegerField()
    class_name = models.CharField(max_length = 20)
    teacher = models.CharField(max_length = 20)
    room_number = models.PositiveSmallIntegerField()
    class_size = models.PositiveSmallIntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    school_year = models.IntegerField()
    created_at = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.class_name}"
