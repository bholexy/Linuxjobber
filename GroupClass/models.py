from django.db import models

class Course(models.Model):
    course_title = models.CharField(max_length = 200)
    
    class Meta:
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return self.course_title
