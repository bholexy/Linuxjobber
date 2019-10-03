from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer, CourseTopicSerializer, LabTaskSerializer
from Courses.models import LabTask, Course, CourseTopic

from rest_framework import generics

from GroupClass import models
from . import serializers
# Create your views here.

# class ListCourses(generics.ListCreateAPIView):
# 	queryset = models.Course.objects.all()
# 	serializer_class = serializers.CourseSerializer


# class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = models.Course.objects.all()
# 	serializer_class = serializers.CourseSerializer 


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseTopicViewSet(viewsets.ModelViewSet):
	queryset = CourseTopic.objects.all()
	serializer_class = CourseTopicSerializer


# class LabViewSet(viewsets.ModelViewSet):
# 	queryset = Lab.objects.all()
# 	serializer_class = LabSerializer


class LabTasksViewSet(viewsets.ModelViewSet):
	queryset = LabTask.objects.all()
	serializer_class = LabTaskSerializer