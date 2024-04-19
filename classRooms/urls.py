from django.urls import path
from classRooms import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('classRoom/', views.ClassRoomList.as_view()),
    path('classRoom/<int:pk>/', views.ClassRoomList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)