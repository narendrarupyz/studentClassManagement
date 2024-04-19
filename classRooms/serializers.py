from classRooms.models import ClassRoom
from rest_framework import serializers  # type: ignore


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['number_of_seat', 'class_room_number',
                  'floor', 'class_room_type']
