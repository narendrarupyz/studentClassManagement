from django.shortcuts import render
from classRooms.models import ClassRoom
from django.http import Http404
from classRooms.serializers import ClassRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
   
   def get_object(self, pk):
      try:
         return ClassRoom.objects.get(pk=pk)
      except ClassRoom.DoesNotExist:
         raise Http404
    
   def get(self, request, pk, format = None):
      classroom = self.get_object(pk)
      serializer = classroom(classroom)
      return Response(serializer.data)
   
   def put(self, request, pk, format = None):
      classroom = self.get_object(pk)
      serializer = ClassRoomSerializer(classroom, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def delete(self, request, pk, format = None):
      classroom = self.get_object(pk)
      classroom.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)