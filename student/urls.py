from django.urls import path
from student import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)