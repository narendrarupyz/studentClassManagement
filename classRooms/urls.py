from django.urls import path
from classRooms import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('classRoom/', views.ClassRoomList.as_view()),
    path('classRoom/<int:class_room_number>/', views.ClassRoomDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)