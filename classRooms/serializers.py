from student.serializers import StudentSerializer
from student.models import Student
from classRooms.models import ClassRoom
from rest_framework import serializers  # type: ignore


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['number_of_seat', 'class_room_number',
                  'floor', 'class_room_type', 'student']
    student = serializers.SerializerMethodField()

    def get_student(self, obj):
        students = Student.objects.filter(class_room=obj)
        serializer = StudentSerializer(students, many=True)
        return serializer.data
