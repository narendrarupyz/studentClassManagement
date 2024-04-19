from django.db import models


class ClassRoom(models.Model):
    AC = 'A/C'
    NON_AC = 'NON A/C'
    CLASSROOM_CHOICES = [
        (AC, 'A/C'),
        (NON_AC, 'NON A/C')
    ]
    number_of_seat = models.IntegerField()
    class_room_number = models.IntegerField(primary_key=True)
    floor = models.IntegerField()
    class_room_type = models.CharField(
        max_length=10, choices=CLASSROOM_CHOICES, default=NON_AC)

    class Meta:
        ordering = ['class_room_number']
