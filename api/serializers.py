from rest_framework import serializers
# from . import models
from Courses.models import  Course, CourseTopic,  LabTask


class LabTaskSerializer(serializers.ModelSerializer):
	

	class Meta:
		model = LabTask
		fields = ('__all__')



class CourseTopicSerializer(serializers.ModelSerializer):
	labTasks = LabTaskSerializer( read_only=True)
	
	class Meta:
		fields = ('id', 'course','topic_number', 'topic', 'video', 'labTasks')
		model = CourseTopic



class CourseSerializer(serializers.ModelSerializer):
	courseTopic = CourseTopicSerializer(read_only=True)

	class Meta:
		model = Course
		fields = ( 'id', 'course_title', 'courseTopic')