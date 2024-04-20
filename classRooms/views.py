from django.shortcuts import render
from classRooms.models import ClassRoom
from django.http import Http404
from classRooms.serializers import ClassRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from student.models import Student
from student.serializers import StudentSerializer

# Create your views here.


class ClassRoomList(APIView):

    def get(self, request, format=None):
        classroom = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classroom, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassRoomDetails(APIView):

    def get_object(self, class_room_number):
        try:
            return ClassRoom.objects.get(class_room_number=class_room_number)
        except ClassRoom.DoesNotExist:
            raise Http404

    def get(self, request, class_room_number, format=None):
        classroom = self.get_object(class_room_number)
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)

    def put(self, request, class_room_number, format=None):
        classroom = self.get_object(class_room_number)
        serializer = ClassRoomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, class_room_number, format=None):
        classroom = self.get_object(class_room_number)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassRoomWithStudents(APIView):
    def get(self, request, class_room_number):
        try:
            classroom = ClassRoom.objects.get(
                class_room_number=class_room_number)

            class_room_data = ClassRoomSerializer(classroom)
            return Response(class_room_data.data, status=status.HTTP_200_OK)
        except ClassRoom.DoesNotExist:
            return Response({'error': 'class does not exist'}, status=status.HTTP_404_NOT_FOUND)
