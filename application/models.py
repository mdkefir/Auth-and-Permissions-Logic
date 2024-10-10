from django.db import models

# Create your models here.
class Student(models.Model):
    fio = models.TextField() # Student's name
    record_number = models.TextField()

    group_name = models.TextField()
