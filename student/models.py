from django.db import models
from classRooms.models import ClassRoom

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=80)
    roll_no = models.TextField(max_length=10, unique=True)
    age = models.TextField(max_length=3)
    address = models.CharField(max_length=100)
    pincode = models.TextField(max_length=8)
    mobile_no = models.TextField(max_length=10)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    class Meta:
        ordering = ['roll_no']