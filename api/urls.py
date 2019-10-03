
# from . import views

# urlpatterns = [
# 	path('', views.ListCourses.as_view()),
# 	path('<int:pk>/', views.DetailCourse.as_view()),
# 	path('rest-auth/', include('rest_auth.urls')),
# ]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CourseTopicViewSet, LabTasksViewSet


router = DefaultRouter()

router.register(prefix = 'course', viewset = CourseViewSet, base_name = "status")
router.register(prefix = 'courseTopic', viewset = CourseTopicViewSet, base_name = "goals")
# router.register(prefix = 'lab', viewset = LabViewSet,  base_name = "story")
router.register(prefix = 'labTasks', viewset = LabTasksViewSet,  base_name = "users")


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns += router.urls